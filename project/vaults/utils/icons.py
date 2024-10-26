from urllib.parse import urlparse

def get_icon_path(url):
        icon_map = {
            "facebook.com": "/static/icons/service_icons/facebook.svg",
            "mail.google.com": "/static/icons/service_icons/gmail.svg",
            "godaddy.com": "/static/icons/service_icons/godaddy.svg",
            "instagram.com": "/static/icons/service_icons/instagram.svg",
            "outlook.live.com": "/static/icons/service_icons/outlook.svg",
            "x.com": "/static/icons/service_icons/x.svg",
        }
        try:
            domain = urlparse(url).hostname.replace("www.", "")
            return icon_map.get(domain, "/static/icons/service_icons/globe.svg")
        except:
            return "/static/icons/service_icons/globe.svg"