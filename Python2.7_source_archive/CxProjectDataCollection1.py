
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;

from datetime import datetime;

import CxServerEndpoint1;
import CxProjectData1;
import CxRestAPIProjectCreationBase1;

class CxProjectDataCollection:

    sClassMod                       = __name__;
    sClassId                        = "CxProjectDataCollection";
    sClassVers                      = "(v1.0501)";
    sClassDisp                      = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag                      = False;
    cxServerEndpoint                = None;
    dictCxProjectDataCollection     = None;
    asCxProjectDataCollectionReport = None;

    # Project Collection stats:

    cLongestProjectName             = 0;
    cMaxProjectId                   = 0;
    cLongestProjectTeamId           = 0;
    cMaxProjectLinks                = 0;
    cMaxProjectCustomFields         = 0;

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

    def getCxProjectDataCollection(self):

        return self.dictCxProjectDataCollection;

    def setCxProjectDataCollection(self, cxprojectdatacollection=None):

        self.dictCxProjectDataCollection = cxprojectdatacollection;

    def getCxProjectDataCollectionReportAsList(self):

        return self.asCxProjectDataCollectionReport;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);

            if self.cxServerEndpoint == None:

                print "%s The 'cxServerEndpoint' has NOT been set..." % (self.sClassDisp);

            else:

                print "%s The 'cxServerEndpoint' is [%s]..." % (self.sClassDisp, self.cxServerEndpoint);

            if self.dictCxProjectDataCollection == None:

                print "%s The 'dictCxProjectDataCollection' has NOT been set..." % (self.sClassDisp);

            else:

                print "%s The 'dictCxProjectDataCollection' is [%s]..." % (self.sClassDisp, self.dictCxProjectDataCollection);

            print "%s The contents of 'asCxProjectDataCollectionReport' is [%s]..." % (self.sClassDisp, self.asCxProjectDataCollectionReport);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'cxServerEndpoint' is [%s], " % (self.cxServerEndpoint));
        asObjDetail.append("'dictCxProjectDataCollection' is [%s], " % (self.dictCxProjectDataCollection));
        asObjDetail.append("'asCxProjectDataCollectionReport' is [%s]. " % (self.asCxProjectDataCollectionReport));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def loadCxProjectDataCollectionFromRestAPI(self):

    #   self.bTraceFlag = True;

        if self.cxServerEndpoint == None:

            print "";
            print "%s NO CxServerEndpoint has been specified nor defined for the Checkmarx CxProjectCreation(s) Collection - one CxServerEndpoint MUST be defined - Error!" % (self.sClassDisp);
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

            print "%s 'loadCxProjectDataCollectionFromRestAPI()' - exception occured..." % (self.sClassDisp);
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

    def addCxProjectDataToCxProjectDataCollection(self, cxprojectdata=None):

    #   self.bTraceFlag = True;

        cxProjectData = cxprojectdata;

        if cxProjectData == None:

            print "";
            print "%s NO CxProjectData has been specified nor defined for the Checkmarx CxProject(s) Collection - one CxProjectData MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.dictCxProjectDataCollection == None:

            if self.bTraceFlag == True:

                print "%s The object 'dictCxProjectDataCollection' has NOT been set - creating an internal instance..." % (self.sClassDisp);

            self.dictCxProjectDataCollection = collections.defaultdict(); 

        bProcessingError = False;

        try:

            sCxProjectName = cxProjectData.getCxProjectName();

            if sCxProjectName != None:

                sCxProjectName = sCxProjectName.strip();

            if sCxProjectName == None or \
                len(sCxProjectName) < 1:

                print "";
                print "%s The CxProjectData has a 'name' that is None or 'empty' - bypassing the addition of this object - Error!" % (self.sClassDisp);
                print "";

                return False;

            # Gather 'max' field width stats:

            if len(sCxProjectName) > self.cLongestProjectName:

                self.cLongestProjectName = len(sCxProjectName);

            cDataMaxProjectId = len(cxProjectData.getCxProjectId());

            if cDataMaxProjectId > self.cMaxProjectId:

                self.cMaxProjectId = cDataMaxProjectId;

            cDataLongestProjectTeamId = len(cxProjectData.getCxProjectTeamId());

            if cDataLongestProjectTeamId > self.cLongestProjectTeamId:

                self.cLongestProjectTeamId = cDataLongestProjectTeamId;

            cDataMaxProjectLinks = len(cxProjectData.getCxProjectLinks()); 
            sDataMaxProjectLinks = ("%d" % cDataMaxProjectLinks);
            cDataMaxProjectLinks = len(sDataMaxProjectLinks); 

            if cDataMaxProjectLinks > self.cMaxProjectLinks:

                self.cMaxProjectLinks = cDataMaxProjectLinks;

            cDataMaxProjectCustomFields = len(cxProjectData.getCxProjectCustomFields()); 
            sDataMaxProjectCustomFields = ("%d" % cDataMaxProjectCustomFields);
            cDataMaxProjectCustomFields = len(sDataMaxProjectCustomFields); 

            if cDataMaxProjectCustomFields > self.cMaxProjectCustomFields:

                self.cMaxProjectCustomFields = cDataMaxProjectCustomFields;

            self.dictCxProjectDataCollection[sCxProjectName] = cxProjectData;

            if self.bTraceFlag == True:

                print "%s CxProjectData named [%s] added to the CxProjectDataCollection..." % (self.sClassDisp, sCxProjectName);

        except Exception, inst:

            print "%s 'addCxProjectDataToCxProjectDataCollection()' - exception occured..." % (self.sClassDisp);
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

    def generateCxProjectDataCollectionReport(self):
 
        bProcessingError = False;

        self.asCxProjectDataCollectionReport = None;
 
        if self.dictCxProjectDataCollection == None or \
           len(self.dictCxProjectDataCollection) < 1:

            print "";
            print "%s NO Checkmarx CxProject(s) have been specified nor defined in the Checkmarx CxProject(s) Collection - at least 1 CxProject MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        try:

            self.asCxProjectDataCollectionReport = list();

            self.asCxProjectDataCollectionReport.append("");
            self.asCxProjectDataCollectionReport.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            self.asCxProjectDataCollectionReport.append("%s Checkmarx CxProject(s) collection for (%d) element(s):" % \
                                                    (self.sClassDisp, len(self.dictCxProjectDataCollection)));
            self.asCxProjectDataCollectionReport.append("");

            cCxProject = 0;

            for sCxProjectName in self.dictCxProjectDataCollection.keys():

                cCxProject += 1;

                cxProjectData = self.dictCxProjectDataCollection[sCxProjectName];

                if cxProjectData == None:

                    continue;

                if self.bTraceFlag == True:

                    self.asCxProjectDataCollectionReport.append("%s CxProjectData element (named '%s')[(%d) of (%d)] is:" % \
                                                            (self.sClassDisp, sCxProjectName, cCxProject, len(self.dictCxProjectDataCollection)));
                    self.asCxProjectDataCollectionReport.append(cxProjectData.toString());
                    self.asCxProjectDataCollectionReport.append("");

                else:

                    self.asCxProjectDataCollectionReport.append("%s CxProject element (%3d) of (%3d): [%s]..." %                    \
                                                            (self.sClassDisp, cCxProject, len(self.dictCxProjectDataCollection),   \
                                                            cxProjectData.toPrettyStringWithWidths(                             \
                                                            cWidthId=self.cMaxProjectId,                                        \
                                                            cWidthLinks=self.cMaxProjectLinks,                                  \
                                                            cWidthCustFields=self.cMaxProjectCustomFields,                      \
                                                            cWidthScans=4,                                                      \
                                                            cWidthTeamId=self.cMaxProjectId,                                    \
                                                            cWidthName=self.cLongestProjectName)));

            self.asCxProjectDataCollectionReport.append("");
            self.asCxProjectDataCollectionReport.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            self.asCxProjectDataCollectionReport.append("");

        except Exception, inst:
 
            print "%s 'generateCxProjectDataCollectionReport()' - exception occured..." % (self.sClassDisp);
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
 
    def saveCxProjectDataCollectionToFile(self, outputprojectdatacollectionfile=None, outputprojectdataname=None):

    #   self.bTraceFlag = True;

        sOutputCxProjectDataCollectionFile = outputprojectdatacollectionfile;

        if sOutputCxProjectDataCollectionFile != None:

            sOutputCxProjectDataCollectionFile = sOutputCxProjectDataCollectionFile.strip();

        if sOutputCxProjectDataCollectionFile == None or \
           len(sOutputCxProjectDataCollectionFile) < 1:

            print "%s Command received an (Output) CxProject Collection filename that is 'null' or Empty - Error!" % (self.sClassDisp);

            return False;

        sOutputCxProjectDataName = outputprojectdataname;

        if sOutputCxProjectDataName != None:
         
            sOutputCxProjectDataName = sOutputCxProjectDataName.strip();
         
        if sOutputCxProjectDataName == None or \
           len(sOutputCxProjectDataName) < 1:
         
            sOutputCxProjectDataName = "New CxProject";
         
        if self.dictCxProjectDataCollection == None or \
           len(self.dictCxProjectDataCollection) < 1:
 
            print "";
            print "%s The CxProject Collection is 'None' or Empty - Severe Error!" % (self.sClassDisp);
 
            return False;

        try:

            print "%s Command is generating the (Output) CxProject Collection named [%s] into a file of [%s]..." % (self.sClassDisp, sOutputCxProjectDataName, sOutputCxProjectDataCollectionFile);
            print "";

            fOutputCxProjectDataCollection = open(sOutputCxProjectDataCollectionFile, "w");

            # <Preset Id="5" Name="PCI">
            #     <OtherQueryIds>

            fOutputCxProjectDataCollection.write("<Preset Id=\"999\" Name=\"%s\">\n" % (sOutputCxProjectDataName));
            fOutputCxProjectDataCollection.write("    <OtherQueryIds>\n");

            cCxProject = 0;

            for sCxProjectName in self.dictCxProjectDataCollection.keys():

                cCxProject += 1;

                cxProjectData = self.dictCxProjectDataCollection[sCxProjectName];

                if cxProjectData == None:

                    continue;

                #         <OtherQueryId>138</OtherQueryId>

                fOutputCxProjectDataCollection.write("        <OtherQueryId>%s</OtherQueryId>\n" % (sCxProjectName));

            #     </OtherQueryIds>
            #     <Queries/>
            # </Preset>

            fOutputCxProjectDataCollection.write("    </OtherQueryIds>\n");
            fOutputCxProjectDataCollection.write("    <Queries/>\n");
            fOutputCxProjectDataCollection.write("</Preset>\n");
            fOutputCxProjectDataCollection.close();

            print "%s Command generated the (Output) CxProject Collection named [%s] into a file of [%s]..." % (self.sClassDisp, sOutputCxProjectDataName, sOutputCxProjectDataCollectionFile);
            print "";

        except Exception, inst:

            print "%s 'saveCxProjectDataCollectionToFile()' - operational exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

