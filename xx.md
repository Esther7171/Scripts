```
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.8.2-1.msi -OutFile ${env.tmp}\wazuh-agent; msiexec.exe /i ${env.tmp}\wazuh-agent /q WAZUH_MANAGER='5qo5ykgau3yq.cloud.wazuh.com' WAZUH_REGISTRATION_PASSWORD='R3KK0nzRplNlI7fsCYYMHJTduzPoFVIE' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='amit-system-win'
```

```
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.8.2-1_amd64.deb && sudo WAZUH_MANAGER='5qo5ykgau3yq.cloud.wazuh.com' WAZUH_REGISTRATION_PASSWORD=$'R3KK0nzRplNlI7fsCYYMHJTduzPoFVIE' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='vitual-kali' dpkg -i ./wazuh-agent_4.8.2-1_amd64.deb
```
```
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```
