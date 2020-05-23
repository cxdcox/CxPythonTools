
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;

from datetime import datetime;

import CxServerEndpoint1;
import CxProjectCreation1;
import CxProjectData1;
import CxRestAPIProjectCreationBase1;

class CxProjectCreationCollection:

    sClassMod                           = __name__;
    sClassId                            = "CxProjectCreationCollection";
    sClassVers                          = "(v1.0501)";
    sClassDisp                          = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag                          = False;
    cxServerEndpoint                    = None;
    dictCxProjectCreationCollection     = None;

    asCxProjectCreationCollectionReport = None;

    # Project Collection 'meta' data:

    dictCxAllTeams                      = None;
    dictCxAllPresets                    = None;
    dictCxAllEngineConfigurations       = None;
    dictCxAllProjects                   = None;

    # Project Collection stats:

    cLongestProjectName                 = 0;
    cMaxProjectId                       = 0;
    cLongestProjectTeamId               = 0;

    def __init__(self, trace=False, cxserverendpoint=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setCxServerEndpoint(cxserverendpoint=cxserverendpoint);

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

    def getCxServerEndpoint(self):

        return self.cxServerEndpoint;

    def setCxServerEndpoint(self, cxserverendpoint=None):

        self.cxServerEndpoint = cxserverendpoint;

    def getCxProjectCreationCollection(self):

        return self.dictCxProjectCreationCollection;

    def setCxProjectCreationCollection(self, cxprojectcreationcollection=None):

        self.dictCxProjectCreationCollection = cxprojectcreationcollection;

    def getCxProjectCreationCollectionReportAsList(self):

        return self.asCxProjectCreationCollectionReport;

    def getCxProjectMetaDataAllTeams(self):

        return self.dictCxAllTeams;

    def addCxProjectMetaDataAllTeams(self, cxteamfullname=None, cxteamid=None):

        sCxTeamFullName = cxteamfullname;

        if sCxTeamFullName != None:

            sCxTeamFullName = sCxTeamFullName.strip();

        if sCxTeamFullName == None or \
            len(sCxTeamFullName) < 1:

            return;

        sCxTeamId = cxteamid;

        if sCxTeamId != None:

            sCxTeamId = sCxTeamId.strip();

        if sCxTeamId == None or \
            len(sCxTeamId) < 1:

            sCxTeamId = "";

        if self.dictCxAllTeams == None:

            self.dictCxAllTeams = collections.defaultdict();

        self.dictCxAllTeams[sCxTeamFullName] = sCxTeamId;

    def getCxProjectMetaDataAllPresets(self):

        return self.dictCxAllPresets;

    def addCxProjectMetaDataAllPresets(self, cxpresetname=None, cxpresetdict=None):

        sCxPresetName = cxpresetname;

        if sCxPresetName != None:

            sCxPresetName = sCxPresetName.strip();

        if sCxPresetName == None or \
            len(sCxPresetName) < 1:

            return;

        dictCxPreset = cxpresetdict;

        if dictCxPreset == None or \
            len(dictCxPreset) < 1:

            return;

        if self.dictCxAllPresets == None:

            self.dictCxAllPresets = collections.defaultdict();

        self.dictCxAllPresets[sCxPresetName] = dictCxPreset;

    def getCxProjectMetaDataAllEngineConfigurations(self):

        return self.dictCxAllEngineConfigurations;

    def addCxProjectMetaDataAllEngineConfigurations(self, cxengineconfigname=None, cxengineconfigid=None):

        sCxEngineConfigName = cxengineconfigname;

        if sCxEngineConfigName != None:

            sCxEngineConfigName = sCxEngineConfigName.strip();

        if sCxEngineConfigName == None or \
            len(sCxEngineConfigName) < 1:

            return;

        sCxEngineConfigId = cxengineconfigid;

        if sCxEngineConfigId != None:

            sCxEngineConfigId = sCxEngineConfigId.strip();

        if sCxEngineConfigId == None or \
            len(sCxEngineConfigId) < 1:

            sCxEngineConfigId = "";

        if self.dictCxAllEngineConfigurations == None:

            self.dictCxAllEngineConfigurations = collections.defaultdict();

        self.dictCxAllEngineConfigurations[sCxEngineConfigName] = sCxEngineConfigId;

    def getCxProjectMetaDataAllProjects(self):

        return self.dictCxAllProjects;

    def addCxProjectMetaDataAllProjects(self, cxprojectdata=None):

        cxProjectData = cxprojectdata;

        if cxProjectData == None:

            return;

        sCxProjectDataName = cxProjectData.getCxProjectName();

        if sCxProjectDataName != None:

            sCxProjectDataName = sCxProjectDataName.strip();

        if sCxProjectDataName == None or \
            len(sCxProjectDataName) < 1:

            return;

        if self.dictCxAllProjects == None:

            self.dictCxAllProjects = collections.defaultdict();

        self.dictCxAllProjects[sCxProjectDataName] = cxProjectData;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);

            if self.cxServerEndpoint == None:

                print "%s The 'cxServerEndpoint' has NOT been set..." % (self.sClassDisp);

            else:

                print "%s The 'cxServerEndpoint' is [%s]..." % (self.sClassDisp, self.cxServerEndpoint);

            if self.dictCxProjectCreationCollection == None:

                print "%s The 'dictCxProjectCreationCollection' has NOT been set..." % (self.sClassDisp);

            else:

                print "%s The 'dictCxProjectCreationCollection' is [%s]..." % (self.sClassDisp, self.dictCxProjectCreationCollection);

            print "%s The contents of 'asCxProjectCreationCollectionReport' is [%s]..." % (self.sClassDisp, self.asCxProjectCreationCollectionReport);
            print "%s The contents of 'dictCxAllTeams' is [%s]..." % (self.sClassDisp, self.dictCxAllTeams);
            print "%s The contents of 'dictCxAllPresets' is [%s]..." % (self.sClassDisp, self.dictCxAllPresets);
            print "%s The contents of 'dictCxAllEngineConfigurations' is [%s]..." % (self.sClassDisp, self.dictCxAllEngineConfigurations);
            print "%s The contents of 'dictCxAllProjects' is [%s]..." % (self.sClassDisp, self.dictCxAllProjects);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'cxServerEndpoint' is [%s], " % (self.cxServerEndpoint));
        asObjDetail.append("'dictCxProjectCreationCollection' is [%s], " % (self.dictCxProjectCreationCollection));
        asObjDetail.append("'asCxProjectCreationCollectionReport' is [%s], " % (self.asCxProjectCreationCollectionReport));
        asObjDetail.append("'dictCxAllTeams' is [%s], " % (self.dictCxAllTeams));
        asObjDetail.append("'dictCxAllPresets' is [%s], " % (self.dictCxAllPresets));
        asObjDetail.append("'dictCxAllEngineConfigurations' is [%s], " % (self.dictCxAllEngineConfigurations));
        asObjDetail.append("'dictCxAllProjects' is [%s]. " % (self.dictCxAllProjects));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def loadCxProjectCreationMetaDataToCollectionFromRestAPI(self):

    #   self.bTraceFlag = True;

        if self.cxServerEndpoint == None:

            print "";
            print "%s NO CxServerEndpoint has been specified nor defined for the Checkmarx CxProject(s) Collection - one CxServerEndpoint MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.cxServerEndpoint.getCxServerEndpointActiveFlag() == False:

            print "";
            print "%s The supplied CxServerEndpoint is NOT marked 'active' - it MUST be marked 'active' to be used - Error!" % (self.sClassDisp);
            print "";

            return False;

        bProcessingError = False;

        try:

            cxProjCreationBase = CxRestAPIProjectCreationBase1.CxRestAPIProjectCreationBase(trace=self.bTraceFlag, cxserverendpoint=self.cxServerEndpoint, cxprojectcreationcollection=self);

            if cxProjCreationBase == None:

                print "";
                print "%s Failed to create a CxRestAPIProjectCreationBase object - Error!" % (self.sClassDisp);
                print "";

                return False;

            bGetProjMetaOk = cxProjCreationBase.getCxRestAPIProjectCreationMetaData();

            if bGetProjMetaOk == False:

                print "";
                print "%s 'cxProjCreationBase.getCxRestAPIProjectCreationMetaData()' API call failed - Error!" % (self.sClassDisp);
                print "";

                bProcessingError = True;

        except Exception, inst:

            print "%s 'loadCxProjectCreationMetaDataToCollectionFromRestAPI()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        if bProcessingError == True:

            return False;

        return True;

    def addCxProjectCreationToCxProjectCreationCollection(self, cxprojectcreation=None):

    #   self.bTraceFlag = True;

        cxProjectCreation = cxprojectcreation;

        if cxProjectCreation == None:

            print "";
            print "%s NO CxProjectCreation has been specified nor defined for the Checkmarx CxProjectCreation(s) Collection - one CxProjectCreation MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.dictCxProjectCreationCollection == None:

            if self.bTraceFlag == True:

                print "%s The object 'dictCxProjectCreationCollection' has NOT been set - creating an internal instance..." % (self.sClassDisp);

            self.dictCxProjectCreationCollection = collections.defaultdict(); 

        bProcessingError = False;

        try:

            sCxProjectName = cxProjectCreation.getCxProjectName();

            if sCxProjectName != None:

                sCxProjectName = sCxProjectName.strip();

            if sCxProjectName == None or \
                len(sCxProjectName) < 1:

                print "";
                print "%s The CxProjectCreation has a 'name' that is None or 'empty' - bypassing the addition of this object - Error!" % (self.sClassDisp);
                print "";

                return False;

            # Gather 'max' field width stats:

            if len(sCxProjectName) > self.cLongestProjectName:

                self.cLongestProjectName = len(sCxProjectName);

        #   cDataMaxProjectId = len(cxProjectCreation.getCxProjectId());
        #
        #   if cDataMaxProjectId > self.cMaxProjectId:
        #
        #       self.cMaxProjectId = cDataMaxProjectId;
        #
        #   cDataLongestProjectTeamId = len(cxProjectCreation.getCxProjectTeamId());
        #
        #   if cDataLongestProjectTeamId > self.cLongestProjectTeamId:
        #
        #       self.cLongestProjectTeamId = cDataLongestProjectTeamId;
        #
        #   cDataMaxProjectLinks = len(cxProjectCreation.getCxProjectLinks()); 
        #   sDataMaxProjectLinks = ("%d" % cDataMaxProjectLinks);
        #   cDataMaxProjectLinks = len(sDataMaxProjectLinks); 
        #
        #   if cDataMaxProjectLinks > self.cMaxProjectLinks:
        #
        #       self.cMaxProjectLinks = cDataMaxProjectLinks;
        #
        #   cDataMaxProjectCustomFields = len(cxProjectCreation.getCxProjectCustomFields()); 
        #   sDataMaxProjectCustomFields = ("%d" % cDataMaxProjectCustomFields);
        #   cDataMaxProjectCustomFields = len(sDataMaxProjectCustomFields); 
        #
        #   if cDataMaxProjectCustomFields > self.cMaxProjectCustomFields:
        #
        #       self.cMaxProjectCustomFields = cDataMaxProjectCustomFields;

            self.dictCxProjectCreationCollection[sCxProjectName] = cxProjectCreation;

            if self.bTraceFlag == True:

                print "%s CxProjectCreation named [%s] added to the CxProjectCreationCollection..." % (self.sClassDisp, sCxProjectName);

        except Exception, inst:

            print "%s 'addCxProjectCreationToCxProjectCreationCollection()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        if bProcessingError == True:

            return False;

        return True;

    def generateCxProjectCreationCollectionReport(self):
 
        bProcessingError = False;

        self.asCxProjectCreationCollectionReport = None;
 
        if self.dictCxProjectCreationCollection == None or \
           len(self.dictCxProjectCreationCollection) < 1:

            print "";
            print "%s NO Checkmarx CxProject(s) have been specified nor defined in the Checkmarx CxProject(s) Collection - at least 1 CxProject MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        try:

            self.asCxProjectCreationCollectionReport = list();

            self.asCxProjectCreationCollectionReport.append("");
            self.asCxProjectCreationCollectionReport.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            self.asCxProjectCreationCollectionReport.append("%s Checkmarx CxProjectCreation(s) collection for (%d) element(s):" % \
                                                    (self.sClassDisp, len(self.dictCxProjectCreationCollection)));
            self.asCxProjectCreationCollectionReport.append("");

            cCxProjectCollection = 0;

            for sCxProjectName in self.dictCxProjectCreationCollection.keys():

                cCxProjectCollection += 1;

                cxProjectCreation = self.dictCxProjectCreationCollection[sCxProjectName];

                if cxProjectCreation == None:

                    continue;

                if self.bTraceFlag == True:

                    self.asCxProjectCreationCollectionReport.append("%s CxProjectCreation element (named '%s')[(%d) of (%d)] is:" % \
                                                            (self.sClassDisp, sCxProjectName, cCxProjectCollection, len(self.dictCxProjectCreationCollection)));
                    self.asCxProjectCreationCollectionReport.append(cxProjectCreation.toString());
                    self.asCxProjectCreationCollectionReport.append("");

                else:

                    self.asCxProjectCreationCollectionReport.append("%s CxProject element (%3d) of (%3d): [%s]..." %                           \
                                                            (self.sClassDisp, cCxProjectCollection, len(self.dictCxProjectCreationCollection), \
                                                            cxProjectCreation.toPrettyStringWithWidths(                                        \
                                                            cWidthId=self.cMaxProjectId,                                                       \
                                                            cWidthTeamId=self.cMaxProjectId,                                                   \
                                                            cWidthName=self.cLongestProjectName)));

            self.asCxProjectCreationCollectionReport.append("");
            self.asCxProjectCreationCollectionReport.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            self.asCxProjectCreationCollectionReport.append("");

        except Exception, inst:
 
            print "%s 'generateCxProjectCreationCollectionReport()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;
 
            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);
 
            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";
 
            return False;
 
        if bProcessingError == True:
 
            return False;
 
        return True;
 
    def saveCxProjectCreationCollectionToFile(self, outputprojectcreationcollectionfile=None, outputprojectcreationname=None):

    #   self.bTraceFlag = True;

        sOutputCxProjectCreationCollectionFile = outputprojectcreationcollectionfile;

        if sOutputCxProjectCreationCollectionFile != None:

            sOutputCxProjectCreationCollectionFile = sOutputCxProjectCreationCollectionFile.strip();

        if sOutputCxProjectCreationCollectionFile == None or \
           len(sOutputCxProjectCreationCollectionFile) < 1:

            print "%s Command received an (Output) CxProject Collection filename that is 'null' or Empty - Error!" % (self.sClassDisp);

            return False;

        sOutputCxProjectCreationName = outputprojectcreationname;

        if sOutputCxProjectCreationName != None:
         
            sOutputCxProjectCreationName = sOutputCxProjectCreationName.strip();
         
        if sOutputCxProjectCreationName == None or \
           len(sOutputCxProjectCreationName) < 1:
         
            sOutputCxProjectCreationName = "New CxProject";
         
        if self.dictCxProjectCreationCollection == None or \
           len(self.dictCxProjectCreationCollection) < 1:
 
            print "";
            print "%s The CxProjectCreation Collection is 'None' or Empty - Severe Error!" % (self.sClassDisp);
 
            return False;

        try:

            print "%s Command is generating the (Output) CxProjectCreation Collection named [%s] into a file of [%s]..." % (self.sClassDisp, sOutputCxProjectCreationName, sOutputCxProjectCreationCollectionFile);
            print "";

            fOutputCxProjectCreationCollection = open(sOutputCxProjectCreationCollectionFile, "w");

            # <Preset Id="5" Name="PCI">
            #     <OtherQueryIds>

            fOutputCxProjectCreationCollection.write("<Preset Id=\"999\" Name=\"%s\">\n" % (sOutputCxProjectCreationName));
            fOutputCxProjectCreationCollection.write("    <OtherQueryIds>\n");

            cCxProjectCollection = 0;

            for sCxProjectName in self.dictCxProjectCreationCollection.keys():

                cCxProjectCollection += 1;

                cxProjectCreation = self.dictCxProjectCreationCollection[sCxProjectName];

                if cxProjectCreation == None:

                    continue;

                #         <OtherQueryId>138</OtherQueryId>

                fOutputCxProjectCreationCollection.write("        <OtherQueryId>%s</OtherQueryId>\n" % (sCxProjectName));

            #     </OtherQueryIds>
            #     <Queries/>
            # </Preset>

            fOutputCxProjectCreationCollection.write("    </OtherQueryIds>\n");
            fOutputCxProjectCreationCollection.write("    <Queries/>\n");
            fOutputCxProjectCreationCollection.write("</Preset>\n");
            fOutputCxProjectCreationCollection.close();

            print "%s Command generated the (Output) CxProjectCreation Collection named [%s] into a file of [%s]..." % (self.sClassDisp, sOutputCxProjectCreationName, sOutputCxProjectCreationCollectionFile);
            print "";

        except Exception, inst:

            print "%s 'saveCxProjectCreationCollectionToFile()' - operational exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

