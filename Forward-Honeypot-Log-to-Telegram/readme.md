# Cowrie Telegram Output Plugin with GeoIP and DNS Enrichment

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
**Real-time Telegram alerts for Cowrie honeypot, enhanced with GeoIP and reverse DNS information.**

---

## Features

* Sends Cowrie honeypot logs to a Telegram chat.
* Supports event types:

  * `cowrie.login.success`
  * `cowrie.command.input`
  * `cowrie.command.failed`
  * `cowrie.session.file_download`
  * `cowrie.session.closed`
* Enriches data with:

  * Reverse DNS Lookup
  * GeoIP (Country, Region, City, ISP)

---

## File Placement

Save this file as:

```
cowrie/src/cowrie/output/telegram.py
```

---

## Configuration

Edit your `cowrie.cfg` file:

```ini
[output_telegram]
enabled = true
bot_token = YOUR_TELEGRAM_BOT_TOKEN
chat_id = YOUR_TELEGRAM_CHAT_ID
```

### How to Get Your Bot Token and Chat ID

1. Create a bot using [@BotFather](https://t.me/BotFather) and copy the token.
2. Start a chat with your bot.
3. Visit:

   ```
   https://api.telegram.org/bot<your_bot_token>/getUpdates
   ```

   Look for the `chat_id` in the response (e.g., `"chat":{"id":12345678,...}`).

---

## Example Output

```
[Cowrie sensor1]
Event: cowrie.login.success
Logon type: SSH
Source IP: 203.0.113.1
Reverse DNS: example.com
Geo Info: United States, California, San Jose | ISP: AT&T
Session: abc123
Username: root
Password: toor
```

---

## Dependencies

Make sure these modules are installed:

```bash
pip install treq requests
```

---

## Restart Cowrie

After placing the file and editing the config, restart Cowrie:

```bash
./bin/cowrie stop
./bin/cowrie start
```
![image](https://github.com/user-attachments/assets/fff182d4-555e-4190-91e9-c78a7daf6074)

Add a rediection to port 22
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 2222 -j REDIRECT --to-port 22
```
