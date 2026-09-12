"""
Jovia Network — SESSION_STRING generator
=========================================
Run this once (on Termux, your laptop, anywhere with Python) to log
into the Telegram account you want the bot to use, and print a
SESSION_STRING you paste into your host's env vars (Railway, etc.) —
so the deployed bot never has to do an interactive login.

USAGE (Termux on Android)
--------------------------
1. Install Termux from F-Droid (the Play Store build is outdated and
   often broken — get it from https://f-droid.org/packages/com.termux/).

2. In Termux, install Python and pip:
       pkg update -y && pkg upgrade -y
       pkg install -y python

3. Install Telethon:
       pip install telethon

4. Get your API_ID and API_HASH from https://my.telegram.org
   (log in -> API Development Tools -> create an app if you haven't).

5. Put this file on the phone (e.g. via Termux's `nano get_session.py`
   and paste it in, or `curl`/transfer it over), then run:
       python get_session.py

6. It will ask for API_ID, API_HASH, your phone number (international
   format, e.g. +2348012345678), the login code Telegram sends you,
   and your 2FA password if you have one set.

7. It prints a long string starting with "1A..." — that is your
   SESSION_STRING. Copy the ENTIRE string (it's long, one line, no
   spaces) and set it as the SESSION_STRING environment variable
   wherever you deploy bot.py (Railway/Render/etc.).

SECURITY NOTE
-------------
Treat SESSION_STRING exactly like your Telegram password — anyone who
has it can log in as you with full account access. Never commit it to
git, never paste it in a chat, never share it publicly. If it ever
leaks, immediately terminate that session from Telegram's
Settings -> Devices on your phone, then generate a fresh one.
"""

from telethon import TelegramClient
from telethon.sessions import StringSession

def main():
    print("=" * 60)
    print("Jovia Network — Telegram SESSION_STRING generator")
    print("=" * 60)

    api_id = input("API_ID: ").strip()
    api_hash = input("API_HASH: ").strip()

    while not api_id.isdigit():
        print("API_ID must be a number.")
        api_id = input("API_ID: ").strip()

    with TelegramClient(StringSession(), int(api_id), api_hash) as client:
        session_string = client.session.save()
        print("\n" + "=" * 60)
        print("SUCCESS — your SESSION_STRING is below.")
        print("Copy the FULL string (one line, no spaces) and set it as")
        print("the SESSION_STRING env var wherever bot.py runs.")
        print("=" * 60)
        print(session_string)
        print("=" * 60)
        print("\nKeep this private — it's equivalent to your Telegram login.")


if __name__ == "__main__":
    main()
