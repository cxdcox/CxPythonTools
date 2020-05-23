
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

from datetime import datetime;

optParser   = optparse.OptionParser();
sScriptId   = optParser.get_prog_name();
sScriptVers = "(v1.0501)";
sScriptDisp = sScriptId+" "+sScriptVers+":"
cScriptArgc = len(sys.argv);

bVerbose    = False;

def main():

    try:

        sServerNode = platform.node();
        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print "%s The Checkmarx Sample Rest API requests #1 is starting execution from Server [%s] on [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp);
        print "";

        optParser.add_option("-v", "--verbose", dest="run_verbose", default=False, help="Run VERBOSE", action="store_True");
     
        (options, args) = optParser.parse_args();
     
        bVerbose = options.run_verbose;
     
        if bVerbose == True:
     
            print "%s Command VERBOSE flag is [%s]..." % (sScriptDisp, bVerbose);
            print "";

        url     = "http://192.168.2.112:8080/cxrestapi/auth/identity/connect/token";
        payload = "username=dcox&password=C0rky9%232016&grant_type=password&scope=sast_rest_api&client_id=resource_owner_client&client_secret=014DF517-39D1-4453-B7B3-9930C563627C";
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
            };

        response    = requests.request("POST", url, data=payload, headers=headers);
        pretty_data = json.dumps(response.json(), indent=4);
         
        if bVerbose == True:

            print("");
            print("=============== JSON 'pretty print' Response {Auth/Token} ===============");
            print(pretty_data);

            print("");
            print("=============== TYPE 'pretty data' Response {Auth/Token} ===============");
            print(type(pretty_data));

            print("");
            print("=============== DIR 'pretty data' Response {Auth/Token} ===============");
            print(dir(pretty_data));

        dict_json = json.loads(pretty_data);

        if bVerbose == True:

            print("");
            print("=============== TYPE 'dict_json' Response {Auth/Token} ===============");
            print(type(dict_json));

            print("");
            print("=============== DIR 'dict_json' Response {Auth/Token} ===============");
            print(dir(dict_json));

            print("");
            print("=============== DIR 'dict_json' Response {Auth/Token} [RAW print] ===============");
            print(dict_json);

        print("");
        print("=============== DICT 'dict_json' Response {Auth/Token} Enumerated ===============");

        token_type    = "";
        access_token  = "";
        cDictJsonItem = 0;

        for dict_json_key in dict_json.keys():

            if dict_json_key == None:

                continue;

            cDictJsonItem += 1;

            dict_json_item = dict_json[dict_json_key];

            print("  Item #(%d): '%s' [%s]..." % (cDictJsonItem, dict_json_key, dict_json_item));

            if dict_json_key == "token_type":

                token_type = dict_json_item;

            if dict_json_key == "access_token":

                access_token = dict_json_item;

        if len(access_token) < 1:

            print "%s Checkmarx 'access_token' is 'empty' - Error!" % (sScriptDisp);

            return False;

        url     = "http://192.168.2.112:8080/cxrestapi/projects";
        payload = "";
        headers = {
            'Content-Type':  "application/json;v=1.0 / 2.0",
            'Authorization': ("%s %s" % (token_type, access_token)),
            'cache-control': "no-cache"
            };

        response    = requests.request("GET", url, data=payload, headers=headers);
        pretty_data = json.dumps(response.json(), indent=4);
         
        if bVerbose == True:

            print("");
            print("=============== JSON 'pretty print' Response {ALL Project(s)} ===============");
            print(pretty_data);

            print("");
            print("=============== TYPE 'pretty data' Response {ALL Project(s)} ===============");
            print(type(pretty_data));

            print("");
            print("=============== DIR 'pretty data' Response {ALL Project(s)} ===============");
            print(dir(pretty_data));

        list_json = json.loads(pretty_data);

        if bVerbose == True:

            print("");
            print("=============== TYPE 'list_json' Response {ALL Project(s)} ===============");
            print(type(list_json));

            print("");
            print("=============== DIR 'list_json' Response {ALL Project(s)} ===============");
            print(dir(list_json));

            print("");
            print("=============== DIR 'list_json' Response {ALL Project(s)} [RAW print] ===============");
            print(list_json);

        print("");
        print("=============== DICT 'list_json' Response {ALL Project(s)} Enumerated ===============");

        cListJsonItem = 0;

        for list_json_item in list_json:

            if list_json_item == None:

                continue;

            cListJsonItem += 1;

            if bVerbose == True:

                print("  Item #(%d): <raw> {%s} [%s]..." % (cListJsonItem, type(list_json_item), list_json_item));

            dict_json = list_json_item;

            cDictJsonItem = 0;

            for dict_json_key in dict_json.keys():

                if dict_json_key == None:

                    continue;

                cDictJsonItem += 1;

                dict_json_item = dict_json[dict_json_key];

                print("    Item #(%d.%d): '%s' [%s]..." % (cListJsonItem, cDictJsonItem, dict_json_key, dict_json_item));

        dtNow       = datetime.now();
        sDTNowStamp = dtNow.strftime("%Y/%m/%d at %H:%M:%S");

        print "";
        print "%s The Checkmarx Sample Rest API requests #1 is ending execution from Server [%s] on [%s]..." % (sScriptDisp, sServerNode, sDTNowStamp);
        print "";

    except Exception, inst:

        print "%s 'main()' - exception occured..." % (sScriptDisp);
        print type(inst);
        print inst;

        excType, excValue, excTraceback = sys.exc_info();
        asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

        print "- - - ";
        print '\n'.join(asTracebackLines);
        print "- - - ";

        return False;

    return True;

if __name__ == '__main__':

    bCmdExecOk = main();

    if bCmdExecOk == False:

        print "%s Exiting with a Return Code of (31)..." % (sScriptDisp);

        sys.exit(31);

    print "%s Exiting with a Return Code of (0)..." % (sScriptDisp);

    sys.exit(0);

