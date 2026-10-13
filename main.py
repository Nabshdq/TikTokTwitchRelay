import asyncio
import signal


from tiktok_worker import TikTokWorker


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
# TWITCH RUNNER
# =========================

async def run_twitch():

    try:

        await start_twitch()



    except asyncio.CancelledError:

        print("Twitch task cancelled")

        raise



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



    # =========================
    # CTRL+C HANDLER
    # =========================

    try:

        loop.add_signal_handler(

            signal.SIGINT,

            shutdown_handler

        )


    except Exception:

        pass





    # =========================
    # START TIKTOK WORKER
    # =========================

    tiktok_worker = TikTokWorker()

    tiktok_worker.start()





    # =========================
    # START TWITCH
    # =========================

    twitch_task = asyncio.create_task(

        run_twitch()

    )



    tasks = [

        twitch_task

    ]





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



        # =========================
        # CLOSE TWITCH
        # =========================

        try:

            await bot.close()


            print(

                "Twitch closed"

            )


        except Exception:

            pass





        # =========================
        # CLOSE TIKTOK WORKER
        # =========================

        try:

            tiktok_worker.stop()


        except Exception as e:


            print("==============================")
            print("TIKTOK WORKER STOP ERROR")
            print(e)
            print("==============================")





        # =========================
        # STOP ASYNC TASKS
        # =========================

        print("Stopping tasks...")


        for task in tasks:


            if not task.done():

                task.cancel()



        await asyncio.gather(

            *tasks,

            return_exceptions=True

        )





        print("==============================")
        print("RELAY CLOSED CLEANLY")
        print("==============================")





# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":


    try:

        asyncio.run(

            main()

        )


    except KeyboardInterrupt:

        pass