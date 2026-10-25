
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone

USERNAME = "3az29"
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()


def notify(message):
    if not NTFY_TOPIC:
        print("Notification skipped: NTFY_TOPIC is not configured.")
        return

    # Send the topic as the URL path, without exposing it in logs.
    url = "https://ntfy.sh/" + NTFY_TOPIC
    request = urllib.request.Request(
        url,
        data=message.encode("utf-8"),
        headers={
            "Title": "Instagram Username Monitor",
            "Priority": "default",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            print(f"Notification sent. HTTP {response.status}")
    except Exception as error:
        print(f"Notification failed: {type(error).__name__}")


def main():
    print("Check time:", datetime.now(timezone.utc).isoformat())
    print(f"Username: @{USERNAME}")

    url = f"https://www.instagram.com/{USERNAME}/"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
            page = response.read(500000).decode("utf-8", errors="replace")

        print(f"Instagram HTTP status: {status}")

        if status == 200:
            print(
                "INCONCLUSIVE: Instagram returned a page. "
                "This does not prove the username is available."
            )
        else:
            print("INCONCLUSIVE: Availability could not be confirmed.")

    except urllib.error.HTTPError as error:
        print(f"INCONCLUSIVE: Instagram returned HTTP {error.code}.")
        print("A public profile check cannot confirm username availability.")

    except Exception as error:
        print(f"INCONCLUSIVE: Request failed ({type(error).__name__}).")

    print("No availability claim will be made from this check.")


if __name__ == "__main__":
    main()
