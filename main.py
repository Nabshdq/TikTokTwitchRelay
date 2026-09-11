import asyncio
import signal


from tiktok_listener import client as tiktok_client

from twitch_bot import (
    start_twitch,
    bot
)



# =========================
# GLOBAL STATE
# =========================

running = True



# =========================
# SHUTDOWN HANDLER
# =========================

def shutdown_handler():

    global running


    if running:

        print()

        print("==============================")
        print("CTRL+C RECEIVED")
        print("==============================")


    running = False




# =========================
# TIKTOK RUNNER
# =========================

async def run_tiktok():

    try:

        await tiktok_client.connect()



    except asyncio.CancelledError:

        pass



    except Exception as e:


        print("==============================")
        print("TIKTOK ERROR")
        print(e)
        print("==============================")





# =========================
# TWITCH RUNNER
# =========================

async def run_twitch():

    try:

        await start_twitch()



    except asyncio.CancelledError:

        pass



    except Exception as e:


        print("==============================")
        print("TWITCH ERROR")
        print(e)
        print("==============================")





# =========================
# MAIN
# =========================

async def main():

    global running



    print("==============================")
    print("TIKTOK TWITCH RELAY STARTING")
    print("==============================")



    loop = asyncio.get_running_loop()



    # CTRL+C handler

    try:

        loop.add_signal_handler(

            signal.SIGINT,

            shutdown_handler

        )


    except Exception:

        pass





    # START SERVICES

    tiktok_task = asyncio.create_task(

        run_tiktok()

    )



    twitch_task = asyncio.create_task(

        run_twitch()

    )





    try:


        while running:

            await asyncio.sleep(1)





    except KeyboardInterrupt:

        shutdown_handler()





    finally:


        print()

        print("==============================")
        print("CLOSING RELAY")
        print("==============================")



        # CLOSE TWITCH

        try:

            await bot.close()


            print(
                "Twitch closed"
            )


        except Exception:

            pass





        # STOP TASK

        twitch_task.cancel()



        await asyncio.gather(

            twitch_task,

            return_exceptions=True

        )





        print("==============================")
        print("RELAY CLOSED CLEANLY")
        print("==============================")





# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":


    asyncio.run(
        main()
    )