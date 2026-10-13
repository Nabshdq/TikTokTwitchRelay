import asyncio

from twitch_bot import (
    start_twitch,
    send_to_twitch,
    bot
)



async def main():

    print("==============================")
    print("TWITCH SEND TEST")
    print("==============================")


    # start bot

    task = asyncio.create_task(
        start_twitch()
    )


    # tunggu bot siap

    await asyncio.sleep(
        8
    )


    # kirim pesan

    await send_to_twitch(
        "Hello from TikTok Relay Test"
    )


    print("==============================")
    print("TEST MESSAGE SENT")
    print("==============================")


    await asyncio.sleep(
        3
    )


    await bot.close()



if __name__ == "__main__":

    asyncio.run(main())