import requests as req
import os
os.system("color")

sites = (
    "tiktok.com/@",
)
flse_pos = (
    "facebook.com/",
    "youtube.com/user/",
    "twitter.com/",
    "reddit.com/user/",
    "steamcommunity.com/id/",
    "twitch.tv/",
    "instastory.net/profile/",
    "linkedin.com/in/"
)

user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

username = input("Enter username:")
for i in sites: # all results are valid
    url = "https://www." + i + username
    try:
        r = req.head(url, allow_redirects=True, headers = user_agent)
        if(r.status_code == 200):
            print("\033[1;92m" + str(r.status_code) + "\033[0m" + " | " + url)
        else:
            print("\033[1;91m" + str(r.status_code) + "\033[0m" + " | " + url)
    except:
        print("Bad Syntax")

url = "https://" + username + ".tumblr.com/"
try: # tumblr search
    r = req.head(url)
    if (r.status_code == 200):
        print("\033[1;92m" + str(r.status_code) + "\033[0m" + " | " + url)
    else:
        print("\033[1;91m" + str(r.status_code) + "\033[0m" + " | " + url)
except:
    print("Bad Syntax")

for i in flse_pos: # false positives
    url = "https://www." + i + username
    try:
        r = req.head(url, allow_redirects=True, headers = user_agent)
        if(r.status_code != 404):
            print("\033[1;93m" + str(r.status_code) + "\033[0m" + " | " + url)
        else:
            print("\033[1;91m" + str(r.status_code) + "\033[0m" + " | " + url)
    except:
        print("Bad Syntax")

input("Enter to leave")