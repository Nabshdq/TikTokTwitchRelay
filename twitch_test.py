import asyncio

from twitch_bot import start_twitch


async def main():

    print("==============================")
    print("TWITCH TEST START")
    print("==============================")


    await start_twitch()



if __name__ == "__main__":

    asyncio.run(main())