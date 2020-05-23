
import optparse;
import os;
import traceback;
import platform;
import re;
import string;
import sys;

from datetime import datetime;

import CxProjectCreation1;
import CxProjectCreationCollectionCheckmarxDefaults1;
import CxProjectCreationCollectionVerizonDefaults1;
import CxProjectCreationCollectionDefaultsCalledTest1;

optParser   = optparse.OptionParser();
sScriptId   = optParser.get_prog_name();
sScriptVers = "(v1.0104)";
sScriptDisp = sScriptId+" "+sScriptVers+":"
cScriptArgc = len(sys.argv);

bVerbose    = False;

def main():

    try:

        sPythonVers = ("v%s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro));
        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("%s The Checkmarx Project 'collection' DEFAULT(S) Caller Test #1 is starting execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_true");
     
        (options, args) = optParser.parse_args();
     
        bVerbose = options.run_verbose;
     
        if bVerbose == True:
     
            print("%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose));
            print("");

        bProcessingError = False;

        cxProjDefaults = CxProjectCreationCollectionCheckmarxDefaults1.CxProjectCreationCollectionCheckmarxDefaults(trace=bVerbose);

        if cxProjDefaults == None:

            print("");
            print("%s The CxProjectCreationCollectionCheckmarxDefaults object is None - this object failed to create - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxProjectCreationCollectionCheckmarxDefaults (after init) is:" % (sScriptDisp));
            print(cxProjDefaults.toString());
            print("");

        cxProjectCreationCollection = CxProjectCreationCollectionDefaultsCalledTest1.CxProjectCreationCollectionDefaultsCalledTest(trace=bVerbose, cxprojectcreationcollectiondefaults=cxProjDefaults);

        if cxProjectCreationCollection == None:

            print("");
            print("%s The CxProjectCreationCollectionDefaultsCalledTest object is None - this object failed to create - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxProjectCreationCollectionDefaultsCalledTest (after init) is:" % (sScriptDisp));
            print(cxProjectCreationCollection.toString());
            print("");

        cxProjectCreationCollection.dumpCxProjectCreationCollectionDefaultsFromSuppliedObject();

        vzProjDefaults = CxProjectCreationCollectionVerizonDefaults1.CxProjectCreationCollectionVerizonDefaults(trace=bVerbose);

        if vzProjDefaults == None:

            print("");
            print("%s The CxProjectCreationCollectionVerizonDefaults object is None - this object failed to create - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxProjectCreationCollectionVerizonDefaults (after init) is:" % (sScriptDisp));
            print(vzProjDefaults.toString());
            print("");

        cxProjectCreationCollection.setCxProjectCreationCollectionDefaults(cxprojectcreationcollectiondefaults=vzProjDefaults);
        cxProjectCreationCollection.dumpCxProjectCreationCollectionDefaultsFromSuppliedObject();

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("");
        print("%s The Checkmarx Project 'collection' DEFAULT(S) Caller Test #1 is ending execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

    except Exception as inst:

        print("%s 'main()' - exception occured..." % (sScriptDisp));
        print(type(inst));
        print(inst);

        excType, excValue, excTraceback = sys.exc_info();
        asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

        print("- - - ");
        print('\n'.join(asTracebackLines));
        print("- - - ");

        return False;

    if bProcessingError == True:

        return False;

    return True;

if __name__ == '__main__':

    try:

        pass;

    except Exception as inst:

        print("%s '<before>-main()' - exception occured..." % (sScriptDisp));
        print(type(inst));
        print(inst);

        excType, excValue, excTraceback = sys.exc_info();
        asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

        print("- - - ");
        print('\n'.join(asTracebackLines));
        print("- - - ");

    bCmdExecOk = main();

    if bCmdExecOk == False:

        print("%s Exiting with a Return Code of (31)..." % (sScriptDisp));

        sys.exit(31);

    print("%s Exiting with a Return Code of (0)..." % (sScriptDisp));

    sys.exit(0);

