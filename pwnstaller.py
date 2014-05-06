#!/usr/bin/python

"""
Pwnstaller v1.0
A generator for obfuscated Pyinstaller runw.exe loaders.

Based on previous work by Giovanni Bajo.
Adapted from https://github.com/pyinstaller/pyinstaller.

See README.md for more information.

By: @harmj0y

"""

import random, string, os, sys, subprocess, argparse

VERSION = "1.0"


def checkDeps():
    """
    Tries to check if the necessary dependencies are installed
    """
    try:
        with open(os.devnull, "w") as f:
            subprocess.call(["which","i686-w64-mingw32-gcc"], stdout=f)
    except:
        print "\n[!] mingw is not installed, run setup.sh"
        sys.exit()

    try:
        with open(os.devnull, "w") as f:
            subprocess.call(["which","wine"], stdout=f)
    except:
        print "\n[!] wine is not installed, run setup.sh"
        sys.exit()
    

def randomString(length=-1):
    """
    Returns a random string of "length" characters.
    If no length is specified, resulting string is in between 6 and 15 characters.
    """
    if length == -1:
        length = random.randrange(6,16)
    random_string = ''.join(random.choice(string.ascii_letters) for x in range(length))
    return random_string


def generate_utils(): 
    """
    Generates an obfuscated version of Pwnstaller's utils.c
    """
    # these two HAVE to go first
    allincludes = "#define _WIN32_WINNT 0x0500\n"
    allincludes += "#include \"utils.h\"\n"

    # includes that are actually needed
    includes = ["#include <windows.h>", "#include <commctrl.h>", "#include <signal.h>", "#include <memory.h>", "#include <string.h>"]

    # "fake"/unnessary includes taken from /usr/i686-w64-mingw32/include/*.h
    # hand stripped list to ensure it should compile
    fake_includes = ['#include <accctrl.h>', '#include <aclapi.h>', '#include <aclui.h>', '#include <activeds.h>', '#include <activscp.h>', '#include <adc.h>', '#include <adhoc.h>', '#include <admex.h>', '#include <adptif.h>', '#include <adtgen.h>', '#include <advpub.h>', '#include <af_irda.h>', '#include <afxres.h>', '#include <agtctl.h>', '#include <agterr.h>', '#include <agtsvr.h>', '#include <amaudio.h>', '#include <aqadmtyp.h>', '#include <asptlb.h>', '#include <assert.h>', '#include <atacct.h>', '#include <atalkwsh.h>', '#include <atsmedia.h>', '#include <audevcod.h>', '#include <audioapotypes.h>', '#include <audioclient.h>', '#include <audioengineendpoint.h>', '#include <audiopolicy.h>', '#include <audiosessiontypes.h>', '#include <austream.h>', '#include <authif.h>', '#include <authz.h>', '#include <avrt.h>', '#include <azroles.h>', '#include <basetsd.h>', '#include <basetyps.h>', '#include <batclass.h>', '#include <bcrypt.h>', '#include <bh.h>', '#include <bidispl.h>', '#include <bits1_5.h>', '#include <bits2_0.h>', '#include <bitscfg.h>', '#include <bits.h>', '#include <bitsmsg.h>', '#include <blberr.h>', '#include <bugcodes.h>', '#include <callobj.h>', '#include <cardmod.h>', '#include <casetup.h>', '#include <cchannel.h>', '#include <cderr.h>', '#include <celib.h>', '#include <certadm.h>', '#include <certbase.h>', '#include <certbcli.h>', '#include <certcli.h>', '#include <certenc.h>', '#include <certenroll.h>', '#include <certexit.h>', '#include <certif.h>', '#include <certmod.h>', '#include <certpol.h>', '#include <certreqd.h>', '#include <certsrv.h>', '#include <certview.h>', '#include <cfg.h>', '#include <cfgmgr32.h>', '#include <cguid.h>', '#include <chanmgr.h>', '#include <cierror.h>', '#include <clfs.h>', '#include <clfsmgmt.h>', '#include <clfsmgmtw32.h>', '#include <clfsw32.h>', '#include <cluadmex.h>', '#include <clusapi.h>', '#include <cluscfgguids.h>', '#include <cluscfgserver.h>', '#include <cluscfgwizard.h>', '#include <cmdtree.h>', '#include <cmnquery.h>', '#include <codecapi.h>', '#include <colordlg.h>', '#include <conio.h>', '#include <control.h>', '#include <corerror.h>', '#include <correg.h>', '#include <cplext.h>', '#include <cpl.h>', '#include <crtdbg.h>', '#include <crtdefs.h>', '#include <cryptuiapi.h>', '#include <cryptxml.h>', '#include <cscapi.h>', '#include <cscobj.h>', '#include <ctxtcall.h>', '#include <ctype.h>', '#include <custcntl.h>', '#include <d2dbasetypes.h>', '#include <d2derr.h>', '#include <datapath.h>', '#include <davclnt.h>', '#include <dbt.h>', '#include <dciddi.h>', '#include <dciman.h>', '#include <dcommon.h>', '#include <delayimp.h>', '#include <devguid.h>', '#include <devicetopology.h>', '#include <devioctl.h>', '#include <devpkey.h>', '#include <devpropdef.h>', '#include <digitalv.h>', '#include <dimm.h>', '#include <direct.h>', '#include <dirent.h>', '#include <dir.h>', '#include <diskguid.h>', '#include <dispdib.h>', '#include <dispex.h>', '#include <dlcapi.h>', '#include <dlgs.h>', '#include <dls1.h>', '#include <dls2.h>', '#include <docobj.h>', '#include <domdid.h>', '#include <dos.h>', '#include <downloadmgr.h>', '#include <driverspecs.h>', '#include <dtchelp.h>', '#include <dwmapi.h>', '#include <eapauthenticatoractiondefine.h>', '#include <eapauthenticatortypes.h>', '#include <eaphosterror.h>', '#include <eaphostpeerconfigapis.h>', '#include <eaphostpeertypes.h>', '#include <eapmethodauthenticatorapis.h>', '#include <eapmethodpeerapis.h>', '#include <eapmethodtypes.h>', '#include <eappapis.h>', '#include <eaptypes.h>', '#include <edevdefs.h>', '#include <emptyvc.h>', '#include <endpointvolume.h>', '#include <errno.h>', '#include <error.h>', '#include <errorrep.h>', '#include <errors.h>', '#include <evcode.h>', '#include <evcoll.h>', '#include <eventsys.h>', '#include <evr9.h>', '#include <evr.h>', '#include <exchform.h>', '#include <excpt.h>', '#include <exdisp.h>', '#include <exdispid.h>', '#include <fci.h>', '#include <fcntl.h>', '#include <fdi.h>', '#include <fenv.h>', '#include <fileextd.h>', '#include <filter.h>', '#include <filterr.h>', '#include <float.h>', '#include <fltdefs.h>', '#include <fpieee.h>', '#include <fsrmenums.h>', '#include <fsrm.h>', '#include <fsrmpipeline.h>', '#include <fsrmquota.h>', '#include <fsrmreports.h>', '#include <fsrmscreen.h>', '#include <ftsiface.h>', '#include <functiondiscoveryapi.h>', '#include <functiondiscoverycategories.h>', '#include <functiondiscoveryconstraints.h>', '#include <functiondiscoverykeys.h>', '#include <functiondiscoverynotification.h>', '#include <fusion.h>', '#include <fwpmtypes.h>', '#include <fwpmu.h>', '#include <fwptypes.h>', '#include <gb18030.h>', '#include <gdiplus.h>', '#include <getopt.h>', '#include <gpmgmt.h>', '#include <guiddef.h>', '#include <hidpi.h>', '#include <hidsdi.h>', '#include <hidusage.h>', '#include <hlguids.h>', '#include <hliface.h>', '#include <hlink.h>', '#include <hostinfo.h>', '#include <htiface.h>', '#include <htiframe.h>', '#include <htmlguid.h>', '#include <htmlhelp.h>', '#include <ia64reg.h>', '#include <iaccess.h>', '#include <iadmext.h>', '#include <iadmw.h>', '#include <iads.h>', '#include <icftypes.h>', '#include <icm.h>', '#include <i_cryptasn1tls.h>', '#include <identitycommon.h>', '#include <identitystore.h>', '#include <idf.h>', '#include <idispids.h>', '#include <iedial.h>', '#include <ieverp.h>', '#include <ifdef.h>', '#include <ime.h>', '#include <imessage.h>', '#include <imm.h>', '#include <in6addr.h>', '#include <inaddr.h>', '#include <indexsrv.h>', '#include <inetreg.h>', '#include <inetsdk.h>', '#include <initguid.h>', '#include <initoid.h>', '#include <inputscope.h>', '#include <intrin.h>', '#include <intshcut.h>', '#include <inttypes.h>', '#include <io.h>', '#include <iscsidsc.h>', '#include <isguids.h>', '#include <isysmon.h>', '#include <iwamreg.h>', '#include <kxia64.h>', '#include <libgen.h>', '#include <libmangle.h>', '#include <limits.h>', '#include <loadperf.h>', '#include <locale.h>', '#include <locationapi.h>', '#include <lpmapi.h>', '#include <lzexpand.h>', '#include <madcapcl.h>', '#include <malloc.h>', '#include <math.h>', '#include <mbctype.h>', '#include <mbstring.h>', '#include <mciavi.h>', '#include <mcx.h>', '#include <mediaerr.h>', '#include <mediaobj.h>', '#include <mem.h>', '#include <memory.h>', '#include <mergemod.h>', '#include <midles.h>', '#include <mimedisp.h>', '#include <mimeinfo.h>', '#include <minmax.h>', '#include <mlang.h>', '#include <mobsync.h>', '#include <mprerror.h>', '#include <mq.h>', '#include <mqmail.h>', '#include <mtsadmin.h>', '#include <mtsevents.h>', '#include <mtsgrp.h>', '#include <mtxadmin.h>', '#include <mtxattr.h>', '#include <mtxdm.h>', '#include <mtx.h>', '#include <muiload.h>', '#include <multimon.h>', '#include <multinfo.h>', '#include <mxdc.h>', '#include <napenforcementclient.h>', '#include <naperror.h>', '#include <napmicrosoftvendorids.h>', '#include <napprotocol.h>', '#include <naptypes.h>', '#include <naputil.h>', '#include <nb30.h>', '#include <ncrypt.h>', '#include <ndattrib.h>', '#include <ndfapi.h>', '#include <ndhelper.h>', '#include <ndr64types.h>', '#include <ndrtypes.h>', '#include <netcon.h>', '#include <neterr.h>', '#include <netevent.h>', '#include <netioapi.h>', '#include <netlistmgr.h>', '#include <netprov.h>', '#include <nettypes.h>', '#include <newapis.h>', '#include <newdev.h>', '#include <new.h>', '#include <nldef.h>', '#include <npapi.h>', '#include <nsemail.h>', '#include <nspapi.h>', '#include <oaidl.h>', '#include <objbase.h>', '#include <objectarray.h>', '#include <objerror.h>', '#include <objidl.h>', '#include <objsafe.h>', '#include <objsel.h>', '#include <ocidl.h>', '#include <ocmm.h>', '#include <opmapi.h>', '#include <optary.h>', '#include <p2p.h>', '#include <patchapi.h>', '#include <patchwiz.h>', '#include <pbt.h>', '#include <pchannel.h>', '#include <pcrt32.h>', '#include <pdh.h>', '#include <pdhmsg.h>', '#include <penwin.h>', '#include <perflib.h>', '#include <perhist.h>', '#include <persist.h>', '#include <pgobootrun.h>', '#include <pla.h>', '#include <polarity.h>', '#include <poppack.h>', '#include <portabledeviceconnectapi.h>', '#include <process.h>', '#include <profile.h>', '#include <profinfo.h>', '#include <propidl.h>', '#include <propkeydef.h>', '#include <propkey.h>', '#include <propsys.h>', '#include <prsht.h>', '#include <psapi.h>', '#include <pstore.h>', '#include <ratings.h>', '#include <rdpencomapi.h>', '#include <reason.h>', '#include <reconcil.h>', '#include <regstr.h>', '#include <restartmanager.h>', '#include <richedit.h>', '#include <richole.h>', '#include <rkeysvcc.h>', '#include <rnderr.h>', '#include <rpcasync.h>', '#include <rpcdce.h>', '#include <rpcdcep.h>', '#include <rpc.h>', '#include <rpcndr.h>', '#include <rpcnsi.h>', '#include <rpcnsip.h>', '#include <rpcnterr.h>', '#include <rpcproxy.h>', '#include <rpcssl.h>', '#include <rrascfg.h>', '#include <rtcapi.h>', '#include <rtccore.h>', '#include <rtcerr.h>', '#include <rtinfo.h>', '#include <rtm.h>', '#include <rtmv2.h>', '#include <rtutils.h>', '#include <scesvc.h>', '#include <schannel.h>', '#include <schedule.h>', '#include <schemadef.h>', '#include <schnlsp.h>', '#include <scode.h>', '#include <scrnsave.h>', '#include <scrptids.h>', '#include <sddl.h>', '#include <sdkddkver.h>', '#include <sdoias.h>', '#include <sdpblb.h>', '#include <sdperr.h>', '#include <search.h>', '#include <sehmap.h>', '#include <sensapi.h>', '#include <sensevts.h>', '#include <sens.h>', '#include <servprov.h>', '#include <setjmpex.h>', '#include <setjmp.h>', '#include <setupapi.h>', '#include <sfc.h>', '#include <shappmgr.h>', '#include <share.h>', '#include <shdeprecated.h>', '#include <shdispid.h>', '#include <shellapi.h>', '#include <shfolder.h>', '#include <shobjidl.h>', '#include <shtypes.h>', '#include <signal.h>', '#include <simpdata.h>', '#include <simpdc.h>', '#include <sipbase.h>', '#include <sisbkup.h>', '#include <slerror.h>', '#include <slpublic.h>', '#include <smpab.h>', '#include <smpms.h>', '#include <smpxp.h>', '#include <smx.h>', '#include <snmp.h>', '#include <softpub.h>', '#include <specstrings.h>', '#include <srrestoreptapi.h>', '#include <srv.h>', '#include <stdarg.h>', '#include <stddef.h>', '#include <stdexcpt.h>', '#include <stdint.h>', '#include <stdio.h>', '#include <stdlib.h>', '#include <stierr.h>', '#include <sti.h>', '#include <stireg.h>', '#include <stllock.h>', '#include <storduid.h>', '#include <storprop.h>', '#include <stralign.h>', '#include <string.h>', '#include <strings.h>', '#include <structuredquerycondition.h>', '#include <subsmgr.h>', '#include <svcguid.h>', '#include <syslimits.h>', '#include <tabflicks.h>', '#include <taskschd.h>', '#include <tbs.h>', '#include <tcerror.h>', '#include <tcguid.h>', '#include <tchar.h>', '#include <tcpestats.h>', '#include <tcpmib.h>', '#include <tdh.h>', '#include <tlhelp32.h>', '#include <tlogstg.h>', '#include <tmschema.h>', '#include <tom.h>', '#include <tpcshrd.h>', '#include <transact.h>', '#include <triedcid.h>', '#include <triediid.h>', '#include <triedit.h>', '#include <tspi.h>', '#include <tssbx.h>', '#include <tvout.h>', '#include <txcoord.h>', '#include <txctx.h>', '#include <txdtc.h>', '#include <txfw32.h>', '#include <uastrfnc.h>', '#include <udpmib.h>', '#include <umx.h>', '#include <unistd.h>', '#include <urlhist.h>', '#include <urlmon.h>', '#include <userenv.h>', '#include <usp10.h>', '#include <uuids.h>', '#include <uxtheme.h>', '#include <vcr.h>', '#include <vdmdbg.h>', '#include <virtdisk.h>', '#include <w32api.h>', '#include <wbemads.h>', '#include <wbemcli.h>', '#include <wbemdisp.h>', '#include <wbemidl.h>', '#include <wbemprov.h>', '#include <wbemtran.h>', '#include <wchar.h>', '#include <wcmconfig.h>', '#include <wcsplugin.h>', '#include <wct.h>', '#include <wctype.h>', '#include <werapi.h>', '#include <wfext.h>', '#include <winable.h>', '#include <winbase.h>', '#include <winber.h>', '#include <wincodec.h>', '#include <wincon.h>', '#include <wincred.h>', '#include <wincrypt.h>', '#include <windef.h>', '#include <windns.h>', '#include <windot11.h>', '#include <windows.h>', '#include <winefs.h>', '#include <winerror.h>', '#include <winevt.h>', '#include <wingdi.h>', '#include <winldap.h>', '#include <winnetwk.h>', '#include <winnls32.h>', '#include <winnls.h>', '#include <winnt.h>', '#include <winnt.rh>', '#include <winperf.h>', '#include <winreg.h>', '#include <winresrc.h>', '#include <winsafer.h>', '#include <winsatcominterfacei.h>', '#include <winscard.h>', '#include <winsmcrd.h>', '#include <winsnmp.h>', '#include <winsplp.h>', '#include <winspool.h>', '#include <winsvc.h>', '#include <winsxs.h>', '#include <winsync.h>', '#include <winuser.h>', '#include <winuser.rh>', '#include <winver.h>', '#include <winwlx.h>', '#include <wlanapi.h>', '#include <wlantypes.h>','#include <wmistr.h>', '#include <wmiutils.h>', '#include <wownt16.h>', '#include <wownt32.h>', '#include <wpapi.h>', '#include <wpapimsg.h>', '#include <wpcapi.h>', '#include <wpcevent.h>', '#include <wpcrsmsg.h>', '#include <wpftpmsg.h>', '#include <wppstmsg.h>', '#include <wpspihlp.h>', '#include <wptypes.h>', '#include <wpwizmsg.h>', '#include <wshisotp.h>', '#include <wsipv6ok.h>', '#include <wsipx.h>', '#include <wsnetbs.h>', '#include <wsnwlink.h>', '#include <wsrm.h>', '#include <wsvns.h>', '#include <wtsapi32.h>', '#include <wtypes.h>', '#include <xa.h>', '#include <xcmcext.h>', '#include <xcmc.h>', '#include <xcmcmsx2.h>', '#include <xcmcmsxt.h>', '#include <xenroll.h>', '#include <xinput.h>', '#include <xlocinfo.h>', '#include <xmath.h>', '#include <xmldomdid.h>', '#include <xmldsodid.h>', '#include <xmllite.h>', '#include <xmltrnsf.h>', '#include <xolehlp.h>', '#include <ymath.h>', '#include <yvals.h>', '#include <zmouse.h>']

    random.shuffle(fake_includes)
    # include a random number of the randomized "fake" includes, between 10-30
    for x in xrange(0, random.randint(10,30)):
        includes.append(fake_includes[x])

    # shuffle up all the includes
    random.shuffle(includes)

    # join all the includes and throw them at the top of the file
    allincludes += "\n".join(includes) + "\n"

    # basename()
    pathName = randomString()
    basenameName = randomString()
    code = "char* basename (char *%s) {\n" % (pathName)
    code += "char *%s = strrchr (%s, '\\\\');\n" %(basenameName, pathName)
    code += "if (!%s) %s = strrchr (%s, '/');\n" % (basenameName, basenameName, pathName)
    code += "return %s ? ++%s : (char*)%s;}\n" % (basenameName, basenameName, pathName)


    # IsXPOrLater()
    osviName = randomString()
    code += "int IsXPOrLater(void) {\n"
    code += "OSVERSIONINFO %s;\n" %(osviName)
    code += "ZeroMemory(&%s, sizeof(OSVERSIONINFO));\n" %(osviName)
    code += "%s.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);\n" %(osviName)
    code += "GetVersionEx(&%s);\n" %(osviName)
    code += "return ((%s.dwMajorVersion > 5) || ((%s.dwMajorVersion == 5) && (%s.dwMinorVersion >= 1)));}\n" %(osviName,osviName,osviName)


    # CreateActContext()
    code += "int CreateActContext(char *%s, char *%s) { return 0; }\n" %(randomString(),randomString())


    # ReleaseActContext()
    k32Name = randomString()
    ReleaseActCtxName = randomString()
    DeactivateActCtxName = randomString()
    code += "void ReleaseActContext(void) {\n"
    code += "void (WINAPI *%s)(HANDLE);\n" %(ReleaseActCtxName)
    code += "BOOL (WINAPI *%s)(DWORD dwFlags, ULONG_PTR ulCookie);\n" %(DeactivateActCtxName)
    code += "HANDLE %s;\n" %(k32Name)
    code += "if (!IsXPOrLater()) return;\n"
    # TODO: obfuscate this string?
    code += "%s = LoadLibrary(\"kernel32\");\n" %(k32Name)
    code += "%s = (void*)GetProcAddress(%s, \"%s\");\n" %(ReleaseActCtxName, k32Name, ReleaseActCtxName)
    code += "%s = (void*)GetProcAddress(%s, \"%s\");\n" %(DeactivateActCtxName, k32Name, DeactivateActCtxName)
    code += "if (!%s || !%s) { return; }}\n" %(ReleaseActCtxName, DeactivateActCtxName)
    

    # init_launcher()
    code += "void init_launcher(void) { InitCommonControls(); }\n"


    # get_thisfile()
    thisfileName = randomString()
    code += "int get_thisfile(char *%s, const char *%s) {\n" %(thisfileName, randomString())
    code += "if (!GetModuleFileNameA(NULL, %s, _MAX_PATH)) { return -1; } return 0; }\n" %(thisfileName)


    # get_thisfilew()
    thisfilewName = randomString()
    code +=  "int get_thisfilew(LPWSTR %s) {\n" %(thisfilewName)
    code +=  "if (!GetModuleFileNameW(NULL, %s, _MAX_PATH)) { return -1; } return 0; }\n" %(thisfilewName)


    # get_homepath()
    homepathName = randomString()
    thisfileName = randomString()
    pName = randomString()
    code +=  "void get_homepath(char *%s, const char *%s) {\n" %(homepathName, thisfileName)
    code +=  "char *%s = NULL;\n" %(pName)
    code +=  "strcpy(%s, %s);\n" %(homepathName, thisfileName)
    code +=  "for (%s = %s + strlen(%s); *%s != '\\\\' && %s >= %s + 2; --%s);\n" %(pName, homepathName, homepathName, pName, pName, homepathName, pName)
    code +=  "*++%s = '\\0'; }\n" %(pName)


    # get_archivefile()
    archivefileName = randomString()
    thisfileName = randomString()
    code +=  "void get_archivefile(char *%s, const char *%s){\n" %(archivefileName, thisfileName)
    code +=  "strcpy(%s, %s);\n" %(archivefileName, thisfileName)
    # TODO: obfuscate this string?
    code +=  "strcpy(%s + strlen(%s) - 3, \"pkg\");}\n" %(archivefileName, archivefileName)


    # set_environment()
    code +=  " int set_environment(const ARCHIVE_STATUS *%s) { return 0; }\n" %(randomString())


    # spawn()
    thisfileName = randomString()
    saName = randomString()
    siName = randomString()
    piName = randomString()
    rcName = randomString()

    code += "int spawn(LPWSTR %s) {\n" %(thisfileName)
    code += "SECURITY_ATTRIBUTES %s;\n" %(saName)
    code += "STARTUPINFOW %s;\n" %(siName)
    code += "PROCESS_INFORMATION %s;\n" %(piName)
    code += "int %s = 0;\n" %(rcName)

    # a set of lines whose order can be randomized safely
    lineSet1 = ["signal(SIGABRT, SIG_IGN);", 
                "signal(SIGINT, SIG_IGN);" , 
                "signal(SIGTERM, SIG_IGN);", 
                "signal(SIGBREAK, SIG_IGN);", 
                "%s.nLength = sizeof(%s);" %(saName,saName), 
                "%s.lpSecurityDescriptor = NULL;" %(saName), 
                "%s.bInheritHandle = TRUE;" %(saName)]
    random.shuffle(lineSet1)
    code += "\n".join(lineSet1) + "\n"

    code += "GetStartupInfoW(&%s);\n" %(siName)

    # another set of lines whose order can be randomized safely
    lineSet2 = [
        "%s.lpReserved = NULL;" %(siName), 
        "%s.lpDesktop = NULL;" %(siName), 
        "%s.lpTitle = NULL;" %(siName), 
        "%s.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW;" %(siName), 
        "%s.wShowWindow = SW_NORMAL;" %(siName), 
        "%s.hStdInput = (void*)_get_osfhandle(fileno(stdin));" %(siName), 
        "%s.hStdOutput = (void*)_get_osfhandle(fileno(stdout));" %(siName), 
        "%s.hStdError = (void*)_get_osfhandle(fileno(stderr));" %(siName)]
    random.shuffle(lineSet2)
    code += "\n".join(lineSet2) + "\n"

    code += "if (CreateProcessW( %s, GetCommandLineW(), &%s, NULL, TRUE, 0,  NULL, NULL, &%s, &%s)) {\n" %(thisfileName, saName, siName, piName )
    code += "WaitForSingleObject(%s.hProcess, INFINITE);\n" %(piName)
    code += "GetExitCodeProcess(%s.hProcess, (unsigned long *)&%s);\n" %(piName, rcName)
    code += "} else { %s = -1; }\n" %(rcName)
    code += "return %s; }\n" %(rcName)


    return (allincludes, code)


