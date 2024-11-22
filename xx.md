```
curl -o wazuh-agent-4.8.2-1.x86_64.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.8.2-1.x86_64.rpm && sudo WAZUH_MANAGER='uh452fu13dg3.cloud.wazuh.com' WAZUH_REGISTRATION_PASSWORD=$'aiTH5fWXZHEdLE9M42li8chzepmeecxV' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='TEST' rpm -ihv wazuh-agent-4.8.2-1.x86_64.rpm
```

```
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```
```
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.8.2-1.msi -OutFile ${env.tmp}\wazuh-agent; msiexec.exe /i ${env.tmp}\wazuh-agent /q WAZUH_MANAGER='uh452fu13dg3.cloud.wazuh.com' WAZUH_REGISTRATION_PASSWORD='aiTH5fWXZHEdLE9M42li8chzepmeecxV' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='TEST'
```
```
NET START WazuhSvc
```
```
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.8.2-1.msi -OutFile ${env.tmp}\wazuh-agent; msiexec.exe /i ${env.tmp}\wazuh-agent /q WAZUH_MANAGER='uh452fu13dg3.cloud.wazuh.com' WAZUH_REGISTRATION_PASSWORD='aiTH5fWXZHEdLE9M42li8chzepmeecxV' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='Windows'
```
```
NET START WazuhSvc
```
```
.\wazuh-agent-4.8.2-1.msi /q WAZUH_MANAGER="uh452fu13dg3.cloud.wazuh.com"
```
