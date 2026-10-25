
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone

USERNAME = "3az29"
URL = f"https://www.instagram.com/{USERNAME}/"

req = urllib.request.Request(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

print(f"Check time: {datetime.now(timezone.utc).isoformat()}")
print(f"Username: @{USERNAME}")

try:
    with urllib.request.urlopen(req, timeout=20) as response:
        page = response.read().decode("utf-8", errors="ignore")
        status = response.status

    if status == 200 and "Page Not Found" not in page:
        print("Profile page responded; username may be reserved or active.")
    else:
        print("INCONCLUSIVE: response does not prove availability.")

except urllib.error.HTTPError as e:
    print(f"INCONCLUSIVE: Instagram returned HTTP {e.code}.")
except Exception as e:
    print(f"INCONCLUSIVE: {type(e).__name__}: {e}")

print("A public profile check cannot confirm username availability.")
