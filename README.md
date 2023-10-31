# Update && Full-Upgrade
```bash
#!/bin/bash
dog="sudo apt-get -y "
meow="sleep 3s"
hii="clear"

echo "*********************"
echo "Updating Your Linux"
echo "*********************"
$meow
$dog update
$hii 
echo "**************************"
echo "Your Linux gonna Upgrade"
echo "**************************"
$meow
$dog upgrade
$hii
echo "**************************"
echo "Your Distro gonna Upgrade"  
echo "**************************"  
$meow
$dog dist-upgrade
$hii
echo "**********************************"
echo " Now Full Upgrade is on the Way"  
echo "**********************************"
$meow
$dog full-upgrade
$hii
echo "************************"
echo " Cleaning your Machine"
echo "************************"
$meow
$dog autoremove
$hii
echo "*****************************"
echo " --SUCCESSFULLY--ALL--DONE--"
echo "*****************************"
```
