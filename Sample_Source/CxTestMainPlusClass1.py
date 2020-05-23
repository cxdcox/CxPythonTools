
import os;
import traceback;
import re;
import string;
import sys;

class CxTestClass:

    sClassMod  = __name__;
    sClassId   = "CxTestClass";
    sClassVers = "(v1.0103)";
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

    sDefaultCxProjectTeamName         = "\\CxServer\\SP\\Company\\Users";
    sDefaultCxProjectPresetName       = "Checkmarx Default";
    sDefaultCxProjectMobilePresetName = "Mobile";

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

    def resetCxTestClassDefaults(self):

        self.sDefaultCxProjectTeamName         = "\\CxServer\\SP\\Company\\Users";
        self.sDefaultCxProjectPresetName       = "Checkmarx Default";
        self.sDefaultCxProjectMobilePresetName = "Mobile";

        return;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print("%s Dump of the variable(s) content of this class:" % (self.sClassDisp));
            print("%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag));
            print("%s The contents of 'sDefaultCxProjectTeamName' is [%s]..." % (self.sClassDisp, self.sDefaultCxProjectTeamName));
            print("%s The contents of 'sDefaultCxProjectPresetName' is [%s]..." % (self.sClassDisp, self.sDefaultCxProjectPresetName));
            print("%s The contents of 'sDefaultCxProjectMobilePresetName' is [%s]..." % (self.sClassDisp, self.sDefaultCxProjectMobilePresetName));

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'sDefaultCxProjectTeamName' is [%s], " % (self.sDefaultCxProjectTeamName));
        asObjDetail.append("'sDefaultCxProjectPresetName' is [%s], " % (self.sDefaultCxProjectPresetName));
        asObjDetail.append("'sDefaultCxProjectMobilePresetName' is [%s]. " % (self.sDefaultCxProjectMobilePresetName));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

bMainVerbose = True;

def main():

    try:

        if bMainVerbose == True:

            cxTestClass = CxTestClass(trace=bMainVerbose);

            cxTestClass.dump_fields();

            print("");

    except Exception as inst:

        print("%s 'main()' - exception occured..." % (CxTestClass.sClassDisp));
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

        print("%s Exiting with a Return Code of (31)..." % (CxTestClass.sClassDisp));

        sys.exit(31);

    print("%s Exiting with a Return Code of (0)..." % (CxTestClass.sClassDisp));

    sys.exit(0);

