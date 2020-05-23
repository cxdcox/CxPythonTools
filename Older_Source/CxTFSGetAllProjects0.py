
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
sScriptVers           = "(v1.0214)";
sScriptDisp           = sScriptId+" "+sScriptVers+":"
cScriptArgc           = len(sys.argv);

bVerbose              = False;
sScriptTFSServerURL   = None;
sScriptTFSUserId      = None;
sScriptTFSPAT         = None;
sScriptOutputJsonFile = "";

def main():

    try:

        sPythonVers = ("v%s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro));
        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("%s The Checkmarx TFS 'Get-ALL-Projects' via Rest API #1 is starting execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        print("");

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_true");
        optParser.add_option("--url", dest="tfs_server_url", default="", help="TFS Server URL - Protocol/Host/Port - sample: --url=http://hostname:8080", metavar="TFS-Server-URL");
        optParser.add_option("--user", dest="tfs_user_id", default="", help="TFS Authentication UserId", metavar="TFS-UserId");
        optParser.add_option("--pat", dest="tfs_pat", default="", help="TFS Authentication PAT (Personal Access Token)", metavar="TFS-PAT");
        optParser.add_option("-o", "--output-json-file", dest="output_json_file", default="", help="(Output) JSON file [generated]");
     
        (options, args) = optParser.parse_args();
     
        bVerbose              = options.run_verbose;
        sScriptTFSServerURL   = options.tfs_server_url.strip();
        sScriptTFSUserId      = options.tfs_user_id.strip();
        sScriptTFSPAT         = options.tfs_pat.strip();
        sScriptOutputJsonFile = options.output_json_file.strip();
     
        if bVerbose == True:
     
            print("%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose));
            print("");
            print("%s Command Tfs Server URL is [%s]..." % (sScriptDisp, sScriptTFSServerURL));
            print("%s Command Tfs UserId is [%s]..." % (sScriptDisp, sScriptTFSUserId));
            print("%s Command Tfs PAT (Personal Access Token) is [%s]..." % (sScriptDisp, sScriptTFSPAT));
            print("%s Command (Output) JSON file is [%s]..." % (sScriptDisp, sScriptOutputJsonFile));
            print("");

        if sScriptTFSServerURL != None:

            sScriptTFSServerURL = sScriptTFSServerURL.strip();

        if sScriptTFSServerURL == None or \
           len(sScriptTFSServerURL) < 1:

            sScriptTFSServerURL = None;

        else:

            sScriptTFSServerURLLow = sScriptTFSServerURL.lower();

            if sScriptTFSServerURLLow.startswith("http://")  == False and \
               sScriptTFSServerURLLow.startswith("https://") == False and \
               sScriptTFSServerURLLow.startswith("ssh://")   == False:

                sScriptTFSServerURL = None;

        if sScriptTFSServerURL != None:

            sScriptTFSServerURL = sScriptTFSServerURL.strip();

        if sScriptTFSServerURL == None or \
           len(sScriptTFSServerURL) < 1:

            print("");
            print("%s The TFS Server URL is None or Empty - this MUST be supplied - Error!" % (sScriptDisp));
            print("");

            return False;

        if sScriptTFSUserId != None:

            sScriptTFSUserId = sScriptTFSUserId.strip();

        if sScriptTFSUserId == None or \
           len(sScriptTFSUserId) < 1:

            sScriptTFSUserId = None;

            print("");
            print("%s The TFS UserId is None or Empty - this SHOULD be supplied - Warning!" % (sScriptDisp));
            print("");

        if sScriptTFSPAT != None:

            sScriptTFSPAT = sScriptTFSPAT.strip();

        if sScriptTFSPAT == None or \
            len(sScriptTFSPAT) < 1:

            sScriptTFSPAT = None;

            print("");
            print("%s The TFS PAT (Personal Access Token) is None or Empty - this SHOULD be supplied - Warning!" % (sScriptDisp));
            print("");

        if sScriptOutputJsonFile != None:

            sScriptOutputJsonFile = sScriptOutputJsonFile.strip();

        if sScriptOutputJsonFile == None or \
           len(sScriptOutputJsonFile) < 1:

            sScriptOutputJsonFile == "CxTFSGetAllProjects0_response.json";

            print("%s Checkmarx (Output) JSON file is None or Empty - defaulting to file [%s] - Warning!" % (sScriptDisp, sScriptOutputJsonFile));

        else:

            if bVerbose == True:

                print("");
                print("%s Generating the Checkmarx (Output) JSON into the file [%s]..." % (sScriptDisp, sScriptOutputJsonFile));
                print("");

        bProcessingError   = False;
        asTFSRestResponses = list();

    #   sTFSUsername    = "dcox";
    #   sTFSPAT         = "3qr6px4yogbtwrx56ios5wcp53kneeojt7tcqj5w3q5fhxah6fhq";
        sTFSUsername    = sScriptTFSUserId;
        sTFSPAT         = sScriptTFSPAT;
        sTFSUserPAT     = "%s:%s" % (sTFSUsername, sTFSPAT);
        sBase64UserPATb = base64.b64encode(bytes(sTFSUserPAT, "utf-8"));
        sBase64UserPAT  = sBase64UserPATb.decode(encoding='UTF-8');

        print("%s Base64: 'sBase64UserPATb' is [%s] and 'sBase64UserPAT' is [%s]..." % (sScriptDisp, sBase64UserPATb, sBase64UserPAT));

        cxRequestVerb  = "GET";
    #   cxRequestURL   = "http://192.168.2.190:9080/tfs/DefaultCollection/_apis/projects";
        cxRequestURL   = ("%s/tfs/DefaultCollection/_apis/projects" % (sScriptTFSServerURL));
    #   cxRequestURL   = ("%s/tfs/ElevateDev/_apis/projects" % (sScriptTFSServerURL));      # Elevate doesn't have 'DefaultCollection'...
        cxReqHeaders   = {
            'Authorization':             ("Basic %s" % (sBase64UserPAT)),
            'Accept-Encoding':           "gzip, deflate",
            'Accept':                    "application/json;api-version=4.1",
            'Connection':                "keep-alive",
            'Content-Type':              "application/json; charset=utf-8",
            'Cache-Control':             "no-cache",
            'cache-control':             "no-cache"
        #   'X-VSS-ForceMsaPassThrough': "true",
            };
        cxReqRespOk    = [200];

        sHeaderMsg = ("%s The Checkmarx TFS 'Get-ALL-Projects' via Rest API #1 is starting execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
        sOutputMsg = ("%s Issuing a [%s] Request of URL [%s] with Header(s) of [%s]..." % (sScriptDisp, cxRequestVerb, cxRequestURL, cxReqHeaders));

        asTFSRestResponses.append("");
        asTFSRestResponses.append(sHeaderMsg);
        asTFSRestResponses.append(sOutputMsg);

        print(sOutputMsg);

    #   cxReqResponse = requests.request(cxRequestVerb, cxRequestURL, headers=cxReqHeaders);
        cxReqResponse = requests.request(cxRequestVerb, cxRequestURL, headers=cxReqHeaders, verify=False);  # HTTPS needs 'verify=False'...

        sOutputMsg = ("%s The URL [%s] Request returned a 'status' code of [%s] Type [%s]..." % (sScriptDisp, cxRequestVerb, cxReqResponse.status_code, type(cxReqResponse.status_code)));

        asTFSRestResponses.append(sOutputMsg);

        if bVerbose == True:

            print(sOutputMsg);
        #   print("%s The URL Response is [%s]..." % (cxReqResponse.text));

        if cxReqResponse.status_code in cxReqRespOk:

            sOutputMsg = ("%s The URL Request returned a 'status' code of [%s] Type [%s] is a 'good' response..." % (sScriptDisp, cxReqResponse.status_code, type(cxReqResponse.status_code)));

            asTFSRestResponses.append(sOutputMsg);

            if bVerbose == True:

                print(sOutputMsg);

        else:

            bProcessingError = True;

            sOutputMsg = ("%s The URL Request returned a 'status' code of [%s] Type [%s] is NOT a 'good' response of [%s] - Error!" % (sScriptDisp, cxReqResponse.status_code, type(cxReqResponse.status_code), cxReqRespOk));

            asTFSRestResponses.append(sOutputMsg);

            print(sOutputMsg);

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

            if type(sReqResponseRaw) == str:

                sOutputMsg = ("%s The JSON Response: LEN (%d) - TYPE [%s]..." % (sScriptDisp, len(sReqResponseRaw), type(sReqResponseRaw)));

            else:

                sOutputMsg = ("%s The JSON Response: LEN (%d) - TYPE [%s] - DIR [%s]..." % (sScriptDisp, len(sReqResponseRaw), type(sReqResponseRaw), dir(sReqResponseRaw)));

            asTFSRestResponses.append("");
            asTFSRestResponses.append("=============== JSON 'string' Response {TFS Get-ALL-Projects} ===============");
            asTFSRestResponses.append(sOutputMsg);
            asTFSRestResponses.append("");
            asTFSRestResponses.append(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ");
            asTFSRestResponses.append(sReqResponseRaw);
            asTFSRestResponses.append(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ");
            asTFSRestResponses.append("");

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

        # Output the JSON response(s)...

        if asTFSRestResponses != None and \
            len(asTFSRestResponses) > 0:

            if sScriptOutputJsonFile != None:

                sScriptOutputJsonFile = sScriptOutputJsonFile.strip();

            if sScriptOutputJsonFile != None and \
                len(sScriptOutputJsonFile) > 0:

                try:

                    print("");
                    print("%s Command is generating the (Output) JSON into a file of [%s]..." % (sScriptDisp, sScriptOutputJsonFile));

                    fScriptOutputJsonFile = open(sScriptOutputJsonFile, "w");

                    fScriptOutputJsonFile.write('\n'.join(asTFSRestResponses));
                    fScriptOutputJsonFile.write('\n');
                    fScriptOutputJsonFile.close();

                    print("%s Command is generated the (Output) JSON into a file of [%s]..." % (sScriptDisp, sScriptOutputJsonFile));
                    print("");

                except Exception as inst:

                    print("%s 'main()' - operational exception occured writing to the (Output) JSON into a file of [%s]..." % (sScriptDisp, sScriptOutputJsonFile));
                    print(type(inst));
                    print(inst);

                    excType, excValue, excTraceback = sys.exc_info();
                    asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

                    print("- - - ");
                    print('\n'.join(asTracebackLines));
                    print("- - - ");

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print("");
        print("%s The Checkmarx TFS 'Get-ALL-Projects' via Rest API #1 is ending execution from Server [%s] on [%s] under Python [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp, sPythonVers));
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

