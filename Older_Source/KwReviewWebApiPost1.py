
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;

import urllib;
import urllib2;

import simplejson as json;

# -------------------------------------------------------------------------------------------------
#
# ...
#
# -------------------------------------------------------------------------------------------------

class KwReviewWebApiPost:

    sClassMod               = __name__;
    sClassId                = "KwReviewWebApiPost";
    sClassVers              = "(v1.2001)";
    sClassDisp              = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag              = False;
    bUserActionPromptFlag   = False;
    sKwServerProjectURL     = None;
    bKwUserIsSuper          = False;
    sKwBasicAuthUserID      = None;
    sKwBasicAuthPassword    = None;
    sKwSourceServerURL      = None;

    bKwBasicAuthUsedFlag    = False;

    sKwServerHostProtocol   = None;
    sKwServerHostName       = None;
    sKwServerPortNumber     = None;
    sKwServerProjectName    = None;

    iKwServerLastRespStatus = 0;
    sKwServerLastRespMsg    = None;
    sKwServerLastRespMsg2   = None;
    sKwServerLastResp       = None;
    asKwServerLastResp      = None;

    sPlatform               = None;
    bPlatformIsWindows      = False;
    sKwUserID               = None;
    sKwUserHomeDirectory    = None;

    bKwLtokenProcessingDone = False;
    sKwReviewLtokenFilespec = None;
    asKwReviewLtokens       = None;
    sKwReviewCurrLtoken     = None;
    sKwReviewCurrLtokenUser = None;

    kwHttpPasswordMgr       = None;
    kwHttpBasicAuthHandler  = None;
    kwHttpOpener            = None;

    def __init__(self, trace=False, useractionprompt=False, kwserverprojecturl=None, kwuserissuper=False, kwbasicauthuserid=None, kwbasicauthpassword=None, kwsourceserverurl=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setUserActionPromptFlag(useractionprompt=useractionprompt);
            self.setKwServerProjectURL(kwserverprojecturl=kwserverprojecturl);
            self.setKwUserIsSuperFlag(kwuserissuper=kwuserissuper);
            self.setKwBasicAuthUserID(kwbasicauthuserid=kwbasicauthuserid);
            self.setKwBasicAuthPassword(kwbasicauthpassword=kwbasicauthpassword);
            self.setKwSourceServerURL(kwsourceserverurl=kwsourceserverurl)

        except Exception, inst:

            print "%s '__init__()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

    def getTraceFlag(self):

        return self.bTraceFlag;

    def setTraceFlag(self, trace=False):

        self.bTraceFlag = trace;

    def getUserActionPromptFlag(self):

        return self.bUserActionPromptFlag;

    def setUserActionPromptFlag(self, useractionprompt=False):

        self.bUserActionPromptFlag = useractionprompt;

    def getKwServerProjectURL(self):

        return self.sKwServerProjectURL;

    def setKwServerProjectURL(self, kwserverprojecturl=None):

        self.sKwServerProjectURL = kwserverprojecturl;

        if self.sKwServerProjectURL != None:

            self.sKwServerProjectURL = self.sKwServerProjectURL.strip();

        if self.sKwServerProjectURL == None or \
           len(self.sKwServerProjectURL) < 1:

            self.sKwServerProjectURL = None;

        else:

            sKwServerProjectURLLow = self.sKwServerProjectURL.lower();

            if sKwServerProjectURLLow.startswith("http://")  == False and \
               sKwServerProjectURLLow.startswith("https://") == False:

                self.sKwServerProjectURL = None;

        self.parseKwServerProjectURL();

    def parseKwServerProjectURL(self):

        self.resetKwReviewWebApiPostObject();

        if self.sKwServerProjectURL != None:

            self.sKwServerProjectURL = self.sKwServerProjectURL.strip();

        if self.sKwServerProjectURL == None or \
           len(self.sKwServerProjectURL) < 1:

            self.sKwServerProjectURL = None;

            return;

        sKwServerProjectURLLow = self.sKwServerProjectURL.lower();

        if sKwServerProjectURLLow.startswith("http://")  == False and \
           sKwServerProjectURLLow.startswith("https://") == False:

            self.sKwServerProjectURL = None;

            return;

        asProtocolSplit = self.sKwServerProjectURL.partition("://");

        if asProtocolSplit == None or \
           len(asProtocolSplit) < 1:

            self.sKwServerProjectURL = None;

            return;

        self.sKwServerHostProtocol = asProtocolSplit[0];

        if self.sKwServerHostProtocol != None:

            self.sKwServerHostProtocol = self.sKwServerHostProtocol.strip();

        if self.sKwServerHostProtocol == None or \
           len(self.sKwServerHostProtocol) < 1:

            self.sKwServerHostProtocol = None;

        else:

            self.sKwServerHostProtocol = self.sKwServerHostProtocol.lower();

        if len(asProtocolSplit) < 3:

            return;

        sKwServerProjectRaw = asProtocolSplit[2];

        if sKwServerProjectRaw != None:

            sKwServerProjectRaw = sKwServerProjectRaw.strip();

        if sKwServerProjectRaw == None or \
           len(sKwServerProjectRaw) < 1:

            return;

        asServerProjectSplit = sKwServerProjectRaw.partition("/");

        if asServerProjectSplit == None or \
           len(asServerProjectSplit) < 1:

            return;

        if len(asServerProjectSplit) >= 1:

            self.sKwServerHostName = asServerProjectSplit[0];

            if len(asServerProjectSplit) >= 3:

                self.sKwServerProjectName = asServerProjectSplit[2];

        if self.sKwServerHostName != None:

            self.sKwServerHostName = self.sKwServerHostName.strip();

        if self.sKwServerHostName != None and \
           len(self.sKwServerHostName) > 0:

            asServerHostPortSplit = self.sKwServerHostName.partition(":");

            if asServerHostPortSplit == None or \
               len(asServerHostPortSplit) < 1:

                return;

            if len(asServerHostPortSplit) >= 1:

                self.sKwServerHostName = asServerHostPortSplit[0];

                if len(asServerHostPortSplit) >= 3:

                    self.sKwServerPortNumber = asServerHostPortSplit[2];

    #   self.determineOSUserHomeDir();
    #   self.determineKwReviewLtoken();

        return;

    def resetKwReviewWebApiPostObject(self):

        self.sKwServerHostProtocol   = None;
        self.sKwServerHostName       = None;
        self.sKwServerPortNumber     = None;
        self.sKwServerProjectName    = None;

        self.iKwServerLastRespStatus = 0;
        self.sKwServerLastRespMsg    = None;
        self.sKwServerLastRespMsg2   = None;
        self.sKwServerLastResp       = None;
        self.asKwServerLastResp      = None;

        self.sPlatform               = None;
        self.bPlatformIsWindows      = False;
        self.sKwUserID               = None;
        self.sKwUserHomeDirectory    = None;

        self.bKwLtokenProcessingDone = False;
        self.sKwReviewLtokenFilespec = None;
        self.asKwReviewLtokens       = None;
        self.sKwReviewCurrLtoken     = None;
        self.sKwReviewCurrLtokenUser = None;

        self.kwHttpPasswordMgr       = None;
        self.kwHttpBasicAuthHandler  = None;
        self.kwHttpOpener            = None;

        return;

    def getKwUserIsSuperFlag(self):

        return self.bKwUserIsSuper;

    def setKwUserIsSuperFlag(self, kwuserissuper=False):

        self.bKwUserIsSuper = kwuserissuper;

    def getKwBasicAuthUserID(self):

        return self.sKwBasicAuthUserID;

    def setKwBasicAuthUserID(self, kwbasicauthuserid=None):

        self.sKwBasicAuthUserID = kwbasicauthuserid;

        if self.sKwBasicAuthUserID != None:

            self.sKwBasicAuthUserID = self.sKwBasicAuthUserID.strip();

        if self.sKwBasicAuthUserID == None or \
           len(self.sKwBasicAuthUserID) < 1:

            self.sKwBasicAuthUserID = None;

        if self.sKwBasicAuthPassword != None:

            self.sKwBasicAuthPassword = self.sKwBasicAuthPassword.strip();

        if self.sKwBasicAuthPassword != None and \
           len(self.sKwBasicAuthPassword) > 0:

            self.bKwBasicAuthUsedFlag = True;

        return;

    def getKwBasicAuthPassword(self):

        return self.sKwBasicAuthPassword;

    def setKwBasicAuthPassword(self, kwbasicauthpassword=None):

        self.sKwBasicAuthPassword = kwbasicauthpassword;

        if self.sKwBasicAuthPassword != None:

            self.sKwBasicAuthPassword = self.sKwBasicAuthPassword.strip();

        if self.sKwBasicAuthPassword == None or \
           len(self.sKwBasicAuthPassword) < 1:

        #   self.sKwBasicAuthPassword = None;
            self.sKwBasicAuthPassword = "";

        if self.sKwBasicAuthUserID != None:

            self.sKwBasicAuthUserID = self.sKwBasicAuthUserID.strip();

        if self.sKwBasicAuthUserID != None and \
           len(self.sKwBasicAuthUserID) > 0:

            self.bKwBasicAuthUsedFlag = True;

        return;

    def getKwSourceServerURL(self):

        return self.sKwSourceServerURL;

    def setKwSourceServerURL(self, kwsourceserverurl=None):

        self.sKwSourceServerURL = kwsourceserverurl;

        if self.sKwSourceServerURL != None:

            self.sKwSourceServerURL = self.sKwSourceServerURL.strip();

        if self.sKwSourceServerURL == None or \
           len(self.sKwSourceServerURL) < 1:

            self.sKwSourceServerURL = None;

        else:

            sKwSourceServerURLLow = self.sKwSourceServerURL.lower();

            if sKwSourceServerURLLow.startswith("http://")  == False and \
               sKwSourceServerURLLow.startswith("https://") == False:

                self.sKwSourceServerURL = None;

    def getKwServerHostProtocol(self):

        return self.sKwServerHostProtocol;

    def getKwServerHostName(self):

        return self.sKwServerHostName;

    def getKwServerPortNumber(self):

        return self.sKwServerPortNumber;

    def getKwServerProjectName(self):

        return self.sKwServerProjectName;

    def getKwServerLastResponseStatus(self):

        return self.iKwServerLastRespStatus;

    def getKwServerLastResponseMsg(self):

        return self.sKwServerLastRespMsg;

    def getKwServerLastResponseMsg2(self):

        return self.sKwServerLastRespMsg2;

    def getKwServerLastResponse(self):

        return self.sKwServerLastResp;

    def getKwServerLastResponseAsList(self):

        return self.asKwServerLastResp;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);
            print "%s The 'bUserActionPromptFlag' boolean is [%s]..." % (self.sClassDisp, self.bUserActionPromptFlag);
            print "%s The contents of 'sKwServerProjectURL' is [%s]..." % (self.sClassDisp, self.sKwServerProjectURL);
            print "%s The contents of 'bKwUserIsSuper' is [%s]..." % (self.sClassDisp, self.bKwUserIsSuper);
            print "%s The contents of 'sKwBasicAuthUserID' is [%s]..." % (self.sClassDisp, self.sKwBasicAuthUserID);
            print "%s The contents of 'sKwBasicAuthPassword' is [%s]..." % (self.sClassDisp, self.sKwBasicAuthPassword);
            print "%s The contents of 'sKwSourceServerURL' is [%s]..." % (self.sClassDisp, self.sKwSourceServerURL);
            print "%s The contents of 'bKwBasicAuthUsedFlag' is [%s]..." % (self.sClassDisp, self.bKwBasicAuthUsedFlag);
            print "%s The contents of 'sKwServerHostProtocol' is [%s]..." % (self.sClassDisp, self.sKwServerHostProtocol);
            print "%s The contents of 'sKwServerHostName' is [%s]..." % (self.sClassDisp, self.sKwServerHostName);
            print "%s The contents of 'sKwServerPortNumber' is [%s]..." % (self.sClassDisp, self.sKwServerPortNumber);
            print "%s The contents of 'sKwServerProjectName' is [%s]..." % (self.sClassDisp, self.sKwServerProjectName);
            print "%s The contents of 'iKwServerLastRespStatus' is (%d)..." % (self.sClassDisp, self.iKwServerLastRespStatus);
            print "%s The contents of 'sKwServerLastRespMsg' is [%s]..." % (self.sClassDisp, self.sKwServerLastRespMsg);
            print "%s The contents of 'sKwServerLastRespMsg2' is [%s]..." % (self.sClassDisp, self.sKwServerLastRespMsg2);
            print "%s The contents of 'sKwServerLastResp' is [%s]..." % (self.sClassDisp, self.sKwServerLastResp);
            print "%s The contents of 'asKwServerLastResp' is [%s]..." % (self.sClassDisp, self.asKwServerLastResp);
            print "%s The contents of 'sPlatform' is [%s]..." % (self.sClassDisp, self.sPlatform);
            print "%s The contents of 'bPlatformIsWindows' is [%s]..." % (self.sClassDisp, self.bPlatformIsWindows);
            print "%s The contents of 'sKwUserID' is [%s]..." % (self.sClassDisp, self.sKwUserID);
            print "%s The contents of 'sKwUserHomeDirectory' is [%s]..." % (self.sClassDisp, self.sKwUserHomeDirectory);
            print "%s The contents of 'bKwLtokenProcessingDone' is [%s]..." % (self.sClassDisp, self.bKwLtokenProcessingDone);
            print "%s The contents of 'sKwReviewLtokenFilespec' is [%s]..." % (self.sClassDisp, self.sKwReviewLtokenFilespec);
            print "%s The contents of 'asKwReviewLtokens' is [%s]..." % (self.sClassDisp, self.asKwReviewLtokens);
            print "%s The contents of 'sKwReviewCurrLtoken' is [%s]..." % (self.sClassDisp, self.sKwReviewCurrLtoken);
            print "%s The contents of 'sKwReviewCurrLtokenUser' is [%s]..." % (self.sClassDisp, self.sKwReviewCurrLtokenUser);
            print "%s The contents of 'kwHttpPasswordMgr' is [%s]..." % (self.sClassDisp, self.kwHttpPasswordMgr);
            print "%s The contents of 'kwHttpBasicAuthHandler' is [%s]..." % (self.sClassDisp, self.kwHttpBasicAuthHandler);
            print "%s The contents of 'kwHttpOpener' is [%s]..." % (self.sClassDisp, self.kwHttpOpener);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'bUserActionPromptFlag' is [%s], " % (self.bUserActionPromptFlag));
        asObjDetail.append("'sKwServerProjectURL' is [%s], " % (self.sKwServerProjectURL));
        asObjDetail.append("'bKwUserIsSuper' is [%s], " % (self.bKwUserIsSuper));
        asObjDetail.append("'sKwBasicAuthUserID' is [%s], " % (self.sKwBasicAuthUserID));
        asObjDetail.append("'sKwBasicAuthPassword' is [%s], " % (self.sKwBasicAuthPassword));
        asObjDetail.append("'sKwSourceServerURL' is [%s], " % (self.sKwSourceServerURL));
        asObjDetail.append("'bKwBasicAuthUsedFlag' is [%s], " % (self.bKwBasicAuthUsedFlag));
        asObjDetail.append("'sKwServerHostProtocol' is [%s], " % (self.sKwServerHostProtocol));
        asObjDetail.append("'sKwServerHostName' is [%s], " % (self.sKwServerHostName));
        asObjDetail.append("'sKwServerPortNumber' is [%s], " % (self.sKwServerPortNumber));
        asObjDetail.append("'sKwServerProjectName' is [%s], " % (self.sKwServerProjectName));
        asObjDetail.append("'iKwServerLastRespStatus' is (%d), " % (self.iKwServerLastRespStatus));
        asObjDetail.append("'sKwServerLastRespMsg' is [%s], " % (self.sKwServerLastRespMsg));
        asObjDetail.append("'sKwServerLastRespMsg2' is [%s], " % (self.sKwServerLastRespMsg2));
        asObjDetail.append("'sKwServerLastResp' is [%s], " % (self.sKwServerLastResp));
        asObjDetail.append("'asKwServerLastResp' is [%s], " % (self.asKwServerLastResp));
        asObjDetail.append("'sPlatform' is [%s], " % (self.sPlatform));
        asObjDetail.append("'bPlatformIsWindows' is [%s], " % (self.bPlatformIsWindows));
        asObjDetail.append("'sKwUserID' is [%s], " % (self.sKwUserID));
        asObjDetail.append("'sKwUserHomeDirectory' is [%s], " % (self.sKwUserHomeDirectory));
        asObjDetail.append("'bKwLtokenProcessingDone' is [%s], " % (self.bKwLtokenProcessingDone));
        asObjDetail.append("'sKwReviewLtokenFilespec' is [%s], " % (self.sKwReviewLtokenFilespec));
        asObjDetail.append("'asKwReviewLtokens' is [%s], " % (self.asKwReviewLtokens));
        asObjDetail.append("'sKwReviewCurrLtokenUser' is [%s], " % (self.sKwReviewCurrLtokenUser));
        asObjDetail.append("'sKwReviewCurrLtoken' is [%s], " % (self.sKwReviewCurrLtoken));
        asObjDetail.append("'kwHttpPasswordMgr' is [%s], " % (self.kwHttpPasswordMgr));
        asObjDetail.append("'kwHttpBasicAuthHandler' is [%s], " % (self.kwHttpBasicAuthHandler));
        asObjDetail.append("'kwHttpOpener' is [%s]. " % (self.kwHttpOpener));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def handleLtokenProcessing(self):

        try:

            if self.bKwLtokenProcessingDone == True:

                if self.bTraceFlag == True:

                    print "%s The flag 'bKwLtokenProcessingDone' is [%s] indicating that the 'ltoken' processing has been done - bypassing further processing..." % (self.sClassDisp, self.bKwLtokenProcessingDone);

                return;

            self.determineOSUserHomeDir();
            self.determineKwReviewLtoken();

        except Exception, inst:

            print "%s 'handleLtokenProcessing()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return;

        return;

    def determineOSUserHomeDir(self):

        try:

            self.sKwUserID            = None;
            self.sKwUserHomeDirectory = None;
            self.sPlatform            = platform.system();
            self.bPlatformIsWindows   = self.sPlatform.startswith('Windows');

            if self.bPlatformIsWindows == False:

                self.bPlatformIsWindows = self.sPlatform.startswith('Microsoft');

            if self.bPlatformIsWindows == True:

                import win32api;

                if self.bTraceFlag == True:

                    print "%s The platform 'system' of [%s] indicates this is a Microsoft/Windows system - 'win32api' has been imported..." % (self.sClassDisp, self.sPlatform);

                self.sKwUserID = win32api.GetUserName();

            else:

                self.sKwUserID = os.getlogin();

            self.sKwUserHomeDirectory = os.path.expanduser('~');

            if self.bTraceFlag == True:

                print "%s The platform 'system' is [%s]..." % (self.sClassDisp, self.sPlatform);
                print "%s The platform 'system' is 'Windows' [%s]..." % (self.sClassDisp, self.bPlatformIsWindows);
                print "%s The platform 'UserID' is [%s]..." % (self.sClassDisp, self.sKwUserID);
                print "%s The platform 'User' HOME Directory is [%s]..." % (self.sClassDisp, self.sKwUserHomeDirectory);
                print "";

        except Exception, inst:

            print "%s 'determineOSUserHomeDir()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return;

        return;

    def determineKwReviewLtoken(self):

        try:

            self.bKwLtokenProcessingDone = False;
            self.asKwReviewLtokens       = None;
            self.sKwReviewCurrLtoken     = None;
            sKwLtokenFilename            = os.path.join(self.sKwUserHomeDirectory, ".klocwork", "ltoken");
            self.sKwReviewLtokenFilespec = os.path.realpath(sKwLtokenFilename);
            bKwReviewLtokenIsFile        = os.path.isfile(self.sKwReviewLtokenFilespec);

            if bKwReviewLtokenIsFile == False:

                if self.bTraceFlag == True:

                    print "%s Command received a Klocwork 'ltoken' file of [%s] that does NOT exist - Warning!" % (self.sClassDisp, self.sKwReviewLtokenFilespec);

                return;

            cKwReviewLtokenFile = os.path.getsize(self.sKwReviewLtokenFilespec);

            if cKwReviewLtokenFile < 1:

                if self.bTraceFlag == True:

                    print "%s Command received a Klocwork 'ltoken' file of [%s] that is Empty (contains 0 bytes) - Warning!" % (self.sClassDisp, self.sKwReviewLtokenFilespec);

                return;

            if self.bTraceFlag == True:

                print "%s Processing a Klocwork 'ltoken' file of [%s] containing (%d) bytes of data..." % (self.sClassDisp, self.sKwReviewLtokenFilespec, cKwReviewLtokenFile);
                print "";

            fKwReviewLtoken        = open(self.sKwReviewLtokenFilespec, "r");
            self.asKwReviewLtokens = fKwReviewLtoken.readlines();

            fKwReviewLtoken.close();

            if len(self.asKwReviewLtokens) < 1:

                if self.bTraceFlag == True:

                    print "%s Read a Klocwork 'ltoken' file of [%s] with (0) input lines - Warning!" % (self.sClassDisp, self.sKwReviewLtokenFilespec);

                return;

        #   sKwLtokenSearch    = "%s;%s;%s;" % (self.sKwServerHostName, self.sKwServerPortNumber, self.sKwUserID);
            sKwLtokenSearch    = "%s;%s;" % (self.sKwServerHostName, self.sKwServerPortNumber);
            sKwLtokenSearchLow = sKwLtokenSearch.lower();

            if self.bTraceFlag == True:

                print "%s Processing a Klocwork 'ltoken' file of [%s] containing (%d) lines of data - searching for a line beginning with [%s]..." % (self.sClassDisp, self.sKwReviewLtokenFilespec, len(self.asKwReviewLtokens), sKwLtokenSearchLow);
                print "";

            idKwReviewLtokensLine  = 0;
            asKwReviewLtokenFields = None;

            for sKwReviewLtokensLine in self.asKwReviewLtokens:

                idKwReviewLtokensLine += 1;

                if self.bTraceFlag == True:

                    print "%s Processing the Klocwork 'ltoken' file of [%s] line #(%d) of [%s]..." % (self.sClassDisp, self.sKwReviewLtokenFilespec, idKwReviewLtokensLine, sKwReviewLtokensLine);

                if sKwReviewLtokensLine != None:

                    sKwReviewLtokensLine = sKwReviewLtokensLine.strip();

                if sKwReviewLtokensLine == None or \
                   len(sKwReviewLtokensLine) < 1:

                    if self.bTraceFlag == True:

                        print "%s For the Klocwork 'ltoken' file of [%s] line #(%d) of [%s] - the line is 'empty' after 'cleaning' - bypassing the line..." % (self.sClassDisp, self.sKwReviewLtokenFilespec, idKwReviewLtokensLine, sKwReviewLtokensLine);

                    continue;

                sKwReviewLtokensLineLow = sKwReviewLtokensLine.lower();

                if sKwReviewLtokensLineLow.startswith(sKwLtokenSearchLow) == False:

                    if self.bTraceFlag == True:

                        print "%s For the Klocwork 'ltoken' file of [%s] line #(%d) of [%s] - the line does NOT begin with [%s] - bypassing the line..." % (self.sClassDisp, self.sKwReviewLtokenFilespec, idKwReviewLtokensLine, sKwReviewLtokensLine, sKwLtokenSearchLow);

                    continue;

            #   asKwReviewLtokens = sKwReviewLtokensLine.rpartition(";");
            #
            #   if asKwReviewLtokens != None and \
            #      len(asKwReviewLtokens) > 0:
            #
            #       sKwReviewLtoken0 = asKwReviewLtokens[0];
            #
            #       if sKwReviewLtoken0 != None:
            #
            #           sKwReviewLtoken0 = sKwReviewLtoken0.strip();
            #
            #       if sKwReviewLtoken0 != None and \
            #          len(sKwReviewLtoken0) > 0:
            #
            #       #   self.sKwReviewCurrLtoken = sKwReviewLtokensLine[len(sKwLtokenSearch):];
            #           self.sKwReviewCurrLtoken = asKwReviewLtokens[2];
            #
            #           if self.sKwReviewCurrLtoken != None:
            #
            #               self.sKwReviewCurrLtoken = self.sKwReviewCurrLtoken.strip();
            #
            #           if self.sKwReviewCurrLtoken == None or \
            #              len(self.sKwReviewCurrLtoken) < 1:
            #
            #               self.sKwReviewCurrLtoken = None;
            #
            #           else:
            #
            #               if self.sKwReviewCurrLtoken == "null":
            #
            #                   self.sKwReviewCurrLtoken = None;
            #
            #           break;
            #
            #       else:
            #
            #           continue;
            #
            #   else:
            #
            #       continue;

                if self.bTraceFlag == True:

                    print "%s For the Klocwork 'ltoken' file of [%s] line #(%d) of [%s] - the line DOES begin with [%s] - processing the line..." % (self.sClassDisp, self.sKwReviewLtokenFilespec, idKwReviewLtokensLine, sKwReviewLtokensLine, sKwLtokenSearchLow);

                asKwReviewLtokenFields = sKwReviewLtokensLine.split(";");

                if asKwReviewLtokenFields != None and \
                   len(asKwReviewLtokenFields) > 0:

                    if self.bTraceFlag == True:

                        print "%s For 'ltoken' line #(%d) of [%s] - the (%d) 'ltoken' field(s) are [%s]..." % (self.sClassDisp, idKwReviewLtokensLine, sKwReviewLtokensLine, len(asKwReviewLtokenFields), asKwReviewLtokenFields);
                
                    if len(asKwReviewLtokenFields) > 2:

                        sCurrLtokenUser = asKwReviewLtokenFields[2];

                        if sCurrLtokenUser != None:
                        
                            sCurrLtokenUser = sCurrLtokenUser.strip();
                        
                        if sCurrLtokenUser == None or \
                           len(sCurrLtokenUser) < 1:
                        
                            sCurrLtokenUser = None;
                        
                        self.sKwReviewCurrLtokenUser = sCurrLtokenUser;

                        if self.bTraceFlag == True:

                            print "%s 'ltoken' field 'self.sKwReviewCurrLtokenUser' set to [%s]..." % (self.sClassDisp, self.sKwReviewCurrLtokenUser);

                        if len(asKwReviewLtokenFields) > 3:

                            sCurrLtoken = asKwReviewLtokenFields[3];

                            if sCurrLtoken != None:
                            
                                sCurrLtoken = sCurrLtoken.strip();
                            
                            if sCurrLtoken == None or \
                               len(sCurrLtoken) < 1:
                            
                                sCurrLtoken = None;
                            
                            self.sKwReviewCurrLtoken = sCurrLtoken;

                            if self.bTraceFlag == True:

                                print "%s 'ltoken' field 'self.sKwReviewCurrLtoken' set to [%s]..." % (self.sClassDisp, self.sKwReviewCurrLtoken);

                        self.bKwLtokenProcessingDone = True;

            if self.bTraceFlag == True:

                print "%s The contents of 'bKwLtokenProcessingDone' is [%s]..." % (self.sClassDisp, self.bKwLtokenProcessingDone);
                print "%s The contents of 'sKwReviewLtokenFilespec' is [%s]..." % (self.sClassDisp, self.sKwReviewLtokenFilespec);
                print "%s The contents of 'asKwReviewLtokens' is [%s]..." % (self.sClassDisp, self.asKwReviewLtokens);
                print "%s The contents of 'asKwReviewLtokenFields' is [%s]..." % (self.sClassDisp, asKwReviewLtokenFields);
                print "%s The contents of 'sKwReviewCurrLtoken' is [%s]..." % (self.sClassDisp, self.sKwReviewCurrLtoken);
                print "%s The contents of 'sKwReviewCurrLtokenUser' is [%s]..." % (self.sClassDisp, self.sKwReviewCurrLtokenUser);
                print "";

        except Exception, inst:

            self.bKwLtokenProcessingDone = False;

            print "%s 'determineKwReviewLtoken()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return;

        return;

    def postHttpRequest2(self, url, postdata={}, headers={}, idhttppostresp=0):

        self.handleLtokenProcessing();

        sHttpPostURL       = url;
        dictHttpPostData   = postdata;
        dictHttpHeaderData = headers;
        idKwWebApiPost     = idhttppostresp;

        try:

            if sHttpPostURL != None:

                sHttpPostURL = sHttpPostURL.strip();

            if sHttpPostURL == None or \
               len(sHttpPostURL) < 1:

                print "%s 'postHttpRequest2()' - The supplied HTTP 'post' URL string is None or 'empty' - this MUST be supplied - Error!" % (self.sClassDisp, sHttpPostURL);

                return None;

            sHttpPostData = None;

            if dictHttpPostData != None and \
               len(dictHttpPostData) > 0:

                sHttpPostData = urllib.urlencode(dictHttpPostData);

            if self.bTraceFlag == True:

                print "%s 'postHttpRequest2()' - Sending a Http 'post' #(%d) with 'data' of [%s] with 'headers' of [%s] to a URL of [%s]..." % (self.sClassDisp, idKwWebApiPost, sHttpPostData, dictHttpHeaderData, sHttpPostURL);
                print "";

            urlRequest = None;

            if dictHttpHeaderData == None or \
               len(dictHttpHeaderData) < 1:

                urlRequest = urllib2.Request(sHttpPostURL, sHttpPostData);

            else:

                urlRequest = urllib2.Request(sHttpPostURL, sHttpPostData, dictHttpHeaderData);

            if self.bKwBasicAuthUsedFlag == True and \
               self.kwHttpPasswordMgr    == None:

                sHttpTopURL = "%s://%s:%s/review/" % (self.sKwServerHostProtocol, self.sKwServerHostName, self.sKwServerPortNumber);
                self.kwHttpPasswordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm();

                self.kwHttpPasswordMgr.add_password(None, sHttpTopURL, self.sKwBasicAuthUserID, self.sKwBasicAuthPassword);

                self.kwHttpBasicAuthHandler = urllib2.HTTPBasicAuthHandler(self.kwHttpPasswordMgr);
                self.kwHttpOpener           = urllib2.build_opener(self.kwHttpBasicAuthHandler);

                urllib2.install_opener(self.kwHttpOpener);

                if self.bTraceFlag == True:

                    print "%s 'postHttpRequest2()' - HTTP 'basic' authentication setup for a UserID of [%s] for a 'top-level' URL of [%s]..." % (self.sClassDisp, self.sKwBasicAuthUserID, sHttpTopURL);
                    print "";

            self.iKwServerLastRespStatus = 0;
            self.sKwServerLastRespMsg    = None;
            self.sKwServerLastRespMsg2   = None;
            self.sKwServerLastResp       = None;
            self.asKwServerLastResp      = None;

            urlResponse = urllib2.urlopen(urlRequest);

            if urlResponse == None:

                print "%s 'postHttpRequest2()' - The Http 'post' #(%d) with 'data' of [%s] with 'headers' of [%s] to a URL of [%s] returned a 'response' object that is None - Error!" % (self.sClassDisp, idKwWebApiPost, sHttpPostData, dictHttpHeaderData, sHttpPostURL);

                return None;

        #   self.iKwServerLastRespStatus = urlResponse.getcode();
            self.iKwServerLastRespStatus = urlResponse.code;
            self.sKwServerLastRespMsg    = urlResponse.msg;

            if self.iKwServerLastRespStatus == 200 or \
               self.iKwServerLastRespStatus == 500:

                asHttpPostRespLines = urlResponse.readlines();

                if asHttpPostRespLines != None and \
                   len(asHttpPostRespLines) > 0:

                    self.sKwServerLastResp = '\n'.join(asHttpPostRespLines);

                    if self.asKwServerLastResp == None:

                        self.asKwServerLastResp = list();

                    if self.bTraceFlag == True:

                        print "%s Http POST Response Data #(%d) split into (%d) line(s)..." % (self.sClassDisp, idKwWebApiPost, len(asHttpPostRespLines));
                        print "";

                    idJsonRespLine = 0;

                    for sJsonRespLine in asHttpPostRespLines:

                        idJsonRespLine += 1;
                        sJsonRespLine   = sJsonRespLine.strip();
                        dictJsonResp    = json.loads(sJsonRespLine);

                        if dictJsonResp == None or \
                           len(dictJsonResp) < 1:

                            dictJsonResp = None;

                        self.asKwServerLastResp.append(dictJsonResp);

                        sDictJsonRespMsg = None;

                        if "message" in dictJsonResp.keys():
                         
                            sDictJsonRespMsg = dictJsonResp["message"];

                        if sDictJsonRespMsg != None:
                         
                            sDictJsonRespMsg = sDictJsonRespMsg.strip();
                         
                        if sDictJsonRespMsg == None or \
                           len(sDictJsonRespMsg) < 1:
                         
                            sDictJsonRespMsg = "";

                        self.sKwServerLastRespMsg2 = sDictJsonRespMsg;
                         
                else:

                    if self.bTraceFlag == True:

                        print "%s Http POST Response Data #(%d) contained NO line(s) - Warning!" % (self.sClassDisp, idKwWebApiPost);
                        print "";

                    self.sKwServerLastResp  = None;
                    self.asKwServerLastResp = None;

            else:

                if self.bTraceFlag == True:

                    print "%s Http ERROR:" % (self.sClassDisp);
                    print "%s Http 'status' is [%s]..." % (self.sClassDisp, self.iKwServerLastRespStatus);
                    print "%s Http 'msg'    is [%s]..." % (self.sClassDisp, urlResponse.msg);
                    print "";

                dictJsonResp = {"status": self.iKwServerLastRespStatus, "message": urlResponse.msg};

                if self.asKwServerLastResp == None:

                    self.asKwServerLastResp = list();

                self.asKwServerLastResp.append(dictJsonResp);

                self.sKwServerLastResp = "%s" % (dictJsonResp);

                sDictJsonRespMsg = None;

                if "message" in dictJsonResp.keys():

                    sDictJsonRespMsg = dictJsonResp["message"];

                if sDictJsonRespMsg != None:

                    sDictJsonRespMsg = sDictJsonRespMsg.strip();

                if sDictJsonRespMsg == None or \
                   len(sDictJsonRespMsg) < 1:

                    sDictJsonRespMsg = "";

                self.sKwServerLastRespMsg2 = sDictJsonRespMsg;

        except urllib2.HTTPError, inst:

            if self.bTraceFlag == True:

                print "%s 'postHttpRequest2()' - 'urllib2.HTTPError' exception occured (and caught)..." % (self.sClassDisp);
                print type(inst);
                print inst;
                print "";

            urlResponse = inst;

            self.iKwServerLastRespStatus = urlResponse.code;
            self.sKwServerLastRespMsg    = urlResponse.msg;

            asHttpPostRespLines = urlResponse.readlines();

            if asHttpPostRespLines != None and \
               len(asHttpPostRespLines) > 0:

                self.sKwServerLastResp = '\n'.join(asHttpPostRespLines);

                if self.asKwServerLastResp == None:

                    self.asKwServerLastResp = list();

                if self.bTraceFlag == True:

                    print "%s Http POST (500) Response Data #(%d) split into (%d) line(s)..." % (self.sClassDisp, idKwWebApiPost, len(asHttpPostRespLines));
                    print "";

                idJsonRespLine = 0;

                for sJsonRespLine in asHttpPostRespLines:

                    idJsonRespLine += 1;
                    sJsonRespLine   = sJsonRespLine.strip();
                    dictJsonResp    = json.loads(sJsonRespLine);

                    if dictJsonResp == None or \
                       len(dictJsonResp) < 1:

                        dictJsonResp = None;

                    self.asKwServerLastResp.append(dictJsonResp);
                    
                    sDictJsonRespMsg = None;

                    if "message" in dictJsonResp.keys():

                        sDictJsonRespMsg = dictJsonResp["message"];

                    if sDictJsonRespMsg != None:
                     
                        sDictJsonRespMsg = sDictJsonRespMsg.strip();
                     
                    if sDictJsonRespMsg == None or \
                       len(sDictJsonRespMsg) < 1:
                     
                        sDictJsonRespMsg = "";

                    self.sKwServerLastRespMsg2 = sDictJsonRespMsg;


            else:

                if self.bTraceFlag == True:

                    print "%s Http POST Response Data #(%d) contained NO line(s) - Warning!" % (self.sClassDisp, idKwWebApiPost);
                    print "";

                self.sKwServerLastResp  = None;
                self.asKwServerLastResp = None;

            return self.sKwServerLastResp;

        except Exception, inst:

            print "%s 'postHttpRequest2()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return None;

        return self.sKwServerLastResp;

    def postKwWebApiRequest(self, postdata={}, headers={}, idhttppostresp=0):

        self.handleLtokenProcessing();

        dictHttpPostData   = postdata;
        dictHttpHeaderData = headers;
        idKwWebApiPost     = idhttppostresp;

        try:

            if self.bKwBasicAuthUsedFlag == True and \
               self.kwHttpPasswordMgr    == None:

                self.sKwUserID           = self.sKwBasicAuthUserID;
                self.sKwReviewCurrLtoken = None;

            if self.sKwUserID != None:

                self.sKwUserID = self.sKwUserID.strip();

            if self.sKwUserID != None and \
               len(self.sKwUserID) > 0:

                dictHttpPostData["user"] = self.sKwUserID;

            if self.sKwReviewCurrLtoken != None:

                self.sKwReviewCurrLtoken = self.sKwReviewCurrLtoken.strip();

            if self.sKwReviewCurrLtoken != None and \
               len(self.sKwReviewCurrLtoken) > 0:

                dictHttpPostData["ltoken"] = self.sKwReviewCurrLtoken;
                dictHttpPostData["user"]   = self.sKwReviewCurrLtokenUser;

            if self.bKwUserIsSuper == True:
            
                dictHttpPostData["sourceURL"]      = self.sKwSourceServerURL;
                dictHttpPostData["sourceAdmin"]    = self.sKwBasicAuthUserID;
                dictHttpPostData["sourcePassword"] = self.sKwBasicAuthPassword;

            sHttpPostURL = "%s://%s:%s/review/api" % (self.sKwServerHostProtocol, self.sKwServerHostName, self.sKwServerPortNumber);

            self.postHttpRequest2(sHttpPostURL, postdata=dictHttpPostData, headers=dictHttpHeaderData, idhttppostresp=idKwWebApiPost);

            if self.bTraceFlag == True:

                self.dumpLastKwWebApiResponse(idhttppostresp=idKwWebApiPost);

            if self.bUserActionPromptFlag == True:

                raw_input("Press <enter> to continue...");

        except Exception, inst:

            print "%s 'postKwWebApiRequest()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return None;

        return self.sKwServerLastResp;

    def dumpLastKwWebApiResponse(self, idhttppostresp=0):

        idHttpPostResp = idhttppostresp;

        if self.bTraceFlag == True:

            print "%s Last Http POST Response Data #(%d) was [%s]..." % (self.sClassDisp, idHttpPostResp, self.sKwServerLastResp);
            print "";

        if self.asKwServerLastResp != None and \
           len(self.asKwServerLastResp) > 0:

            if self.bTraceFlag == True:

                print "%s Http POST Response Data #(%d) split into (%d) line(s)..." % (self.sClassDisp, idHttpPostResp, len(self.asKwServerLastResp));
                print "";

            idJsonRespLine = 0;

            for dictJsonResp in self.asKwServerLastResp:

                idJsonRespLine += 1;

                if dictJsonResp != None and \
                   len(dictJsonResp) > 0:

                    if self.bTraceFlag == True:

                        print "%s 'dictJsonResp' #(%d).(%d) is [%s]..." % (self.sClassDisp, idHttpPostResp, idJsonRespLine, dictJsonResp);
                        print "";

                    print "'dictJsonResp' #(%d).(%d) break-down:" % (idHttpPostResp, idJsonRespLine);

                    for sJsonKey in dictJsonResp.keys():

                        print "#(%d).(%d) - KEY [%s] Value [%s]..." % (idHttpPostResp, idJsonRespLine, sJsonKey, dictJsonResp[sJsonKey]);

                    print "";

            if self.bTraceFlag == True:

                print "";

        else:

            print "%s Http POST Response Data #(%d) contained NO line(s) - Warning!" % (self.sClassDisp, idHttpPostResp);
            print "";

        return;

    def mainUnitTest(self):

        try:

            print "%s Executing the KwReviewWebApiPost #1 'UnitTest'..." % (self.sClassDisp);
            print "";

            if self.sKwServerProjectURL != None:

                self.sKwServerProjectURL = self.sKwServerProjectURL.strip();

            if self.sKwServerProjectURL == None or \
               len(self.sKwServerProjectURL) < 1:

            #   self.setKwServerProjectURL(kwserverprojecturl="http://darylcoxe36c:8080/CVS");
            #   self.setKwServerProjectURL(kwserverprojecturl="http://192.168.1.134:8080/CVS");
                self.setKwServerProjectURL(kwserverprojecturl="http://192.168.1.162:8080/TestBugTracking");

            if self.bTraceFlag == True:

                self.dump_fields();

                print "";

            dictHttpPostData           = collections.defaultdict();
            dictHttpPostData["action"] = "projects";

            idUnitTest = 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "builds";
            dictHttpPostData["project"] = self.sKwServerProjectName;

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "views";
            dictHttpPostData["project"] = self.sKwServerProjectName;

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "modules";
            dictHttpPostData["project"] = self.sKwServerProjectName;

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "views";
            dictHttpPostData["project"] = "XYZ_123";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "search";
            dictHttpPostData["project"] = self.sKwServerProjectName;
            dictHttpPostData["view"]    = "*default*";
            dictHttpPostData["query"]   = "status:+Analyze severity:1";
            dictHttpPostData["limit"]   = "5";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "search";
            dictHttpPostData["project"] = self.sKwServerProjectName;
            dictHttpPostData["query"]   = "code:MLK";
            dictHttpPostData["limit"]   = "10";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "search";
            dictHttpPostData["project"] = self.sKwServerProjectName;
            dictHttpPostData["query"]   = "'MLK'";
            dictHttpPostData["limit"]   = "15";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postKwWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            print "%s Executed the KwReviewWebApiPost #1 'UnitTest'..." % (self.sClassDisp);
            print "";

        except Exception, inst:

            print "%s 'mainUnitTest()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

