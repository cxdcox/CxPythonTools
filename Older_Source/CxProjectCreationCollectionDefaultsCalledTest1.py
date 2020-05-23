
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;

from datetime import datetime;

import CxProjectCreation1;

class CxProjectCreationCollectionDefaultsCalledTest:

    sClassMod                           = __name__;
    sClassId                            = "CxProjectCreationCollectionDefaultsCalledTest";
    sClassVers                          = "(v1.0103)";
    sClassDisp                          = sClassMod+"."+sClassId+" "+sClassVers+": ";

    # Project 'instance' field(s):

    bTraceFlag                          = False;

    cxProjectCreationCollectionDefaults = None;

    def __init__(self, trace=False, cxprojectcreationcollectiondefaults=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setCxProjectCreationCollectionDefaults(cxprojectcreationcollectiondefaults=cxprojectcreationcollectiondefaults);

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

    def getCxProjectCreationCollectionDefaults(self):

        return self.cxProjectCreationCollectionDefaults;

    def setCxProjectCreationCollectionDefaults(self, cxprojectcreationcollectiondefaults=None):

        self.cxProjectCreationCollectionDefaults = cxprojectcreationcollectiondefaults;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print("%s Dump of the variable(s) content of this class:" % (self.sClassDisp));
            print("%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag));
            print("%s The contents of 'cxProjectCreationCollectionDefaults' is [%s]..." % (self.sClassDisp, self.cxProjectCreationCollectionDefaults));

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'cxProjectCreationCollectionDefaults' is [%s]. " % (self.cxProjectCreationCollectionDefaults));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def dumpCxProjectCreationCollectionDefaultsFromSuppliedObject(self):
 
    #   self.bTraceFlag = True;
 
        if self.cxProjectCreationCollectionDefaults == None:
 
            print("");
            print("%s NO CxProjectCreationCollectionDefaults object has been specified nor defined for this Checkmarx CxProject(s) Collection - one MUST be defined - Error!" % (self.sClassDisp));
            print("");
 
            return False;
 
        bProcessingError = False;
 
        try:

            print("");
            print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =");
            print("");
            print("%s cxProjectCreationCollectionDefaults.getTraceFlag() returned [%s]..." % (self.sClassDisp, self.cxProjectCreationCollectionDefaults.getTraceFlag()));
            print("%s cxProjectCreationCollectionDefaults.getDefaultCxProjectTeamName() returned [%s]..." % (self.sClassDisp, self.cxProjectCreationCollectionDefaults.getDefaultCxProjectTeamName()));
            print("%s cxProjectCreationCollectionDefaults.getDefaultCxProjectPresetName() returned [%s]..." % (self.sClassDisp, self.cxProjectCreationCollectionDefaults.getDefaultCxProjectPresetName()));
            print("%s cxProjectCreationCollectionDefaults.getDefaultCxProjectMobilePresetName() returned [%s]..." % (self.sClassDisp, self.cxProjectCreationCollectionDefaults.getDefaultCxProjectMobilePresetName()));
            print("");
            print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -");
            print("");
        #   print("%s cxProjectCreationCollectionDefaults.() returned [%s]..." % (self.sClassDisp, self.cxProjectCreationCollectionDefaults.()));
        #   print("");
            print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =");
            print("");
 
        except Exception as inst:
 
            print("%s 'dumpCxProjectCreationCollectionDefaultsFromSuppliedObject()' - exception occured..." % (self.sClassDisp));
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

