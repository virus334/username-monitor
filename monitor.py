
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone

USERNAME = "3az29"
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()


def notify(message):
    if not NTFY_TOPIC:
        print("ERROR: NTFY_TOPIC secret is missing.")
        return False

    request = urllib.request.Request(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": "Instagram Username Monitor",
            "Priority": "default",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            print(f"Notification sent. HTTP {response.status}")
            return True
    except Exception as error:
        print(f"Notification failed: {type(error).__name__}")
        return False


def check_instagram():
    url = f"https://www.instagram.com/{USERNAME}/"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            print(f"Instagram HTTP status: {response.status}")
            print(
                "INCONCLUSIVE: A successful page response does not "
                "prove that the username is available."
            )
            return "inconclusive"

    except urllib.error.HTTPError as error:
        print(f"INCONCLUSIVE: Instagram returned HTTP {error.code}.")
        print("A public profile check cannot confirm username availability.")
        return "inconclusive"

    except Exception as error:
        print(f"INCONCLUSIVE: Request failed ({type(error).__name__}).")
        return "error"


def main():
    print("Check time:", datetime.now(timezone.utc).isoformat())
    print(f"Username: @{USERNAME}")

    result = check_instagram()

    # Temporary test: send one notification on every run.
    message = (
        f"Monitor ran for @{USERNAME}.\n"
        f"Check result: {result}.\n"
        "Username availability is NOT confirmed."
    )
    notify(message)


if __name__ == "__main__":
    main()