
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;
import requests;
import json;

from datetime import datetime;

import CxProjectCreation1;
import CxProjectData1;
import CxServerEndpoint1;
import CxRestAPIStatistics1;
import CxRestAPITokenAuthenticationBase1;

class CxRestAPIProjectCreationBase:

    sClassMod                   = __name__;
    sClassId                    = "CxRestAPIProjectCreationBase";
    sClassVers                  = "(v1.0501)";
    sClassDisp                  = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag                  = False;
    cxServerEndpoint            = None;
    cxProjectCreationCollection = None;

    # Constructed objects:

    cxRestAPITokenAuth          = None;

    def __init__(self, trace=False, cxserverendpoint=None, cxprojectcreationcollection=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setCxServerEndpoint(cxserverendpoint=cxserverendpoint);
            self.setCxProjectCreationCollection(cxprojectcreationcollection=cxprojectcreationcollection);

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

        return self.cxProjectCreationCollection;

    def setCxProjectCreationCollection(self, cxprojectcreationcollection=None):

        self.cxProjectCreationCollection = cxprojectcreationcollection;

    def resetCxRestAPIProjectCreationBase(self):

        return;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);
            print "%s The contents of 'cxServerEndpoint' is [%s]..." % (self.sClassDisp, self.cxServerEndpoint);
            print "%s The contents of 'cxProjectCreationCollection' is [%s]..." % (self.sClassDisp, self.cxProjectCreationCollection);
            print "%s The contents of 'cxRestAPITokenAuth' is [%s]..." % (self.sClassDisp, self.cxRestAPITokenAuth);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'cxServerEndpoint' is [%s], " % (self.cxServerEndpoint));
        asObjDetail.append("'cxProjectCreationCollection' is [%s], " % (self.cxProjectCreationCollection));
        asObjDetail.append("'cxRestAPITokenAuth' is [%s]. " % (self.cxRestAPITokenAuth));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def getCxRestAPIProjectCreationMetaData(self):

        if self.cxServerEndpoint == None:

            print "";
            print "%s NO CxServerEndpoint has been specified nor defined - a CxServerEndpoint MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.cxServerEndpoint.getCxServerEndpointActiveFlag() == False:

            print "";
            print "%s The supplied CxServerEndpoint is NOT marked 'active' - it MUST be marked 'active' to be used - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.cxProjectCreationCollection == None:

            print "";
            print "%s NO CxProjectCreationCollection has been specified nor defined - a CxProjectCreationCollection MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        try:

            bGetCxAuthTokenOk = self.getCxRestAPIAuthToken();

            if bGetCxAuthTokenOk == False:

                print "";
                print "%s Invocation of 'getCxRestAPIAuthToken()' failed - Error!" % (self.sClassDisp);
                print "";

                return False;

            bGetCxAllTeams = self.getCxRestAPIAllTeams();
         
            if bGetCxAllTeams == False:
         
                print "";
                print "%s Invocation of 'getCxRestAPIAllTeams()' failed - Error!" % (self.sClassDisp);
                print "";
         
                return False;

            if self.bTraceFlag == True:

                print "";
                print "%s CxProjectCreationCollection (after 1st 'meta' data) is:" % (self.sClassDisp);
                print self.cxProjectCreationCollection.toString();
                print "";
         
            bGetCxAllPresets = self.getCxRestAPIAllPresets();

            if bGetCxAllPresets == False:

                print "";
                print "%s Invocation of 'getCxRestAPIAllPresets()' failed - Error!" % (self.sClassDisp);
                print "";

                return False;

            if self.bTraceFlag == True:

                print "";
                print "%s CxProjectCreationCollection (after 2nd 'meta' data) is:" % (self.sClassDisp);
                print self.cxProjectCreationCollection.toString();
                print "";

            bGetCxAllEngineConfigurations = self.getCxRestAPIAllEngineConfigurations();

            if bGetCxAllEngineConfigurations == False:

                print "";
                print "%s Invocation of 'getCxRestAPIAllEngineConfigurations()' failed - Error!" % (self.sClassDisp);
                print "";

                return False;

            if self.bTraceFlag == True:

                print "";
                print "%s CxProjectCreationCollection (after 3rd 'meta' data) is:" % (self.sClassDisp);
                print self.cxProjectCreationCollection.toString();
                print "";

            bGetCxAllProjectDataOk = self.getCxRestAPIAllProjectData();

            if bGetCxAllProjectDataOk == False:

                print "";
                print "%s Invocation of 'getCxRestAPIAllProjectData()' failed - Error!" % (self.sClassDisp);
                print "";

                return False;

        except Exception, inst:

            print "%s 'getCxRestAPIProjectCreationMetaData()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

    def getCxRestAPIAuthToken(self):

        if self.cxServerEndpoint == None:

            print "";
            print "%s NO CxServerEndpoint has been specified nor defined - a CxServerEndpoint MUST be defined - Error!" % (self.sClassDisp);
            print "";

            return False;

        if self.cxServerEndpoint.getCxServerEndpointActiveFlag() == False:

            print "";
            print "%s The supplied CxServerEndpoint is NOT marked 'active' - it MUST be marked 'active' to be used - Error!" % (self.sClassDisp);
            print "";

            return False;

        try:

            self.cxRestAPITokenAuth = CxRestAPITokenAuthenticationBase1.CxRestAPITokenAuthenticationBase(trace=self.bTraceFlag, cxserverendpoint=self.cxServerEndpoint);

            bGetCxRestAPIAuthTokenOk = self.cxRestAPITokenAuth.getCxRestAPITokenAuthentication();

            if bGetCxRestAPIAuthTokenOk == False:

                print "";
                print "%s Invocation of 'cxRestAPITokenAuth.getCxRestAPITokenAuthentication()' failed - Error!" % (self.sClassDisp);
                print "";

                return False;

        except Exception, inst:

            print "%s 'getCxRestAPIAuthToken()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

    def getCxRestAPIAllTeams(self):

        try:

            CxRestAPIStatistics1.cRestAPICallsMade += 1;

            cxRequestURL = "%s/cxrestapi/auth/teams" % (self.cxServerEndpoint.getCxServerURL());
            cxReqPayload = "";
            cxReqHeaders = {
                'Content-Type':  "application/json;v=1.0",
                'Authorization': ("%s %s" % (self.cxServerEndpoint.getCxTokenType(), self.cxServerEndpoint.getCxAccessToken())),
                'cache-control': "no-cache"
                };

            if self.bTraceFlag == True:

                print "%s Issuing Request #(%d) of URL [%s] with a Payload of [%s] and Header(s) of [%s]..." % (self.sClassDisp, CxRestAPIStatistics1.cRestAPICallsMade, cxRequestURL, cxReqPayload, cxReqHeaders);

            cxReqResponse   = requests.request("GET", cxRequestURL, data=cxReqPayload, headers=cxReqHeaders);
            sReqResponseRaw = json.dumps(cxReqResponse.json(), indent=4);
             
            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON Response {ALL EngineConfiguration(s)} ===============");
                print(type(sReqResponseRaw));

                print("");
                print("=============== DIR JSON Response {ALL EngineConfiguration(s)} ===============");
                print(dir(sReqResponseRaw));

                print("");
                print("=============== JSON 'string' Response {ALL EngineConfiguration(s)} ===============");
                print(sReqResponseRaw);

            listCxReqResponseJson = json.loads(sReqResponseRaw);

            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON 'list' Response {ALL EngineConfiguration(s)} ===============");
                print(type(listCxReqResponseJson));

                print("");
                print("=============== DIR JSON 'list' Response {ALL EngineConfiguration(s)} ===============");
                print(dir(listCxReqResponseJson));

                print("");
                print("=============== JSON 'list' Response {ALL EngineConfiguration(s)} [RAW print] ===============");
                print(listCxReqResponseJson);

                print("");
                print("=============== JSON 'list' Response {ALL EngineConfiguration(s)} Enumerated ===============");

            cListJsonItem = 0;

            for listCxReqResponseJsonItem in listCxReqResponseJson:

                if listCxReqResponseJsonItem == None:

                    continue;

                cListJsonItem += 1;

                if self.bTraceFlag == True:

                    print("  Item #(%d): <raw> {%s} [%s]..." % (cListJsonItem, type(listCxReqResponseJsonItem), listCxReqResponseJsonItem));

                dictCxReqResponseJson = listCxReqResponseJsonItem;

                cDictJsonItem   = 0;
                sCxTeamFullName = "";
                sCxTeamId       = "";

                for dictCxReqResponseJsonKey in dictCxReqResponseJson.keys():

                    if dictCxReqResponseJsonKey == None:

                        continue;

                    cDictJsonItem += 1;

                    dictCxReqResponseJsonItem = dictCxReqResponseJson[dictCxReqResponseJsonKey];

                    if self.bTraceFlag == True:

                        print("    Item #(%d.%d): '%s' %s [%s]..." % (cListJsonItem, cDictJsonItem, dictCxReqResponseJsonKey, type(dictCxReqResponseJsonItem), dictCxReqResponseJsonItem));

                    # --------------------------------------------------------------------------------------------------
                    # Item #(1): <raw> {<type 'dict'>} [{u'fullName': u'\\CxServer', u'id': u'00000000-1111-1111-b111-989c9070eb11'}]...
                    #   Item #(1.1): 'fullName' <type 'unicode'> [\CxServer]...
                    #   Item #(1.2): 'id' <type 'unicode'> [00000000-1111-1111-b111-989c9070eb11]...
                    # --------------------------------------------------------------------------------------------------

                    if dictCxReqResponseJsonKey == "fullName":

                        if type(dictCxReqResponseJsonItem) == unicode:

                            sCxTeamFullName = dictCxReqResponseJsonItem.encode('ascii', 'ignore');

                        else:

                            sCxTeamFullName = dictCxReqResponseJsonItem;

                    if dictCxReqResponseJsonKey == "id":

                        sCxTeamId = dictCxReqResponseJsonItem;

                self.cxProjectCreationCollection.addCxProjectMetaDataAllTeams(cxteamfullname=sCxTeamFullName, cxteamid=sCxTeamId);

        except Exception, inst:

            print "%s 'getCxRestAPIAllTeams()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

    def getCxRestAPIAllPresets(self):

        try:

            CxRestAPIStatistics1.cRestAPICallsMade += 1;

            cxRequestURL = "%s/cxrestapi/sast/presets" % (self.cxServerEndpoint.getCxServerURL());
            cxReqPayload = "";
            cxReqHeaders = {
                'Content-Type':  "application/json;v=1.0",
                'Authorization': ("%s %s" % (self.cxServerEndpoint.getCxTokenType(), self.cxServerEndpoint.getCxAccessToken())),
                'cache-control': "no-cache"
                };

            if self.bTraceFlag == True:

                print "%s Issuing Request #(%d) of URL [%s] with a Payload of [%s] and Header(s) of [%s]..." % (self.sClassDisp, CxRestAPIStatistics1.cRestAPICallsMade, cxRequestURL, cxReqPayload, cxReqHeaders);

            cxReqResponse   = requests.request("GET", cxRequestURL, data=cxReqPayload, headers=cxReqHeaders);
            sReqResponseRaw = json.dumps(cxReqResponse.json(), indent=4);
             
            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON Response {All Preset(s)} ===============");
                print(type(sReqResponseRaw));

                print("");
                print("=============== DIR JSON Response {All Preset(s)} ===============");
                print(dir(sReqResponseRaw));

                print("");
                print("=============== JSON 'string' Response {All Preset(s)} ===============");
                print(sReqResponseRaw);

            listCxReqResponseJson = json.loads(sReqResponseRaw);

            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON 'list' Response {All Preset(s)} ===============");
                print(type(listCxReqResponseJson));

                print("");
                print("=============== DIR JSON 'list' Response {All Preset(s)} ===============");
                print(dir(listCxReqResponseJson));

                print("");
                print("=============== JSON 'list' Response {All Preset(s)} [RAW print] ===============");
                print(listCxReqResponseJson);

                print("");
                print("=============== JSON 'list' Response {All Preset(s)} Enumerated ===============");

            cListJsonItem = 0;

            for listCxReqResponseJsonItem in listCxReqResponseJson:

                if listCxReqResponseJsonItem == None:

                    continue;

                cListJsonItem += 1;

                if self.bTraceFlag == True:

                    print("  Item #(%d): <raw> {%s} [%s]..." % (cListJsonItem, type(listCxReqResponseJsonItem), listCxReqResponseJsonItem));

                dictCxReqResponseJson = listCxReqResponseJsonItem;

                cDictJsonItem      = 0;
                sCxPresetName      = "";
                sCxPresetOwnerName = "";
                sCxPresetId        = "";

                for dictCxReqResponseJsonKey in dictCxReqResponseJson.keys():

                    if dictCxReqResponseJsonKey == None:

                        continue;

                    cDictJsonItem += 1;

                    dictCxReqResponseJsonItem = dictCxReqResponseJson[dictCxReqResponseJsonKey];

                    if self.bTraceFlag == True:

                        print("    Item #(%d.%d): '%s' %s [%s]..." % (cListJsonItem, cDictJsonItem, dictCxReqResponseJsonKey, type(dictCxReqResponseJsonItem), dictCxReqResponseJsonItem));

                    # --------------------------------------------------------------------------------------------------
                    # Item #(1): <raw> {<type 'dict'>} [{u'fullName': u'\\CxServer', u'id': u'00000000-1111-1111-b111-989c9070eb11'}]...
                    #   Item #(1.1): 'fullName' <type 'unicode'> [\CxServer]...
                    #   Item #(1.2): 'id' <type 'unicode'> [00000000-1111-1111-b111-989c9070eb11]...
                    # --------------------------------------------------------------------------------------------------

                    if dictCxReqResponseJsonKey == "name":

                        if type(dictCxReqResponseJsonItem) == unicode:

                            sCxPresetName = dictCxReqResponseJsonItem.encode('ascii', 'ignore');

                        else:

                            sCxPresetName = dictCxReqResponseJsonItem;

                    if dictCxReqResponseJsonKey == "ownerName":

                        if type(dictCxReqResponseJsonItem) == unicode:

                            sCxPresetOwnerName = dictCxReqResponseJsonItem.encode('ascii', 'ignore');

                        else:

                            sCxPresetOwnerName = dictCxReqResponseJsonItem;

                    if dictCxReqResponseJsonKey == "id":

                        sCxPresetId = "%d" % (dictCxReqResponseJsonItem);

                dictCxPreset = collections.defaultdict();

                dictCxPreset["name"]      = sCxPresetName;
                dictCxPreset["ownerName"] = sCxPresetOwnerName;
                dictCxPreset["id"]        = sCxPresetId;

                self.cxProjectCreationCollection.addCxProjectMetaDataAllPresets(cxpresetname=sCxPresetName, cxpresetdict=dictCxPreset);

        except Exception, inst:

            print "%s 'getCxRestAPIAllPresets()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

    def getCxRestAPIAllEngineConfigurations(self):

        try:

            CxRestAPIStatistics1.cRestAPICallsMade += 1;

            cxRequestURL = "%s/cxrestapi/sast/engineConfigurations" % (self.cxServerEndpoint.getCxServerURL());
            cxReqPayload = "";
            cxReqHeaders = {
                'Content-Type':  "application/json;v=1.0",
                'Authorization': ("%s %s" % (self.cxServerEndpoint.getCxTokenType(), self.cxServerEndpoint.getCxAccessToken())),
                'cache-control': "no-cache"
                };

            if self.bTraceFlag == True:

                print "%s Issuing Request #(%d) of URL [%s] with a Payload of [%s] and Header(s) of [%s]..." % (self.sClassDisp, CxRestAPIStatistics1.cRestAPICallsMade, cxRequestURL, cxReqPayload, cxReqHeaders);

            cxReqResponse   = requests.request("GET", cxRequestURL, data=cxReqPayload, headers=cxReqHeaders);
            sReqResponseRaw = json.dumps(cxReqResponse.json(), indent=4);
             
            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON Response {ALL EngineConfiguration(s)} ===============");
                print(type(sReqResponseRaw));

                print("");
                print("=============== DIR JSON Response {ALL EngineConfiguration(s)} ===============");
                print(dir(sReqResponseRaw));

                print("");
                print("=============== JSON 'string' Response {ALL EngineConfiguration(s)} ===============");
                print(sReqResponseRaw);

            listCxReqResponseJson = json.loads(sReqResponseRaw);

            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON 'list' Response {ALL EngineConfiguration(s)} ===============");
                print(type(listCxReqResponseJson));

                print("");
                print("=============== DIR JSON 'list' Response {ALL EngineConfiguration(s)} ===============");
                print(dir(listCxReqResponseJson));

                print("");
                print("=============== JSON 'list' Response {ALL EngineConfiguration(s)} [RAW print] ===============");
                print(listCxReqResponseJson);

                print("");
                print("=============== JSON 'list' Response {ALL EngineConfiguration(s)} Enumerated ===============");

            cListJsonItem = 0;

            for listCxReqResponseJsonItem in listCxReqResponseJson:

                if listCxReqResponseJsonItem == None:

                    continue;

                cListJsonItem += 1;

                if self.bTraceFlag == True:

                    print("  Item #(%d): <raw> {%s} [%s]..." % (cListJsonItem, type(listCxReqResponseJsonItem), listCxReqResponseJsonItem));

                dictCxReqResponseJson = listCxReqResponseJsonItem;

                cDictJsonItem       = 0;
                sCxEngineConfigName = "";
                sCxEngineConfigId   = "";

                for dictCxReqResponseJsonKey in dictCxReqResponseJson.keys():

                    if dictCxReqResponseJsonKey == None:

                        continue;

                    cDictJsonItem += 1;

                    dictCxReqResponseJsonItem = dictCxReqResponseJson[dictCxReqResponseJsonKey];

                    if self.bTraceFlag == True:

                        print("    Item #(%d.%d): '%s' %s [%s]..." % (cListJsonItem, cDictJsonItem, dictCxReqResponseJsonKey, type(dictCxReqResponseJsonItem), dictCxReqResponseJsonItem));

                    # --------------------------------------------------------------------------------------------------
                    # Item #(4): <raw> {<type 'dict'>} [{u'id': 5, u'name': u'Multi-language Scan'}]...
                    #   Item #(4.1): 'id' <type 'int'> [5]...
                    #   Item #(4.2): 'name' <type 'unicode'> [Multi-language Scan]...
                    # --------------------------------------------------------------------------------------------------

                    if dictCxReqResponseJsonKey == "name":

                        if type(dictCxReqResponseJsonItem) == unicode:

                            sCxEngineConfigName = dictCxReqResponseJsonItem.encode('ascii', 'ignore');

                        else:

                            sCxEngineConfigName = dictCxReqResponseJsonItem;

                    if dictCxReqResponseJsonKey == "id":

                        sCxEngineConfigId = "%d" % (dictCxReqResponseJsonItem);

                self.cxProjectCreationCollection.addCxProjectMetaDataAllEngineConfigurations(cxengineconfigname=sCxEngineConfigName, cxengineconfigid=sCxEngineConfigId);

        except Exception, inst:

            print "%s 'getCxRestAPIAllEngineConfigurations()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

    def getCxRestAPIAllProjectData(self):

        try:

            CxRestAPIStatistics1.cRestAPICallsMade += 1;

            cxRequestURL = "%s/cxrestapi/projects" % (self.cxServerEndpoint.getCxServerURL());
            cxReqPayload = "";
            cxReqHeaders = {
                'Content-Type':  "application/json;v=1.0 / 2.0",
                'Authorization': ("%s %s" % (self.cxServerEndpoint.getCxTokenType(), self.cxServerEndpoint.getCxAccessToken())),
                'cache-control': "no-cache"
                };

            if self.bTraceFlag == True:

                print "%s Issuing Request #(%d) of URL [%s] with a Payload of [%s] and Header(s) of [%s]..." % (self.sClassDisp, CxRestAPIStatistics1.cRestAPICallsMade, cxRequestURL, cxReqPayload, cxReqHeaders);

            cxReqResponse   = requests.request("GET", cxRequestURL, data=cxReqPayload, headers=cxReqHeaders);
            sReqResponseRaw = json.dumps(cxReqResponse.json(), indent=4);
             
            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON Response {ALL Project(s)} ===============");
                print(type(sReqResponseRaw));

                print("");
                print("=============== DIR JSON Response {ALL Project(s)} ===============");
                print(dir(sReqResponseRaw));

                print("");
                print("=============== JSON 'string' Response {ALL Project(s)} ===============");
                print(sReqResponseRaw);

            listCxReqResponseJson = json.loads(sReqResponseRaw);

            if self.bTraceFlag == True:

                print("");
                print("=============== TYPE JSON 'list' Response {ALL Project(s)} ===============");
                print(type(listCxReqResponseJson));

                print("");
                print("=============== DIR JSON 'list' Response {ALL Project(s)} ===============");
                print(dir(listCxReqResponseJson));

                print("");
                print("=============== JSON 'list' Response {ALL Project(s)} [RAW print] ===============");
                print(listCxReqResponseJson);

                print("");
                print("=============== JSON 'list' Response {ALL Project(s)} Enumerated ===============");

            cListJsonItem = 0;

            for listCxReqResponseJsonItem in listCxReqResponseJson:

                if listCxReqResponseJsonItem == None:

                    continue;

                cListJsonItem += 1;

                if self.bTraceFlag == True:

                    print("  Item #(%d): <raw> {%s} [%s]..." % (cListJsonItem, type(listCxReqResponseJsonItem), listCxReqResponseJsonItem));

                dictCxReqResponseJson = listCxReqResponseJsonItem;

                cDictJsonItem = 0;
                cxProjectData = CxProjectData1.CxProjectData(trace=self.bTraceFlag);

                for dictCxReqResponseJsonKey in dictCxReqResponseJson.keys():

                    if dictCxReqResponseJsonKey == None:

                        continue;

                    cDictJsonItem += 1;

                    dictCxReqResponseJsonItem = dictCxReqResponseJson[dictCxReqResponseJsonKey];

                    if self.bTraceFlag == True:

                        print("    Item #(%d.%d): '%s' %s [%s]..." % (cListJsonItem, cDictJsonItem, dictCxReqResponseJsonKey, type(dictCxReqResponseJsonItem), dictCxReqResponseJsonItem));

                    # --------------------------------------------------------------------------------------------------
                    # Item #(13):
                    #   Item #(13.1): 'name' [CheckmarxXcodePlugin1]...
                    #   Item #(13.2): 'links' [[{u'uri': u'/projects/390093', u'rel': u'self'}, 
                    #                           {u'uri': u'/auth/teams/', u'rel': u'teams'}, 
                    #                           {u'uri': u'/sast/scans?projectId=390093&last=1', u'rel': u'latestscan'}, 
                    #                           {u'uri': u'/sast/scans?projectId=390093', u'rel': u'allscans'}, 
                    #                           {u'uri': u'/sast/scanSettings/390093', u'rel': u'scansettings'}, 
                    #                           {u'type': u'local', u'uri': None, u'rel': u'source'}]]...
                    #   Item #(13.3): 'isPublic' [True]...
                    #   Item #(13.4): 'teamId' [00000000-1111-1111-b111-989c9070eb11]...
                    #   Item #(13.5): 'customFields' [[]]...
                    #   Item #(13.6): 'id' [390093]...
                    # --------------------------------------------------------------------------------------------------

                    if dictCxReqResponseJsonKey == "name":

                        cxProjectData.setCxProjectName(cxprojectname=dictCxReqResponseJsonItem);

                    if dictCxReqResponseJsonKey == "id":

                        cxProjectData.setCxProjectId(cxprojectid=dictCxReqResponseJsonItem);

                    if dictCxReqResponseJsonKey == "isPublic":

                        cxProjectData.setCxProjectIsPublic(cxprojectispublic=dictCxReqResponseJsonItem);

                    if dictCxReqResponseJsonKey == "teamId":

                        cxProjectData.setCxProjectTeamId(cxprojectteamid=dictCxReqResponseJsonItem);

                    if dictCxReqResponseJsonKey == "links":

                        cxProjectData.setCxProjectLinks(cxprojectlinks=dictCxReqResponseJsonItem);

                    if dictCxReqResponseJsonKey == "customFields":

                        cxProjectData.setCxProjectCustomFields(cxprojectcustomfields=dictCxReqResponseJsonItem);

                self.cxProjectCreationCollection.addCxProjectMetaDataAllProjects(cxprojectdata=cxProjectData);

        except Exception, inst:

            print "%s 'getCxRestAPIAllProjectData()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;


