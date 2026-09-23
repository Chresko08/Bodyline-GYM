import urllib.request
import re

url = "https://maps.app.goo.gl/WcPwVtqRU2bPp93A9"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print("Redirected to:", response.url)
        matches = re.findall(r'https://lh5\.googleusercontent\.com/p/[a-zA-Z0-9_-]+', html)
        if matches:
            print(list(set(matches))[:10])
        else:
            matches2 = re.findall(r'https://[^"]*googleusercontent\.com/p/[a-zA-Z0-9_-]+', html)
            if matches2:
                print(list(set(matches2))[:10])
            else:
                print("No googleusercontent URLs found.")
except Exception as e:
    print(e)
