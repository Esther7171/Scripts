1. Bash Script (System Update + Logging)

Install python-docx system-wide (Recommended)

Run:
```
sudo apt update
sudo apt install python3-docx -y
```
If you already used pip (common mistake)
You probably did:
```
sudo pip3 install python-docx --break-system-packages
```

Create script:
```
sudo nano /usr/local/bin/weekly_update.sh
```
Paste:
```
#!/bin/bash

LOG_DIR="/var/log/maintainance"
LOG_FILE="$LOG_DIR/maintainance.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')
USER_HOME=$(eval echo ~${SUDO_USER:-$USER})
REPORT_DIR="$USER_HOME/Documents/maintainance"

mkdir -p $LOG_DIR
mkdir -p $REPORT_DIR

echo "[$DATE] Starting weekly update..." >> $LOG_FILE

# Run update
apt update >> $LOG_FILE 2>&1
apt upgrade -y >> $LOG_FILE 2>&1

if [ $? -eq 0 ]; then
    STATUS="SUCCESS"
    echo "[$DATE] Update completed successfully." >> $LOG_FILE
else
    STATUS="FAILED"
    echo "[$DATE] Update failed!" >> $LOG_FILE
fi

# Call Python script to generate Word report
python3 /usr/local/bin/log_to_docx.py "$LOG_FILE" "$REPORT_DIR" "$STATUS"

echo "[$DATE] Report generated." >> $LOG_FILE
```
Make executable:
```
sudo chmod +x /usr/local/bin/weekly_update.sh
```

2. Cron Job (Monday 8 AM)

Edit cron:
```
sudo crontab -e
```
Add:
```
0 8 * * 1 /usr/local/bin/weekly_update.sh
```

3. Log Rotation (Keeps logs small)

Create:
```
sudo nano /etc/logrotate.d/maintainance
```
Paste:
```
/var/log/maintainance/maintainance.log {
    weekly
    rotate 4
    compress
    missingok
    notifempty
}
```

4. Python Script (Log → Word Report)

Install dependency:
```
pip install python-docx
```
Create script:
```
sudo nano /usr/local/bin/log_to_docx.py
```
Paste:
```
from docx import Document
from docx.shared import Pt
import sys
import datetime
import os
import socket
import hashlib
import subprocess

log_file = sys.argv[1]
report_dir = sys.argv[2]
status = sys.argv[3]

# Create document
doc = Document()

# ===== HEADER =====
doc.add_heading('LokCapital Company', 0)
doc.add_paragraph('IT Infrastructure Maintenance Compliance Report')

# ===== META INFO =====
now = datetime.datetime.now()
hostname = socket.gethostname()

doc.add_paragraph(f"Report Generated: {now}")
doc.add_paragraph(f"System Hostname: {hostname}")
doc.add_paragraph(f"Overall Status: {status}")

# ===== SYSTEM INFO TABLE =====
doc.add_heading('System Information', level=1)

table = doc.add_table(rows=4, cols=2)
table.style = 'Table Grid'

table.cell(0,0).text = 'Parameter'
table.cell(0,1).text = 'Value'

table.cell(1,0).text = 'Hostname'
table.cell(1,1).text = hostname

# OS info
os_info = subprocess.getoutput("lsb_release -d")
table.cell(2,0).text = 'Operating System'
table.cell(2,1).text = os_info

kernel = subprocess.getoutput("uname -r")
table.cell(3,0).text = 'Kernel Version'
table.cell(3,1).text = kernel

# ===== UPDATE SUMMARY =====
doc.add_heading('Update Summary', level=1)

if status == "SUCCESS":
    doc.add_paragraph("✔ System updates installed successfully. System is compliant.")
else:
    doc.add_paragraph("✖ Update process failed. Immediate attention required.")

# ===== PATCH DETAILS =====
doc.add_heading('Recent Update Log (Summary)', level=1)

with open(log_file, 'r') as f:
    lines = f.readlines()[-15:]

for line in lines:
    doc.add_paragraph(line.strip())

# ===== LOG INTEGRITY =====
doc.add_heading('Log Integrity Verification', level=1)

with open(log_file, 'rb') as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

doc.add_paragraph(f"SHA256 Hash of Log File: {file_hash}")

# ===== COMPLIANCE CHECK TABLE =====
doc.add_heading('Compliance Checklist', level=1)

check_table = doc.add_table(rows=4, cols=3)
check_table.style = 'Table Grid'

check_table.cell(0,0).text = 'Control'
check_table.cell(0,1).text = 'Status'
check_table.cell(0,2).text = 'Remarks'

check_table.cell(1,0).text = 'Weekly Patch Applied'
check_table.cell(1,1).text = status
check_table.cell(1,2).text = 'Auto via cron'

check_table.cell(2,0).text = 'Log Generated'
check_table.cell(2,1).text = 'SUCCESS'
check_table.cell(2,2).text = 'Stored in /var/log/maintainance'

check_table.cell(3,0).text = 'Report Generated'
check_table.cell(3,1).text = 'SUCCESS'
check_table.cell(3,2).text = 'Saved in Documents'

# ===== SIGNATURE SECTION =====
doc.add_heading('Approval & Sign-off', level=1)

doc.add_paragraph("\nSystem Administrator: ________________________")
doc.add_paragraph("Signature: ________________________")
doc.add_paragraph("Date: ________________________\n")

doc.add_paragraph("Security Auditor: ________________________")
doc.add_paragraph("Signature: ________________________")
doc.add_paragraph("Date: ________________________")

# ===== SAVE FILE =====
os.makedirs(report_dir, exist_ok=True)

filename = f"{report_dir}/Maintenance_Report_{now.strftime('%Y%m%d_%H%M')}.docx"
doc.save(filename)

print("Enterprise report generated:", filename)
```
Make executable:
```
sudo chmod +x /usr/local/bin/log_to_docx.py
```

Check Permissions
```
sudo chmod +x /usr/local/bin/weekly_update.sh
sudo chmod +x /usr/local/bin/log_to_docx.py
```

Also ensure your user can access Documents:
```
sudo chown -R $USER:$USER ~/Documents/maintainance
```
