$BODY = "This machine's IP is " + ((Get-NetIPAddress).IPv4Address | Select-String "192*") + ". User is " + [System.Environment]::UserName + ". Hostname is " + (hostname) + ". PowerShell Version" + $HOST.Version.Major + ". Today's Date is " + (Get-Date -Format "dddd, MM dd yyyy")

$BODY | Out-File ~\machineinfo.txt