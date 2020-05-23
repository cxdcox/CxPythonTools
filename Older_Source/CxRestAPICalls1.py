
import os;
import traceback;
import platform;
import re;
import string;
import sys;
import collections;

import urllib;
import urllib2;

import simplejson as json;

# -------------------------------------------------------------------------------------------------
#
# ...
#
# -------------------------------------------------------------------------------------------------

class CxRestAPICalls:

    sClassMod               = __name__;
    sClassId                = "CxRestAPICalls";
    sClassVers              = "(v1.0501)";
    sClassDisp              = sClassMod+"."+sClassId+" "+sClassVers+": ";

    bTraceFlag              = False;
    bUserActionPromptFlag   = False;
    sCxServerURL            = None;
    bCxUserIsSuper          = False;
    sCxBasicAuthUserID      = None;
    sCxBasicAuthPassword    = None;
    sCxSourceServerURL      = None;

    bCxBasicAuthUsedFlag    = False;

    sCxServerHostProtocol   = None;
    sCxServerHostName       = None;
    sCxServerPortNumber     = None;
    sCxServerProjectName    = None;

    iCxServerLastRespStatus = 0;
    sCxServerLastRespMsg    = None;
    sCxServerLastRespMsg2   = None;
    sCxServerLastResp       = None;
    asCxServerLastResp      = None;

    sPlatform               = None;
    bPlatformIsWindows      = False;
    sCxUserID               = None;
    sCxUserHomeDirectory    = None;

    bCxAuthTokenProcDone    = False;
    sCxAuthTokenFilespec    = None;
    asCxAuthTokens          = None;
    sCurrCxAuthToken        = None;
    sCurrCxAuthTokenUser    = None;

    cxHttpPasswordMgr       = None;
    cxHttpBasicAuthHandler  = None;
    cxHttpOpener            = None;

    def __init__(self, trace=False, useractionprompt=False, cxserverurl=None, cxuserissuper=False, cxbasicauthuserid=None, cxbasicauthpassword=None, cxsourceserverurl=None):

        try:

            self.setTraceFlag(trace=trace);
            self.setUserActionPromptFlag(useractionprompt=useractionprompt);
            self.setCxServerURL(cxserverurl=cxserverurl);
            self.setCxUserIsSuperFlag(cxuserissuper=cxuserissuper);
            self.setCxBasicAuthUserID(cxbasicauthuserid=cxbasicauthuserid);
            self.setCxBasicAuthPassword(cxbasicauthpassword=cxbasicauthpassword);
            self.setCxSourceServerURL(cxsourceserverurl=cxsourceserverurl)

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

    def getUserActionPromptFlag(self):

        return self.bUserActionPromptFlag;

    def setUserActionPromptFlag(self, useractionprompt=False):

        self.bUserActionPromptFlag = useractionprompt;

    def getCxServerURL(self):

        return self.sCxServerURL;

    def setCxServerURL(self, cxserverurl=None):

        self.sCxServerURL = cxserverurl;

        if self.sCxServerURL != None:

            self.sCxServerURL = self.sCxServerURL.strip();

        if self.sCxServerURL == None or \
           len(self.sCxServerURL) < 1:

            self.sCxServerURL = None;

        else:

            sCxServerURLLow = self.sCxServerURL.lower();

            if sCxServerURLLow.startswith("http://")  == False and \
               sCxServerURLLow.startswith("https://") == False:

                self.sCxServerURL = None;

        self.parseCxServerURL();

    def parseCxServerURL(self):

        self.resetCxRestAPICallsObject();

        if self.sCxServerURL != None:

            self.sCxServerURL = self.sCxServerURL.strip();

        if self.sCxServerURL == None or \
           len(self.sCxServerURL) < 1:

            self.sCxServerURL = None;

            return;

        sCxServerURLLow = self.sCxServerURL.lower();

        if sCxServerURLLow.startswith("http://")  == False and \
           sCxServerURLLow.startswith("https://") == False:

            self.sCxServerURL = None;

            return;

        asProtocolSplit = self.sCxServerURL.partition("://");

        if asProtocolSplit == None or \
           len(asProtocolSplit) < 1:

            self.sCxServerURL = None;

            return;

        self.sCxServerHostProtocol = asProtocolSplit[0];

        if self.sCxServerHostProtocol != None:

            self.sCxServerHostProtocol = self.sCxServerHostProtocol.strip();

        if self.sCxServerHostProtocol == None or \
           len(self.sCxServerHostProtocol) < 1:

            self.sCxServerHostProtocol = None;

        else:

            self.sCxServerHostProtocol = self.sCxServerHostProtocol.lower();

        if len(asProtocolSplit) < 3:

            return;

        sCxServerProjectRaw = asProtocolSplit[2];

        if sCxServerProjectRaw != None:

            sCxServerProjectRaw = sCxServerProjectRaw.strip();

        if sCxServerProjectRaw == None or \
           len(sCxServerProjectRaw) < 1:

            return;

        asServerProjectSplit = sCxServerProjectRaw.partition("/");

        if asServerProjectSplit == None or \
           len(asServerProjectSplit) < 1:

            return;

        if len(asServerProjectSplit) >= 1:

            self.sCxServerHostName = asServerProjectSplit[0];

            if len(asServerProjectSplit) >= 3:

                self.sCxServerProjectName = asServerProjectSplit[2];

        if self.sCxServerHostName != None:

            self.sCxServerHostName = self.sCxServerHostName.strip();

        if self.sCxServerHostName != None and \
           len(self.sCxServerHostName) > 0:

            asServerHostPortSplit = self.sCxServerHostName.partition(":");

            if asServerHostPortSplit == None or \
               len(asServerHostPortSplit) < 1:

                return;

            if len(asServerHostPortSplit) >= 1:

                self.sCxServerHostName = asServerHostPortSplit[0];

                if len(asServerHostPortSplit) >= 3:

                    self.sCxServerPortNumber = asServerHostPortSplit[2];

    #   self.determineOSUserHomeDir();
    #   self.determineCxReviewCxAuthToken();

        return;

    def resetCxRestAPICallsObject(self):

        self.sCxServerHostProtocol   = None;
        self.sCxServerHostName       = None;
        self.sCxServerPortNumber     = None;
        self.sCxServerProjectName    = None;

        self.iCxServerLastRespStatus = 0;
        self.sCxServerLastRespMsg    = None;
        self.sCxServerLastRespMsg2   = None;
        self.sCxServerLastResp       = None;
        self.asCxServerLastResp      = None;

        self.sPlatform               = None;
        self.bPlatformIsWindows      = False;
        self.sCxUserID               = None;
        self.sCxUserHomeDirectory    = None;

        self.bCxAuthTokenProcDone = False;
        self.sCxAuthTokenFilespec = None;
        self.asCxAuthTokens       = None;
        self.sCurrCxAuthToken     = None;
        self.sCurrCxAuthTokenUser = None;

        self.cxHttpPasswordMgr       = None;
        self.cxHttpBasicAuthHandler  = None;
        self.cxHttpOpener            = None;

        return;

    def getCxUserIsSuperFlag(self):

        return self.bCxUserIsSuper;

    def setCxUserIsSuperFlag(self, cxuserissuper=False):

        self.bCxUserIsSuper = cxuserissuper;

    def getCxBasicAuthUserID(self):

        return self.sCxBasicAuthUserID;

    def setCxBasicAuthUserID(self, cxbasicauthuserid=None):

        self.sCxBasicAuthUserID = cxbasicauthuserid;

        if self.sCxBasicAuthUserID != None:

            self.sCxBasicAuthUserID = self.sCxBasicAuthUserID.strip();

        if self.sCxBasicAuthUserID == None or \
           len(self.sCxBasicAuthUserID) < 1:

            self.sCxBasicAuthUserID = None;

        if self.sCxBasicAuthPassword != None:

            self.sCxBasicAuthPassword = self.sCxBasicAuthPassword.strip();

        if self.sCxBasicAuthPassword != None and \
           len(self.sCxBasicAuthPassword) > 0:

            self.bCxBasicAuthUsedFlag = True;

        return;

    def getCxBasicAuthPassword(self):

        return self.sCxBasicAuthPassword;

    def setCxBasicAuthPassword(self, cxbasicauthpassword=None):

        self.sCxBasicAuthPassword = cxbasicauthpassword;

        if self.sCxBasicAuthPassword != None:

            self.sCxBasicAuthPassword = self.sCxBasicAuthPassword.strip();

        if self.sCxBasicAuthPassword == None or \
           len(self.sCxBasicAuthPassword) < 1:

        #   self.sCxBasicAuthPassword = None;
            self.sCxBasicAuthPassword = "";

        if self.sCxBasicAuthUserID != None:

            self.sCxBasicAuthUserID = self.sCxBasicAuthUserID.strip();

        if self.sCxBasicAuthUserID != None and \
           len(self.sCxBasicAuthUserID) > 0:

            self.bCxBasicAuthUsedFlag = True;

        return;

    def getCxSourceServerURL(self):

        return self.sCxSourceServerURL;

    def setCxSourceServerURL(self, cxsourceserverurl=None):

        self.sCxSourceServerURL = cxsourceserverurl;

        if self.sCxSourceServerURL != None:

            self.sCxSourceServerURL = self.sCxSourceServerURL.strip();

        if self.sCxSourceServerURL == None or \
           len(self.sCxSourceServerURL) < 1:

            self.sCxSourceServerURL = None;

        else:

            sCxSourceServerURLLow = self.sCxSourceServerURL.lower();

            if sCxSourceServerURLLow.startswith("http://")  == False and \
               sCxSourceServerURLLow.startswith("https://") == False:

                self.sCxSourceServerURL = None;

    def getCxServerHostProtocol(self):

        return self.sCxServerHostProtocol;

    def getCxServerHostName(self):

        return self.sCxServerHostName;

    def getCxServerPortNumber(self):

        return self.sCxServerPortNumber;

    def getCxServerProjectName(self):

        return self.sCxServerProjectName;

    def getCxServerLastResponseStatus(self):

        return self.iCxServerLastRespStatus;

    def getCxServerLastResponseMsg(self):

        return self.sCxServerLastRespMsg;

    def getCxServerLastResponseMsg2(self):

        return self.sCxServerLastRespMsg2;

    def getCxServerLastResponse(self):

        return self.sCxServerLastResp;

    def getCxServerLastResponseAsList(self):

        return self.asCxServerLastResp;

    def dump_fields(self):

        if self.bTraceFlag == True:

            print "%s Dump of the variable(s) content of this class:" % (self.sClassDisp);
            print "%s The 'bTraceFlag' boolean is [%s]..." % (self.sClassDisp, self.bTraceFlag);
            print "%s The 'bUserActionPromptFlag' boolean is [%s]..." % (self.sClassDisp, self.bUserActionPromptFlag);
            print "%s The contents of 'sCxServerURL' is [%s]..." % (self.sClassDisp, self.sCxServerURL);
            print "%s The contents of 'bCxUserIsSuper' is [%s]..." % (self.sClassDisp, self.bCxUserIsSuper);
            print "%s The contents of 'sCxBasicAuthUserID' is [%s]..." % (self.sClassDisp, self.sCxBasicAuthUserID);
            print "%s The contents of 'sCxBasicAuthPassword' is [%s]..." % (self.sClassDisp, self.sCxBasicAuthPassword);
            print "%s The contents of 'sCxSourceServerURL' is [%s]..." % (self.sClassDisp, self.sCxSourceServerURL);
            print "%s The contents of 'bCxBasicAuthUsedFlag' is [%s]..." % (self.sClassDisp, self.bCxBasicAuthUsedFlag);
            print "%s The contents of 'sCxServerHostProtocol' is [%s]..." % (self.sClassDisp, self.sCxServerHostProtocol);
            print "%s The contents of 'sCxServerHostName' is [%s]..." % (self.sClassDisp, self.sCxServerHostName);
            print "%s The contents of 'sCxServerPortNumber' is [%s]..." % (self.sClassDisp, self.sCxServerPortNumber);
            print "%s The contents of 'sCxServerProjectName' is [%s]..." % (self.sClassDisp, self.sCxServerProjectName);
            print "%s The contents of 'iCxServerLastRespStatus' is (%d)..." % (self.sClassDisp, self.iCxServerLastRespStatus);
            print "%s The contents of 'sCxServerLastRespMsg' is [%s]..." % (self.sClassDisp, self.sCxServerLastRespMsg);
            print "%s The contents of 'sCxServerLastRespMsg2' is [%s]..." % (self.sClassDisp, self.sCxServerLastRespMsg2);
            print "%s The contents of 'sCxServerLastResp' is [%s]..." % (self.sClassDisp, self.sCxServerLastResp);
            print "%s The contents of 'asCxServerLastResp' is [%s]..." % (self.sClassDisp, self.asCxServerLastResp);
            print "%s The contents of 'sPlatform' is [%s]..." % (self.sClassDisp, self.sPlatform);
            print "%s The contents of 'bPlatformIsWindows' is [%s]..." % (self.sClassDisp, self.bPlatformIsWindows);
            print "%s The contents of 'sCxUserID' is [%s]..." % (self.sClassDisp, self.sCxUserID);
            print "%s The contents of 'sCxUserHomeDirectory' is [%s]..." % (self.sClassDisp, self.sCxUserHomeDirectory);
            print "%s The contents of 'bCxAuthTokenProcDone' is [%s]..." % (self.sClassDisp, self.bCxAuthTokenProcDone);
            print "%s The contents of 'sCxAuthTokenFilespec' is [%s]..." % (self.sClassDisp, self.sCxAuthTokenFilespec);
            print "%s The contents of 'asCxAuthTokens' is [%s]..." % (self.sClassDisp, self.asCxAuthTokens);
            print "%s The contents of 'sCurrCxAuthToken' is [%s]..." % (self.sClassDisp, self.sCurrCxAuthToken);
            print "%s The contents of 'sCurrCxAuthTokenUser' is [%s]..." % (self.sClassDisp, self.sCurrCxAuthTokenUser);
            print "%s The contents of 'cxHttpPasswordMgr' is [%s]..." % (self.sClassDisp, self.cxHttpPasswordMgr);
            print "%s The contents of 'cxHttpBasicAuthHandler' is [%s]..." % (self.sClassDisp, self.cxHttpBasicAuthHandler);
            print "%s The contents of 'cxHttpOpener' is [%s]..." % (self.sClassDisp, self.cxHttpOpener);

    def toString(self):

        asObjDetail = list();

        asObjDetail.append("'sClassDisp' is [%s], " % (self.sClassDisp));
        asObjDetail.append("'bTraceFlag' is [%s], " % (self.bTraceFlag));
        asObjDetail.append("'bUserActionPromptFlag' is [%s], " % (self.bUserActionPromptFlag));
        asObjDetail.append("'sCxServerURL' is [%s], " % (self.sCxServerURL));
        asObjDetail.append("'bCxUserIsSuper' is [%s], " % (self.bCxUserIsSuper));
        asObjDetail.append("'sCxBasicAuthUserID' is [%s], " % (self.sCxBasicAuthUserID));
        asObjDetail.append("'sCxBasicAuthPassword' is [%s], " % (self.sCxBasicAuthPassword));
        asObjDetail.append("'sCxSourceServerURL' is [%s], " % (self.sCxSourceServerURL));
        asObjDetail.append("'bCxBasicAuthUsedFlag' is [%s], " % (self.bCxBasicAuthUsedFlag));
        asObjDetail.append("'sCxServerHostProtocol' is [%s], " % (self.sCxServerHostProtocol));
        asObjDetail.append("'sCxServerHostName' is [%s], " % (self.sCxServerHostName));
        asObjDetail.append("'sCxServerPortNumber' is [%s], " % (self.sCxServerPortNumber));
        asObjDetail.append("'sCxServerProjectName' is [%s], " % (self.sCxServerProjectName));
        asObjDetail.append("'iCxServerLastRespStatus' is (%d), " % (self.iCxServerLastRespStatus));
        asObjDetail.append("'sCxServerLastRespMsg' is [%s], " % (self.sCxServerLastRespMsg));
        asObjDetail.append("'sCxServerLastRespMsg2' is [%s], " % (self.sCxServerLastRespMsg2));
        asObjDetail.append("'sCxServerLastResp' is [%s], " % (self.sCxServerLastResp));
        asObjDetail.append("'asCxServerLastResp' is [%s], " % (self.asCxServerLastResp));
        asObjDetail.append("'sPlatform' is [%s], " % (self.sPlatform));
        asObjDetail.append("'bPlatformIsWindows' is [%s], " % (self.bPlatformIsWindows));
        asObjDetail.append("'sCxUserID' is [%s], " % (self.sCxUserID));
        asObjDetail.append("'sCxUserHomeDirectory' is [%s], " % (self.sCxUserHomeDirectory));
        asObjDetail.append("'bCxAuthTokenProcDone' is [%s], " % (self.bCxAuthTokenProcDone));
        asObjDetail.append("'sCxAuthTokenFilespec' is [%s], " % (self.sCxAuthTokenFilespec));
        asObjDetail.append("'asCxAuthTokens' is [%s], " % (self.asCxAuthTokens));
        asObjDetail.append("'sCurrCxAuthTokenUser' is [%s], " % (self.sCurrCxAuthTokenUser));
        asObjDetail.append("'sCurrCxAuthToken' is [%s], " % (self.sCurrCxAuthToken));
        asObjDetail.append("'cxHttpPasswordMgr' is [%s], " % (self.cxHttpPasswordMgr));
        asObjDetail.append("'cxHttpBasicAuthHandler' is [%s], " % (self.cxHttpBasicAuthHandler));
        asObjDetail.append("'cxHttpOpener' is [%s]. " % (self.cxHttpOpener));

        return str(asObjDetail);

    def __str__(self):

        return self.toString();

    def __repr__(self):

        return self.toString();

    def handleCxAuthTokenProcessing(self):

        try:

            if self.bCxAuthTokenProcDone == True:

                if self.bTraceFlag == True:

                    print "%s The flag 'bCxAuthTokenProcDone' is [%s] indicating that the 'ltoken' processing has been done - bypassing further processing..." % (self.sClassDisp, self.bCxAuthTokenProcDone);

                return;

            self.determineOSUserHomeDir();
            self.determineCxReviewCxAuthToken();

        except Exception, inst:

            print "%s 'handleCxAuthTokenProcessing()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return;

        return;

    def determineOSUserHomeDir(self):

        try:

            self.sCxUserID            = None;
            self.sCxUserHomeDirectory = None;
            self.sPlatform            = platform.system();
            self.bPlatformIsWindows   = self.sPlatform.startswith('Windows');

            if self.bPlatformIsWindows == False:

                self.bPlatformIsWindows = self.sPlatform.startswith('Microsoft');

            if self.bPlatformIsWindows == True:

                import win32api;

                if self.bTraceFlag == True:

                    print "%s The platform 'system' of [%s] indicates this is a Microsoft/Windows system - 'win32api' has been imported..." % (self.sClassDisp, self.sPlatform);

                self.sCxUserID = win32api.GetUserName();

            else:

                self.sCxUserID = os.getlogin();

            self.sCxUserHomeDirectory = os.path.expanduser('~');

            if self.bTraceFlag == True:

                print "%s The platform 'system' is [%s]..." % (self.sClassDisp, self.sPlatform);
                print "%s The platform 'system' is 'Windows' [%s]..." % (self.sClassDisp, self.bPlatformIsWindows);
                print "%s The platform 'UserID' is [%s]..." % (self.sClassDisp, self.sCxUserID);
                print "%s The platform 'User' HOME Directory is [%s]..." % (self.sClassDisp, self.sCxUserHomeDirectory);
                print "";

        except Exception, inst:

            print "%s 'determineOSUserHomeDir()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return;

        return;

    def determineCxReviewCxAuthToken(self):

        try:

            self.bCxAuthTokenProcDone = False;
            self.asCxAuthTokens       = None;
            self.sCurrCxAuthToken     = None;
            sCxAuthTokenFilename            = os.path.join(self.sCxUserHomeDirectory, ".klocwork", "ltoken");
            self.sCxAuthTokenFilespec = os.path.realpath(sCxAuthTokenFilename);
            bCxReviewCxAuthTokenIsFile        = os.path.isfile(self.sCxAuthTokenFilespec);

            if bCxReviewCxAuthTokenIsFile == False:

                if self.bTraceFlag == True:

                    print "%s Command received a Klocwork 'ltoken' file of [%s] that does NOT exist - Warning!" % (self.sClassDisp, self.sCxAuthTokenFilespec);

                return;

            cCxReviewCxAuthTokenFile = os.path.getsize(self.sCxAuthTokenFilespec);

            if cCxReviewCxAuthTokenFile < 1:

                if self.bTraceFlag == True:

                    print "%s Command received a Klocwork 'ltoken' file of [%s] that is Empty (contains 0 bytes) - Warning!" % (self.sClassDisp, self.sCxAuthTokenFilespec);

                return;

            if self.bTraceFlag == True:

                print "%s Processing a Klocwork 'ltoken' file of [%s] containing (%d) bytes of data..." % (self.sClassDisp, self.sCxAuthTokenFilespec, cCxReviewCxAuthTokenFile);
                print "";

            fCxReviewCxAuthToken        = open(self.sCxAuthTokenFilespec, "r");
            self.asCxAuthTokens = fCxReviewCxAuthToken.readlines();

            fCxReviewCxAuthToken.close();

            if len(self.asCxAuthTokens) < 1:

                if self.bTraceFlag == True:

                    print "%s Read a Klocwork 'ltoken' file of [%s] with (0) input lines - Warning!" % (self.sClassDisp, self.sCxAuthTokenFilespec);

                return;

        #   sCxAuthTokenSearch    = "%s;%s;%s;" % (self.sCxServerHostName, self.sCxServerPortNumber, self.sCxUserID);
            sCxAuthTokenSearch    = "%s;%s;" % (self.sCxServerHostName, self.sCxServerPortNumber);
            sCxAuthTokenSearchLow = sCxAuthTokenSearch.lower();

            if self.bTraceFlag == True:

                print "%s Processing a Klocwork 'ltoken' file of [%s] containing (%d) lines of data - searching for a line beginning with [%s]..." % (self.sClassDisp, self.sCxAuthTokenFilespec, len(self.asCxAuthTokens), sCxAuthTokenSearchLow);
                print "";

            idCxReviewCxAuthTokensLine  = 0;
            asCxAuthTokenFields = None;

            for sCxAuthTokensLine in self.asCxAuthTokens:

                idCxReviewCxAuthTokensLine += 1;

                if self.bTraceFlag == True:

                    print "%s Processing the Klocwork 'ltoken' file of [%s] line #(%d) of [%s]..." % (self.sClassDisp, self.sCxAuthTokenFilespec, idCxReviewCxAuthTokensLine, sCxAuthTokensLine);

                if sCxAuthTokensLine != None:

                    sCxAuthTokensLine = sCxAuthTokensLine.strip();

                if sCxAuthTokensLine == None or \
                   len(sCxAuthTokensLine) < 1:

                    if self.bTraceFlag == True:

                        print "%s For the Klocwork 'ltoken' file of [%s] line #(%d) of [%s] - the line is 'empty' after 'cleaning' - bypassing the line..." % (self.sClassDisp, self.sCxAuthTokenFilespec, idCxReviewCxAuthTokensLine, sCxAuthTokensLine);

                    continue;

                sCxAuthTokensLineLow = sCxAuthTokensLine.lower();

                if sCxAuthTokensLineLow.startswith(sCxAuthTokenSearchLow) == False:

                    if self.bTraceFlag == True:

                        print "%s For the Klocwork 'ltoken' file of [%s] line #(%d) of [%s] - the line does NOT begin with [%s] - bypassing the line..." % (self.sClassDisp, self.sCxAuthTokenFilespec, idCxReviewCxAuthTokensLine, sCxAuthTokensLine, sCxAuthTokenSearchLow);

                    continue;

            #   asCxAuthTokens = sCxAuthTokensLine.rpartition(";");
            #
            #   if asCxAuthTokens != None and \
            #      len(asCxAuthTokens) > 0:
            #
            #       sCxAuthToken0 = asCxAuthTokens[0];
            #
            #       if sCxAuthToken0 != None:
            #
            #           sCxAuthToken0 = sCxAuthToken0.strip();
            #
            #       if sCxAuthToken0 != None and \
            #          len(sCxAuthToken0) > 0:
            #
            #       #   self.sCurrCxAuthToken = sCxAuthTokensLine[len(sCxAuthTokenSearch):];
            #           self.sCurrCxAuthToken = asCxAuthTokens[2];
            #
            #           if self.sCurrCxAuthToken != None:
            #
            #               self.sCurrCxAuthToken = self.sCurrCxAuthToken.strip();
            #
            #           if self.sCurrCxAuthToken == None or \
            #              len(self.sCurrCxAuthToken) < 1:
            #
            #               self.sCurrCxAuthToken = None;
            #
            #           else:
            #
            #               if self.sCurrCxAuthToken == "null":
            #
            #                   self.sCurrCxAuthToken = None;
            #
            #           break;
            #
            #       else:
            #
            #           continue;
            #
            #   else:
            #
            #       continue;

                if self.bTraceFlag == True:

                    print "%s For the Klocwork 'ltoken' file of [%s] line #(%d) of [%s] - the line DOES begin with [%s] - processing the line..." % (self.sClassDisp, self.sCxAuthTokenFilespec, idCxReviewCxAuthTokensLine, sCxAuthTokensLine, sCxAuthTokenSearchLow);

                asCxAuthTokenFields = sCxAuthTokensLine.split(";");

                if asCxAuthTokenFields != None and \
                   len(asCxAuthTokenFields) > 0:

                    if self.bTraceFlag == True:

                        print "%s For 'ltoken' line #(%d) of [%s] - the (%d) 'ltoken' field(s) are [%s]..." % (self.sClassDisp, idCxReviewCxAuthTokensLine, sCxAuthTokensLine, len(asCxAuthTokenFields), asCxAuthTokenFields);
                
                    if len(asCxAuthTokenFields) > 2:

                        sCurrCxAuthTokenUser = asCxAuthTokenFields[2];

                        if sCurrCxAuthTokenUser != None:
                        
                            sCurrCxAuthTokenUser = sCurrCxAuthTokenUser.strip();
                        
                        if sCurrCxAuthTokenUser == None or \
                           len(sCurrCxAuthTokenUser) < 1:
                        
                            sCurrCxAuthTokenUser = None;
                        
                        self.sCurrCxAuthTokenUser = sCurrCxAuthTokenUser;

                        if self.bTraceFlag == True:

                            print "%s 'ltoken' field 'self.sCurrCxAuthTokenUser' set to [%s]..." % (self.sClassDisp, self.sCurrCxAuthTokenUser);

                        if len(asCxAuthTokenFields) > 3:

                            sCurrCxAuthToken = asCxAuthTokenFields[3];

                            if sCurrCxAuthToken != None:
                            
                                sCurrCxAuthToken = sCurrCxAuthToken.strip();
                            
                            if sCurrCxAuthToken == None or \
                               len(sCurrCxAuthToken) < 1:
                            
                                sCurrCxAuthToken = None;
                            
                            self.sCurrCxAuthToken = sCurrCxAuthToken;

                            if self.bTraceFlag == True:

                                print "%s 'ltoken' field 'self.sCurrCxAuthToken' set to [%s]..." % (self.sClassDisp, self.sCurrCxAuthToken);

                        self.bCxAuthTokenProcDone = True;

            if self.bTraceFlag == True:

                print "%s The contents of 'bCxAuthTokenProcDone' is [%s]..." % (self.sClassDisp, self.bCxAuthTokenProcDone);
                print "%s The contents of 'sCxAuthTokenFilespec' is [%s]..." % (self.sClassDisp, self.sCxAuthTokenFilespec);
                print "%s The contents of 'asCxAuthTokens' is [%s]..." % (self.sClassDisp, self.asCxAuthTokens);
                print "%s The contents of 'asCxAuthTokenFields' is [%s]..." % (self.sClassDisp, asCxAuthTokenFields);
                print "%s The contents of 'sCurrCxAuthToken' is [%s]..." % (self.sClassDisp, self.sCurrCxAuthToken);
                print "%s The contents of 'sCurrCxAuthTokenUser' is [%s]..." % (self.sClassDisp, self.sCurrCxAuthTokenUser);
                print "";

        except Exception, inst:

            self.bCxAuthTokenProcDone = False;

            print "%s 'determineCxReviewCxAuthToken()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return;

        return;

    def postHttpRequest2(self, url, postdata={}, headers={}, idhttppostresp=0):

        self.handleCxAuthTokenProcessing();

        sHttpPostURL       = url;
        dictHttpPostData   = postdata;
        dictHttpHeaderData = headers;
        idCxWebApiPost     = idhttppostresp;

        try:

            if sHttpPostURL != None:

                sHttpPostURL = sHttpPostURL.strip();

            if sHttpPostURL == None or \
               len(sHttpPostURL) < 1:

                print "%s 'postHttpRequest2()' - The supplied HTTP 'post' URL string is None or 'empty' - this MUST be supplied - Error!" % (self.sClassDisp, sHttpPostURL);

                return None;

            sHttpPostData = None;

            if dictHttpPostData != None and \
               len(dictHttpPostData) > 0:

                sHttpPostData = urllib.urlencode(dictHttpPostData);

            if self.bTraceFlag == True:

                print "%s 'postHttpRequest2()' - Sending a Http 'post' #(%d) with 'data' of [%s] with 'headers' of [%s] to a URL of [%s]..." % (self.sClassDisp, idCxWebApiPost, sHttpPostData, dictHttpHeaderData, sHttpPostURL);
                print "";

            urlRequest = None;

            if dictHttpHeaderData == None or \
               len(dictHttpHeaderData) < 1:

                urlRequest = urllib2.Request(sHttpPostURL, sHttpPostData);

            else:

                urlRequest = urllib2.Request(sHttpPostURL, sHttpPostData, dictHttpHeaderData);

            if self.bCxBasicAuthUsedFlag == True and \
               self.cxHttpPasswordMgr    == None:

                sHttpTopURL = "%s://%s:%s/review/" % (self.sCxServerHostProtocol, self.sCxServerHostName, self.sCxServerPortNumber);
                self.cxHttpPasswordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm();

                self.cxHttpPasswordMgr.add_password(None, sHttpTopURL, self.sCxBasicAuthUserID, self.sCxBasicAuthPassword);

                self.cxHttpBasicAuthHandler = urllib2.HTTPBasicAuthHandler(self.cxHttpPasswordMgr);
                self.cxHttpOpener           = urllib2.build_opener(self.cxHttpBasicAuthHandler);

                urllib2.install_opener(self.cxHttpOpener);

                if self.bTraceFlag == True:

                    print "%s 'postHttpRequest2()' - HTTP 'basic' authentication setup for a UserID of [%s] for a 'top-level' URL of [%s]..." % (self.sClassDisp, self.sCxBasicAuthUserID, sHttpTopURL);
                    print "";

            self.iCxServerLastRespStatus = 0;
            self.sCxServerLastRespMsg    = None;
            self.sCxServerLastRespMsg2   = None;
            self.sCxServerLastResp       = None;
            self.asCxServerLastResp      = None;

            urlResponse = urllib2.urlopen(urlRequest);

            if urlResponse == None:

                print "%s 'postHttpRequest2()' - The Http 'post' #(%d) with 'data' of [%s] with 'headers' of [%s] to a URL of [%s] returned a 'response' object that is None - Error!" % (self.sClassDisp, idCxWebApiPost, sHttpPostData, dictHttpHeaderData, sHttpPostURL);

                return None;

        #   self.iCxServerLastRespStatus = urlResponse.getcode();
            self.iCxServerLastRespStatus = urlResponse.code;
            self.sCxServerLastRespMsg    = urlResponse.msg;

            if self.iCxServerLastRespStatus == 200 or \
               self.iCxServerLastRespStatus == 500:

                asHttpPostRespLines = urlResponse.readlines();

                if asHttpPostRespLines != None and \
                   len(asHttpPostRespLines) > 0:

                    self.sCxServerLastResp = '\n'.join(asHttpPostRespLines);

                    if self.asCxServerLastResp == None:

                        self.asCxServerLastResp = list();

                    if self.bTraceFlag == True:

                        print "%s Http POST Response Data #(%d) split into (%d) line(s)..." % (self.sClassDisp, idCxWebApiPost, len(asHttpPostRespLines));
                        print "";

                    idJsonRespLine = 0;

                    for sJsonRespLine in asHttpPostRespLines:

                        idJsonRespLine += 1;
                        sJsonRespLine   = sJsonRespLine.strip();
                        dictJsonResp    = json.loads(sJsonRespLine);

                        if dictJsonResp == None or \
                           len(dictJsonResp) < 1:

                            dictJsonResp = None;

                        self.asCxServerLastResp.append(dictJsonResp);

                        sDictJsonRespMsg = None;

                        if "message" in dictJsonResp.keys():
                         
                            sDictJsonRespMsg = dictJsonResp["message"];

                        if sDictJsonRespMsg != None:
                         
                            sDictJsonRespMsg = sDictJsonRespMsg.strip();
                         
                        if sDictJsonRespMsg == None or \
                           len(sDictJsonRespMsg) < 1:
                         
                            sDictJsonRespMsg = "";

                        self.sCxServerLastRespMsg2 = sDictJsonRespMsg;
                         
                else:

                    if self.bTraceFlag == True:

                        print "%s Http POST Response Data #(%d) contained NO line(s) - Warning!" % (self.sClassDisp, idCxWebApiPost);
                        print "";

                    self.sCxServerLastResp  = None;
                    self.asCxServerLastResp = None;

            else:

                if self.bTraceFlag == True:

                    print "%s Http ERROR:" % (self.sClassDisp);
                    print "%s Http 'status' is [%s]..." % (self.sClassDisp, self.iCxServerLastRespStatus);
                    print "%s Http 'msg'    is [%s]..." % (self.sClassDisp, urlResponse.msg);
                    print "";

                dictJsonResp = {"status": self.iCxServerLastRespStatus, "message": urlResponse.msg};

                if self.asCxServerLastResp == None:

                    self.asCxServerLastResp = list();

                self.asCxServerLastResp.append(dictJsonResp);

                self.sCxServerLastResp = "%s" % (dictJsonResp);

                sDictJsonRespMsg = None;

                if "message" in dictJsonResp.keys():

                    sDictJsonRespMsg = dictJsonResp["message"];

                if sDictJsonRespMsg != None:

                    sDictJsonRespMsg = sDictJsonRespMsg.strip();

                if sDictJsonRespMsg == None or \
                   len(sDictJsonRespMsg) < 1:

                    sDictJsonRespMsg = "";

                self.sCxServerLastRespMsg2 = sDictJsonRespMsg;

        except urllib2.HTTPError, inst:

            if self.bTraceFlag == True:

                print "%s 'postHttpRequest2()' - 'urllib2.HTTPError' exception occured (and caught)..." % (self.sClassDisp);
                print type(inst);
                print inst;
                print "";

            urlResponse = inst;

            self.iCxServerLastRespStatus = urlResponse.code;
            self.sCxServerLastRespMsg    = urlResponse.msg;

            asHttpPostRespLines = urlResponse.readlines();

            if asHttpPostRespLines != None and \
               len(asHttpPostRespLines) > 0:

                self.sCxServerLastResp = '\n'.join(asHttpPostRespLines);

                if self.asCxServerLastResp == None:

                    self.asCxServerLastResp = list();

                if self.bTraceFlag == True:

                    print "%s Http POST (500) Response Data #(%d) split into (%d) line(s)..." % (self.sClassDisp, idCxWebApiPost, len(asHttpPostRespLines));
                    print "";

                idJsonRespLine = 0;

                for sJsonRespLine in asHttpPostRespLines:

                    idJsonRespLine += 1;
                    sJsonRespLine   = sJsonRespLine.strip();
                    dictJsonResp    = json.loads(sJsonRespLine);

                    if dictJsonResp == None or \
                       len(dictJsonResp) < 1:

                        dictJsonResp = None;

                    self.asCxServerLastResp.append(dictJsonResp);
                    
                    sDictJsonRespMsg = None;

                    if "message" in dictJsonResp.keys():

                        sDictJsonRespMsg = dictJsonResp["message"];

                    if sDictJsonRespMsg != None:
                     
                        sDictJsonRespMsg = sDictJsonRespMsg.strip();
                     
                    if sDictJsonRespMsg == None or \
                       len(sDictJsonRespMsg) < 1:
                     
                        sDictJsonRespMsg = "";

                    self.sCxServerLastRespMsg2 = sDictJsonRespMsg;


            else:

                if self.bTraceFlag == True:

                    print "%s Http POST Response Data #(%d) contained NO line(s) - Warning!" % (self.sClassDisp, idCxWebApiPost);
                    print "";

                self.sCxServerLastResp  = None;
                self.asCxServerLastResp = None;

            return self.sCxServerLastResp;

        except Exception, inst:

            print "%s 'postHttpRequest2()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return None;

        return self.sCxServerLastResp;

    def postCxWebApiRequest(self, postdata={}, headers={}, idhttppostresp=0):

        self.handleCxAuthTokenProcessing();

        dictHttpPostData   = postdata;
        dictHttpHeaderData = headers;
        idCxWebApiPost     = idhttppostresp;

        try:

            if self.bCxBasicAuthUsedFlag == True and \
               self.cxHttpPasswordMgr    == None:

                self.sCxUserID           = self.sCxBasicAuthUserID;
                self.sCurrCxAuthToken = None;

            if self.sCxUserID != None:

                self.sCxUserID = self.sCxUserID.strip();

            if self.sCxUserID != None and \
               len(self.sCxUserID) > 0:

                dictHttpPostData["user"] = self.sCxUserID;

            if self.sCurrCxAuthToken != None:

                self.sCurrCxAuthToken = self.sCurrCxAuthToken.strip();

            if self.sCurrCxAuthToken != None and \
               len(self.sCurrCxAuthToken) > 0:

                dictHttpPostData["ltoken"] = self.sCurrCxAuthToken;
                dictHttpPostData["user"]   = self.sCurrCxAuthTokenUser;

            if self.bCxUserIsSuper == True:
            
                dictHttpPostData["sourceURL"]      = self.sCxSourceServerURL;
                dictHttpPostData["sourceAdmin"]    = self.sCxBasicAuthUserID;
                dictHttpPostData["sourcePassword"] = self.sCxBasicAuthPassword;

            sHttpPostURL = "%s://%s:%s/review/api" % (self.sCxServerHostProtocol, self.sCxServerHostName, self.sCxServerPortNumber);

            self.postHttpRequest2(sHttpPostURL, postdata=dictHttpPostData, headers=dictHttpHeaderData, idhttppostresp=idCxWebApiPost);

            if self.bTraceFlag == True:

                self.dumpLastCxWebApiResponse(idhttppostresp=idCxWebApiPost);

            if self.bUserActionPromptFlag == True:

                raw_input("Press <enter> to continue...");

        except Exception, inst:

            print "%s 'postCxWebApiRequest()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return None;

        return self.sCxServerLastResp;

    def dumpLastCxWebApiResponse(self, idhttppostresp=0):

        idHttpPostResp = idhttppostresp;

        if self.bTraceFlag == True:

            print "%s Last Http POST Response Data #(%d) was [%s]..." % (self.sClassDisp, idHttpPostResp, self.sCxServerLastResp);
            print "";

        if self.asCxServerLastResp != None and \
           len(self.asCxServerLastResp) > 0:

            if self.bTraceFlag == True:

                print "%s Http POST Response Data #(%d) split into (%d) line(s)..." % (self.sClassDisp, idHttpPostResp, len(self.asCxServerLastResp));
                print "";

            idJsonRespLine = 0;

            for dictJsonResp in self.asCxServerLastResp:

                idJsonRespLine += 1;

                if dictJsonResp != None and \
                   len(dictJsonResp) > 0:

                    if self.bTraceFlag == True:

                        print "%s 'dictJsonResp' #(%d).(%d) is [%s]..." % (self.sClassDisp, idHttpPostResp, idJsonRespLine, dictJsonResp);
                        print "";

                    print "'dictJsonResp' #(%d).(%d) break-down:" % (idHttpPostResp, idJsonRespLine);

                    for sJsonKey in dictJsonResp.keys():

                        print "#(%d).(%d) - KEY [%s] Value [%s]..." % (idHttpPostResp, idJsonRespLine, sJsonKey, dictJsonResp[sJsonKey]);

                    print "";

            if self.bTraceFlag == True:

                print "";

        else:

            print "%s Http POST Response Data #(%d) contained NO line(s) - Warning!" % (self.sClassDisp, idHttpPostResp);
            print "";

        return;

    def mainUnitTest(self):

        try:

            print "%s Executing the CxRestAPICalls #1 'UnitTest'..." % (self.sClassDisp);
            print "";

            if self.sCxServerURL != None:

                self.sCxServerURL = self.sCxServerURL.strip();

            if self.sCxServerURL == None or \
               len(self.sCxServerURL) < 1:

            #   self.setCxServerURL(cxserverurl="http://darylcoxe36c:8080/CVS");
            #   self.setCxServerURL(cxserverurl="http://192.168.1.134:8080/CVS");
                self.setCxServerURL(cxserverurl="http://192.168.1.162:8080/TestBugTracking");

            if self.bTraceFlag == True:

                self.dump_fields();

                print "";

            dictHttpPostData           = collections.defaultdict();
            dictHttpPostData["action"] = "projects";

            idUnitTest = 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "builds";
            dictHttpPostData["project"] = self.sCxServerProjectName;

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "views";
            dictHttpPostData["project"] = self.sCxServerProjectName;

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "modules";
            dictHttpPostData["project"] = self.sCxServerProjectName;

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "views";
            dictHttpPostData["project"] = "XYZ_123";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "search";
            dictHttpPostData["project"] = self.sCxServerProjectName;
            dictHttpPostData["view"]    = "*default*";
            dictHttpPostData["query"]   = "status:+Analyze severity:1";
            dictHttpPostData["limit"]   = "5";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "search";
            dictHttpPostData["project"] = self.sCxServerProjectName;
            dictHttpPostData["query"]   = "code:MLK";
            dictHttpPostData["limit"]   = "10";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            dictHttpPostData            = collections.defaultdict();
            dictHttpPostData["action"]  = "search";
            dictHttpPostData["project"] = self.sCxServerProjectName;
            dictHttpPostData["query"]   = "'MLK'";
            dictHttpPostData["limit"]   = "15";

            idUnitTest += 1;

            print " ===================================================================== ";
            print "";
            print "%s Http POST Data #%d [%s]..." % (self.sClassDisp, idUnitTest, dictHttpPostData);
            print "";

            sPostResp = self.postCxWebApiRequest(postdata=dictHttpPostData, idhttppostresp=idUnitTest);

            print "%s Executed the CxRestAPICalls #1 'UnitTest'..." % (self.sClassDisp);
            print "";

        except Exception, inst:

            print "%s 'mainUnitTest()' - exception occured..." % (self.sClassDisp);
            print type(inst);
            print inst;

            excType, excValue, excTraceback = sys.exc_info();
            asTracebackLines                = traceback.format_exception(excType, excValue, excTraceback);

            print "- - - ";
            print '\n'.join(asTracebackLines);
            print "- - - ";

            return False;

        return True;

