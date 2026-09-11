import os

from dotenv import load_dotenv

from twitchio.ext import commands



# =========================
# LOAD ENV
# =========================

load_dotenv()



# =========================
# CONFIG
# =========================

BOT_USERNAME = os.getenv(
    "TWITCH_BOT_USERNAME"
)

BOT_ID = os.getenv(
    "TWITCH_BOT_ID"
)

CLIENT_ID = os.getenv(
    "TWITCH_CLIENT_ID"
)

CLIENT_SECRET = os.getenv(
    "TWITCH_CLIENT_SECRET"
)

TOKEN = os.getenv(
    "TWITCH_TOKEN"
)

CHANNEL = os.getenv(
    "TWITCH_CHANNEL"
)

BROADCASTER_ID = os.getenv(
    "TWITCH_BROADCASTER_ID"
)



# =========================
# CHANNEL CACHE
# =========================

twitch_channel = None



# =========================
# TWITCH BOT
# =========================

class TwitchBot(commands.Bot):


    def __init__(self):


        if not TOKEN:

            raise Exception(
                "TWITCH_TOKEN missing"
            )


        if not BROADCASTER_ID:

            raise Exception(
                "TWITCH_BROADCASTER_ID missing"
            )


        if not BOT_ID:

            raise Exception(
                "TWITCH_BOT_ID missing"
            )


        super().__init__(

            token=TOKEN,

            client_id=CLIENT_ID,

            client_secret=CLIENT_SECRET,

            prefix="!",

            initial_channels=[

                CHANNEL

            ]

        )



    # =====================
    # READY
    # =====================

    async def event_ready(self):

        global twitch_channel


        print("==============================")
        print("TWITCH BOT CONNECTED")
        print("==============================")


        print(
            f"Bot : {BOT_USERNAME}"
        )


        print(
            f"Channel : {CHANNEL}"
        )



        users = await self.fetch_users(

            ids=[

                BROADCASTER_ID

            ]

        )


        if users:

            twitch_channel = users[0]


            print(
                "CHANNEL READY"
            )



    # =====================
    # CHAT LISTENER
    # =====================

    async def event_message(
        self,
        message
    ):


        if message.echo:

            return



        print(
            f"{message.author.name}: {message.content}"
        )



# =========================
# INSTANCE
# =========================

bot = TwitchBot()



# =========================
# SEND MESSAGE
# =========================

async def send_to_twitch(
    message
):


    try:


        if twitch_channel is None:

            print(
                "[TWITCH] Channel not ready"
            )

            return



        await twitch_channel.send_message(

            message,

            BOT_ID

        )



        print("==============================")
        print("[TWITCH SENT]")
        print(message)
        print("==============================")


    except Exception as e:


        print("==============================")
        print("[TWITCH ERROR]")
        print(e)
        print("==============================")



# =========================
# START
# =========================

async def start_twitch():

    await bot.start()



# =========================
# STOP
# =========================

async def stop_twitch():

    await bot.close()