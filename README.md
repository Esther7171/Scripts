```
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.13.0-1.msi -OutFile $env:tmp\wazuh-agent; msiexec.exe /i $env:tmp\wazuh-agent /q WAZUH_MANAGER='122.160.144.106' WAZUH_AGENT_GROUP='Netcomm' WAZUH_AGENT_NAME='netcomm-2' 
```

# I'm creating Scripts to automate my daily base task adding some scripts here that help everone.

# To make scripts as commands.
```
git clone https://github.com/Esther7171/Scripts
cd Scripts
sudo mv <script> /usr/local/bin
```


<!--
```
service
```
```
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico --add-data "logo.png;." --manifest admin.manifest zerosync.py
```


