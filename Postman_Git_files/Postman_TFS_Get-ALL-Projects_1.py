
import optparse;
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;
import requests;
import json;
import base64;

from datetime import datetime;

optParser             = optparse.OptionParser();
sScriptId             = optParser.get_prog_name();
sScriptVers           = "(v1.0109)";
sScriptDisp           = sScriptId+" "+sScriptVers+":"
cScriptArgc           = len(sys.argv);

bVerbose              = False;
sScriptOutputJsonFile = "";

def main():

    try:

        sPythonVers = ("v%s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro));
        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("%s The Checkmarx Postman TFS 'Get-ALL-Projects' via Rest API #1 is starting execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_true");
        optParser.add_option("-o", "--output-json-file", dest="output_json_file", default="", help="(Output) JSON file [generated]");
     
        (options, args) = optParser.parse_args();
     
        bVerbose              = options.run_verbose;
        sScriptOutputJsonFile = options.output_json_file.strip();
     
        if bVerbose == True:
     
            print("%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose));
            print("%s Command (Output) JSON file is [%s]..." % (sScriptDisp, sScriptOutputJsonFile));
            print("");

        if sScriptOutputJsonFile != None:

            sScriptOutputJsonFile = sScriptOutputJsonFile.strip();

        if sScriptOutputJsonFile == None or \
           len(sScriptOutputJsonFile) < 1:

            print("%s Checkmarx (Output) JSON file is None or Empty - this output will be bypassed - Warning!" % (sScriptDisp));

            sScriptOutputJsonFile == None;

        else:

            if bVerbose == True:

                print("");
                print("%s Generating the Checkmarx (Output) JSON into the file [%s]..." % (sScriptDisp, sScriptOutputJsonFile));
                print("");

        bProcessingError = False;

        sTFSUsername    = "dcox";
        sTFSPAT         = "3qr6px4yogbtwrx56ios5wcp53kneeojt7tcqj5w3q5fhxah6fhq";
        sTFSUserPAT     = "%s:%s" % (sTFSUsername, sTFSPAT);
        sBase64UserPATb = base64.b64encode(bytes(sTFSUserPAT, "utf-8"));
        sBase64UserPAT  = sBase64UserPATb.decode(encoding='UTF-8');

        print("%s Base64: 'sBase64UserPATb' is [%s] and 'sBase64UserPAT' is [%s]..." % (sScriptDisp, sBase64UserPATb, sBase64UserPAT));

        cxRequestURL   = "http://192.168.2.190:9080/tfs/DefaultCollection/_apis/projects";
        cxReqHeaders   = {
        #   'Authorization':             "Basic ZGNveDozcXI2cHg0eW9nYnR3cng1NmlvczV3Y3A1M2tuZWVvanQ3dGNxajV3M3E1Zmh4YWg2Zmhx",
            'Authorization':             ("Basic %s" % (sBase64UserPAT)),
            'Accept-Encoding':           "gzip, deflate",
            'Accept':                    "application/json;api-version=4.1",
            'Connection':                "keep-alive",
            'Content-Type':              "application/json; charset=utf-8",
            'Cache-Control':             "no-cache",
            'cache-control':             "no-cache"
        #   'X-VSS-ForceMsaPassThrough': "true",
        #   'User-Agent':     "PostmanRuntime/7.17.1",
        #   'Postman-Token': "197f02d5-5741-4ed0-89ee-f7b89e202108,47229239-fe86-4b3d-b127-2fa5af151321",
        #   'Host':          "192.168.2.190:9080",
            };
        cxReqRespOk    = [200];

        print("%s Issuing a 'Get' Request of URL [%s] with Header(s) of [%s]..." % (sScriptDisp, cxRequestURL, cxReqHeaders));

        cxReqResponse = requests.request("GET", cxRequestURL, headers=cxReqHeaders);

        if bVerbose == True:

            print("%s The URL Request returned a 'status' code of [%s] Type [%s]..." % (sScriptDisp, cxReqResponse.status_code, type(cxReqResponse.status_code)));
        #   print("%s The URL Response is [%s]..." % (cxReqResponse.text));
            # int(cxReqResponse.text);

        if cxReqResponse.status_code in cxReqRespOk:

            if bVerbose == True:

                print("%s The URL Request returned a 'status' code of [%s] Type [%s] is a 'good' response..." % (sScriptDisp, cxReqResponse.status_code, type(cxReqResponse.status_code)));

        else:

            bProcessingError = True;

            print("%s The URL Request returned a 'status' code of [%s] Type [%s] is NOT a 'good' response of [%s] - Error!" % (sScriptDisp, cxReqResponse.status_code, type(cxReqResponse.status_code), cxReqRespOk));

        jsonReqResponse = cxReqResponse.json();

        if jsonReqResponse != None:

            sReqResponseRaw = json.dumps(cxReqResponse.json(), indent=4);

            if bVerbose == True:

                print("");
                print("=============== TYPE JSON Response {TFS Get-ALL-Projects} ===============");
                print((type(sReqResponseRaw)));

                print("");
                print("=============== DIR JSON Response {TFS Get-ALL-Projects} ===============");
                print((dir(sReqResponseRaw)));

                print("");
                print("=============== JSON 'string' Response {TFS Get-ALL-Projects} ===============");
                print(sReqResponseRaw);

            dictCxReqResponseJson = json.loads(sReqResponseRaw);

            if bVerbose == True:

                print("");
                print("=============== TYPE JSON 'dictionary' Response {TFS Get-ALL-Projects} ===============");
                print((type(dictCxReqResponseJson)));

                print("");
                print("=============== DIR JSON 'dictionary' Response {TFS Get-ALL-Projects} ===============");
                print((dir(dictCxReqResponseJson)));

                print("");
                print("=============== JSON 'dictionary' Response {TFS Get-ALL-Projects} [RAW print] ===============");
                print(dictCxReqResponseJson);

                print("");
                print("=============== JSON 'dictionary' Response {TFS Get-ALL-Projects} Enumerated ===============");

            cDictJsonItem = 0;

            for dictCxReqResponseJsonKey in list(dictCxReqResponseJson.keys()):

                if dictCxReqResponseJsonKey == None:

                    continue;

                cDictJsonItem += 1;

                dictCxReqResponseJsonItem = dictCxReqResponseJson[dictCxReqResponseJsonKey];

                if bVerbose == True:

                    print(("  Item #(%d): '%s' [%s]..." % (cDictJsonItem, dictCxReqResponseJsonKey, dictCxReqResponseJsonItem)));

                    if type(dictCxReqResponseJsonItem) == dict:

                        dictSubItem  = dictCxReqResponseJsonItem;
                        cDictSubItem = 0;

                        for sDictItemKey in dictSubItem.keys():

                            cDictSubItem += 1;

                            objDictItemValue = dictSubItem[sDictItemKey];

                            print("%s The DICT Item #(%d) of (%d) 'sDictItemKey' Type [%s] is [%s] 'objDictItemValue' Type [%s] is [%s]:" % (sScriptDisp, cDictSubItem, len(dictSubItem), type(sDictItemKey), sDictItemKey, type(objDictItemValue), objDictItemValue));

                    else:

                        if type(dictCxReqResponseJsonItem) == list:

                            listSubItems = dictCxReqResponseJsonItem;
                            cListSubItem = 0;

                            for objListSubItem in listSubItems:

                                cListSubItem += 1;

                                print("%s The LIST Item #(%d) of (%d) 'objListSubItem' Type [%s] is [%s]..." % (sScriptDisp, cListSubItem, len(listSubItems), type(objListSubItem), objListSubItem));

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("");
        print("%s The Checkmarx Postman TFS 'Get-ALL-Projects' via Rest API #1 is ending execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

    except Exception as inst:

        print("%s 'main()' - exception occured..." % (sScriptDisp));
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

if __name__ == '__main__':

    try:

        pass;

    except Exception as inst:

        print("%s '<before>-main()' - exception occured..." % (sScriptDisp));
        print(type(inst));
        print(inst);

        excType, excValue, excTraceback = sys.exc_info();
        asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

        print("- - - ");
        print('\n'.join(asTracebackLines));
        print("- - - ");

    bCmdExecOk = main();

    if bCmdExecOk == False:

        print("%s Exiting with a Return Code of (31)..." % (sScriptDisp));

        sys.exit(31);

    print("%s Exiting with a Return Code of (0)..." % (sScriptDisp));

    sys.exit(0);

