import socket
import requests
import treq
from twisted.python import log
import cowrie.core.output
from cowrie.core.config import CowrieConfig


def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "No PTR Record"


def geo_lookup(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        data = r.json()
        if data.get("status") == "success":
            return f"{data['country']}, {data['regionName']}, {data['city']} | ISP: {data['isp']}"
        else:
            return "Geo info not found"
    except Exception:
        return "Geo API error"


class Output(cowrie.core.output.Output):
    """
    Telegram output plugin for Cowrie with geo-IP and reverse DNS lookup
    """

    def start(self):
        self.bot_token = CowrieConfig.get("output_telegram", "bot_token")
        self.chat_id = CowrieConfig.get("output_telegram", "chat_id")

    def stop(self):
        pass

    def write(self, event):
        for key in list(event.keys()):
            if key.startswith("log_"):
                del event[key]

        logon_type = ""
        if "HoneyPotSSHTransport" in (event.get("system", "").split(","))[0]:
            logon_type = "SSH"
        elif "CowrieTelnetTransport" in (event.get("system", "").split(","))[0]:
            logon_type = "Telnet"

        src_ip = event.get("src_ip", "Unknown")
        hostname = reverse_dns(src_ip)
        geoinfo = geo_lookup(src_ip)

        msgtxt = "<strong>[Cowrie {0}]</strong>".format(event.get("sensor", "unknown"))
        msgtxt += "\nEvent: {0}".format(event.get("eventid", "unknown"))
        msgtxt += "\nLogon type: {0}".format(logon_type)
        msgtxt += "\nSource IP: <code>{0}</code>".format(src_ip)
        msgtxt += "\nReverse DNS: <code>{0}</code>".format(hostname)
        msgtxt += "\nGeo Info: <code>{0}</code>".format(geoinfo)
        msgtxt += "\nSession: <code>{0}</code>".format(event.get("session", "N/A"))

        if event["eventid"] == "cowrie.login.success":
            msgtxt += "\nUsername: <code>{0}</code>".format(event.get("username", ""))
            msgtxt += "\nPassword: <code>{0}</code>".format(event.get("password", ""))
            self.send_message(msgtxt)

        elif event["eventid"] in ["cowrie.command.input", "cowrie.command.failed"]:
            msgtxt += "\nCommand: <pre>{0}</pre>".format(event.get("input", ""))
            self.send_message(msgtxt)

        elif event["eventid"] == "cowrie.session.file_download":
            msgtxt += "\nUrl: {0}".format(event.get("url", ""))
            self.send_message(msgtxt)

        elif event["eventid"] == "cowrie.session.closed":
            duration = event.get("duration", 0)
            try:
                msgtxt += "\nSession closed after: {0:.1f} seconds".format(float(duration))
            except (ValueError, TypeError):
                msgtxt += "\nSession closed after: unknown duration"
            self.send_message(msgtxt)

    def send_message(self, message):
        log.msg("Telegram plugin will try to call TelegramBot")
        try:
            treq.get(
                f"https://api.telegram.org/bot{self.bot_token}/sendMessage",
                params={
                    "chat_id": str(self.chat_id),
                    "parse_mode": "HTML",
                    "text": message,
                },
            )
        except Exception as e:
            log.msg(f"Telegram plugin request error: {e}")
