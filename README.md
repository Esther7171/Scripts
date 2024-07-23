C13z49vRyXAGQtZce4tYqzVdN72h5N
sudo pro attach C13z49vRyXAGQtZce4tYqzVdN72h5N





# Update && Full-Upgrade
```bash
#!/bin/bash
clear
echo -e "\e[1;33m________________________________________\e[0m" #orange
echo ""
echo -e "\e[7;1;5;33m U P D A T I N G  I N  P R O G R E S S \e[0m" 
echo -e "\e[1;33m________________________________________\e[0m"
echo ""
never=$(sudo apt-get update -y)
clear
echo -e "\e[1;31m________________________________________\e[0m" #red
echo ""
echo -e "\e[7;1;5;31m U P G R A D E   I N   P R O G R E S S \e[0m"
echo -e "\e[1;31m________________________________________\e[0m"
sleep 2s
echo ""
bankai=$(sudo apt-get upgrade -y)
clear
echo -e "\e[1;35m_____________________________________________________\e[0m" #purple
echo ""
echo -e "\e[7;1;5;35m D I S T R O - U P G R A D E   I N   P R O G R E S S \e[0m"
echo -e "\e[1;35m_____________________________________________________\e[0m"
sleep 2s
echo ""
mcat=$(sudo apt-get dist-upgrade -y)
clear
echo -e "\e[1;34m_________________________________________________\e[0m"  #blue
echo ""
echo -e "\e[7;1;5;34m F U L L - U P G R A D E   I N   P R O G R E S S \e[0m"
echo -e "\e[1;34m_________________________________________________\e[0m"
echo ""
sleep 2s
kill=(sudo apt-get full-update -y)
clear
echo -e "\e[1;32m_______________________________________\e[0m" #green
echo ""
echo -e "\e[7;1;5;32m C L E A N I N G  I N  P R O G R E S S \e[0m"
echo -e "\e[1;32m_______________________________________\e[0m"
sleep 2s
echo ""
shadeep=$(sudo apt-get autoremove -y)
clear
echo -e "\e[1;33m__________________________________________\e[0m"
echo ""
echo -e "\e[7;1;5;33m            A L L  D O N E            \e[0m"
echo -e "\e[1;33m___________________________________________\e[0m"
sleep 2s
clear
exit
```