def generate_utils_h(methodSubs):
    """
    Generate an obfuscated version of Pwnstaller's utils.h
    """
    code = "#include \"launch.h\"\n"
    code += "void init_launcher(void);\n"
    code += "int get_thisfile(char *%s, const char *%s);\n" %(randomString(), randomString())
    code += "int CreateActContext(char *%s, char *%s);\n" %(randomString(), randomString())
    code += "void ReleaseActContext(void);\n"
    code += "int get_thisfilew(LPWSTR %s);\n" %(randomString())
    code += "void get_homepath(char *%s, const char *%s);\n" %(randomString(), randomString())
    code += "void get_archivefile(char *%s, const char *%s);\n" %(randomString(),randomString())
    code += "int set_environment(const ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "int spawn(LPWSTR %s);\n" %(randomString())

    
    # replace all method names with their randomized choices from the passed list
    for m in methodSubs: code = code.replace(m[0], m[1])

    return code


def generate_main():
    """
    Generate an obfuscated version of Pwnstaller's main.c
    """

    allincludes = "#include \"utils.h\"\n"

    status_listName = randomString()
    thisfileName = randomString()
    thisfilewName = randomString()
    homepathName = randomString()
    archivefileName = randomString()
    extractionpathName = randomString()
    rcName = randomString()

    # same obsfuscation as used in Veil-Evasion's c/meterpreter/* payloads

    # max length string for obfuscation
    global_max_string_length = 10000
    max_string_length = random.randint(100,global_max_string_length)
    max_num_strings = 10000
    
    # TODO: add in more string processing functions
    randName1 = randomString() # reverse()
    randName2 = randomString() # doubles characters
    stringModFunctions = [  (randName1, "char* %s(const char *t) { int length= strlen(t); int i; char* t2 = (char*)malloc((length+1) * sizeof(char)); for(i=0;i<length;i++) { t2[(length-1)-i]=t[i]; } t2[length] = '\\0'; return t2; }" %(randName1)), 
                            (randName2, "char* %s(char* s){ char *result =  malloc(strlen(s)*2+1); int i; for (i=0; i<strlen(s)*2+1; i++){ result[i] = s[i/2]; result[i+1]=s[i/2];} result[i] = '\\0'; return result; }" %(randName2))
                         ]
                        
    random.shuffle(stringModFunctions)

    # obfuscation "logical nop" string generation functions
    randString1 = randomString(50)
    randName1 = randomString()
    randVar1 = randomString()
    randName2 = randomString()
    randVar2 = randomString()
    randVar3 = randomString()
    randName3 = randomString()
    randVar4 = randomString()
    randVar5 = randomString()

    # obfuscation char arrays
    char_array_name_1 = randomString()
    number_of_strings_1 = random.randint(1,max_num_strings)
    char_array_name_2 = randomString()
    number_of_strings_2 = random.randint(1,max_num_strings)
    char_array_name_3 = randomString()
    number_of_strings_3 = random.randint(1,max_num_strings)

    # more obfuscation
    stringGenFunctions = [  (randName1, "char* %s(){ char *%s = %s(\"%s\"); return strstr( %s, \"%s\" );}" %(randName1, randVar1, stringModFunctions[0][0], randString1, randVar1, randString1[len(randString1)/2])),
                            (randName2, "char* %s(){ char %s[%s], %s[%s/2]; strcpy(%s,\"%s\"); strcpy(%s,\"%s\"); return %s(strcat( %s, %s)); }" % (randName2, randVar2, max_string_length, randVar3, max_string_length, randVar2, randomString(50), randVar3, randomString(50), stringModFunctions[1][0], randVar2, randVar3)),
                            (randName3, "char* %s() { char %s[%s] = \"%s\"; char *%s = strupr(%s); return strlwr(%s); }" % (randName3, randVar4, max_string_length, randomString(50), randVar5, randVar4, randVar5))
                         ]
    random.shuffle(stringGenFunctions)

    code = stringModFunctions[0][1] + "\n"
    code += stringModFunctions[1][1] + "\n"

    # string "logical nop" functions
    code += stringGenFunctions[0][1] + "\n"
    code += stringGenFunctions[1][1] + "\n"
    code += stringGenFunctions[2][1] + "\n"

    code += "int APIENTRY WinMain( HINSTANCE %s, HINSTANCE %s, LPSTR %s, int %s ) {\n" % (randomString(), randomString(), randomString(), randomString(), )
    
    # all of these initialization ran be randomized in order
    # TODO: obfuscate the MEIPASS string?
    initializations = [ "ARCHIVE_STATUS *%s[20];" %(status_listName),
                        "char %s[_MAX_PATH];" %(thisfileName),
                        "WCHAR %s[_MAX_PATH + 1];" %(thisfilewName),
                        "char %s[_MAX_PATH];" %(homepathName),
                        "char %s[_MAX_PATH + 5];" %(archivefileName),
                        "char MEIPASS2[_MAX_PATH + 11] = \"_MEIPASS2=\";",
                        "int %s = 0;" %(rcName),
                        "char *%s = NULL;" %(extractionpathName),
                        "int argc = __argc;",
                        "char* %s[%s];" % (char_array_name_1, number_of_strings_1),
                        "char* %s[%s];" % (char_array_name_2, number_of_strings_2),
                        "char* %s[%s];" % (char_array_name_3, number_of_strings_3),
                        "char **argv = __argv;",
                        "int i = 0;"]
    random.shuffle(initializations)
    code += "\n".join(initializations) + "\n"

    # main body of WinMain()
    code += "memset(&%s, 0, 20 * sizeof(ARCHIVE_STATUS *));\n" %(status_listName)

    # malloc our first string obfuscation array
    code += "for (i = 0;  i < %s;  ++i) %s[i] = malloc (%s);" %(number_of_strings_1, char_array_name_1, random.randint(max_string_length,global_max_string_length)) 

    code += "if ((%s[SELF] = (ARCHIVE_STATUS *) calloc(1, sizeof(ARCHIVE_STATUS))) == NULL){ return -1; }\n" %(status_listName)
    code += "get_thisfile(%s, argv[0]);\n" %(thisfileName)
    code += "get_thisfilew(%s);\n" %(thisfilewName)

    # malloc our second string obfuscation array
    code += "for (i = 0;  i < %s;  ++i) %s[i] = malloc (%s);" %(number_of_strings_2, char_array_name_2, random.randint(max_string_length,global_max_string_length))
    
    code += "get_archivefile(%s, %s);\n" %(archivefileName, thisfileName)
    code += "get_homepath(%s, %s);\n" %(homepathName, thisfileName)

    # malloc our third string obfuscation array
    code += "for (i = 0;  i < %s;  ++i) %s[i] = malloc (%s);" %(number_of_strings_3, char_array_name_3, random.randint(max_string_length,global_max_string_length))
        
    # TODO: obfuscate this string?
    code += "%s = getenv( \"_MEIPASS2\" );\n" %(extractionpathName)
    code += "if (%s && *%s == 0) { %s = NULL; }\n" %(extractionpathName,extractionpathName,extractionpathName)

    code += "if (init(%s[SELF], %s, &%s[strlen(%s)])) {\n" %(status_listName, homepathName, thisfileName, homepathName)
    code += "    if (init(%s[SELF], %s, &%s[strlen(%s)])) { return -1; } }\n" %(status_listName, homepathName, archivefileName, homepathName)
    code += "if (!%s && !needToExtractBinaries(%s)) {\n" %(extractionpathName,status_listName)
    code += "    %s = %s;\n" %(extractionpathName,homepathName)
    code += "    strcat(MEIPASS2, %s);\n" %(homepathName)
    code += "    putenv(MEIPASS2); }\n"

    code += "if (%s) {\n" %(extractionpathName)
    code += "    if (strcmp(%s, %s) != 0) {\n" %(homepathName, extractionpathName)
    code += "        strcpy(%s[SELF]->temppath, %s);\n" %(status_listName, extractionpathName)
    code += "        strcpy(%s[SELF]->temppathraw, %s); }\n" %(status_listName, extractionpathName)
    code += "    CreateActContext(%s, %s);\n" %(extractionpathName, thisfileName)
    
    # first string obfuscation method
    code += "for (i=0; i<%s; ++i){strcpy(%s[i], %s());}" %(number_of_strings_1, char_array_name_1, stringGenFunctions[0][0])

    code += "    %s = doIt(%s[SELF], argc, argv);\n" %(rcName, status_listName)
    code += "    ReleaseActContext();\n"
    code += "    finalizePython();\n"
    code += "} else { \n"

    code += "    if (extractBinaries(%s)) { return -1; }\n" %(status_listName)
    
    # second string obfuscation method
    code += "for (i=0; i<%s; ++i){strcpy(%s[i], %s());}" %(number_of_strings_2, char_array_name_2, stringGenFunctions[1][0])

    code += "    strcat(MEIPASS2, %s[SELF]->temppath[0] != 0 ? %s[SELF]->temppath : %s);\n" %(status_listName, status_listName, homepathName)
    code += "    putenv(MEIPASS2);\n"
    code += "    if (set_environment(%s[SELF]) == -1) return -1;\n" %(status_listName)
    code += "    %s = spawn(%s);\n" %(rcName, thisfilewName)
    code += "    if (%s[SELF]->temppath[0] != 0) clear(%s[SELF]->temppath);\n" %(status_listName,status_listName)
    code += "    for (i = SELF; %s[i] != NULL; i++) { free(%s[i]); }}\n" %(status_listName, status_listName)
    
    # third string obfuscation method
    code += "for (i=0; i<%s; ++i){strcpy(%s[i], %s());}" %(number_of_strings_3, char_array_name_3, stringGenFunctions[2][0])
        
    code += "return %s; }\n" %(rcName)

    return (allincludes, code)


