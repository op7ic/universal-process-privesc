By adjusting process token its possible to elevate your current process privileges to enable certain functionality not available otherwise.

Basically steps we follow are :
1) Get current process handle
2) Get current process token
3) Resolve SeDebugPrivilege value
4) Created new Token with the resolved value from step 3
5) Adjust the token of the current process with new privilege
6) Close process handle