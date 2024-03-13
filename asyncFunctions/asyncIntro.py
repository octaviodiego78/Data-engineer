import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(*[count(),count()])


if __name__ == "__main__":
    #we must await a coroutine
    #Await must be inside an async function
    asyncio.run(main())

    


    