def generate_launch():

    """
    Generate obfuscated versions of Pwnstaller's launch.c and launch.h

    This is the tough one- ~1600 original lines, trimmed down to a more 
    manageable and necessary ~500.
    """
    allincludes = ""

    # I *think* these imports can be randomized...
    imports = [ "#include <stdio.h>", "#include <windows.h>", "#include <direct.h>", "#include <process.h>",
                "#include <io.h>", "#define unsetenv(x) _putenv(x \"=\")", "#include <sys/types.h>", "#include <sys/stat.h>",
                "#include \"launch.h\"", "#include <string.h>", "#include \"zlib.h\"", "#define snprintf _snprintf", "#define vsnprintf _vsnprintf"]
    random.shuffle(imports)
    allincludes = "\n".join(imports) + "\n"

    # Python Entry point declarations, these can definitely be shuffled
    # removed:  Py_OptimizeFlag, Py_VerboseFlag, PySys_SetArgv, PyFile_FromString, PyObject_CallObject, PySys_AddWarnOption
    #           PyEval_InitThreads, PyEval_AcquireThread, PyEval_ReleaseThread, PyThreadState_Swap, Py_NewInterpreter, PySys_SetObject
    entries = ["DECLVAR(Py_FrozenFlag);","DECLVAR(Py_NoSiteFlag);","DECLPROC(Py_Initialize);","DECLPROC(Py_Finalize);","DECLPROC(Py_IncRef);","DECLPROC(Py_DecRef);","DECLPROC(PyImport_ExecCodeModule);","DECLPROC(PyRun_SimpleString);","DECLPROC(Py_SetProgramName);","DECLPROC(PyImport_ImportModule);","DECLPROC(PyImport_AddModule);","DECLPROC(PyObject_SetAttrString);","DECLPROC(PyList_New);","DECLPROC(PyList_Append);","DECLPROC(Py_BuildValue);","DECLPROC(PyString_FromStringAndSize);","DECLPROC(PyString_AsString);","DECLPROC(PyObject_CallFunction);","DECLPROC(PyModule_GetDict);","DECLPROC(PyDict_GetItemString);","DECLPROC(PyErr_Clear);","DECLPROC(PyErr_Occurred);","DECLPROC(PyErr_Print);","DECLPROC(PyObject_CallMethod);","DECLPROC(PyInt_AsLong);","DECLPROC(PySys_SetObject);"]
    random.shuffle(entries)
    code = "\n".join(entries) + "\n"


    # intial extract() def
    code += "unsigned char *extract(ARCHIVE_STATUS *%s, TOC *%s);\n" %(randomString(), randomString())


    # getTempPath()
    buffName = randomString()
    retName = randomString()
    prefixName = randomString()
    code += "int getTempPath(char *%s){\n" %(buffName)
    code += "int i;\n"
    code += "char *%s;\n" %(retName)
    code += "char %s[16];\n" %(prefixName)
    code += "GetTempPath(MAX_PATH, %s);\n" %(buffName)
    # TODO: obfuscate this string?
    code += "sprintf(%s, \"_MEI%%d\", getpid());\n" %(prefixName)
    code += "for (i=0;i<5;i++) {\n"
    code += "    %s = _tempnam(%s, %s);\n" %(retName, buffName, prefixName)
    code += "    if (mkdir(%s) == 0) {\n" %(retName)
    code += "        strcpy(%s, %s); strcat(%s, \"\\\\\");\n" %(buffName, retName, buffName)
    code += "        free(%s); return 1;\n" %(retName)
    code += "    } free(%s);\n" %(retName)
    code += "} return 0; }\n"


    # checkFile()
    bufName = randomString()
    fmtName = randomString()
    argsName = randomString()
    tmpName = randomString()
    code += "static int checkFile(char *%s, const char *%s, ...){\n" %(bufName, fmtName)
    code += "    va_list %s;\n" %(argsName)
    code += "    struct stat %s;\n" %(tmpName)
    code += "    va_start(%s, %s);\n" %(argsName, fmtName)
    code += "    vsnprintf(%s, _MAX_PATH, %s, %s);\n" %(bufName, fmtName, argsName)
    code += "    va_end(%s);\n" %(argsName)
    code += "    return stat(%s, &%s); }\n" %(bufName, tmpName)


    # setPaths()
    statusName = randomString()
    archivePathName = randomString()
    archiveNameName = randomString()
    pName = randomString()
    code += "int setPaths(ARCHIVE_STATUS *%s, char const * %s, char const * %s) {\n" %(statusName, archivePathName, archiveNameName)
    code += "    char *%s;\n" %(pName)
    code += "    strcpy(%s->archivename, %s);\n" %(statusName, archivePathName)
    code += "    strcat(%s->archivename, %s);\n" %(statusName, archiveNameName)
    code += "    strcpy(%s->homepath, %s);\n" %(statusName, archivePathName)
    code += "    strcpy(%s->homepathraw, %s);\n" %(statusName, archivePathName)
    code += "    for ( %s = %s->homepath; *%s; %s++ ) if (*%s == '\\\\') *%s = '/';\n" %(pName,statusName,pName,pName,pName,pName)
    code += "    return 0;}\n"


    # checkCookie()
    statusName = randomString()
    filelenName = randomString()
    code += "int checkCookie(ARCHIVE_STATUS *%s, int %s) {\n" %(statusName, filelenName)
    code += "    if (fseek(%s->fp, %s-(int)sizeof(COOKIE), SEEK_SET)) return -1;\n" %(statusName, filelenName)
    code += "    if (fread(&(%s->cookie), sizeof(COOKIE), 1, %s->fp) < 1) return -1;\n" %(statusName,statusName)
    code += "    if (strncmp(%s->cookie.magic, MAGIC, strlen(MAGIC))) return -1;\n" %(statusName)
    code += "    return 0;}\n"


    # openArchive()
    statusName = randomString()
    filelenName = randomString()
    code += "    int openArchive(ARCHIVE_STATUS *%s){\n" %(statusName)
    code += "        int i; int %s;\n" %(filelenName)
    code += "        %s->fp = fopen(%s->archivename, \"rb\");\n" %(statusName,statusName)
    code += "        if (%s->fp == NULL) { return -1;}\n" %(statusName)
    code += "        fseek(%s->fp, 0, SEEK_END);\n" %(statusName)
    code += "        %s = ftell(%s->fp);\n" %(filelenName, statusName)
    code += "        if (checkCookie(%s, %s) < 0) { return -1;}\n" %(statusName, filelenName)
    code += "        %s->pkgstart = %s - ntohl(%s->cookie.len);\n" %(statusName, filelenName, statusName)
    code += "        fseek(%s->fp, %s->pkgstart + ntohl(%s->cookie.TOC), SEEK_SET);\n" %(statusName,statusName,statusName)
    code += "        %s->tocbuff = (TOC *) malloc(ntohl(%s->cookie.TOClen));\n" %(statusName,statusName)
    code += "        if (%s->tocbuff == NULL){ return -1; }\n" %(statusName)
    code += "        if (fread(%s->tocbuff, ntohl(%s->cookie.TOClen), 1, %s->fp) < 1) { return -1; }\n" %(statusName,statusName,statusName)
    code += "        %s->tocend = (TOC *) (((char *)%s->tocbuff) + ntohl(%s->cookie.TOClen));\n" %(statusName,statusName,statusName)
    code += "        if (ferror(%s->fp)) { return -1; }\n" %(statusName)
    code += "        return 0;}\n"


    # emulated incref/decref
    # NOTE: not sure what can be randomized here...
    code += "        struct _old_typeobject;\n"
    code += "        typedef struct _old_object { int ob_refcnt; struct _old_typeobject *ob_type;} OldPyObject;\n"
    code += "        typedef void (*destructor)(PyObject *);\n"
    code += "        typedef struct _old_typeobject { int ob_refcnt; struct _old_typeobject *ob_type; int ob_size; char *tp_name;\n"
    code += "            int tp_basicsize, tp_itemsize; destructor tp_dealloc; } OldPyTypeObject;\n"
    code += "        static void _EmulatedIncRef(PyObject *o){\n"
    code += "            OldPyObject *oo = (OldPyObject*)o;\n"
    code += "            if (oo) oo->ob_refcnt++;}\n"
    code += "        static void _EmulatedDecRef(PyObject *o){\n"
    code += "            #define _Py_Dealloc(op) (*(op)->ob_type->tp_dealloc)((PyObject *)(op))\n"
    code += "            OldPyObject *oo = (OldPyObject*)o;\n"
    code += "            if (--(oo)->ob_refcnt == 0) _Py_Dealloc(oo);}\n"


    # mapNames()
    dllName = randomString()
    code += "int mapNames(HMODULE %s, int %s){\n" %(dllName, randomString())
    # Python Entry point declarations, these can definitely be shuffled
    # removed:  Py_OptimizeFlag, Py_VerboseFlag, PySys_SetArgv, PyFile_FromString, PyObject_CallObject, PySys_AddWarnOption
    #           PyEval_InitThreads, PyEval_AcquireThread, PyEval_ReleaseThread, PyThreadState_Swap, Py_NewInterpreter, PySys_SetObject
    entry_points = ["GETVAR(dll, Py_FrozenFlag);","GETVAR(dll, Py_NoSiteFlag);","GETPROC(dll, Py_Initialize);","GETPROC(dll, Py_Finalize);","GETPROCOPT(dll, Py_IncRef);","GETPROCOPT(dll, Py_DecRef);","GETPROC(dll, PyImport_ExecCodeModule);","GETPROC(dll, PyRun_SimpleString);","GETPROC(dll, PyString_FromStringAndSize);","GETPROC(dll, Py_SetProgramName);","GETPROC(dll, PyImport_ImportModule);","GETPROC(dll, PyImport_AddModule);","GETPROC(dll, PyObject_SetAttrString);","GETPROC(dll, PyList_New);","GETPROC(dll, PyList_Append);","GETPROC(dll, Py_BuildValue);","GETPROC(dll, PyString_AsString);","GETPROC(dll, PyObject_CallFunction);","GETPROC(dll, PyModule_GetDict);","GETPROC(dll, PyDict_GetItemString);","GETPROC(dll, PyErr_Clear);","GETPROC(dll, PyErr_Occurred);","GETPROC(dll, PyErr_Print);","GETPROC(dll, PyObject_CallMethod);","GETPROC(dll, PyInt_AsLong);"]
    entry_points = [x.replace("dll", dllName) for x in entry_points]
    random.shuffle(entry_points)
    code += "\n".join(entry_points) + "\n"

    code += "    if (!PI_Py_IncRef) PI_Py_IncRef = _EmulatedIncRef;\n"
    code += "    if (!PI_Py_DecRef) PI_Py_DecRef = _EmulatedDecRef;\n"
    code += "    return 0;}\n"


    # loadPython()
    statusName = randomString()
    dllPathName = randomString()
    dllName = randomString()
    pyversName = randomString()
    code += "int loadPython(ARCHIVE_STATUS *%s){\n" %(statusName)
    code += "    HINSTANCE %s;\n" %(dllName)
    code += "    char %s[_MAX_PATH + 1];\n" %(dllPathName)
    code += "    int %s = ntohl(%s->cookie.pyvers);\n" %(pyversName, statusName)
    # TODO: obfuscate this string?
    code += "    sprintf(%s, \"%%spython%%02d.dll\", %s->homepathraw, %s);\n" %(dllPathName,statusName,pyversName)
    code += "    %s = LoadLibraryExA(%s, NULL, LOAD_WITH_ALTERED_SEARCH_PATH);\n" %(dllName, dllPathName)
    # TODO: obfuscate this string?
    code += "    if (!%s) {sprintf(%s, \"%%spython%%02d.dll\", %s->temppathraw, %s);\n" %(dllName, dllPathName,statusName,pyversName)
    code += "        %s = LoadLibraryExA(%s, NULL, LOAD_WITH_ALTERED_SEARCH_PATH );}\n" %(dllName, dllPathName)
    code += "    if (%s == 0) { return -1; }\n" %(dllName)
    code += "    mapNames(%s, %s);\n" %(dllName,pyversName)
    code += "    return 0;}\n"


    # incrementTocPtr()
    statusName = randomString()
    ptocName = randomString()
    resultName = randomString()
    code += " TOC *incrementTocPtr(ARCHIVE_STATUS *%s, TOC* %s){\n" %(statusName,ptocName)
    code += "     TOC *%s = (TOC*)((char *)%s + ntohl(%s->structlen));\n" %(resultName,ptocName,ptocName)
    code += "     if (%s < %s->tocbuff) { return %s->tocend; }\n" %(resultName,statusName,statusName)
    code += "     return %s;}\n" %(resultName)


    # startPython()
    statusName = randomString()
    pypathName = randomString()
    py_argvName = randomString()
    cmdName = randomString()
    tmpName = randomString()
    code += "int startPython(ARCHIVE_STATUS *%s, int argc, char *argv[]) {\n" %(statusName)
    code += "static char %s[2*_MAX_PATH + 14];\n" %(pypathName)
    code += "int i;\n"
    code += "char %s[_MAX_PATH+1+80];\n" %(cmdName)
    code += "char %s[_MAX_PATH+1];\n" %(tmpName)
    code += "PyObject *%s;\n" %(py_argvName)
    code += "PyObject *val;\n"
    code += "PyObject *sys;\n"
    # TODO: obfuscate this string?
    code += "strcpy(%s, \"PYTHONPATH=\");\n" %(pypathName)
    code += "if (%s->temppath[0] != '\\0') { strcat(%s, %s->temppath); %s[strlen(%s)-1] = '\\0'; strcat(%s, \";\"); }\n" %(statusName, pypathName, statusName, pypathName, pypathName, pypathName)
    code += "strcat(%s, %s->homepath);\n" %(pypathName, statusName)
    code += "if (strlen(%s) > 14) %s[strlen(%s)-1] = '\\0';\n" %(pypathName, pypathName, pypathName)
    code += "putenv(%s);\n" %(pypathName)
    # TODO: obfuscate this string?
    code += "strcpy(%s, \"PYTHONHOME=\");\n" %(pypathName)
    code += "strcat(%s, %s->temppath);\n" %(pypathName, statusName)
    code += "putenv(%s);\n" %(pypathName)
    code += "*PI_Py_NoSiteFlag = 1; *PI_Py_FrozenFlag = 1;\n"
    # TODO: can we randomize the program name?
    code += "PI_Py_SetProgramName(%s->archivename);\n" %(statusName)
    code += "PI_Py_Initialize();\n"
    # TODO: obfuscate this string?
    code += "PI_PyRun_SimpleString(\"import sys\\n\");\n"
    # TODO: obfuscate this string?
    code += "PI_PyRun_SimpleString(\"del sys.path[:]\\n\");\n"
    code += "if (%s->temppath[0] != '\\0') {\n" %(statusName)
    code += "    strcpy(%s, %s->temppath);\n" %(tmpName, statusName)
    code += "    %s[strlen(%s)-1] = '\\0';\n" %(tmpName, tmpName)
    # TODO: obfuscate this string?
    code += "    sprintf(%s, \"sys.path.append(r\\\"%%s\\\")\", %s);\n" %(cmdName, tmpName)
    code += "    PI_PyRun_SimpleString(%s);}\n" %(cmdName)
    code += "strcpy(%s, %s->homepath);\n" %(tmpName, statusName)
    code += "%s[strlen(%s)-1] = '\\0';\n" %(tmpName, tmpName)
    code += "sprintf(%s, \"sys.path.append(r\\\"%%s\\\")\", %s);\n" %(cmdName, tmpName)
    code += "PI_PyRun_SimpleString (%s);\n" %(cmdName)
    code += "%s = PI_PyList_New(0);\n" %(py_argvName)
    code += "val = PI_Py_BuildValue(\"s\", %s->archivename);\n" %(statusName)
    code += "PI_PyList_Append(%s, val);\n" %(py_argvName)
    code += "for (i = 1; i < argc; ++i) { val = PI_Py_BuildValue (\"s\", argv[i]); PI_PyList_Append (%s, val); }\n" %(py_argvName)
    code += "sys = PI_PyImport_ImportModule(\"sys\");\n"
    code += "PI_PyObject_SetAttrString(sys, \"argv\", %s);\n" %(py_argvName)
    code += "return 0;}\n"


    # importModules() -> problem here, causing a fail
    statusName = randomString()
    ptocName = randomString()
    marshaldictName = randomString()
    marshalName = randomString()
    loadfuncName = randomString()
    modbufName = randomString()
    code += "int importModules(ARCHIVE_STATUS *%s){\n" %(statusName)
    code += "    PyObject *%s; PyObject *%s; PyObject *%s;\n" %(marshalName, marshaldictName, loadfuncName)
    code += "    TOC *%s; PyObject *co; PyObject *mod;\n" %(ptocName)
    # TODO: obfuscate this string?
    code += "    %s = PI_PyImport_ImportModule(\"marshal\");\n" %(marshalName)
    code += "    %s = PI_PyModule_GetDict(%s);\n" %(marshaldictName, marshalName)
    # TODO: obfuscate this string?
    code += "    %s = PI_PyDict_GetItemString(%s, \"loads\");\n" %(loadfuncName, marshaldictName)
    code += "    %s = %s->tocbuff;\n" %(ptocName, statusName)
    code += "    while (%s < %s->tocend) {\n" %(ptocName, statusName)
    code += "        if (%s->typcd == 'm' || %s->typcd == 'M'){\n" %(ptocName, ptocName)
    code += "            unsigned char *%s = extract(%s, %s);\n" %(modbufName, statusName, ptocName)
    code += "            co = PI_PyObject_CallFunction(%s, \"s#\", %s+8, ntohl(%s->ulen)-8);\n" %(loadfuncName, modbufName, ptocName)
    code += "            mod = PI_PyImport_ExecCodeModule(%s->name, co);\n" %(ptocName)
    code += "            if (PI_PyErr_Occurred()) { PI_PyErr_Print(); PI_PyErr_Clear(); }\n"
    code += "            free(%s);\n" %(modbufName)
    code += "        }\n"
    code += "        %s = incrementTocPtr(%s, %s);\n" %(ptocName, statusName, ptocName)
    code += "    } return 0; }\n"


    # installZlib()
    statusName = randomString()
    ptocName = randomString()
    zlibposName = randomString()
    cmdName = randomString()
    tmplName = randomString()
    rcName = randomString()
    code += "int installZlib(ARCHIVE_STATUS *%s, TOC *%s){\n" %(statusName, ptocName)
    code += "    int %s; int %s = %s->pkgstart + ntohl(%s->pos);\n" %(rcName, zlibposName, statusName, ptocName)
    # TODO: obfuscate this string?
    code += "    char *%s = \"sys.path.append(r\\\"%%s?%%d\\\")\\n\";\n" %(tmplName)
    code += "    char *%s = (char *) malloc(strlen(%s) + strlen(%s->archivename) + 32);\n" %(cmdName, tmplName, statusName)
    code += "    sprintf(%s, %s, %s->archivename, %s);\n" %(cmdName, tmplName, statusName, zlibposName)
    code += "    %s = PI_PyRun_SimpleString(%s);\n" %(rcName, cmdName)
    code += "    if (%s != 0){ free(%s); return -1; }\n" %(rcName, cmdName)
    code += "    free(%s); return 0;}\n" %(cmdName)


    # installZlibs()
    statusName = randomString()
    ptocName = randomString()
    code += "int installZlibs(ARCHIVE_STATUS *%s){\n" %(statusName)
    code += "TOC * %s; %s = %s->tocbuff;\n" %(ptocName, ptocName, statusName)
    code += "while (%s < %s->tocend) {\n" %(ptocName, statusName)
    code += "    if (%s->typcd == 'z') { installZlib(%s, %s); }\n" %(ptocName, statusName, ptocName)
    code += "    %s = incrementTocPtr(%s, %s); }\n" %(ptocName, statusName, ptocName)
    code += "return 0; }\n"


    # decompress()
    buffName = randomString()
    ptocName = randomString()
    outName = randomString()
    zstreamName = randomString()
    rcName = randomString()
    code += "unsigned char *decompress(unsigned char * %s, TOC *%s){\n" %(buffName, ptocName)
    code += "unsigned char *%s; z_stream %s; int %s;\n" %(outName, zstreamName, rcName)
    code += "%s = (unsigned char *)malloc(ntohl(%s->ulen));\n" %(outName, ptocName)
    code += "if (%s == NULL) { return NULL; }\n" %(outName)
    code += "%s.zalloc = NULL;\n" %(zstreamName)
    code += "%s.zfree = NULL;\n" %(zstreamName)
    code += "%s.opaque = NULL;\n" %(zstreamName)
    code += "%s.next_in = %s;\n" %(zstreamName, buffName)
    code += "%s.avail_in = ntohl(%s->len);\n" %(zstreamName, ptocName)
    code += "%s.next_out = %s;\n" %(zstreamName, outName)
    code += "%s.avail_out = ntohl(%s->ulen);\n" %(zstreamName, ptocName)
    code += "%s = inflateInit(&%s);\n" %(rcName, zstreamName)
    code += "if (%s >= 0) { \n" %(rcName)
    code += "    %s = (inflate)(&%s, Z_FINISH);\n" %(rcName, zstreamName)
    code += "    if (%s >= 0) { %s = (inflateEnd)(&%s); }\n" %(rcName, rcName, zstreamName)
    code += "    else { return NULL; } }\n"
    code += "else { return NULL; }\n"
    code += "return %s;}\n" %(outName)


    # extract()
    statusName = randomString()
    ptocName = randomString()
    dataName = randomString()
    AESName = randomString()
    tmpName = randomString()
    func_newName = randomString()
    ddataName = randomString()
    aes_dictName = randomString()
    aes_objName = randomString()
    code += "unsigned char *extract(ARCHIVE_STATUS *%s, TOC *%s){\n" %(statusName, ptocName)
    code += "unsigned char *%s;unsigned char *%s;\n" %(dataName, tmpName)
    code += "fseek(%s->fp, %s->pkgstart + ntohl(%s->pos), SEEK_SET);\n" %(statusName, statusName, ptocName)
    code += "%s = (unsigned char *)malloc(ntohl(%s->len));\n" %(dataName, ptocName)
    code += "if (%s == NULL) { return NULL; }\n" %(dataName)
    code += "if (fread(%s, ntohl(%s->len), 1, %s->fp) < 1) { return NULL; }\n" %(dataName, ptocName, statusName)
    code += "if (%s->cflag == '\\2') {\n" %(ptocName)
    code += "    static PyObject *%s = NULL;\n" %(AESName)
    code += "    PyObject *%s; PyObject *%s; PyObject *%s; PyObject *%s;\n" %(func_newName, aes_dictName, aes_objName, ddataName)
    code += "    long block_size; char *iv;\n"
    code += "    if (!%s) %s = PI_PyImport_ImportModule(\"AES\");\n" %(AESName,AESName)
    code += "    %s = PI_PyModule_GetDict(%s);\n" %(aes_dictName, AESName)
    code += "    %s = PI_PyDict_GetItemString(%s, \"new\");\n" %(func_newName, aes_dictName)
    code += "    block_size = PI_PyInt_AsLong(PI_PyDict_GetItemString(%s, \"block_size\"));\n" %(aes_dictName)
    code += "    iv = malloc(block_size);\n"
    code += "    memset(iv, 0, block_size);\n"
    code += "    %s = PI_PyObject_CallFunction(%s, \"s#Os#\", %s, 32, PI_PyDict_GetItemString(%s, \"MODE_CFB\"), iv, block_size);\n" %(aes_objName, func_newName, dataName, aes_dictName)
    code += "    %s = PI_PyObject_CallMethod(%s, \"decrypt\", \"s#\", %s+32, ntohl(%s->len)-32);\n" %(ddataName, aes_objName, dataName, ptocName)
    code += "    memcpy(%s, PI_PyString_AsString(%s), ntohl(%s->len)-32);\n" %(dataName, ddataName, ptocName)
    code += "    Py_DECREF(%s); Py_DECREF(%s);}\n" %(aes_objName, ddataName)
    code += "if (%s->cflag == '\\1' || %s->cflag == '\\2') {\n" %(ptocName, ptocName)
    code += "    %s = decompress(%s, %s);\n" %(tmpName, dataName, ptocName)
    code += "    free(%s); %s = %s;\n" %(dataName, dataName, tmpName)
    code += "    if (%s == NULL) { return NULL; } }\n" %(dataName)
    code += "return %s;}\n" %(dataName)


    # openTarget()
    pathName = randomString()
    name_Name = randomString()
    sbufName = randomString()
    nameName = randomString()
    fnmName = randomString()
    dirName = randomString()
    code += "FILE *openTarget(const char *%s, const char* %s) {\n" %(pathName, name_Name)
    code += "struct stat %s; char %s[_MAX_PATH+1]; char %s[_MAX_PATH+1]; char *%s;\n" %(sbufName, fnmName, nameName, dirName)
    code += "strcpy(%s, %s); strcpy(%s, %s); %s[strlen(%s)-1] = '\\0';\n" %(fnmName, pathName, nameName, name_Name, fnmName, fnmName)
    code += "%s = strtok(%s, \"/\\\\\");\n" %(dirName, nameName)
    code += "while (%s != NULL){\n" %(dirName)
    code += "    strcat(%s, \"\\\\\");\n" %(fnmName)
    code += "    strcat(%s, %s);\n" %(fnmName, dirName)
    code += "    %s = strtok(NULL, \"/\\\\\");\n" %(dirName)
    code += "    if (!%s) break;\n" %(dirName)
    code += "    if (stat(%s, &%s) < 0) {mkdir(%s);} }\n" %(fnmName, sbufName, fnmName)
    code += "return fopen(%s, \"wb\"); }\n" %(fnmName)


    # createTempPath()
    statusName = randomString()
    pName = randomString()
    code += "static int createTempPath(ARCHIVE_STATUS *%s) {\n" %(statusName)
    code += "char *%s;\n" %(pName)
    code += "if (%s->temppath[0] == '\\0') {\n" %(statusName)
    code += "    if (!getTempPath(%s->temppath)) {return -1;}\n" %(statusName)
    code += "    strcpy(%s->temppathraw, %s->temppath);\n" %(statusName, statusName)
    code += "    for ( %s=%s->temppath; *%s; %s++ ) if (*%s == '\\\\') *%s = '/';}\n" %(pName, statusName, pName, pName, pName, pName)
    code += "return 0;}\n"


    # extract2fs()
    statusName = randomString()
    ptocName = randomString()
    outName = randomString()
    dataName = randomString()
    code += "int extract2fs(ARCHIVE_STATUS *%s, TOC *%s) {\n" %(statusName, ptocName)
    code += "FILE *%s; unsigned char *%s = extract(%s, %s);\n" %(outName, dataName, statusName, ptocName)
    code += "if (createTempPath(%s) == -1){ return -1; }\n" %(statusName)
    code += "%s = openTarget(%s->temppath, %s->name);\n" %(outName, statusName, ptocName)
    code += "if (%s == NULL)  { return -1; }\n" %(outName)
    code += "else { fwrite(%s, ntohl(%s->ulen), 1, %s); fclose(%s); }\n" %(dataName, ptocName, outName, outName)
    code += "free(%s); return 0; }\n" %(dataName)


    # splitName()
    pathName = randomString()
    filenameName = randomString()
    itemName = randomString()
    nameName = randomString()
    code += "static int splitName(char *%s, char *%s, const char *%s) {\n" %(pathName, filenameName, itemName)
    code += "char %s[_MAX_PATH + 1];\n" %(nameName)
    code += "strcpy(%s, %s);\n" %(nameName, itemName)
    code += "strcpy(%s, strtok(%s, \":\"));\n" %(pathName, nameName)
    code += "strcpy(%s, strtok(NULL, \":\")) ;\n" %(filenameName)
    code += "if (%s[0] == 0 || %s[0] == 0) return -1;\n" %(pathName, filenameName)
    code += "return 0; }\n"


    # copyFile()
    srcName = randomString()
    dstName = randomString()
    filenameName = randomString()
    inName = randomString()
    outName = randomString()
    code += "static int copyFile(const char *%s, const char *%s, const char *%s) {\n" %(srcName, dstName, filenameName)
    code += "FILE *%s = fopen(%s, \"rb\"); FILE *%s = openTarget(%s, %s);\n" %(inName, srcName, outName, dstName, filenameName)
    code += "char buf[4096]; int error = 0;\n"
    code += "if (%s == NULL || %s == NULL) return -1;\n" %(inName, outName)
    code += "while (!feof(%s)) {\n" %(inName)
    code += "    if (fread(buf, 4096, 1, %s) == -1) {\n" %(inName)
    code += "        if (ferror(%s)) { clearerr(%s); error = -1; break; }\n" %(inName, inName)
    code += "    } else {\n"
    code += "        fwrite(buf, 4096, 1, %s);\n" %(outName)
    code += "        if (ferror(%s)) { clearerr(%s); error = -1; break;}}}\n" %(outName, outName)
    code += "fclose(%s); fclose(%s); return error; }\n" %(inName, outName)


    # dirName()
    fullpathName = randomString()
    matchName = randomString()
    pathnameName = randomString()
    code += "static char *dirName(const char *%s) {\n" %(fullpathName)
    code += "char *%s = strrchr(%s, '\\\\');\n" %(matchName, fullpathName)
    code += "char *%s = (char *) calloc(_MAX_PATH, sizeof(char));\n" %(pathnameName)
    code += "if (%s != NULL) strncpy(%s, %s, %s - %s + 1);\n" %(matchName, pathnameName, fullpathName, matchName, fullpathName)
    code += "else strcpy(%s, %s);\n" %(pathnameName, fullpathName)
    code += "return %s; }\n" %(pathnameName)


    # copyDependencyFromDir()
    statusName = randomString()
    srcpathName = randomString()
    filenameString = randomString()
    code += "static int copyDependencyFromDir(ARCHIVE_STATUS *%s, const char *%s, const char *%s){\n" %(statusName, srcpathName, filenameString)
    code += "if (createTempPath(%s) == -1){ return -1; }\n" %(statusName)
    code += "if (copyFile(%s, %s->temppath, %s) == -1) { return -1; }\n" %(srcpathName, statusName, filenameString)
    code += "return 0; }\n"


    # get_archive()
    statusName = randomString()
    pathName = randomString()
    status_listName = randomString()
    code += "static ARCHIVE_STATUS *get_archive(ARCHIVE_STATUS *%s[], const char *%s) {\n" %(status_listName, pathName)
    code += "ARCHIVE_STATUS *%s = NULL; int i = 0;\n" %(statusName)
    code += "if (createTempPath(%s[SELF]) == -1){ return NULL; } \n" %(status_listName)
    code += "for (i = 1; %s[i] != NULL; i++){ if (strcmp(%s[i]->archivename, %s) == 0) { return %s[i]; } }\n" %(status_listName, status_listName, pathName, status_listName)
    code += "if ((%s = (ARCHIVE_STATUS *) calloc(1, sizeof(ARCHIVE_STATUS))) == NULL) { return NULL; }\n" %(statusName)
    code += "strcpy(%s->archivename, %s);\n" %(statusName, pathName)
    code += "strcpy(%s->homepath, %s[SELF]->homepath);\n" %(statusName, status_listName)
    code += "strcpy(%s->temppath, %s[SELF]->temppath);\n" %(statusName, status_listName)
    code += "strcpy(%s->homepathraw, %s[SELF]->homepathraw);\n" %(statusName, status_listName)
    code += "strcpy(%s->temppathraw, %s[SELF]->temppathraw);\n" %(statusName, status_listName)
    code += "if (openArchive(%s)) { free(%s); return NULL; }\n" %(statusName, statusName)
    code += "%s[i] = %s; return %s; }\n" %(status_listName, statusName, statusName)


    # extractDependencyFromArchive()
    statusName = randomString()
    filenameName = randomString()
    ptocName = randomString()
    code += "static int extractDependencyFromArchive(ARCHIVE_STATUS *%s, const char *%s) {\n" %(statusName, filenameName)
    code += "TOC * %s = %s->tocbuff;\n" %(ptocName, statusName)
    code += "while (%s < %s->tocend) {\n" %(ptocName, statusName)
    code += "    if (strcmp(%s->name, %s) == 0) if (extract2fs(%s, %s)) return -1;\n" %(ptocName, filenameName, statusName, ptocName)
    code += "    %s = incrementTocPtr(%s, %s); }\n" %(ptocName, statusName, ptocName)
    code += "return 0; }\n"


    # extractDependency()
    statusName = randomString()
    status_listName = randomString()
    itemName = randomString()
    pathName = randomString()
    filenameName = randomString()
    archive_pathName = randomString()
    dirnameName = randomString()
    code += "static int extractDependency(ARCHIVE_STATUS *%s[], const char *%s) {\n" %(status_listName, itemName)
    code += "ARCHIVE_STATUS *%s = NULL;\n" %(statusName)
    code += "char %s[_MAX_PATH + 1]; char %s[_MAX_PATH + 1];\n" %(pathName, filenameName)
    code += "char %s[_MAX_PATH + 1]; char *%s = NULL;\n" %(archive_pathName, dirnameName)
    code += "if (splitName(%s, %s, %s) == -1) return -1;\n" %(pathName, filenameName, itemName)
    code += "%s = dirName(%s);\n" %(dirnameName, pathName)
    code += "if (%s[0] == 0) { free(%s); return -1; }\n" %(dirnameName, dirnameName)
    code += "if ((checkFile(%s, \"%%s%%s.pkg\", %s[SELF]->homepath, %s) != 0) &&\n" %(archive_pathName, status_listName, pathName)
    code += "    (checkFile(%s, \"%%s%%s.exe\", %s[SELF]->homepath, %s) != 0) &&\n" %(archive_pathName, status_listName, pathName)
    code += "    (checkFile(%s, \"%%s%%s\", %s[SELF]->homepath, %s) != 0)) { return -1; }\n" %(archive_pathName, status_listName, pathName)
    code += "    if ((%s = get_archive(%s, %s)) == NULL) { return -1; }\n" %(statusName, status_listName, archive_pathName)
    code += "if (extractDependencyFromArchive(%s, %s) == -1) { free(%s); return -1; }\n" %(statusName, filenameName, statusName)
    code += "free(%s); return 0; }\n" %(dirnameName)


    # needToExtractBinaries()
    status_listName = randomString()
    ptocName = randomString()
    code += "int needToExtractBinaries(ARCHIVE_STATUS *%s[]) {\n" %(status_listName)
    code += "TOC * %s = %s[SELF]->tocbuff;\n" %(ptocName, status_listName)
    code += "while (%s < %s[SELF]->tocend) {\n" %(ptocName, status_listName)
    code += "    if (%s->typcd == 'b' || %s->typcd == 'x' || %s->typcd == 'Z') return 1;\n" %(ptocName, ptocName, ptocName)
    code += "    if (%s->typcd == 'd')  return 1;\n" %(ptocName)
    code += "    %s = incrementTocPtr(%s[SELF], %s);\n" %(ptocName, status_listName, ptocName)
    code += "} return 0; }\n"


    # extractBinaries()
    status_listName = randomString()
    ptocName = randomString()
    code += "int extractBinaries(ARCHIVE_STATUS *%s[]) {\n" %(status_listName)
    code += "TOC * %s = %s[SELF]->tocbuff;\n" %(ptocName, status_listName)
    code += "while (%s < %s[SELF]->tocend) {\n" %(ptocName, status_listName)
    code += "    if (%s->typcd == 'b' || %s->typcd == 'x' || %s->typcd == 'Z')\n" %(ptocName, ptocName, ptocName)
    code += "        if (extract2fs(%s[SELF], %s)) return -1;\n" %(status_listName, ptocName)
    code += "    if (%s->typcd == 'd') {\n" %(ptocName)
    code += "        if (extractDependency(%s, %s->name) == -1) return -1; }\n" %(status_listName, ptocName)
    code += "    %s = incrementTocPtr(%s[SELF], %s); }\n" %(ptocName, status_listName, ptocName)
    code += "return 0; }\n"


    # runScripts()
    statusName = randomString()
    dataName = randomString()
    bufName = randomString()
    rcName = randomString()
    ptocName = randomString()
    code += "int runScripts(ARCHIVE_STATUS *%s) {\n" %(statusName)
    code += "unsigned char *%s; char %s[_MAX_PATH]; int %s = 0;\n" %(dataName, bufName, rcName)
    code += "TOC * %s = %s->tocbuff;\n" %(ptocName, statusName)
    code += "PyObject *__main__ = PI_PyImport_AddModule(\"__main__\"); PyObject *__file__;\n"
    code += "while (%s < %s->tocend) {\n" %(ptocName, statusName)
    code += "    if (%s->typcd == 's') {\n" %(ptocName)
    code += "        %s = extract(%s, %s);\n" %(dataName, statusName, ptocName)
    code += "        strcpy(%s, %s->name); strcat(%s, \".py\");\n" %(bufName, ptocName, bufName)
    code += "        __file__ = PI_PyString_FromStringAndSize(%s, strlen(%s));\n" %(bufName, bufName)
    code += "        PI_PyObject_SetAttrString(__main__, \"__file__\", __file__); Py_DECREF(__file__);\n"
    code += "        %s = PI_PyRun_SimpleString(%s);\n" %(rcName, dataName) 
    code += "        if (%s != 0) return %s; free(%s); }\n" %(rcName, rcName, dataName)
    code += "    %s = incrementTocPtr(%s, %s);\n" %(ptocName, statusName, ptocName)
    code += "} return 0; }\n"


    # init()
    statusName = randomString()
    archivePathName = randomString()
    archiveNameName = randomString()
    code += "int init(ARCHIVE_STATUS *%s, char const * %s, char  const * %s) {\n" %(statusName, archivePathName, archiveNameName)
    code += "if (setPaths(%s, %s, %s)) return -1;\n" %(statusName, archivePathName, archiveNameName)
    code += "if (openArchive(%s)) return -1;\n" %(statusName)
    code += "return 0; }\n"


    # doIt()
    statusName = randomString()
    rcName = randomString()
    code += "int doIt(ARCHIVE_STATUS *%s, int argc, char *argv[]) {\n" %(statusName)
    code += "int %s = 0;\n" %(rcName)
    code += "if (loadPython(%s)) return -1;\n" %(statusName)
    code += "if (startPython(%s, argc, argv)) return -1;\n" %(statusName)
    code += "if (importModules(%s)) return -1;\n" %(statusName)
    code += "if (installZlibs(%s)) return -1;\n" %(statusName)
    code += "%s = runScripts(%s);\n" %(rcName, statusName)
    code += "return %s; }\n" %(rcName)


    # clear() dec
    code += "void clear(const char *%s);\n" %(randomString())


    # removeOne()
    fnmName = randomString()
    posName = randomString()
    finfoName = randomString()
    code += "void removeOne(char *%s, int %s, struct _finddata_t %s) {\n" %(fnmName, posName, finfoName)
    code += "if ( strcmp(%s.name, \".\")==0  || strcmp(%s.name, \"..\") == 0 ) return;\n" %(finfoName, finfoName)
    code += "%s[%s] = '\\0';\n" %(fnmName, posName)
    code += "strcat(%s, %s.name);\n" %(fnmName, finfoName)
    code += "if ( %s.attrib & _A_SUBDIR ) clear(%s);\n" %(finfoName, fnmName)
    code += " else if (remove(%s)) { Sleep(100); remove(%s); } }\n" %(fnmName, fnmName)


    # clear()
    dirName = randomString()
    fnmName = randomString()
    finfoName = randomString()
    hName = randomString()
    dirnmlenName = randomString()
    code += "void clear(const char *%s) {\n" %(dirName)
    code += "char %s[_MAX_PATH+1]; struct _finddata_t %s;\n" %(fnmName, finfoName)
    code += "long %s; int %s; strcpy(%s, %s);\n" %(hName, dirnmlenName, fnmName, dirName)
    code += "%s = strlen(%s);\n" %(dirnmlenName, fnmName)
    code += "if ( %s[%s-1] != '/' && %s[%s-1] != '\\\\' ) { strcat(%s, \"\\\\\"); %s++; }\n" %(fnmName, dirnmlenName, fnmName, dirnmlenName, fnmName, dirnmlenName)
    code += "strcat(%s, \"*\");\n" %(fnmName)
    code += "%s = _findfirst(%s, &%s);\n" %(hName, fnmName, finfoName)
    code += "if (%s != -1) {\n" %(hName)
    code += "    removeOne(%s, %s, %s);\n" %(fnmName, dirnmlenName, finfoName)
    code += "    while ( _findnext(%s, &%s) == 0 ) removeOne(%s, %s, %s);\n" %(hName, finfoName, fnmName, dirnmlenName, finfoName)
    code += "    _findclose(%s); }\n" %(hName)
    code += "rmdir(%s); }\n" %(dirName)


    # cleanUp()
    statusName = randomString()
    code += "void cleanUp(ARCHIVE_STATUS *%s) { if (%s->temppath[0]) clear(%s->temppath); }\n" %(statusName, statusName, statusName)


    # getPyVersion()
    statusName = randomString()
    code += "int getPyVersion(ARCHIVE_STATUS *%s) { return ntohl(%s->cookie.pyvers); }\n" %(statusName, statusName)


    # finalizePython()
    code += "void finalizePython(void) { PI_Py_Finalize(); } \n"

    return (allincludes, code)


