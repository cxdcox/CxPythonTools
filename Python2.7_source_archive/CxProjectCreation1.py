
import os;
import traceback;
import re;
import string;
import sys;
import collections;

class CxProjectCreation:

    sClassMod                  = __name__;
    sClassId                   = "CxProjectCreation";
    sClassVers                 = "(v1.0501)";
    sClassDisp                 = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag                 = False;

    sCxProjectName             = None;
    bCxProjectIsPublic         = False;
    sCxProjectSubName          = None;
    sCxProjectTeamName         = None;
    sCxProjectPresetName       = None;
    sCxProjectEngineConfigName = None;
    asCxProjectBranchNames     = None;          # Array of 'name(s)' of 'branches' of a given Project.

    # Fields that are determined by 'lookup' or Rest API response:

    sCxProjectId               = None;
    sCxProjectTeamId           = None;
    sCxProjectPresetId         = None;
    sCxProjectEngineConfigId   = None;
    dictCxProjectBranchedNames = None;          # Dictionary of 'branched' Project 'name(s)': ["project-branch-name", "project-branch_project-id"]

    def __init__(self, trace=False, cxprojectname=None, cxprojectispublic=True, cxprojectsubname=None, cxprojectteamname=None, cxprojectpresetname=None, cxprojectengineconfigname=None, cxprojectbranchnames=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setCxProjectName(cxprojectname=cxprojectname);
            self.setCxProjectIsPublic(cxprojectispublic=cxprojectispublic);
            self.setCxProjectSubName(cxprojectsubname=cxprojectsubname);
            self.setCxProjectTeamName(cxprojectteamname=cxprojectteamname);
            self.setCxProjectPresetName(cxprojectpresetname=cxprojectpresetname);
            self.setCxProjectEngineConfigName(cxprojectengineconfigname=cxprojectengineconfigname);
            self.setCxProjectBranchNames(cxprojectbranchnames=cxprojectbranchnames);

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

    def getCxProjectName(self):

        return self.sCxProjectName;

    def setCxProjectName(self, cxprojectname=None):

        self.sCxProjectName = cxprojectname;

        if self.sCxProjectName != None:

            self.sCxProjectName = self.sCxProjectName.strip();

        if self.sCxProjectName == None or \
           len(self.sCxProjectName) < 1:
         
            self.sCxProjectName = None;
         
    def getCxProjectIsPublic(self):

        return self.bCxProjectIsPublic;

    def setCxProjectIsPublic(self, cxprojectispublic=False):

        self.bCxProjectIsPublic = cxprojectispublic;

    def getCxProjectSubName(self):

        return self.sCxProjectSubName;

    def setCxProjectSubName(self, cxprojectsubname=None):

        self.sCxProjectSubName = cxprojectsubname;

        if self.sCxProjectSubName != None:

            self.sCxProjectSubName = self.sCxProjectSubName.strip();

        if self.sCxProjectSubName == None or \
           len(self.sCxProjectSubName) < 1:

            self.sCxProjectSubName = None;

    def getCxProjectTeamName(self):

        return self.sCxProjectTeamName;

    def setCxProjectTeamName(self, cxprojectteamname=None):

        self.sCxProjectTeamName = cxprojectteamname;

        if self.sCxProjectTeamName != None:

            self.sCxProjectTeamName = self.sCxProjectTeamName.strip();

        if self.sCxProjectTeamName == None or \
           len(self.sCxProjectTeamName) < 1:

            self.sCxProjectTeamName = None;

    def getCxProjectPresetName(self):

        return self.sCxProjectPresetName;

    def setCxProjectPresetName(self, cxprojectpresetname=None):

        self.sCxProjectPresetName = cxprojectpresetname;

        if self.sCxProjectPresetName != None:

            self.sCxProjectPresetName = self.sCxProjectPresetName.strip();

        if self.sCxProjectPresetName == None or \
           len(self.sCxProjectPresetName) < 1:

            self.sCxProjectPresetName = None;

    def getCxProjectEngineConfigName(self):

        return self.sCxProjectEngineConfigName;

    def setCxProjectEngineConfigName(self, cxprojectengineconfigname=None):

        self.sCxProjectEngineConfigName = cxprojectengineconfigname;

        if self.sCxProjectEngineConfigName != None:

            self.sCxProjectEngineConfigName = self.sCxProjectEngineConfigName.strip();

        if self.sCxProjectEngineConfigName == None or \
           len(self.sCxProjectEngineConfigName) < 1:

            self.sCxProjectEngineConfigName = None;

    def getCxProjectBranchNames(self):

        return self.asCxProjectBranchNames;

    def setCxProjectBranchNames(self, cxprojectbranchnames=None):

        sCxProjectBranchNames   = cxprojectbranchnames;
        asSetProjectBranchNames = None;

        if type(sCxProjectBranchNames) == list:

            asSetProjectBranchNames = sCxProjectBranchNames;

        else:

            if type(sCxProjectBranchNames) == str:

                if sCxProjectBranchNames != None:

                    sCxProjectBranchNames = sCxProjectBranchNames.strip();

                if sCxProjectBranchNames == None or \
                    len(sCxProjectBranchNames) < 1:

                    self.asCxProjectBranchNames = None;

                    return;

                asSetProjectBranchNames = sCxProjectBranchNames.split(',');

        if asSetProjectBranchNames == None or \
           len(asSetProjectBranchNames) < 1:

            self.asCxProjectBranchNames = None;

            return;

        for sSetProjectBranchName in asSetProjectBranchNames:

            sSetProjectBranchName = sSetProjectBranchName.strip();

            if sSetProjectBranchName == None or \
               len(sSetProjectBranchName) < 1:

                continue;

            if self.asCxProjectBranchNames == None:

                self.asCxProjectBranchNames = [];

            self.asCxProjectBranchNames.append(sSetProjectBranchName);

    # Fields that are determined by 'lookup' or Rest API response:

    def getCxProjectId(self):

        return self.sCxProjectId;

    def setCxProjectId(self, cxprojectid=None):

        if type(cxprojectid) == str:

            self.sCxProjectId = cxprojectid;

            if self.sCxProjectId != None:

                self.sCxProjectId = self.sCxProjectId.strip();

            if self.sCxProjectId == None or \
               len(self.sCxProjectId) < 1:

                self.sCxProjectId = "";

        else:

            self.sCxProjectId = ("%d" % cxprojectid);

    def getCxProjectTeamId(self):

        return self.sCxProjectTeamId;

    def setCxProjectTeamId(self, cxprojectteamid=None):

        self.sCxProjectTeamId = cxprojectteamid;

        if self.sCxProjectTeamId == None or \
           len(self.sCxProjectTeamId) < 1:

            self.sCxProjectTeamId = "";

    def getCxProjectPresetId(self):

        return self.sCxProjectPresetId;

    def setCxProjectPresetId(self, cxprojectpresetid=None):

        if type(cxprojectid) == str:

            self.sCxProjectPresetId = cxprojectpresetid;

            if self.sCxProjectPresetId != None:

                self.sCxProjectPresetId = self.sCxProjectPresetId.strip();

            if self.sCxProjectPresetId == None or \
               len(self.sCxProjectPresetId) < 1:

                self.sCxProjectPresetId = "";

        else:

            self.sCxProjectPresetId = ("%d" % cxprojectpresetid);

    def getCxProjectEngineConfigId(self):

        return self.sCxProjectEngineConfigId;

    def setCxProjectEngineConfigId(self, cxprojectengineconfigid=None):

        if type(cxprojectid) == str:

            self.sCxProjectEngineConfigId = cxprojectengineconfigid;

            if self.sCxProjectEngineConfigId != None:

                self.sCxProjectEngineConfigId = self.sCxProjectEngineConfigId.strip();

            if self.sCxProjectEngineConfigId == None or \
               len(self.sCxProjectEngineConfigId) < 1:

                self.sCxProjectEngineConfigId = "";

        else:

            self.sCxProjectEngineConfigId = ("%d" % cxprojectengineconfigid);

    def getCxProjectBranchedNames(self):

        return self.dictCxProjectBranchedNames;

    def setCxProjectBranchedNames(self, cxprojectbranchednames=None):

        if type(cxprojectbranchednames) == dict:

            self.dictCxProjectBranchedNames = cxprojectbranchednames;

            if self.dictCxProjectBranchedNames == None or \
               len(self.dictCxProjectBranchedNames) < 1:

                self.dictCxProjectBranchedNames = None;

        else:

            self.dictCxProjectBranchedNames = None;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);
            print "%s The contents of 'sCxProjectName' is [%s]..." % (self.sClassDisp, self.sCxProjectName);
            print "%s The contents of 'bCxProjectIsPublic' is [%s]..." % (self.sClassDisp, self.bCxProjectIsPublic);
            print "%s The contents of 'sCxProjectSubName' is [%s]..." % (self.sClassDisp, self.sCxProjectSubName);
            print "%s The contents of 'sCxProjectTeamName' is [%s]..." % (self.sClassDisp, self.sCxProjectTeamName);
            print "%s The contents of 'sCxProjectPresetName' is [%s]..." % (self.sClassDisp, self.sCxProjectPresetName);
            print "%s The contents of 'sCxProjectEngineConfigName' is [%s]..." % (self.sClassDisp, self.sCxProjectEngineConfigName);
            print "%s The contents of 'asCxProjectBranchNames' is [%s]..." % (self.sClassDisp, self.asCxProjectBranchNames);
            print "%s The contents of 'sCxProjectId' is [%s]..." % (self.sClassDisp, self.sCxProjectId);
            print "%s The contents of 'sCxProjectTeamId' is [%s]..." % (self.sClassDisp, self.sCxProjectTeamId);
            print "%s The contents of 'sCxProjectPresetId' is [%s]..." % (self.sClassDisp, self.sCxProjectPresetId);
            print "%s The contents of 'sCxProjectEngineConfigId' is [%s]..." % (self.sClassDisp, self.sCxProjectEngineConfigId);
            print "%s The contents of 'dictCxProjectBranchedNames' is [%s]..." % (self.sClassDisp, self.dictCxProjectBranchedNames);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'sCxProjectName' is [%s], " % (self.sCxProjectName));
        asObjDetail.append("'bCxProjectIsPublic' is [%s], " % (self.bCxProjectIsPublic));
        asObjDetail.append("'sCxProjectSubName' is [%s], " % (self.sCxProjectSubName));
        asObjDetail.append("'sCxProjectTeamName' is [%s], " % (self.sCxProjectTeamName));
        asObjDetail.append("'sCxProjectPresetName' is [%s], " % (self.sCxProjectPresetName));
        asObjDetail.append("'sCxProjectEngineConfigName' is [%s], " % (self.sCxProjectEngineConfigName));
        asObjDetail.append("'asCxProjectBranchNames' is [%s], " % (self.asCxProjectBranchNames));
        asObjDetail.append("'sCxProjectId' is [%s], " % (self.sCxProjectId));
        asObjDetail.append("'sCxProjectTeamId' is [%s], " % (self.sCxProjectTeamId));
        asObjDetail.append("'sCxProjectPresetId' is [%s], " % (self.sCxProjectPresetId));
        asObjDetail.append("'sCxProjectEngineConfigId' is [%s], " % (self.sCxProjectEngineConfigId));
        asObjDetail.append("'dictCxProjectBranchedNames' is [%s]. " % (self.dictCxProjectBranchedNames));

        return ''.join(asObjDetail);

    def toPrettyString(self):

        return self.toPrettyStringWithWidths();

    def toPrettyStringWithWidths(self, cWidthTeamId=36, cWidthPreset=24, cWidthSubName=20, cWidthName=70):

        asObjDetail = list();

        asObjDetail.append("'Public?' [%5s], " % (self.bCxProjectIsPublic));
        asObjDetail.append("'TeamId' [%*s], " % (cWidthTeamId, self.sCxProjectTeamId));
        asObjDetail.append("'Preset' [%*s], " % (cWidthPreset, self.sCxProjectPresetName));

        sCxProjectSubName = "";

        if self.sCxProjectSubName != None:

            self.sCxProjectSubName = self.sCxProjectSubName.strip();

        if self.sCxProjectSubName != None and \
            len(self.sCxProjectSubName) > 0:

            sCxProjectSubName = self.sCxProjectSubName;
         
        asObjDetail.append("'Name' [%-*s], " % (cWidthSubName, sCxProjectSubName));

        sCxProjectName = "";

        if self.sCxProjectName != None:

            self.sCxProjectName = self.sCxProjectName.strip();

        if self.sCxProjectName != None and \
            len(self.sCxProjectName) > 0:

            sCxProjectName = self.sCxProjectName;
         
        asObjDetail.append("'Name' [%-*s], " % (cWidthName, sCxProjectName));

        return ''.join(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

