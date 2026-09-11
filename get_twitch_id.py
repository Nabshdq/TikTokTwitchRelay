import os
import asyncio

from dotenv import load_dotenv
from twitchio import Client


# =========================
# LOAD ENV
# =========================

load_dotenv()


# =========================
# CONFIG
# =========================

CLIENT_ID = os.getenv(
    "TWITCH_CLIENT_ID"
)

CLIENT_SECRET = os.getenv(
    "TWITCH_CLIENT_SECRET"
)

TOKEN = os.getenv(
    "TWITCH_TOKEN"
)


# =========================
# TARGET USER
# =========================

TARGET_USERNAME = "parad0o0"



# =========================
# MAIN
# =========================

async def main():


    client = Client(

        client_id=CLIENT_ID,

        client_secret=CLIENT_SECRET

    )


    await client.login(

        token=TOKEN.replace(
            "oauth:",
            ""
        )

    )



    users = await client.fetch_users(

        logins=[

            TARGET_USERNAME

        ]

    )



    print("==============================")
    print("TWITCH USER LOOKUP")
    print("==============================")



    if users:


        user = users[0]


        print(
            f"Username : {user.name}"
        )


        print(
            f"User ID  : {user.id}"
        )


    else:


        print(
            "User tidak ditemukan"
        )



    await client.close()



# =========================
# RUN
# =========================

asyncio.run(main())