
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;
import plistlib;

from datetime import datetime;

import DrcDirectoryFileSearch1;

import CxProjectCreation1;

class CxApplicationConfigCollection:

    sClassMod                             = __name__;
    sClassId                              = "CxApplicationConfigCollection";
    sClassVers                            = "(v1.0201)";
    sClassDisp                            = sClassMod+"."+sClassId+" "+sClassVers+": ";

    # Project 'instance' field(s):

    bTraceFlag                            = False;
    bSearchRecursiveFlag                  = False;
    bSearchCaseSensitive                  = False;
    sSearchDirectory                      = None;
    sSearchFilePatterns                   = None;
    listApplicationConfigFiles            = None;
    dictCxApplicationConfigCollection     = None;

    asCxApplicationConfigCollectionReport = None;

    def __init__(self, trace=False, searchrecursive=False, searchcasesensitive=False, searchdirectory=None, searchfilepatterns=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setSearchRecursiveFlag(searchrecursive=searchrecursive);
            self.setSearchCaseSensitiveFlag(searchcasesensitive=searchcasesensitive);
            self.setSearchDirectory(searchdirectory=searchdirectory);
            self.setSearchFilePatterns(searchfilepatterns=searchfilepatterns);

        except Exception as inst:

            print("%s '__init__()' - exception occured..." % (self.sClassDisp));
            print(type(inst));
            print(inst);

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print("- - - ");
            print('\n'.join(asTracebackLines));
            print("- - - ");

    def getTraceFlag(self):

        return self.bTraceFlag;

    def setTraceFlag(self, trace=False):

        self.bTraceFlag = trace;

    def getSearchRecursiveFlag(self):

        return self.bSearchRecursiveFlag;

    def setSearchRecursiveFlag(self, searchrecursive=False):

        self.bSearchRecursiveFlag = searchrecursive;

    def getSearchCaseSensitiveFlag(self):

        return self.bSearchCaseSensitive;

    def setSearchCaseSensitiveFlag(self, searchcasesensitive=False):

        self.bSearchCaseSensitive = searchcasesensitive;

    def getSearchDirectory(self):

        return self.sSearchDirectory;

    def setSearchDirectory(self, searchdirectory=None):

        self.sSearchDirectory = searchdirectory;

    def getSearchFilePatterns(self):

        return self.sSearchFilePatterns;

    def setSearchFilePatterns(self, searchfilepatterns=None):

        self.sSearchFilePatterns = searchfilepatterns;

    def getCxApplicationConfigCollection(self):

        return self.dictCxApplicationConfigCollection;

    def setCxApplicationConfigCollection(self, cxprojectcreationcollection=None):

        self.dictCxApplicationConfigCollection = cxprojectcreationcollection;

    def getCxApplicationConfigCollectionReportAsList(self):

        return self.asCxApplicationConfigCollectionReport;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print("%s Dump of the variable(s) content of this class:" % (self.sClassDisp));
            print("%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag));
            print("%s The 'bSearchRecursiveFlag' boolean is [%s]..." % (self.sClassDisp, self.bSearchRecursiveFlag));
            print("%s The 'bSearchCaseSensitive' boolean is [%s]..." % (self.sClassDisp, self.bSearchCaseSensitive));
            print("%s The contents of 'sSearchDirectory' is [%s]..." % (self.sClassDisp, self.sSearchDirectory));
            print("%s The contents of 'sSearchFilePatterns' is [%s]..." % (self.sClassDisp, self.sSearchFilePatterns));
            print("%s The contents of 'listApplicationConfigFiles' is [%s]..." % (self.sClassDisp, self.listApplicationConfigFiles));

            if self.dictCxApplicationConfigCollection == None:

                print("%s The 'dictCxApplicationConfigCollection' has NOT been set..." % (self.sClassDisp));

            else:

                print("%s The 'dictCxApplicationConfigCollection' is [%s]..." % (self.sClassDisp, self.dictCxApplicationConfigCollection));

            print("%s The contents of 'asCxApplicationConfigCollectionReport' is [%s]..." % (self.sClassDisp, self.asCxApplicationConfigCollectionReport));

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'bSearchRecursiveFlag' is [%s], " % (self.bSearchRecursiveFlag));
        asObjDetail.append("'bSearchCaseSensitive' is [%s], " % (self.bSearchCaseSensitive));
        asObjDetail.append("'sSearchDirectory' is [%s], " % (self.sSearchDirectory));
        asObjDetail.append("'sSearchFilePatterns' is [%s], " % (self.sSearchFilePatterns));
        asObjDetail.append("'listApplicationConfigFiles' is [%s], " % (self.listApplicationConfigFiles));
        asObjDetail.append("'dictCxApplicationConfigCollection' is [%s], " % (self.dictCxApplicationConfigCollection));
        asObjDetail.append("'asCxApplicationConfigCollectionReport' is [%s]. " % (self.asCxApplicationConfigCollectionReport));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def loadCxApplicationConfigCollectionFromPlistFiles(self):

    #   self.bTraceFlag = True;

        if self.sSearchDirectory == None or \
           len(self.sSearchDirectory) < 1:

            print("");
            print("%s The supplied 'search' Directory (to be input from) 'sSearchDirectory' is None or Empty - Severe Error!" % (self.sClassDisp));
            print("");

            return False;

        if self.sSearchFilePatterns == None or \
           len(self.sSearchFilePatterns) < 1:

            print("");
            print("%s The supplied 'search' File Patterns to be scanned for 'sSearchFilePatterns' is None or Empty - defaulting to '*.plist' - Warning!" % (self.sClassDisp));
            print("");

            self.setSearchFilePatterns(searchfilepatterns="*.plist");

        else:

            print("");
            print("%s The supplied 'search' File Patterns to be scanned for 'sSearchFilePatterns' is [%s]..." % (self.sClassDisp, self.sSearchFilePatterns));
            print("");

        self.listProjectCreationPlistFiles = None;

        bProcessingError = False;

        try:

            drcDirSearch = DrcDirectoryFileSearch1.DrcDirectoryFileSearcher(trace=self.bTraceFlag, searchrecursive=self.bSearchRecursiveFlag, searchcasesensitive=self.bSearchCaseSensitive, searchdirectories=self.sSearchDirectory, searchfilepatterns=self.sSearchFilePatterns);

            drcDirSearch.searchDirectoriesForFiles();

            if self.bTraceFlag == True:

                print("%s 'drcDirSearch' (after search) is [%s]..." % (self.sClassDisp, drcDirSearch.toString()));
                print("");

            asFileSearchResults = drcDirSearch.renderDictSearchResultsAsList();

            if self.bTraceFlag == True:

                print("%s 'asFileSearchResults' [list] (after search) is:" % (self.sClassDisp));
                print(asFileSearchResults);
                print("");

            if asFileSearchResults == None or \
               len(asFileSearchResults) < 1:

                print("%s Directory search produced a File(s) listing array that is 'null' or Empty - Error!" % (self.sClassDisp));

                return False;

            print("%s Directory search produced a File(s) listing array with (%d) elements..." % (self.sClassDisp, len(asFileSearchResults)));
            print("");

            idProjectCreationPlistFile = 0;

            for sProjectCreationPlistFile in asFileSearchResults:

                sProjectCreationPlistFilespec = os.path.realpath(sProjectCreationPlistFile);
                bProjectCreationPlistIsFile   = os.path.isfile(sProjectCreationPlistFilespec);

                if bProjectCreationPlistIsFile == False:

                    print("%s Command received a Project Creation 'plist' filespec of [%s] that does NOT exist - Error!" % (self.sClassDisp, sProjectCreationPlistFilespec));

                    continue;

                idProjectCreationPlistFile += 1;

                if self.bTraceFlag == True:

                    print("%s Command is adding a Project Creation 'plist' filespec #(%d) of [%s]..." % (self.sClassDisp, idProjectCreationPlistFile, sProjectCreationPlistFilespec));
                    print("");

                if self.listProjectCreationPlistFiles == None:

                    self.listProjectCreationPlistFiles = list();

                self.listProjectCreationPlistFiles.append(sProjectCreationPlistFilespec);

                print("%s Command added a Project Creation 'plist' filespec #(%d) of [%s]..." % (self.sClassDisp, idProjectCreationPlistFile, sProjectCreationPlistFilespec));

            bLoadPlistFilesOk = self.loadProjectCreationPlistFilesToCollection();

            if bLoadPlistFilesOk == None:
         
                print("");
                print("%s 'loadProjectCreationPlistFilesToCollection()' API call failed - Error!" % (self.sClassDisp));
                print("");
         
                return False;

        except Exception as inst:

            print("%s 'loadCxApplicationConfigCollectionFromPlistFiles()' - exception occured..." % (self.sClassDisp));
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

    def loadProjectCreationPlistFilesToCollection(self):

    #   self.bTraceFlag = True;

        if self.listProjectCreationPlistFiles == None or \
           len(self.listProjectCreationPlistFiles) < 1:

            print("%s The generated Project Creation 'plist' file(s) 'search' List is None or Empty - Severe Error!" % (self.sClassDisp));

            return False;

        bProcessingError = False;

        try:

            idProjectCreationPlistFile = 0;

            for sProjectCreationPlistFile in self.listProjectCreationPlistFiles:

                idProjectCreationPlistFile += 1;

                if sProjectCreationPlistFile != None:

                    sProjectCreationPlistFile = sProjectCreationPlistFile.strip();

                if sProjectCreationPlistFile == None or \
                   len(sProjectCreationPlistFile) < 1:

                    if self.bTraceFlag == True:

                        print("%s The Project Creation 'plist' file #(%d) has a name that is None or Empty - bypassing the entry..." % (self.sClassDisp, idProjectCreationPlistFile));
                        print("");

                    continue;

                sProjectCreationPlistFilespec = os.path.realpath(sProjectCreationPlistFile);
                bProjectCreationPlistIsFile   = os.path.isfile(sProjectCreationPlistFilespec);

                if bProjectCreationPlistIsFile == False:

                    print("%s Command received a Project Creation 'plist' #(%d) filespec of [%s] that does NOT exist - bypassing the entry - Error!" % (self.sClassDisp, idProjectCreationPlistFile, sProjectCreationPlistFilespec));

                    continue;

                cProjectCreationPlistFile = os.path.getsize(sProjectCreationPlistFilespec);

                if self.bTraceFlag == True:

                    print("%s Loading a Project Creation 'plist' #(%d) filespec of [%s] containing (%d) bytes..." % (self.sClassDisp, idProjectCreationPlistFile, sProjectCreationPlistFilespec, cProjectCreationPlistFile));
                    print("");

                bLoadProjectCreationPlistFileOk = self.loadProjectCreationPlistFile(projectcreationplistfile=sProjectCreationPlistFilespec);

                if bLoadProjectCreationPlistFileOk == None:

                    print("");
                    print("%s 'loadProjectCreationPlistFile()' API call failed - Error!" % (self.sClassDisp));
                    print("");

                    return False;

                print("%s Loaded a Project Creation 'plist' #(%d) filespec of [%s] containing (%d) bytes..." % (self.sClassDisp, idProjectCreationPlistFile, sProjectCreationPlistFilespec, cProjectCreationPlistFile));

        except Exception as inst:

            print("%s 'loadProjectCreationPlistFilesToCollection()' - exception occured..." % (self.sClassDisp));
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

    def loadProjectCreationPlistFile(self, projectcreationplistfile=None):

    #   self.bTraceFlag = True;

        sProjectCreationPlistFile = projectcreationplistfile;

        if sProjectCreationPlistFile != None:
         
            sProjectCreationPlistFile = sProjectCreationPlistFile.strip();
         
        if sProjectCreationPlistFile == None or \
           len(sProjectCreationPlistFile) < 1:
         
            print("");
            print("%s The supplied Project Creation 'plist' file is 'None' or Empty - Severe Error!" % (self.sClassDisp));

            return False;

        bProjectCreationPlistIsFile = os.path.isfile(sProjectCreationPlistFile);

        if bProjectCreationPlistIsFile == False:

            print("");
            print("%s The supplied Project Creation 'plist' file [%s] does NOT exist - bypassing the file - Warning!" % (self.sClassDisp, sProjectCreationPlistFile));

            return False;

        cProjectCreationPlistFile = os.path.getsize(sProjectCreationPlistFile);

        print("");
        print("%s Loading the supplied Project Creation 'plist' from the file [%s] containing (%d) bytes of data..." % (self.sClassDisp, sProjectCreationPlistFile, cProjectCreationPlistFile));
        print("");

        cxProjectCreation1 = None;

        try:

            asProjectCreationPlist = list();

            with open(sProjectCreationPlistFile, 'rb') as fProjectCreationPlist:

                dictProjectCreationPlist = plistlib.load(fProjectCreationPlist);

            print("%s Command read the (Input) 'plist' file of [%s] into 'dictProjectCreationPlist'..." % (self.sClassDisp, cProjectCreationPlistFile));
            print("%s The OBJECT 'dictProjectCreationPlist' Type [%s] is [%s]..." % (self.sClassDisp, type(dictProjectCreationPlist), dictProjectCreationPlist));

            if type(dictProjectCreationPlist) != dict:

                print("%s Command has processed a Project Creation 'plist' filespec of [%s] producing a 'dictProjectCreationPlist' object that is NOT of type(dict) - Error!" % (self.sClassDisp, sProjectCreationPlistFile));

                return False;

            if dictProjectCreationPlist == None or \
               len(dictProjectCreationPlist) < 1:

                print("%s Command has processed a Project Creation 'plist' filespec of [%s] producing a 'dictProjectCreationPlist' that is None or Empty - Error!" % (self.sClassDisp, sProjectCreationPlistFile));

                return False;

            # --------------------------------------------------------------------------------------------------
            # <dict>
            #     <key>Application</key>
            #     <string>ElevateSampleApp1</string>
            #     <key>AppActive</key>
            #     <string>true</string>
            #     <key>AppCxTeam</key>
            #     <string>\CxServer\SP\Company\Users</string>
            #     <key>AppCxPreset</key>
            #     <string>Checkmarx Default</string>
            #     <key>AppCxEngineConfig</key>
            #     <string>Default Configuration</string>
            #     <key>AppRepos</key>
            #     <array>
            #         <dict>
            #             <key>RepoTitle</key>
            #             <string>AppRepo1</string>
            #             <key>RepoActive</key>
            #             <string>true</string>
            #             <key>RepoURL</key>
            #             <string>http://Elevate/App/Repo1</string>
            #             <key>RepoBranches</key>
            #             <array>
            #                 <dict>
            #                     <key>BranchTitle</key>
            #                     <string>Master1</string>
            #                     <key>BranchActive</key>
            #                     <string>true</string>
            #                     <key>BranchName</key>
            #                     <string>refs/heads/master</string>
            #                 </dict>
            #             </array>
            #         </dict>
            #         <dict>
            #             <key>RepoTitle</key>
            #             <string>AppRepo2</string>
            #             <key>RepoActive</key>
            #             <string>true</string>
            #             <key>RepoURL</key>
            #             <string>http://Elevate/App/Repo2</string>
            #             <key>RepoBranches</key>
            #             <array>
            #                 <dict>
            #                     <key>BranchTitle</key>
            #                     <string>Master2</string>
            #                     <key>BranchActive</key>
            #                     <string>true</string>
            #                     <key>BranchName</key>
            #                     <string>refs/heads/master</string>
            #                 </dict>
            #             </array>
            #         </dict>
            #         <dict>
            #             <key>RepoTitle</key>
            #             <string>AppRepo3</string>
            #             <key>RepoActive</key>
            #             <string>true</string>
            #             <key>RepoURL</key>
            #             <string>http://Elevate/App/Repo3</string>
            #             <key>RepoBranches</key>
            #             <array>
            #                 <dict>
            #                     <key>BranchTitle</key>
            #                     <string>Master3</string>
            #                     <key>BranchActive</key>
            #                     <string>true</string>
            #                     <key>BranchName</key>
            #                     <string>refs/heads/master</string>
            #                 </dict>
            #                 <dict>
            #                     <key>BranchTitle</key>
            #                     <string>Release3</string>
            #                     <key>BranchActive</key>
            #                     <string>true</string>
            #                     <key>BranchName</key>
            #                     <string>refs/heads/release</string>
            #                 </dict>
            #                 <dict>
            #                     <key>BranchTitle</key>
            #                     <string>Staging3</string>
            #                     <key>BranchActive</key>
            #                     <string>true</string>
            #                     <key>BranchName</key>
            #                     <string>refs/heads/staging</string>
            #                 </dict>
            #             </array>
            #         </dict>
            #     </array>
            # </dict>
            # --------------------------------------------------------------------------------------------------

            sCxProjectName = dictProjectCreationPlist["Application"];

            if sCxProjectName != None:

                sCxProjectName = sCxProjectName.strip();

            if sCxProjectName == None or \
                len(sCxProjectName) < 1:

                sCxProjectName = None;

            if sCxProjectName == None or \
                len(sCxProjectName) < 1:

                print("");
                print("%s The CxProjectCreation has a 'name' that is None or 'empty' - bypassing the Project(s)/Branch(s) 'creation' of this object - Error!" % (self.sClassDisp));
                print("");

                return False;

            sCxProjectIsActive = dictProjectCreationPlist["AppActive"]; 

            if sCxProjectIsActive != None:

                sCxProjectIsActive = sCxProjectIsActive.strip();

            if sCxProjectIsActive == None or \
                len(sCxProjectIsActive) < 1:

                sCxProjectIsActive = "false";

            sCxProjectIsActiveLow = sCxProjectIsActive.lower();

            if sCxProjectIsActiveLow == "false":

                print("");
                print("%s The CxProjectCreation named [%s] is marked NOT 'active' - bypassing the Project(s)/Branch(s) 'creation' of this object - Error!" % (self.sClassDisp, sCxProjectName));
                print("");

                return False;

            if cxProjectCreation1 == None:

                cxProjectCreation1 = CxProjectCreation1.CxProjectCreation(trace=self.bTraceFlag, cxprojectispublic=True, cxprojectteamname=self.cxApplicationConfigCollectionDefaults.getDefaultCxProjectTeamName(), cxprojectpresetname=self.cxApplicationConfigCollectionDefaults.getDefaultCxProjectPresetName(), cxprojectengineconfigname="Default Configuration");

                if cxProjectCreation1 == None:

                    print("");
                    print("%s Failed to create a CxProjectCreation object - Error!" % (self.sClassDisp));
                    print("");

                    return False;

            cxProjectCreation1.setCxProjectBaseName(cxprojectbasename=sCxProjectName);
            cxProjectCreation1.setCxProjectName(cxprojectname=sCxProjectName);
        #   cxProjectCreation1.setCxProjectTeamName(cxprojectteamname=dictProjectCreationPlist["AppCxTeam"]);
        #   cxProjectCreation1.setCxProjectPresetName(cxprojectpresetname=dictProjectCreationPlist["AppCxPreset"]); 
        #   cxProjectCreation1.setCxProjectEngineConfigName(cxprojectengineconfigname=dictProjectCreationPlist["AppCxEngineConfig"]);
            cxProjectCreation1.setCxProjectExtraField1(cxprojectextrafield1=dictProjectCreationPlist["AppRepos"]);

        #   listCxAppRepos = cxProjectCreation1.getCxProjectExtraField1();
        #
        #   if listCxAppRepos != None and \
        #       len(listCxAppRepos) > 0:
        #
        #       asCxProjectBranches = list();
        #
        #       for dictProjectBranch in listCxAppRepos:
        #
        #           if dictProjectBranch == None:
        #
        #               continue;
        #
        #           sCxAppRepoName = dictProjectBranch["RepoTitle"];
        #
        #           if sCxAppRepoName != None:
        #
        #               sCxAppRepoName = sCxAppRepoName.strip();
        #
        #           if sCxAppRepoName != None and \
        #               len(sCxAppRepoName) > 0:
        #
        #               asCxProjectBranches.append(sCxAppRepoName);
        #
        #       if asCxProjectBranches != None and \
        #           len(asCxProjectBranches) > 0:
        #
        #           cxProjectCreation1.setCxProjectBranchNames(cxprojectbranchnames=asCxProjectBranches);  

            bAddProjCreationToCollectionOk = self.addCxProjectCreationToCxApplicationConfigCollection(cxprojectcreation=cxProjectCreation1);

            if bAddProjCreationToCollectionOk == False:

                print("");
                print("%s The 'addCxProjectCreationToCxApplicationConfigCollection()' call failed - Error!" % (self.sClassDisp));
                print("");

                return False;

            dictProjectCreationPlist = None;
            cxProjectCreation1       = None;

        except Exception as inst:

            print("%s 'loadProjectCreationPlistFile()' - load of the Project Creation 'plist' file [%s] - operational exception occured..." % (self.sClassDisp, sProjectCreationPlistFile));
            print(type(inst));
            print(inst);

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print("- - - ");
            print('\n'.join(asTracebackLines));
            print("- - - ");

            return False;

        return True;

    def addCxProjectCreationToCxApplicationConfigCollection(self, cxprojectcreation=None):

    #   self.bTraceFlag = True;

        cxProjectCreation = cxprojectcreation;

        if cxProjectCreation == None:

            print("");
            print("%s NO CxProjectCreation has been specified nor defined for the Checkmarx CxProjectCreation(s) Collection - one CxProjectCreation MUST be defined - Error!" % (self.sClassDisp));
            print("");

            return False;

        if self.dictCxApplicationConfigCollection == None:

            if self.bTraceFlag == True:

                print("%s The object 'dictCxApplicationConfigCollection' has NOT been set - creating an internal instance..." % (self.sClassDisp));

            self.dictCxApplicationConfigCollection = collections.defaultdict(); 

        bProcessingError = False;

        try:

            sCxProjectName = cxProjectCreation.getCxProjectName();

            if sCxProjectName != None:

                sCxProjectName = sCxProjectName.strip();

            if sCxProjectName == None or \
                len(sCxProjectName) < 1:

                print("");
                print("%s The CxProjectCreation has a 'name' that is None or 'empty' - bypassing the addition of this object - Error!" % (self.sClassDisp));
                print("");

                return False;

            self.dictCxApplicationConfigCollection[sCxProjectName] = cxProjectCreation;

            if self.bTraceFlag == True:

                print("%s CxProjectCreation named [%s] added to the CxApplicationConfigCollection..." % (self.sClassDisp, sCxProjectName));

        except Exception as inst:

            print("%s 'addCxProjectCreationToCxApplicationConfigCollection()' - exception occured..." % (self.sClassDisp));
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

    def generateCxApplicationConfigCollectionReport(self):
 
        bProcessingError = False;

        self.asCxApplicationConfigCollectionReport = None;
 
        if self.dictCxApplicationConfigCollection == None or \
           len(self.dictCxApplicationConfigCollection) < 1:

            print("");
            print("%s NO Checkmarx CxProjectCreation(s) have been specified nor defined in the Checkmarx CxProjectCreation(s) Collection - at least 1 CxProjectCreation MUST be defined - Error!" % (self.sClassDisp));
            print("");

            return False;

        try:

            asCxApplicationConfigCollectionReportDebug = list();
            self.asCxApplicationConfigCollectionReport = list();

            self.asCxApplicationConfigCollectionReport.append("");
            self.asCxApplicationConfigCollectionReport.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            self.asCxApplicationConfigCollectionReport.append("%s Checkmarx CxProjectCreation(s) collection for (%d) element(s):" % \
                                                            (self.sClassDisp, len(self.dictCxApplicationConfigCollection)));
            self.asCxApplicationConfigCollectionReport.append("");

            asCxApplicationConfigCollectionReportDebug.append("");
            asCxApplicationConfigCollectionReportDebug.append("- - - - - - - - - - - - - - - - DEBUG - - - - - - - - - - - - - - - - - - - - - -");
            asCxApplicationConfigCollectionReportDebug.append("%s Checkmarx CxProjectCreation(s) collection for (%d) element(s):" % \
                                                       (self.sClassDisp, len(self.dictCxApplicationConfigCollection)));
            asCxApplicationConfigCollectionReportDebug.append("");

            cCxApplicationConfigCollection = 0;

            for sCxProjectName in list(self.dictCxApplicationConfigCollection.keys()):

                cCxApplicationConfigCollection += 1;

                cxProjectCreation = self.dictCxApplicationConfigCollection[sCxProjectName];

                if cxProjectCreation == None:

                    continue;

                self.asCxApplicationConfigCollectionReport.append("%s CxProjectCreation element (%3d) of (%3d):" % \
                                                                (self.sClassDisp, cCxApplicationConfigCollection, len(self.dictCxApplicationConfigCollection)));
                self.asCxApplicationConfigCollectionReport.append(cxProjectCreation.toPrettyStringWithWidths(dictcxprojectcreationcollectionstats=self.dictCxApplicationConfigCollectionStats));

                if self.bTraceFlag == True:

                    asCxApplicationConfigCollectionReportDebug.append("%s CxProjectCreation element (named '%s')[(%d) of (%d)] is:" % \
                                                            (self.sClassDisp, sCxProjectName, cCxApplicationConfigCollection, len(self.dictCxApplicationConfigCollection)));
                    asCxApplicationConfigCollectionReportDebug.append(cxProjectCreation.toString());
                    asCxApplicationConfigCollectionReportDebug.append("");

            self.asCxApplicationConfigCollectionReport.append("");
            self.asCxApplicationConfigCollectionReport.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            self.asCxApplicationConfigCollectionReport.append("");

            if self.bTraceFlag == True:

                asCxApplicationConfigCollectionReportDebug.append("");
                asCxApplicationConfigCollectionReportDebug.append("- - - - - - - - - - - - - - - - DEBUG - - - - - - - - - - - - - - - - - - - - - -");
                asCxApplicationConfigCollectionReportDebug.append("");

                self.asCxApplicationConfigCollectionReport.extend(asCxApplicationConfigCollectionReportDebug);

        except Exception as inst:
 
            print("%s 'generateCxApplicationConfigCollectionReport()' - exception occured..." % (self.sClassDisp));
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
 
    def saveCxApplicationConfigCollectionReportToFile(self, outputprojectcreationcollectionfile=None):

    #   self.bTraceFlag = True;

        sOutputCxApplicationConfigCollectionFile = outputprojectcreationcollectionfile;

        if sOutputCxApplicationConfigCollectionFile != None:

            sOutputCxApplicationConfigCollectionFile = sOutputCxApplicationConfigCollectionFile.strip();

        if sOutputCxApplicationConfigCollectionFile == None or \
           len(sOutputCxApplicationConfigCollectionFile) < 1:

            print("%s Command received an (Output) CxProjectCreation Collection filename that is 'null' or Empty - Error!" % (self.sClassDisp));

            return False;

        if self.asCxApplicationConfigCollectionReport == None or \
            len(self.asCxApplicationConfigCollectionReport) < 1:

            print("");
            print("%s The CxProjectCreation Collection 'report' is 'None' or Empty - Severe Error!" % (self.sClassDisp));
 
            return False;

        try:

            print("%s Command is generating the (Output) CxProjectCreation Collection 'report' into a file of [%s]..." % (self.sClassDisp, sOutputCxApplicationConfigCollectionFile));
            print("");

            fOutputCxApplicationConfigCollection = open(sOutputCxApplicationConfigCollectionFile, "w");

            fOutputCxApplicationConfigCollection.write('\n'.join(self.asCxApplicationConfigCollectionReport));
            fOutputCxApplicationConfigCollection.close();

            print("%s Command generated the (Output) CxProjectCreation Collection 'report' into a file of [%s]..." % (self.sClassDisp, sOutputCxApplicationConfigCollectionFile));
            print("");

        except Exception as inst:

            print("%s 'saveCxApplicationConfigCollectionReportToFile()' - operational exception occured..." % (self.sClassDisp));
            print(type(inst));
            print(inst);

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print("- - - ");
            print('\n'.join(asTracebackLines));
            print("- - - ");

            return False;

        return True;

