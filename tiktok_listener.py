import os

from dotenv import load_dotenv

from TikTokLive import TikTokLiveClient

from TikTokLive.events import (
    ConnectEvent,
    CommentEvent,
    FollowEvent,
    GiftEvent,
    DisconnectEvent
)


from formatter import (
    format_chat,
    format_follow,
    format_gift
)

from filter import should_send_chat

from relay_manager import relay_message

from gift_manager import add_gift



# =========================
# LOAD ENV
# =========================

load_dotenv()



# =========================
# CONFIG
# =========================

TIKTOK_USERNAME = os.getenv(
    "TIKTOK_USERNAME"
)


if not TIKTOK_USERNAME:

    raise ValueError(
        "TIKTOK_USERNAME belum ada di .env"
    )



# =========================
# CLIENT
# =========================

client = TikTokLiveClient(

    unique_id=TIKTOK_USERNAME

)



# =========================
# CLEAN USERNAME
# =========================

def clean_username(name):

    if not name:

        return "TikTok User"


    name = str(name).strip()


    if name == "":

        return "TikTok User"


    return name



# =========================
# CONNECT
# =========================

@client.on(ConnectEvent)
async def on_connect(event):

    print("==============================")
    print("CONNECTED TO TIKTOK LIVE")
    print("==============================")


    print(
        f"Room ID: {event.room_id}"
    )



# =========================
# CHAT
# =========================

@client.on(CommentEvent)
async def on_comment(event):


    username = clean_username(
        event.user.nickname
    )


    message = event.comment



    if not should_send_chat(

        username,

        message

    ):

        return



    output = format_chat(

        username,

        message

    )


    await relay_message(

        output

    )



# =========================
# FOLLOW
# =========================

@client.on(FollowEvent)
async def on_follow(event):


    username = clean_username(

        event.user.nickname

    )


    output = format_follow(

        username

    )


    await relay_message(

        output

    )



# =========================
# GIFT CALLBACK
# =========================

async def send_gift_preview(

    username,

    gift_name,

    count

):


    output = format_gift(

        username,

        gift_name,

        count

    )


    await relay_message(

        output

    )



# =========================
# GIFT EVENT
# =========================

@client.on(GiftEvent)
async def on_gift(event):


    username = clean_username(

        event.user.nickname

    )


    gift_name = event.gift.name



    # =========================
    # HANDLE GIFT STREAK
    # =========================
    #
    # TikTok gift menggunakan
    # sistem streak/combo.
    #
    # Saat user melakukan combo:
    #
    # Rose x1
    # Rose x5
    # Rose x13
    #
    # TikTokLive dapat mengirim
    # beberapa event.
    #
    # Kita hanya proses event
    # terakhir saat streak selesai.
    #


    if hasattr(

        event,

        "streaking"

    ):


        if event.streaking:

            return



    # =========================
    # FINAL COUNT
    # =========================
    #
    # repeat_count pada event
    # terakhir berisi jumlah
    # gift final.
    #

    count = getattr(

        event,

        "repeat_count",

        1

    )



    await add_gift(

        username,

        gift_name,

        send_gift_preview,

        count

    )



# =========================
# DISCONNECT
# =========================

@client.on(DisconnectEvent)
async def on_disconnect(event):

    print("==============================")
    print("TIKTOK DISCONNECTED")
    print("==============================")



# =========================
# MAIN
# =========================

def main():

    print("==============================")
    print("TIKTOK PREVIEW RELAY STARTED")
    print("==============================")


    print(
        f"Listening: @{TIKTOK_USERNAME}"
    )



    try:

        client.run()



    except KeyboardInterrupt:


        print()

        print("==============================")
        print("MANUAL STOP")
        print("==============================")



    except Exception as e:


        print()

        print("==============================")
        print("TIKTOK ERROR")
        print(type(e).__name__)
        print(e)

        print("==============================")



    finally:


        print()

        print("==============================")
        print("RELAY CLOSED")
        print("==============================")



if __name__ == "__main__":

    main()