import os

from dotenv import load_dotenv


load_dotenv()



# =========================
# CONFIG
# =========================

RELAY_ENABLED = (
    os.getenv(
        "RELAY_ENABLED",
        "false"
    ).lower()
    == "true"
)



# =========================
# RELAY MESSAGE
# =========================

async def relay_message(message):


    if not message:

        return



    # =========================
    # PREVIEW
    # =========================

    print(message)



    # =========================
    # TWITCH RELAY CONTROL
    # =========================

    if not RELAY_ENABLED:

        return



    # =========================
    # SEND TO TWITCH
    # =========================

    await send_to_twitch(
        message
    )



# =========================
# TWITCH CONNECTOR
# =========================

async def send_to_twitch(
    message
):


    try:

        from twitch_bot import send_to_twitch as twitch_send


        await twitch_send(
            message
        )


    except Exception as e:


        print("==============================")
        print("[RELAY TWITCH ERROR]")
        print(e)
        print("==============================")