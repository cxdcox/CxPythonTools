
import optparse;
import os;
import traceback;
import platform;
import re;
import string;
import sys;

from datetime import datetime;

import CxApplicationConfigCollection1;
import CxProjectCreation1;

optParser               = optparse.OptionParser();
sScriptId               = optParser.get_prog_name();
sScriptVers             = "(v1.0101)";
sScriptDisp             = sScriptId+" "+sScriptVers+":"
cScriptArgc             = len(sys.argv);

bVerbose                = False;
bScriptRecursive        = False;
bScriptCaseSensitive    = False;
sScriptDirectory        = "";
sScriptFilePatterns     = "";
sScriptOutputConfigFile = "";

def main():

    try:

        sPythonVers = ("v%s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro));
        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("%s The Checkmarx Application 'config' Creator #1 is starting execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_true");
        optParser.add_option("-r", "--recursive", dest="search_recursive", default=False, help="Search Directory PATHS recursively", action="store_true");
        optParser.add_option("-c", "--case-sensitive", dest="case_sensitive", default=False, help="Search Directory PATHS with case-sensitivity", action="store_true");
        optParser.add_option("-d", "--data-directory", dest="data_directory", default="", help="Directory with file(s) to process", metavar="DIRECTORY-of-Files-to-Process");
        optParser.add_option("-p", "--file-patterns", dest="file_patterns", default="*.plist", help="File 'patterns' to search for (semicolon delimited) [default is '*.properties']", metavar="FILE-PATTERNS");
        optParser.add_option("-o", "--output-config-file", dest="output_config_file", default="", help="(Output) 'config' file [generated]");
     
        (options, args) = optParser.parse_args();
     
        bVerbose                = options.run_verbose;
        bScriptRecursive        = options.search_recursive;
        bScriptCaseSensitive    = options.case_sensitive;
        sScriptDirectory        = options.data_directory.strip();
        sScriptFilePatterns     = options.file_patterns.strip();
        sScriptOutputConfigFile = options.output_config_file.strip();
     
        if bVerbose == True:
     
            print("%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose));
            print("");
            print("%s Command Search 'recursive' flag is [%s]..." % (sScriptDisp, bScriptRecursive));
            print("%s Command Search 'case-sensitive' flag is [%s]..." % (sScriptDisp, bScriptCaseSensitive));
            print("%s Command Data Directory to search is [%s]..." % (sScriptDisp, sScriptDirectory));
            print("%s Command File 'patterns' to search for are [%s]..." % (sScriptDisp, sScriptFilePatterns));
            print("%s Command (Output) 'config' file is [%s]..." % (sScriptDisp, sScriptOutputConfigFile));
            print("");

        if len(sScriptDirectory) < 1:

            print("%s Command received a Data Directory string to search that is 'null' or Empty - Error!" % (sScriptDisp));

            return False;

        if sScriptOutputConfigFile != None:

            sScriptOutputConfigFile = sScriptOutputConfigFile.strip();

        if sScriptOutputConfigFile == None or \
           len(sScriptOutputConfigFile) < 1:

            print("%s Checkmarx (Output) 'config' file is None or Empty - this output file is REQUIRED - Error!" % (sScriptDisp));

            return False;

        if bVerbose == True:

            print("");
            print("%s Generating the Checkmarx (Output) 'config' into the file [%s]..." % (sScriptDisp, sScriptOutputConfigFile));
            print("");

        bProcessingError = False;

        cxAppCollection = CxApplicationConfigCollection1.CxApplicationConfigCollection(trace=bVerbose, searchrecursive=bScriptRecursive, searchcasesensitive=bScriptCaseSensitive, searchdirectory=sScriptDirectory, searchfilepatterns=sScriptFilePatterns);

        if cxAppCollection == None:

            print("");
            print("%s The CxApplicationConfigCollection object is None - this object failed to create - Error!" % (sScriptDisp));
            print("");

            return False;

        if bVerbose == True:

            print("");
            print("%s CxApplicationConfigCollection (after init) is:" % (sScriptDisp));
            print(cxAppCollection.toString());
            print("");

        bAppCollectionReposLoadOk = cxAppCollection.loadCxApplicationConfigCollectionFromRepos();
     
        if bAppCollectionReposLoadOk == False:
     
            print("");
            print("%s The CxApplicationConfigCollection.loadCxApplicationConfigCollectionFromRepos() call failed - Error!" % (sScriptDisp));
            print("");
     
            return False;
     
        if bVerbose == True:
     
            print("");
            print("%s CxApplicationConfigCollection (after 'repos' load) is:" % (sScriptDisp));
            print(cxAppCollection.toString());
            print("");

    #   cxProjectCreation1 = CxProjectCreation1.CxProjectCreation(trace=bVerbose, cxprojectname="CxProjCreationMainTest1", cxprojectispublic=True, cxprojectteamname="\\CxServer\\SP\\Company\\Users", cxprojectpresetname="Checkmarx Default", cxprojectengineconfigname="Default Configuration", cxprojectbranchnames=["Branch1"]);
    #
    #   if cxProjectCreation1 == None:
    #
    #       print("");
    #       print("%s Failed to create a CxProjectCreation object - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   if bVerbose == True:
    #
    #       print("");
    #       print("%s CxProjectCreation (after init) is:" % (sScriptDisp));
    #       print(cxProjectCreation1.toString());
    #       print("");
    #
    #   bAddProjCreationToCollectionOk = cxAppCollection.addCxProjectCreationToCxApplicationConfigCollection(cxprojectcreation=cxProjectCreation1);
    #
    #   if bAddProjCreationToCollectionOk == False:
    #
    #       print("");
    #       print("%s The CxApplicationConfigCollection.addCxProjectCreationToCxApplicationConfigCollection() call failed - Error!" % (sScriptDisp));
    #       print("");
    #
    #       return False;
    #
    #   if bVerbose == True:
    #
    #       print("");
    #       print("%s CxApplicationConfigCollection (after add) is:" % (sScriptDisp));
    #       print(cxAppCollection.toString());
    #       print("");
     
    # TEMP:
    #
    #   return False;
    #
    # TEMP:
     
        bGenerateProjReportOk = cxAppCollection.generateCxApplicationConfigCollectionReport();
     
        if bGenerateProjReportOk == False:
     
            print("");
            print("%s The CxApplicationConfigCollection.generateCxApplicationConfigCollectionReport() call failed - Error!" % (sScriptDisp));
            print("");
     
            return False;
     
        if bVerbose == True:
     
            print("");
            print("%s CxApplicationConfigCollection (after report) is:" % (sScriptDisp));
            print(cxAppCollection.toString());
            print("");
     
        asCxApplicationConfigCollectionReport = cxAppCollection.getCxApplicationConfigCollectionReportAsList();
     
        if asCxApplicationConfigCollectionReport == None or \
            len(asCxApplicationConfigCollectionReport) < 1:
     
            print("");
            print("%s The CxApplicationConfigCollection generated 'report' is None or 'empty' - Error!" % (sScriptDisp));
            print("");
     
            return False;
     
        print('\n'.join(asCxApplicationConfigCollectionReport));
     
        if sScriptOutputConfigFile != None:
     
            sScriptOutputConfigFile = sScriptOutputConfigFile.strip();
     
        if sScriptOutputConfigFile != None and \
            len(sScriptOutputConfigFile) > 0:
     
            bSaveCreationCollectionOk = cxAppCollection.saveCxApplicationConfigCollectionReportToFile(outputprojectcreationcollectionfile=sScriptOutputConfigFile);
     
            if bSaveCreationCollectionOk == False:
     
                print("");
                print("%s The CxApplicationConfigCollection generated 'report' failed to save to the file [%s] - Error!" % (sScriptDisp, sScriptOutputConfigFile));
                print("");
     
                bProcessingError = True;

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("");
        print("%s The Checkmarx Application 'config' Creator #1 is ending execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
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

