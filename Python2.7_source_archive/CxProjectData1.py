
import os;
import traceback;
import re;
import string;
import sys;
import collections;

import CxProjectScan1;

class CxProjectData:

    sClassMod      = __name__;
    sClassId       = "CxProjectData";
    sClassVers     = "(v1.0501)";
    sClassDisp     = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag     = False;

    # --------------------------------------------------------------------------------------------------
    # Item #(14): 
    #   Item #(14.1): 'name' <type 'unicode'> [TestCLI3]...
    #   Item #(14.2): 'links' <type 'list'> 
    #                     [[{u'uri': u'/projects/390094', u'rel': u'self'},
    #                       {u'uri': u'/auth/teams/', u'rel': u'teams'}, 
    #                       {u'uri': u'/sast/scans?projectId=390094&last=1', u'rel': u'latestscan'},
    #                       {u'uri': u'/sast/scans?projectId=390094', u'rel': u'allscans'}, 
    #                       {u'uri': u'/sast/scanSettings/390094', u'rel': u'scansettings'}, 
    #                       {u'type': u'local', u'uri': None, u'rel': u'source'}]]...
    #   Item #(14.3): 'isPublic' <type 'bool'> [True]...
    #   Item #(14.4): 'teamId' <type 'unicode'> [22222222-2222-448d-b029-989c9070eb23]...
    #   Item #(14.5): 'customFields' <type 'list'> [[]]...
    #   Item #(14.6): 'id' <type 'int'> [390094]...
    # --------------------------------------------------------------------------------------------------

    sCxProjectName          = None;
    sCxProjectId            = "-undefined-";
    iCxProjectId            = 0;
    bCxProjectIsPublic      = False;
    sCxProjectTeamId        = None;
    asCxProjectLinks        = [];
    asCxProjectCustomFields = [];

    dictCxProjectScans      = None;

    def __init__(self, trace=False, cxprojectname=None, cxprojectid=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setCxProjectName(cxprojectname=cxprojectname);
            self.setCxProjectId(cxprojectid=cxprojectid);

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

        if self.sCxProjectName == None or \
           len(self.sCxProjectName) < 1:
         
            self.sCxProjectName = None;
         
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
                self.iCxProjectId = -1;

            else:

                self.iCxProjectId = int(self.sCxProjectId);

        else:

            self.iCxProjectId = cxprojectid;

            if self.iCxProjectId < 0:

                self.sCxProjectId = "";
                self.iCxProjectId = -1;

            else:

                self.sCxProjectId = ("%d" % self.iCxProjectId);

    def getCxProjectIsPublic(self):

        return self.bCxProjectIsPublic;

    def setCxProjectIsPublic(self, cxprojectispublic=False):

        self.bCxProjectIsPublic = cxprojectispublic;

    def getCxProjectTeamId(self):

        return self.sCxProjectTeamId;

    def setCxProjectTeamId(self, cxprojectteamid=None):

        self.sCxProjectTeamId = cxprojectteamid;

        if self.sCxProjectTeamId == None or \
           len(self.sCxProjectTeamId) < 1:
         
            self.sCxProjectTeamId = None;
         
    def getCxProjectLinks(self):

        return self.asCxProjectLinks;

    def setCxProjectLinks(self, cxprojectlinks=None):

        self.asCxProjectLinks = cxprojectlinks;

    def getCxProjectCustomFields(self):

        return self.asCxProjectCustomFields;

    def setCxProjectCustomFields(self, cxprojectcustomfields=None):

        self.asCxProjectCustomFields = cxprojectcustomfields;

    def getCxProjectScans(self):

        return self.dictCxProjectScans;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);
            print "%s The contents of 'sCxProjectName' is [%s]..." % (self.sClassDisp, self.sCxProjectName);
            print "%s The contents of 'sCxProjectId' is [%s]..." % (self.sClassDisp, self.sCxProjectId);
            print "%s The contents of 'iCxProjectId' is (%d)..." % (self.sClassDisp, self.iCxProjectId);
            print "%s The contents of 'bCxProjectIsPublic' is [%s]..." % (self.sClassDisp, self.bCxProjectIsPublic);
            print "%s The contents of 'sCxProjectTeamId' is [%s]..." % (self.sClassDisp, self.sCxProjectTeamId);
            print "%s The contents of 'asCxProjectLinks' is [%s]..." % (self.sClassDisp, self.asCxProjectLinks);
            print "%s The contents of 'asCxProjectCustomFields' is [%s]..." % (self.sClassDisp, self.asCxProjectCustomFields);
            print "%s The contents of 'dictCxProjectScans' is [%s]..." % (self.sClassDisp, self.dictCxProjectScans);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'sCxProjectName' is [%s], " % (self.sCxProjectName));
        asObjDetail.append("'sCxProjectId' is [%s], " % (self.sCxProjectId));
        asObjDetail.append("'iCxProjectId' is (%d), " % (self.iCxProjectId));
        asObjDetail.append("'bCxProjectIsPublic' is [%s], " % (self.bCxProjectIsPublic));
        asObjDetail.append("'sCxProjectTeamId' is [%s], " % (self.sCxProjectTeamId));
        asObjDetail.append("'asCxProjectLinks' is [%s], " % (self.asCxProjectLinks));
        asObjDetail.append("'asCxProjectCustomFields' is [%s], " % (self.asCxProjectCustomFields));
        asObjDetail.append("'dictCxProjectScans' is [%s]. " % (self.dictCxProjectScans));

        return ''.join(asObjDetail);

    def toPrettyString(self):

        return self.toPrettyStringWithWidths();

    def toPrettyStringWithWidths(self, cWidthId=6, cWidthLinks=3, cWidthCustFields=3, cWidthScans=3, cWidthTeamId=36, cWidthName=70):

        asObjDetail = list();

        asObjDetail.append("'Id' [%*s], " % (cWidthId, self.sCxProjectId));
        asObjDetail.append("'Public?' [%5s], " % (self.bCxProjectIsPublic));
        asObjDetail.append("'# Link(s)' (%*d), " % (cWidthLinks, len(self.asCxProjectLinks)));
        asObjDetail.append("'# C.Field(s)' (%*d), " % (cWidthCustFields, len(self.asCxProjectCustomFields)));
        asObjDetail.append("'# Scan(s)' (%*d), " % (cWidthScans, len(self.dictCxProjectScans)));
        asObjDetail.append("'TeamId' [%*s], " % (cWidthTeamId, self.sCxProjectTeamId));

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

    def addCxProjectScanToCxProjectData(self, cxprojectscan=None):

    #   self.bTraceFlag = True;

        cxProjectScan = cxprojectscan;

        if cxProjectScan == None:

            print "";
            print "%s NO CxProjectScan object has been specified nor defined - a CxProjectScan object MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.dictCxProjectScans == None:

            if self.bTraceFlag == True:

                print "%s The object 'dictCxProjectScans' has NOT been set - creating an internal instance..." % (self.sClassDisp);

            self.dictCxProjectScans = collections.defaultdict(); 

        bProcessingError = False;

        try:

            sCxProjectScanId = cxProjectScan.getCxScanId();

            if sCxProjectScanId != None:

                sCxProjectScanId = sCxProjectScanId.strip();

            if sCxProjectScanId == None or \
                len(sCxProjectScanId) < 1:

                print "";
                print "%s The CxProjectScan has an 'id' that is None or 'empty' - bypassing the addition of this object - Error!" % (self.sClassDisp);
                print "";

                return False;

            self.dictCxProjectScans[sCxProjectScanId] = cxProjectScan;

            if self.bTraceFlag == True:

                print "%s CxProjectScan with 'id' of [%s] added to the CxProjectData..." % (self.sClassDisp, sCxProjectScanId);

        except Exception, inst:

            print "%s 'addCxProjectScanToCxProjectData()' - exception occured..." % (self.sClassDisp);
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

