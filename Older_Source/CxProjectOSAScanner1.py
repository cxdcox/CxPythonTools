
import optparse;
import os;
import traceback;
import platform;
import re;
import string;
import sys;

from datetime import datetime;

import CxServerEndpoint1;
import CxProjectCreation1;
import CxProjectCreationCollection1;

optParser                = optparse.OptionParser();
sScriptId                = optParser.get_prog_name();
sScriptVers              = "(v1.0103)";
sScriptDisp              = sScriptId+" "+sScriptVers+":"
cScriptArgc              = len(sys.argv);

bVerbose                 = False;
sScriptOSAScanDirectory  = "";
sScriptOSAScanDirectory  = "";
sScriptOSAProjectName    = "";
sScriptCxServerURL       = None;
sScriptCxAuthUserId      = None;
sScriptCxAuthPassword    = None;
sScriptOutputOSAScanFile = "";

def main():

    try:

        sPythonVers = ("v%s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro));
        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("%s The Checkmarx Project OSA 'scan' via Rest API #1 is starting execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_true");
        optParser.add_option("-d", "--data-directory", dest="data_directory", default="", help="Directory with file(s) to process", metavar="DIRECTORY-of-Files-to-Process");
        optParser.add_option("-p", "--project-name", dest="project_name", default="", help="Checkmarx Project 'name' to scan to", metavar="Checkmarx-Project-name");
        optParser.add_option("--url", dest="cx_server_url", default="", help="Checkmarx Server URL - Protocol/Host/Port - sample: --url=http://hostname:8080", metavar="Checkmarx-Server-URL");
        optParser.add_option("--user", dest="cx_auth_user", default="", help="Checkmarx Authentication UserId", metavar="Checkmarx-UserId");
        optParser.add_option("--pswd", dest="cx_auth_pswd", default="", help="Checkmarx Authentication Password", metavar="Checkmarx-Password");
        optParser.add_option("-o", "--output-OSA-Scan-file", dest="output_osa_scan_file", default="", help="(Output) OSA Scan 'report' file [generated]");
     
        (options, args) = optParser.parse_args();
     
        bVerbose                 = options.run_verbose;
        sScriptOSAScanDirectory  = options.data_directory.strip();
        sScriptOSAProjectName    = options.project_name.strip();
        sScriptCxServerURL       = options.cx_server_url.strip();
        sScriptCxAuthUserId      = options.cx_auth_user.strip();
        sScriptCxAuthPassword    = options.cx_auth_pswd.strip();
        sScriptOutputOSAScanFile = options.output_osa_scan_file.strip();
     
        if bVerbose == True:
     
            print("%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose));
            print("%s Command Data Directory to scan from is [%s]..." % (sScriptDisp, sScriptOSAScanDirectory));
            print("%s Command Checkmarx Project 'name' to scan to [%s]..." % (sScriptDisp, sScriptOSAProjectName));
            print("%s Command Checkmarx Server URL is [%s]..." % (sScriptDisp, sScriptCxServerURL));
            print("%s Command Checkmarx Authentication UserId is [%s]..." % (sScriptDisp, sScriptCxAuthUserId));
            print("%s Command Checkmarx Authentication Password is [%s]..." % (sScriptDisp, sScriptCxAuthPassword));
            print("%s Command (Output) OSA Scan 'report' file is [%s]..." % (sScriptDisp, sScriptOutputOSAScanFile));
            print("");

        if len(sScriptOSAScanDirectory) < 1:

            print("%s Command received a Data Directory string to search that is 'null' or Empty - Error!" % (sScriptDisp));

            return False;

        if sScriptCxServerURL != None:

            sScriptCxServerURL = sScriptCxServerURL.strip();

        if sScriptCxServerURL == None or \
           len(sScriptCxServerURL) < 1:

            sScriptCxServerURL = None;

        else:

            sScriptCxServerURLLow = sScriptCxServerURL.lower();

            if sScriptCxServerURLLow.startswith("http://")  == False and \
               sScriptCxServerURLLow.startswith("https://") == False:

                sScriptCxServerURL = None;

        if sScriptCxServerURL != None:

            sScriptCxServerURL = sScriptCxServerURL.strip();

        if sScriptCxServerURL == None or \
           len(sScriptCxServerURL) < 1:

            print("");
            print("%s The Checkmarx Server URL is None or Empty - this MUST be supplied - Error!" % (sScriptDisp));
            print("");

            return False;

        if sScriptCxAuthUserId != None:

            sScriptCxAuthUserId = sScriptCxAuthUserId.strip();

        if sScriptCxAuthUserId == None or \
            len(sScriptCxAuthUserId) < 1:

            sScriptCxAuthUserId = None;

            print("");
            print("%s The Checkmarx Auth UserId is None or Empty - this SHOULD be supplied - Warning!" % (sScriptDisp));
            print("");

        if sScriptCxAuthPassword != None:

            sScriptCxAuthPassword = sScriptCxAuthPassword.strip();

        if sScriptCxAuthPassword == None or \
            len(sScriptCxAuthPassword) < 1:

            sScriptCxAuthPassword = None;

            print("");
            print("%s The Checkmarx Auth Password is None or Empty - this SHOULD be supplied - Warning!" % (sScriptDisp));
            print("");

        if sScriptOutputOSAScanFile != None:

            sScriptOutputOSAScanFile = sScriptOutputOSAScanFile.strip();

        if sScriptOutputOSAScanFile == None or \
           len(sScriptOutputOSAScanFile) < 1:

            print("%s Checkmarx (Output) OSA Scan 'report' file is None or Empty - this output will be bypassed - Warning!" % (sScriptDisp));

            sScriptOutputOSAScanFile == None;

        else:

            if bVerbose == True:

                print("");
                print("%s Generating the Checkmarx (Output) OSA Scan 'report' into the file [%s]..." % (sScriptDisp, sScriptOutputOSAScanFile));
                print("");

        bProcessingError = False;

        cxServerEndpoint = CxServerEndpoint1.CxServerEndpoint(trace=bVerbose, cxserverendpointactive=True, cxserverurl=sScriptCxServerURL, cxauthuserid=sScriptCxAuthUserId, cxauthpassword=sScriptCxAuthPassword);

        if cxServerEndpoint == None:

            print("");
            print("%s The CxServerEndpoint object is None - this object failed to create - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxServerEndpoint (after init) is:" % (sScriptDisp));
            print(cxServerEndpoint.toString());
            print("");

        if cxServerEndpoint.getCxServerEndpointActiveFlag() == False:

            print("");
            print("%s The CxServerEndpoint is NOT marked 'active' - it MUST be marked 'active' to be used - Error!" % (sScriptDisp));
            print("");

            return False;

        cxProjCollection = CxProjectCreationCollection1.CxProjectCreationCollection(trace=bVerbose, searchrecursive=False, searchcasesensitive=False, searchdirectory=sScriptOSAScanDirectory, searchfilepatterns="*", cxserverendpoint=cxServerEndpoint);

        if cxProjCollection == None:

            print("");
            print("%s The CxProjectCreationCollection object is None - this object failed to create - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxProjectCreationCollection (after init) is:" % (sScriptDisp));
            print(cxProjCollection.toString());
            print("");

    #   bProjCollectionPropertiesLoadOk = cxProjCollection.loadCxProjectCreationCollectionFromPropertiesFiles();
    #
    #   if bProjCollectionPropertiesLoadOk == False:
    #
    #       print("");
    #       print("%s The CxProjectCreationCollection.loadCxProjectCreationCollectionFromPropertiesFiles() call failed - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   if bVerbose == True:
    #
    #       print("");
    #       print("%s CxProjectCreationCollection (after 'properties' load) is:" % (sScriptDisp));
    #       print(cxProjCollection.toString());
    #       print("");

        bProjCollectionMetaLoadOk = cxProjCollection.loadCxProjectCreationMetaDataToCollectionFromRestAPI();

        if bProjCollectionMetaLoadOk == False:

            print("");
            print("%s The CxProjectCreationCollection.loadCxProjectCreationMetaDataToCollectionFromRestAPI() call failed - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxProjectCreationCollection (after load) is:" % (sScriptDisp));
            print(cxProjCollection.toString());
            print("");

    #   cxProjectCreation1 = CxProjectCreation1.CxProjectCreation(trace=bVerbose, cxprojectname="10101-VastId_Dept", cxprojectispublic=True, cxprojectteamname="\\CxServer\\SP\\Company\\Users", cxprojectpresetname="Checkmarx Default", cxprojectengineconfigname="Default Configuration", cxprojectbranchnames=["Branch1", "Branch2", "Branch3"]);
    #
    #   if cxProjectCreation1 == None:
    #
    #       print("");
    #       print("%s Failed to create a CxProjectCreation object - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   bAddProjCreationToCollectionOk = cxProjCollection.addCxProjectCreationToCxProjectCreationCollection(cxprojectcreation=cxProjectCreation1);
    #
    #   if bAddProjCreationToCollectionOk == False:
    #
    #       print("");
    #       print("%s The CxProjectCreationCollection.addCxProjectCreationToCxProjectCreationCollection() call failed - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   if bVerbose == True:
    #
    #       print("");
    #       print("%s CxProjectCreationCollection (after add) is:" % (sScriptDisp));
    #       print(cxProjCollection.toString());
    #       print("");
    #
    # TEMP:
    #
    #   return False;
    #
    # TEMP:

    #   if bScriptCxForceDelete == False:
    #
    #       bCreateProjBranchesOk = cxProjCollection.createCxProjectsAndBranchesFromCxProjectCreationCollection();
    #
    #       if bCreateProjBranchesOk == False:
    #
    #           print("");
    #           print("%s The CxProjectCreationCollection.createCxProjectsAndBranchesFromCxProjectCreationCollection() call failed - Error!" % (sScriptDisp));
    #           print("");
    #
    #           return False;
    #
    #       if bVerbose == True:
    #
    #           print("");
    #           print("%s CxProjectCreationCollection (after create) is:" % (sScriptDisp));
    #           print(cxProjCollection.toString());
    #           print("");
    #
    #   else:
    #
    #       bDeleteProjBranchesOk = cxProjCollection.deleteCxProjectsAndBranchesFromCxProjectCreationCollection();
    #
    #       if bDeleteProjBranchesOk == False:
    #
    #           print("");
    #           print("%s The CxProjectCreationCollection.deleteCxProjectsAndBranchesFromCxProjectCreationCollection() call failed - Error!" % (sScriptDisp));
    #           print("");
    #
    #           return False;
    #
    #       if bVerbose == True:
    #
    #           print("");
    #           print("%s CxProjectCreationCollection (after 'force' delete) is:" % (sScriptDisp));
    #           print(cxProjCollection.toString());
    #           print("");
    #
    #   bGenerateProjReportOk = cxProjCollection.generateCxProjectCreationCollectionReport();
    #
    #   if bGenerateProjReportOk == False:
    #
    #       print("");
    #       print("%s The CxProjectCreationCollection.generateCxProjectCreationCollectionReport() call failed - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   if bVerbose == True:
    #
    #       print("");
    #       print("%s CxProjectCreationCollection (after report) is:" % (sScriptDisp));
    #       print(cxProjCollection.toString());
    #       print("");
    #
    #   asCxProjectCreationCollectionReport = cxProjCollection.getCxProjectCreationCollectionReportAsList();
    #
    #   if asCxProjectCreationCollectionReport == None or \
    #       len(asCxProjectCreationCollectionReport) < 1:
    #
    #       print("");
    #       print("%s The CxProjectCreationCollection generated 'report' is None or 'empty' - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   print('\n'.join(asCxProjectCreationCollectionReport));
    #
    #   if sScriptOutputOSAScanFile != None:
    #
    #       sScriptOutputOSAScanFile = sScriptOutputOSAScanFile.strip();
    #
    #   if sScriptOutputOSAScanFile != None and \
    #       len(sScriptOutputOSAScanFile) > 0:
    #
    #       bSaveCreationCollectionOk = cxProjCollection.saveCxProjectCreationCollectionReportToFile(outputprojectcreationcollectionfile=sScriptOutputOSAScanFile);
    #
    #       if bSaveCreationCollectionOk == False:
    #
    #           print("");
    #           print("%s The CxProjectCreationCollection generated 'report' failed to save to the file [%s] - Error!" % (sScriptDisp, sScriptOutputOSAScanFile));
    #           print("");
    #
    #           bProcessingError = True;

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("");
        print("%s The Checkmarx Project OSA 'scan' via Rest API #1 is ending execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
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

