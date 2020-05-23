
import sys;
import traceback;

sStatsId      = "CxProjectCreationCollectionDefaults1.py";
sStatsVers    = "(v1.0501)";
sStatsDisp    = sStatsId+" "+sStatsVers+":"

bStatsVerbose = True;

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

#sDefaultCxProjectTeamName            = "\\CxServer\\SP\\Company\\Users";
#sDefaultCxProjectPresetName          = "Checkmarx Default";
#sDefaultCxProjectMobilePresetName    = "Mobile";
sDefaultCxProjectTeamName            = "\\CxServer\\SP\\Verizon";
sDefaultCxProjectPresetName          = "VERIZON";
sDefaultCxProjectMobilePresetName    = "VERIZON_MOBILE";

def main():

    try:

        if bStatsVerbose == True:

            print("%s 'creation' Collection VERBOSE flag is [%s]..." % (sStatsDisp, bStatsVerbose));
            print("");
            print("%s 'default' CxProject 'TeamName' is [%s]..." % (sStatsDisp, sDefaultCxProjectTeamName));
            print("%s 'default' CxProject 'PresetName' is [%s]..." % (sStatsDisp, sDefaultCxProjectPresetName));
            print("%s 'default' CxProject MOBILE 'PresetName' is [%s]..." % (sStatsDisp, sDefaultCxProjectMobilePresetName));
            print("");

    except Exception as inst:

        print("%s 'main()' - exception occured..." % (sStatsDisp));
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

        print("%s Exiting with a Return Code of (31)..." % (sStatsDisp));

        sys.exit(31);

    print("%s Exiting with a Return Code of (0)..." % (sStatsDisp));

    sys.exit(0);

