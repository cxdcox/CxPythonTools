
import os;
import traceback;
import re;
import string;
import sys;
import collections;
import zope.interface;

import CxProjectCreation1;

from CxProjectCreationCollectionInterfaceDefaults1 import CxProjectCreationCollectionInterfaceDefaults;

class CxProjectCreationCollectionVerizonDefaults(interface.implements(CxProjectCreationCollectionInterfaceDefaults)):

    sClassMod  = __name__;
    sClassId   = "CxProjectCreationCollectionVerizonDefaults";
    sClassVers = "(v1.0202)";
    sClassDisp = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag = False;

    # -------------------------------------------------------------------
    #
    # The following section contains the fields that may be customized
    # to support the CxProject 'creation' collection:
    #
    #   1) 'default' Project TeamName
    #   2) 'default' Project PresetName
    #   3) 'default' Project Mobile PresetName
    #
    # -------------------------------------------------------------------

    # Project 'default' field(s):

    sDefaultCxProjectTeamName         = "\\CxServer\\SP\\Verizon";
    sDefaultCxProjectPresetName       = "VERIZON";
    sDefaultCxProjectMobilePresetName = "VERIZON_MOBILE";

    def __init__(self, trace=False):

        try:

            self.setTraceFlag(trace=trace);

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

    def getDefaultCxProjectTeamName(self):

        return self.sDefaultCxProjectTeamName;

    def getDefaultCxProjectPresetName(self):

        return self.sDefaultCxProjectPresetName;

    def getDefaultCxProjectMobilePresetName(self):

        return self.sDefaultCxProjectMobilePresetName;

    def resetCxProjectCreationCollectionDefaultsDefaults(self):

        self.sDefaultCxProjectTeamName         = "\\CxServer\\SP\\Verizon";
        self.sDefaultCxProjectPresetName       = "VERIZON";
        self.sDefaultCxProjectMobilePresetName = "VERIZON_MOBILE";

        return;

    # Project 'overrides' for various field(s):

    # --------------------------------------------------------------------------------------------------
    # dictProjectCreationProperties = ["project.name",
    #                                  "project.team",
    #                                  "project.version",
    #                                  "project.tier",
    #                                  "project.visibility",
    #                                  "project.language.list",
    #                                  "project.cx.branches",
    #                                  "project.cx.teamname"
    #                                  "project.cx.presetname"
    #                                  "vast.id"];
    # --------------------------------------------------------------------------------------------------

    def getCxProjectBaseName(self, cxprojectcreation=None, dictprojectcreationproperties=None):

        if cxprojectcreation == None:

            return None;

        cxProjectCreation = cxprojectcreation;

        if dictprojectcreationproperties == None:

            return None;

        dictProjectCreationProperties = dictprojectcreationproperties;

        sGeneratedProjectName = "";
        sFieldProjectVastId   = dictProjectCreationProperties["vast.id"];
        
        if sFieldProjectVastId != None:
        
            sFieldProjectVastId = sFieldProjectVastId.strip();
        
        if sFieldProjectVastId != None and \
            len(sFieldProjectVastId) > 0:
        
            sGeneratedProjectName = sFieldProjectVastId;

        sFieldProjectName = dictProjectCreationProperties["project.name"];
        
        if sFieldProjectName != None:
        
            sFieldProjectName = sFieldProjectName.strip();
        
        if sFieldProjectName != None and \
            len(sFieldProjectName) > 0:
        
            sFieldProjectName = sFieldProjectName.replace(' ', '-');

            if sGeneratedProjectName != None:
        
                sGeneratedProjectName = sGeneratedProjectName.strip();
        
            if sGeneratedProjectName == None or \
                len(sGeneratedProjectName) < 1:
        
                sGeneratedProjectName = sFieldProjectName;
        
            else:
        
                sGeneratedProjectName = "%s-%s" % (sGeneratedProjectName, sFieldProjectName);

        return sGeneratedProjectName;

    def getCxProjectName(self, cxprojectcreation=None, dictprojectcreationproperties=None):

        if cxprojectcreation == None:

            return None;

        cxProjectCreation = cxprojectcreation;

        if dictprojectcreationproperties == None:

            return None;

        dictProjectCreationProperties = dictprojectcreationproperties;

        sGeneratedProjectName = "%s_Main" % (cxProjectCreation.getCxProjectBaseName());

        return sGeneratedProjectName;

    def getExtraCxProjectBranchNames(self, cxprojectcreation=None, dictprojectcreationproperties=None):

        if cxprojectcreation == None:

            return None;

        cxProjectCreation = cxprojectcreation;

        if dictprojectcreationproperties == None:

            return None;

        dictProjectCreationProperties = dictprojectcreationproperties;

        sFieldProjectTeam = cxProjectCreation.getCxProjectTeam();
        
        if sFieldProjectTeam != None:
        
            sFieldProjectTeam = sFieldProjectTeam.strip();
        
        if sFieldProjectTeam != None and \
            len(sFieldProjectTeam) > 0:

            return sFieldProjectTeam;

        return None;

    def getCxProjectTeamName(self, cxprojectcreation=None, dictprojectcreationproperties=None):

        if cxprojectcreation == None:

            return None;

        cxProjectCreation = cxprojectcreation;

        if dictprojectcreationproperties == None:

            return None;

        dictProjectCreationProperties = dictprojectcreationproperties;

        sGeneratedProjectTeamName = "";
        sFieldProjectName         = dictProjectCreationProperties["project.name"];
        
        if sFieldProjectName != None:
        
            sFieldProjectName = sFieldProjectName.strip();
        
        if sFieldProjectName != None and \
            len(sFieldProjectName) > 0:
        
            sFieldProjectName  = sFieldProjectName.replace(' ', '-');
            sCxProjectTeamName = cxProjectCreation.getCxProjectTeamName();
        
            if sCxProjectTeamName != None:
        
                sCxProjectTeamName = sCxProjectTeamName.strip();
        
            if sCxProjectTeamName != None and \
                len(sCxProjectTeamName) > 0:
        
                if sCxProjectTeamName.endswith(sFieldProjectName) == False:
        
                    sGeneratedProjectTeamName = ("%s\\%s" % (sCxProjectTeamName, sFieldProjectName));
        
            else:
        
                sGeneratedProjectTeamName = ("%s\\%s" % (self.sDefaultCxProjectTeamName, sFieldProjectName));

            return sGeneratedProjectTeamName;

        return self.sDefaultCxProjectTeamName;

    def getCxProjectBranchedName(self, cxprojectcreation=None, cxprojectbranchname=None):

        if cxprojectcreation == None:

            return None;

        cxProjectCreation = cxprojectcreation;

        sCxProjectBaseName = cxProjectCreation.getCxProjectBaseName();

        if sCxProjectBaseName != None:

            sCxProjectBaseName = sCxProjectBaseName.strip();

        if sCxProjectBaseName == None or \
            len(sCxProjectBaseName) < 1:

            return None;

        if cxprojectbranchname == None:

            return None;

        sCxProjectBranchName = cxprojectbranchname;

        if sCxProjectBranchName != None:

            sCxProjectBranchName = sCxProjectBranchName.strip();

        if sCxProjectBranchName == None or \
            len(sCxProjectBranchName) < 1:

            return None;

        sGeneratedProjectBranchedName = "%s_BR_%s" % (sCxProjectBaseName, sCxProjectBranchName); 

        return sGeneratedProjectBranchedName;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print("%s Dump of the variable(s) content of this class:" % (self.sClassDisp));
            print("%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag));
            print("%s The contents of 'sDefaultCxProjectTeamName' is [%s]..." % (self.sClassDisp, self.getDefaultCxProjectTeamName()));
            print("%s The contents of 'sDefaultCxProjectPresetName' is [%s]..." % (self.sClassDisp, self.getDefaultCxProjectPresetName()));
            print("%s The contents of 'sDefaultCxProjectMobilePresetName' is [%s]..." % (self.sClassDisp, self.getDefaultCxProjectMobilePresetName()));

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'sDefaultCxProjectTeamName' is [%s], " % (self.getDefaultCxProjectTeamName()));
        asObjDetail.append("'sDefaultCxProjectPresetName' is [%s], " % (self.getDefaultCxProjectPresetName()));
        asObjDetail.append("'sDefaultCxProjectMobilePresetName' is [%s]. " % (self.getDefaultCxProjectMobilePresetName()));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

bMainVerbose = True;

def main():

    try:

        if bMainVerbose == True:

            cxProjectCreationCollectionDefaults = CxProjectCreationCollectionVerizonDefaults(trace=bMainVerbose);

            cxProjectCreationCollectionDefaults.dump_fields();

            print("");

            dictProjectCreationProperties = collections.defaultdict(); 

            dictProjectCreationProperties["project.name"]          = "Black Duck";
            dictProjectCreationProperties["project.team"]          = "ACSS";
            dictProjectCreationProperties["project.version"]       = "2019-10-31";
            dictProjectCreationProperties["project.tier"]          = "prod";
            dictProjectCreationProperties["project.visibility"]    = "public";
            dictProjectCreationProperties["project.language.list"] = "java,c,scala";
        #   dictProjectCreationProperties["project.cx.branches"]   = "Branch1,Branch2,Branch3,Branch4";
        #   dictProjectCreationProperties["project.cx.teamname"]   = "\CxServer\SP\Company\Users";
        #   dictProjectCreationProperties["project.cx.presetname"] = "Checkmarx Default";
            dictProjectCreationProperties["vast.id"]               = "24436";

            cxProjectCreation1 = CxProjectCreation1.CxProjectCreation(trace=bMainVerbose, cxprojectispublic=True, cxprojectteamname=cxProjectCreationCollectionDefaults.getDefaultCxProjectTeamName(), cxprojectpresetname=cxProjectCreationCollectionDefaults.getDefaultCxProjectPresetName(), cxprojectengineconfigname="Default Configuration");

            cxProjectCreation1.setCxProjectTeam(cxprojectteam=dictProjectCreationProperties["project.team"]); 
            cxProjectCreation1.setCxProjectVersion(cxprojectversion=dictProjectCreationProperties["project.version"]); 
        #   cxProjectCreation1.setCxProjectTeamName(cxprojectteamname=dictProjectCreationProperties["project.cx.teamname"]); 
        #   cxProjectCreation1.setCxProjectPresetName(cxprojectpresetname=dictProjectCreationProperties["project.cx.presetname"]); 

            cxProjectCreation1.setCxProjectBaseName(cxprojectbasename=cxProjectCreationCollectionDefaults.getCxProjectBaseName(cxprojectcreation=cxProjectCreation1, dictprojectcreationproperties=dictProjectCreationProperties));
            cxProjectCreation1.setCxProjectName(cxprojectname=cxProjectCreationCollectionDefaults.getCxProjectName(cxprojectcreation=cxProjectCreation1, dictprojectcreationproperties=dictProjectCreationProperties)); 
            cxProjectCreation1.setCxProjectBranchNames(cxprojectbranchnames=cxProjectCreationCollectionDefaults.getExtraCxProjectBranchNames(cxprojectcreation=cxProjectCreation1, dictprojectcreationproperties=dictProjectCreationProperties));  
            cxProjectCreation1.setCxProjectTeamName(cxprojectteamname=cxProjectCreationCollectionDefaults.getCxProjectTeamName(cxprojectcreation=cxProjectCreation1, dictprojectcreationproperties=dictProjectCreationProperties));  

            print("");
            print("Generated 'CxProjectBaseName'    is [%s]..." % (cxProjectCreation1.getCxProjectBaseName()));
            print("Generated 'CxProjectName'        is [%s]..." % (cxProjectCreation1.getCxProjectName()));
            print("Generated 'CxProjectBranchNames' is [%s]..." % (cxProjectCreation1.getCxProjectBranchNames()));
            print("Generated 'CxProjectTeamName'    is [%s]..." % (cxProjectCreation1.getCxProjectTeamName()));
            print("");
            print("'dictProjectCreationProperties'  is [%s]..." % (dictProjectCreationProperties));
            print("'cxProjectCreation1'             is [%s]..." % (cxProjectCreation1.toString()));
            print("");

            asCxProjectBranchNames = cxProjectCreation1.getCxProjectBranchNames();
            cCxProjectBranchedName = 0;

            if asCxProjectBranchNames != None and \
               len(asCxProjectBranchNames) > 0:

                for sCxProjectBranchName in asCxProjectBranchNames:

                    if sCxProjectBranchName != None:

                        sCxProjectBranchName = sCxProjectBranchName.strip();

                    if sCxProjectBranchName == None or \
                        len(sCxProjectBranchName) < 1:

                        continue;

                    cCxProjectBranchedName += 1;

                    sCxProjectBranchedName = cxProjectCreationCollectionDefaults.getCxProjectBranchedName(cxprojectcreation=cxProjectCreation1, cxprojectbranchname=sCxProjectBranchName);

                    print("#(%d) of (%d): 'sCxProjectBranchName' is [%s] and 'sCxProjectBranchedName' is [%s]..." % (cCxProjectBranchedName, len(asCxProjectBranchNames), sCxProjectBranchName, sCxProjectBranchedName));

            print("");

    except Exception as inst:

        print("%s 'main()' - exception occured..." % (CxProjectCreationCollectionVerizonDefaults.sClassDisp));
        print(type(inst));
        print(inst);

        excType, excValue, excTraceback = sys.exc_info();
        asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

        print("- - - ");
        print('\n'.join(asTracebackLines));
        print("- - - ");

        return False;

    return True;

if __name__ == '__main__':

    bCmdExecOk = main();

    if bCmdExecOk == False:

        print("%s Exiting with a Return Code of (31)..." % (CxProjectCreationCollectionVerizonDefaults.sClassDisp));

        sys.exit(31);

    print("%s Exiting with a Return Code of (0)..." % (CxProjectCreationCollectionVerizonDefaults.sClassDisp));

    sys.exit(0);