def generate_launch_h(methodSubs):
    """
    Generate obfuscated version of Pwnstaller's launch.h
    """
    code = "#ifndef LAUNCH_H\n"
    code += "#define LAUNCH_H\n"
    code += "#include <stdio.h>\n"
    code += "#include <string.h>\n"
    code += "#include <stdlib.h>\n"
    code += "#include <io.h>\n"
    code += "#include <fcntl.h>\n"
    code += "#include <winsock.h>\n"
    code += "#define EXTDECLPROC(result, name, args) typedef result (__cdecl *__PROC__##name) args; extern __PROC__##name PI_##name;\n"
    code += "#define EXTDECLVAR(vartyp, name) typedef vartyp __VAR__##name; extern __VAR__##name *PI_##name;\n"
    code += "struct _object;\n"
    code += "typedef struct _object PyObject;\n"
    code += "struct _PyThreadState;\n"
    code += "typedef struct _PyThreadState PyThreadState;\n"
    code += "EXTDECLVAR(int, Py_FrozenFlag);\n"
    code += "EXTDECLVAR(int, Py_NoSiteFlag);\n"
    code += "EXTDECLPROC(int, Py_Initialize, (void));\n"
    code += "EXTDECLPROC(int, Py_Finalize, (void));\n"
    code += "EXTDECLPROC(void, Py_IncRef, (PyObject *));\n"
    code += "EXTDECLPROC(void, Py_DecRef, (PyObject *));\n"
    code += "EXTDECLPROC(PyObject *, PyImport_ExecCodeModule, (char *, PyObject *));\n"
    code += "EXTDECLPROC(int, PyRun_SimpleString, (char *));\n"
    code += "EXTDECLPROC(void, Py_SetProgramName, (char *));\n"
    code += "EXTDECLPROC(PyObject *, PyImport_ImportModule, (char *));\n"
    code += "EXTDECLPROC(PyObject *, PyImport_AddModule, (char *));\n"
    code += "EXTDECLPROC(int, PyObject_SetAttrString, (PyObject *, char *, PyObject *));\n"
    code += "EXTDECLPROC(PyObject *, PyList_New, (int));\n"
    code += "EXTDECLPROC(int, PyList_Append, (PyObject *, PyObject *));\n"
    code += "EXTDECLPROC(PyObject *, Py_BuildValue, (char *, ...));\n"
    code += "EXTDECLPROC(PyObject *, PyString_FromStringAndSize, (const char *, int));\n"
    code += "EXTDECLPROC(char *, PyString_AsString, (PyObject *));\n"
    code += "EXTDECLPROC(PyObject *, PyObject_CallFunction, (PyObject *, char *, ...));\n"
    code += "EXTDECLPROC(PyObject *, PyModule_GetDict, (PyObject *));\n"
    code += "EXTDECLPROC(PyObject *, PyDict_GetItemString, (PyObject *, char *));\n"
    code += "EXTDECLPROC(void, PyErr_Clear, (void) );\n"
    code += "EXTDECLPROC(PyObject *, PyErr_Occurred, (void) );\n"
    code += "EXTDECLPROC(void, PyErr_Print, (void) );\n"
    code += "EXTDECLPROC(PyObject *, PyObject_CallMethod, (PyObject *, char *, char *, ...) );\n"
    code += "EXTDECLPROC(void, Py_EndInterpreter, (PyThreadState *) );\n"
    code += "EXTDECLPROC(long, PyInt_AsLong, (PyObject *) );\n"
    code += "EXTDECLPROC(int, PySys_SetObject, (char *, PyObject *));\n"
    code += "#define Py_XINCREF(o)    PI_Py_IncRef(o)\n"
    code += "#define Py_XDECREF(o)    PI_Py_DecRef(o)\n"
    code += "#define Py_DECREF(o)     Py_XDECREF(o)\n"
    code += "#define Py_INCREF(o)     Py_XINCREF(o)\n"
    code += "#define DECLPROC(name) __PROC__##name PI_##name = NULL;\n"
    code += "#define GETPROCOPT(dll, name) PI_##name = (__PROC__##name)GetProcAddress (dll, #name)\n"
    code += "#define GETPROC(dll, name) GETPROCOPT(dll, name); if (!PI_##name) { return -1;}\n"
    code += "#define DECLVAR(name) __VAR__##name *PI_##name = NULL;\n"
    code += "#define GETVAR(dll, name) PI_##name = (__VAR__##name *)GetProcAddress (dll, #name); if (!PI_##name) { return -1;}\n"
    code += "#define MAGIC \"MEI\\014\\013\\012\\013\\016\"\n"
    code += "# define FATALERROR mbfatalerror\n"
    code += "# define OTHERERROR mbothererror\n"
    code += "#ifndef _MAX_PATH\n"
    code += "#define _MAX_PATH 256\n"
    code += "#endif\n"
    code += "#define SELF 0\n"

    code += "typedef struct _toc { int structlen; int pos; int len; int ulen; char cflag; char typcd; char name[1]; } TOC;\n"
    code += "typedef struct _cookie { char magic[8]; int len; int TOC; int TOClen; int pyvers; } COOKIE;\n"
    code += "typedef struct _archive_status {\n"
    code += "    FILE *fp; int pkgstart; TOC *tocbuff; TOC *tocend; COOKIE cookie;\n"
    code += "    char archivename[_MAX_PATH + 1]; char homepath[_MAX_PATH + 1];\n"
    code += "    char temppath[_MAX_PATH + 1]; char homepathraw[_MAX_PATH + 1];\n"
    code += "    char temppathraw[_MAX_PATH + 1];} ARCHIVE_STATUS;\n"
    code += "int init(ARCHIVE_STATUS *%s, char const * %s, char  const * %s);\n" %(randomString(), randomString(), randomString())
    code += "int extractBinaries(ARCHIVE_STATUS *%s[]);\n" %(randomString())
    code += "int doIt(ARCHIVE_STATUS *%s, int %s, char *%s[]);\n" %(randomString(), randomString(), randomString())
    code += "int callSimpleEntryPoint(char *%s, int *%s);\n" %(randomString(), randomString())
    code += "void cleanUp(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "int getPyVersion(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "void finalizePython(void);\n"
    code += "int setPaths(ARCHIVE_STATUS *%s, char const * %s, char const * %s);\n" %(randomString(), randomString(), randomString())
    code += "int openArchive(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "int attachPython(ARCHIVE_STATUS *%s, int *%s);\n" %(randomString(), randomString())
    code += "int loadPython(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "int startPython(ARCHIVE_STATUS *%s, int %s, char *%s[]);\n" %(randomString(), randomString(), randomString())
    code += "int importModules(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "int installZlibs(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "int runScripts(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "TOC *getFirstTocEntry(ARCHIVE_STATUS *%s);\n" %(randomString())
    code += "TOC *getNextTocEntry(ARCHIVE_STATUS *%s, TOC *%s);\n" %(randomString(), randomString())
    code += "void clear(const char *%s);\n" %(randomString())
    code += "#endif\n"

    # replace all method names with their randomized choices from the passed list
    for m in methodSubs: code = code.replace(m[0], m[1])

    return code


def generate_runwrc():
    """
    Generate Pwnstaller's runw.rc code
    """
    code = "#include \"resource.h\"\n"
    code += "#define APSTUDIO_READONLY_SYMBOLS\n"
    code += "#include \"windows.h\"\n"
    code += "#undef APSTUDIO_READONLY_SYMBOLS\n"
    code += "#if !defined(AFX_RESOURCE_DLL) || defined(AFX_TARG_ENU)\n"
    code += "#ifdef _WIN32\n"
    code += "LANGUAGE LANG_NEUTRAL, SUBLANG_NEUTRAL\n"

    # TODO: can this safely be randomized?
    code += "#pragma code_page(1252)\n"
    code += "#endif\n"

    # get a random icon
    # Creative Commons icons from https://www.iconfinder.com/search/?q=iconset%3Aflat-ui-icons-24-px
    #   license - http://creativecommons.org/licenses/by/3.0/
    code += "IDI_ICON1               ICON    DISCARDABLE     \"./icons/%s\"\n" %(random.choice(os.listdir("./source/icons")))
    code += "#endif\n"

    return code


# all methods in util.c paired with a randomized name to substitute in
util_methods = [    ('basename(',randomString()+"("), 
                    ('IsXPOrLater(',randomString()+"("), 
                    ('CreateActContext(',randomString()+"("), 
                    ('ReleaseActContext(',randomString()+"("), 
                    ('init_launcher(',randomString()+"("), 
                    ('get_thisfile(',randomString()+"("), 
                    ('get_thisfilew(',randomString()+"("), 
                    ('get_homepath(',randomString()+"("), 
                    ('get_archivefile(',randomString()+"("), 
                    ('set_environment(',randomString()+"("), 
                    ('spawn(',randomString()+"(")]


# all methods in util.c paired with a randomized name to substitute in
launch_methods = [  ("extract(", randomString()+"("),
                    ("getTempPath(", randomString()+"("),
                    ("checkFile(", randomString()+"("),
                    ("setPaths(", randomString()+"("),
                    ("checkCookie(", randomString()+"("),
                    ("openArchive(", randomString()+"("),
                    ("mapNames(", randomString()+"("),
                    ("loadPython(", randomString()+"("),
                    ("incrementTocPtr(", randomString()+"("),
                    ("startPython(", randomString()+"("),
                    ("importModules(", randomString()+"("),
                    ("installZlib(", randomString()+"("),
                    ("installZlibs(", randomString()+"("),
                    ("decompress(", randomString()+"("), 
                    ("extract(", randomString()+"("),
                    ("openTarget(", randomString()+"("),
                    ("createTempPath(", randomString()+"("),
                    ("extract2fs(", randomString()+"("),
                    ("splitName(", randomString()+"("),
                    ("copyFile(", randomString()+"("),
                    ("dirName(", randomString()+"("),
                    ("copyDependencyFromDir(", randomString()+"("),
                    ("get_archive(", randomString()+"("),
                    ("extractDependencyFromArchive(", randomString()+"("),
                    ("extractDependency(", randomString()+"("),
                    ("needToExtractBinaries(",randomString()+"("),
                    ("extractBinaries(", randomString()+"("),
                    ("runScripts(", randomString()+"("),
                    ("init(", randomString()+"("),
                    ("doIt(", randomString()+"("),
                    ("clear(", randomString()+"("),
                    ("removeOne(", randomString()+"("),
                    ("cleanUp(", randomString()+"("),
                    ("getPyVersion(", randomString()+"("),
                    ("finalizePython(", randomString()+"(")]


# main Pwnstaller generation method
def generate():

    # generate our utils.c source and utils.h declaration with
    # our randomized method name list
    (util_includes, util_source) = generate_utils()
    utils_h = generate_utils_h(util_methods)


    # generate our launch.c source and launch.h declaration with
    # our randomized method name list
    (launch_includes, launch_source) = generate_launch()
    launch_h = generate_launch_h(launch_methods)


    # generate main.c, nothing to sub in here as there's only WinMain()
    (main_includes, main_source) = generate_main()


    # generate our .rc source with a randomized icon
    rc_source = generate_runwrc()


    # build the total.c source of all the main three files (utils.c, launch.c, main.c)
    totalSource = util_includes
    totalSource += main_includes
    totalSource += launch_includes
    totalSource += util_source
    totalSource += launch_source
    totalSource += main_source


    # patch in util method randomizations
    for m in util_methods: totalSource = totalSource.replace(m[0], m[1])

    # patch in launch method randomizations
    for m in launch_methods: totalSource = totalSource.replace(m[0], m[1])

    # write out the utils.h file
    f = open("./source/common/utils.h", 'w')
    f.write(utils_h)
    f.close()

    # write out the launch.h file
    f = open("./source/common/launch.h", 'w')
    f.write(launch_h)
    f.close()

    # write all the main logic out
    f = open("./source/total.c", 'w')
    f.write(totalSource)
    f.close()

    # write out the resource declaration
    f = open("./source/runw.rc", 'w')
    f.write(rc_source)
    f.close()


# executes all the mingw32 commands needed to compile the new runw.exe
def compileRunw():
    
    libraries = []

    # "fake" libraries to include with compilation
    # taken from /usr/i686-w64-mingw32/lib/*
    fake_libraries = ['-laclui', '-ladvapi32', '-lapcups', '-lauthz', '-lavicap32', '-lavifil32', '-lbcrypt', '-lbootvid', '-lbthprops', '-lcap', '-lcfgmgr32', '-lclasspnp', '-lclfsw32', '-lclusapi', '-lcmutil', '-lcomctl32', '-lcomdlg32', '-lconnect', '-lcredui', '-lcrypt32', '-lcryptnet', '-lcryptsp', '-lcryptxml', '-lcscapi', '-lctl3d32', '-ld2d1', '-ld3d8', '-ld3d9', '-ld3dcompiler_33', '-ld3dcompiler_34', '-ld3dcompiler_35', '-ld3dcompiler_36', '-ld3dcompiler_37', '-ld3dcompiler_38', '-ld3dcompiler_39', '-ld3dcompiler_40', '-ld3dcompiler_41', '-ld3dcompiler_42', '-ld3dcompiler_43', '-ld3dcompiler', '-ld3dcsxd_43', '-ld3dcsxd', '-ld3dim', '-ld3drm', '-ld3dx10_33', '-ld3dx10_34', '-ld3dx10_35', '-ld3dx10_36', '-ld3dx10_37', '-ld3dx10_38', '-ld3dx10_39', '-ld3dx10_40', '-ld3dx10_41', '-ld3dx10_42', '-ld3dx10_43', '-ld3dx10', '-ld3dx11_42', '-ld3dx11_43', '-ld3dx11', '-ld3dx8d', '-ld3dx9_24', '-ld3dx9_25', '-ld3dx9_26', '-ld3dx9_27', '-ld3dx9_28', '-ld3dx9_29', '-ld3dx9_30', '-ld3dx9_31', '-ld3dx9_32', '-ld3dx9_33', '-ld3dx9_34', '-ld3dx9_35', '-ld3dx9_36', '-ld3dx9_37', '-ld3dx9_38', '-ld3dx9_39', '-ld3dx9_40', '-ld3dx9_41', '-ld3dx9_42', '-ld3dx9_43', '-ld3dx9', '-ld3dx9d', '-ld3dxof', '-ldavclnt', '-ldbgeng', '-ldbghelp', '-lddraw', '-ldelayimp', '-ldhcpcsvc6', '-ldhcpcsvc', '-ldhcpsapi', '-ldinput8', '-ldinput', '-ldlcapi', '-ldmoguids', '-ldnsapi', '-ldplayx', '-ldpnaddr', '-ldpnet', '-ldpnlobby', '-ldpvoice', '-ldsetup', '-ldsound', '-ldssec', '-ldwmapi', '-ldwrite', '-ldxapi', '-ldxerr8', '-ldxerr9', '-ldxgi', '-ldxguid', '-ldxva2', '-leapp3hst', '-leappcfg', '-leappgnui', '-leapphost', '-leappprxy', '-lesent', '-levr', '-lfaultrep', '-lfwpuclnt', '-lgdi32', '-lgdiplus', '-lglaux', '-lglu32', '-lglut32', '-lglut', '-lgmon', '-lgpapi', '-lgpedit', '-lgpprefcl', '-lgpscript', '-lgptext', '-lhal', '-lhid', '-lhidclass', '-lhidparse', '-lhttpapi', '-licmui', '-ligmpagnt', '-limagehlp', '-limm32', '-liphlpapi', '-liscsidsc', '-lkernel32', '-lks', '-lksproxy', '-lksuser', '-lktmw32', '-llargeint', '-llz32', '-lm', '-lmangle', '-lmapi32', '-lmcd', '-lmf', '-lmfcuia32', '-lmfplat', '-lmgmtapi', '-lmoldname', '-lmpr', '-lmprapi', '-lmqrt', '-lmsacm32', '-lmscms', '-lmsctfmonitor', '-lmsdmo', '-lmsdrm', '-lmshtml', '-lmshtmled', '-lmsi', '-lmsimg32', '-lmstask', '-lmswsock', '-lncrypt', '-lnddeapi', '-lndfapi', '-lndis', '-lnetapi32', '-lnewdev', '-lnormaliz', '-lntdll', '-lntdsapi', '-lntmsapi', '-lntoskrnl', '-lodbc32', '-lodbccp32', '-lole32', '-loleacc', '-loleaut32', '-lolecli32', '-loledlg', '-lolepro32', '-lolesvr32', '-lopengl32', '-lp2p', '-lp2pcollab', '-lp2pgraph', '-lpcwum', '-lpdh', '-lpdhui', '-lpenwin32', '-lpkpd32', '-lpowrprof', '-lpsapi', '-lpseh', '-lquartz', '-lqutil', '-lqwave', '-lrapi', '-lrasapi32', '-lrasdlg', '-lresutil', '-lrpcdce4', '-lrpcdiag', '-lrpchttp', '-lrpcns4', '-lrpcrt4', '-lrstrmgr', '-lrtm', '-lrtutils', '-lscrnsave', '-lscrnsavw', '-lscsiport', '-lsecur32', '-lsetupapi', '-lshell32', '-lshfolder', '-lshlwapi', '-lslc', '-lslcext', '-lslwga', '-lsnmpapi', '-lspoolss', '-lsspicli', '-lstrmiids', '-lsvrapi', '-lsxs', '-ltapi32', '-ltbs', '-ltdh', '-ltdi', '-ltxfw32', '-lurl', '-lusbcamd2', '-lusbcamd', '-lusbd', '-lusbport', '-luser32', '-luserenv', '-lusp10', '-luuid', '-luxtheme', '-lvdmdbg', '-lversion', '-lvfw32', '-lvideoprt', '-lvirtdisk', '-lvssapi', '-lvss_ps', '-lvsstrace', '-lwdsclient', '-lwdsclientapi', '-lwdscore', '-lwdscsl', '-lwdsimage', '-lwdstptc', '-lwdsupgcompl', '-lwdsutil', '-lwecapi', '-lwer', '-lwevtapi', '-lwevtfwd', '-lwin32k', '-lwin32spl', '-lwininet', '-lwinmm', '-lwinscard', '-lwinspool', '-lwinstrm', '-lwinusb', '-lwlanapi', '-lwlanui', '-lwlanutil', '-lwldap32', '-lwow32', '-lws2_32', '-lwsdapi', '-lwsnmp32', '-lwsock32', '-lwst', '-lwtsapi32', '-lx3daudio1_2', '-lx3daudio1_3', '-lx3daudio1_4', '-lx3daudio1_5', '-lx3daudio1_6', '-lx3daudio1_7', '-lx3daudio', '-lx3daudiod1_7', '-lxapofx1_0', '-lxapofx1_1', '-lxapofx1_2', '-lxapofx1_3', '-lxapofx1_4', '-lxapofx1_5', '-lxapofx', '-lxapofxd1_5', '-lxaudio2_0', '-lxaudio2_1', '-lxaudio2_2', '-lxaudio2_3', '-lxaudio2_4', '-lxaudio2_5', '-lxaudio2_6', '-lxaudio2_7', '-lxaudio', '-lxaudiod2_7', '-lxaudiod', '-lxinput1_1', '-lxinput1_2', '-lxinput1_3', '-lxinput']

    # shuffle up all the libraries
    random.shuffle(fake_libraries)

    # include a random number of the randomized "fake" libraries, between 4-15
    for x in xrange(0, random.randint(5,15)):
        libraries.append(fake_libraries[x])

    # do it all up yo'
    os.system('mkdir build')
    os.system('i686-w64-mingw32-windres -DWIN32 -DWINDOWED -I./source/zlib -I./source/common -IC:\\\\Python27\\\\include -o ./build/runw.rc.o -i ./source/runw.rc')
    os.system('i686-w64-mingw32-gcc -Wdeclaration-after-statement -mms-bitfields -m32 -O2 -fno-strict-aliasing -I./source/zlib -I./source/common -IC:\\\\Python27\\\\include -DWIN32 -DWINDOWED ./source/total.c -c -o ./build/total.o')
    os.system('i686-w64-mingw32-gcc ./build/runw.rc.o ./build/total.o -o runw.exe -Wl,--enable-auto-import -mwindows -Wl,-Bstatic -Lreleasew -LC:\\\\Python27\\\\libs -Wl,-Bstatic -L./source/ -lstaticlib_zlib -Wl,-Bdynamic -luser32 -lcomctl32 -lkernel32 -lws2_32 ' + " ".join(libraries))
    os.system('rm -rf build')



if __name__=='__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument('-o', metavar="OUTPUTFILE", help='Output name/path for the runw.exe executable.')
    parser.add_argument('--copy', action='store_true', help='Copy the final exectuable to the Pyinstaller location.')
    parser.add_argument('--nocopy', action='store_true', help='Don\'t copy the final executable.')
    args = parser.parse_args()

    os.system('clear')

    print ""
    print "========================================================================="
    print " Pwnstaller | [Version]: %s" %(VERSION) 
    print "========================================================================="
    print " [Web]: http://harmj0y.net/ | [Twitter]: @harmj0y"
    print "========================================================================="
    print "\n"

    # check the needed depencies
    checkDeps()

    print " [*] Generating new runw source files...\n"

    # generate the new source files
    generate()

    print " [*] Compiling a new runw.exe...\n"

    # compile it all up
    compileRunw()

    # move the file to the new path/name if specified
    if args.o:
        os.system("mv runw.exe " + args.o )
        print " [*] Output file: %s\n" %(args.o)

    print " [*] Generation complete!\n"

    # skip if no copy for the exe is specified
    if not args.nocopy:
        if os.path.isdir('/usr/share/pyinstaller'):
            if not args.copy:
                choice = raw_input(" [>] Copy runw.exe to /usr/share/pyinstaller/support/loader/Windows-32bit/? [Y/n] ")
                if choice != "" and choice.lower()[0] == "y":
                    os.system('cp runw.exe /usr/share/pyinstaller/support/loader/Windows-32bit/')
            else:
                os.system('cp runw.exe /usr/share/pyinstaller/support/loader/Windows-32bit/')
                print " [*] runw.exe copied to/usr/share/pyinstaller/support/loader/Windows-32bit/\n"
        elif os.path.isdir('/opt/pyinstaller-2.0'):
            if not args.copy:
                choice = raw_input(" [>] Copy runw.exe to /opt/pyinstaller-2.0/support/loader/Windows-32bit/? [Y/n] ")
                if choice != "" and choice.lower()[0] == "y":
                    os.system('cp runw.exe /opt/pyinstaller-2.0/support/loader/Windows-32bit/')
            else:
                os.system('cp runw.exe /opt/pyinstaller-2.0/support/loader/Windows-32bit/')
                print " [*] runw.exe copied to /opt/pyinstaller-2.0/support/loader/Windows-32bit/\n"
        else:
            print " [!] Could not find pyinstalled installation!"
            print " [*] Move runw.exe to pyinstaller/support/loader/Windows-32bit/\n\n"

        print ""

