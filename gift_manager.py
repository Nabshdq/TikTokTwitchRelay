import asyncio
import os

from dotenv import load_dotenv


# =========================
# LOAD ENV
# =========================

load_dotenv()



# =========================
# CONFIG
# =========================

GIFT_DELAY = int(
    os.getenv(
        "GIFT_DELAY",
        "10"
    )
)



# =========================
# STORAGE
# =========================

gift_buffer = {}

gift_tasks = {}



# =========================
# ADD GIFT
# =========================

async def add_gift(
    username,
    gift_name,
    callback,
    count=1
):


    key = (
        username,
        gift_name
    )



    # =========================
    # EXISTING GIFT
    # =========================

    if key in gift_buffer:


        gift_buffer[key]["count"] += count


        return



    # =========================
    # NEW GIFT
    # =========================

    gift_buffer[key] = {

        "username": username,

        "gift_name": gift_name,

        "count": count

    }



    # =========================
    # START TIMER
    # =========================

    task = asyncio.create_task(

        gift_timer(
            key,
            callback
        )

    )


    gift_tasks[key] = task





# =========================
# TIMER
# =========================

async def gift_timer(
    key,
    callback
):


    try:


        await asyncio.sleep(
            GIFT_DELAY
        )



        if key not in gift_buffer:

            return



        data = gift_buffer.pop(
            key
        )



        await callback(

            data["username"],

            data["gift_name"],

            data["count"]

        )



    except asyncio.CancelledError:

        pass



    finally:


        gift_tasks.pop(
            key,
            None
        )





# =========================
# CLEAR BUFFER
# =========================

async def clear_gifts():


    for task in gift_tasks.values():

        task.cancel()



    gift_buffer.clear()


    gift_tasks.clear()