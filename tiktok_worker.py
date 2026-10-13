import asyncio
import threading


from tiktok_listener import client



class TikTokWorker:


    def __init__(self):

        self.thread = None

        self.loop = None

        self.running = False

        self.stop_event = threading.Event()



    def start(self):

        if self.thread and self.thread.is_alive():

            return


        self.running = True

        self.stop_event.clear()


        self.thread = threading.Thread(

            target=self._run,

            daemon=False

        )


        self.thread.start()



    def _run(self):

        self.loop = asyncio.new_event_loop()


        asyncio.set_event_loop(
            self.loop
        )


        try:

            self.loop.run_until_complete(

                self._connect()

            )


        except Exception as e:

            if self.running:

                print("==============================")
                print("TIKTOK WORKER ERROR")
                print(e)
                print("==============================")


        finally:

            try:

                self.loop.close()


            except Exception:

                pass



    async def _connect(self):

        print("==============================")
        print("TIKTOK WORKER START")
        print("==============================")


        try:

            await client.connect()


        except asyncio.CancelledError:

            pass




    def stop(self):

        if not self.loop:

            return



        print("==============================")
        print("STOPPING TIKTOK WORKER")
        print("==============================")


        self.running = False



        def shutdown():

            for task in asyncio.all_tasks(
                self.loop
            ):

                task.cancel()



        self.loop.call_soon_threadsafe(
            shutdown
        )



        if self.thread:

            self.thread.join(
                timeout=10
            )


        print("==============================")
        print("TIKTOK WORKER STOPPED")
        print("==============================")