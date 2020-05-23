#!/usr/bin/python2.5

import optparse;
import os;
import platform;
import re;
import string;
import sys;
import collections;

import KwReviewWebApiPost1;

from datetime import datetime;

optParser                   = optparse.OptionParser();
sScriptId                   = optParser.get_prog_name();
sScriptVers                 = "(v1.0501)";
sScriptDisp                 = sScriptId+" "+sScriptVers+":"
cScriptArgc                 = len(sys.argv);

bVerbose                    = False;
bScriptTestOnly             = False;
bUserActionPrompt           = False;
sScriptKwBasicAuthUserID    = None;
sScriptKwBasicAuthPassword  = None;
sScriptKwServerProjectURL   = None;

def main():

    try:

        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print "%s The Klocwork Review WebAPI 'post' Tester #1 is starting execution from Server [%s] on [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp);
        print "";

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_True");
        optParser.add_option("-t", "--test-only", dest="test_only", default=False, help="Test ONLY - do not execute 'kwbuildproject'/'kwadmin load'", action="store_True");
        optParser.add_option("-p", "--prompt", dest="run_prompted", default=False, help="Run PROMPTED", action="store_True");
        optParser.add_option("--basic-user", dest="kw_basic_auth_user", default="", help="Klocwork 'basic' authentication UserID", metavar="Klocwork-Basic-UserID");
        optParser.add_option("--basic-pswd", dest="kw_basic_auth_pswd", default="", help="Klocwork 'basic' authentication Password", metavar="Klocwork-Basic-Password");
        optParser.add_option("--url", dest="kw_server_url", default="", help="Klocwork (server/project) URL - Host/Port/Project - use the Project_Name here - sample: --url=http://hostname:8080/Project1", metavar="Klocwork-Server-URL");

        (options, args) = optParser.parse_args();

        bVerbose                   = options.run_verbose;
        bScriptTestOnly            = options.test_only;
        bUserActionPrompt          = options.run_prompted;
        sScriptKwBasicAuthUserID   = options.kw_basic_auth_user.strip();
        sScriptKwBasicAuthPassword = options.kw_basic_auth_pswd.strip();
        sScriptKwServerProjectURL  = options.kw_server_url.strip();

    #   if bVerbose == True:

        print "%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose);
        print "%s Command Test 'only' flag is [%s]..." % (sScriptDisp, bScriptTestOnly);
        print "%s User 'action' PROMPT flag is [%s]..." % (sScriptDisp, bUserActionPrompt);
        print "";
        print "%s Command Klocwork 'basic' authentication UserID is [%s]..." % (sScriptDisp, sScriptKwBasicAuthUserID);
        print "%s Command Klocwork 'basic' authentication Password is [%s]..." % (sScriptDisp, sScriptKwBasicAuthPassword);
        print "%s Command Klocwork 'server' URL is [%s]..." % (sScriptDisp, sScriptKwServerProjectURL);
        print "";

        if sScriptKwServerProjectURL != None:
        
            sScriptKwServerProjectURL = sScriptKwServerProjectURL.strip();
        
        if sScriptKwServerProjectURL == None or \
           len(sScriptKwServerProjectURL) < 1:
        
            sScriptKwServerProjectURL = None;
        
        else:
        
            sScriptKwServerProjectURLLow = sScriptKwServerProjectURL.lower();

            if sScriptKwServerProjectURLLow.startswith("http://")  == False and \
               sScriptKwServerProjectURLLow.startswith("https://") == False:
            
                sScriptKwServerProjectURL = None;
            
        if sScriptKwServerProjectURL != None:

            sScriptKwServerProjectURL = sScriptKwServerProjectURL.strip();

        if sScriptKwServerProjectURL == None or \
           len(sScriptKwServerProjectURL) < 1:

            print "";
            print "%s The Klocwork Server/Project URL is None or Empty - this SHOULD be supplied - Warning!" % (sScriptDisp);
            print "";

        bProcessingError = False;

        kwWebApiPost = KwReviewWebApiPost1.KwReviewWebApiPost(trace=bVerbose, useractionprompt=bUserActionPrompt, kwserverprojecturl=sScriptKwServerProjectURL, kwuserissuper=False, kwbasicauthuserid=sScriptKwBasicAuthUserID, kwbasicauthpassword=sScriptKwBasicAuthPassword, kwsourceserverurl=None);

        kwWebApiPost.mainUnitTest();

        if bVerbose == True:

            print "";
            print "%s Klocwork Review WebAPI Post (after test) is:" % (sScriptDisp);
            print kwWebApiPost.toString();
            print "";

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print "%s The Klocwork Review WebAPI 'post' Tester #1 is ending execution from Server [%s] on [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp);
        print "";

    except Exception, inst:

        print "%s 'main()' - exception occured..." % (sScriptDisp);
        print type(inst);
        print inst;

        return False;

    return True;

if __name__ == '__main__':

    bCmdExecOk = main();

    if bCmdExecOk == False:

        print "%s Exiting with a Return Code of (31)..." % (sScriptDisp);

        sys.exit(31);

    print "%s Exiting with a Return Code of (0)..." % (sScriptDisp);

    sys.exit(0);

