import asyncio
import time

async def inform(wait_second,message):
    print(f"Before delay: {message}, sleep= {wait_second} s")
    await asyncio.sleep(wait_second)
    print(f"After delay: {message}")


async def main():
    start = time.time()

    print("Demonstrate async program:")
    print(f"Start time: {time.strftime('%X')}")

    async_task_1 = asyncio.create_task(inform(1,"Task1"))
    async_task_2 = asyncio.create_task(inform(2,"Task2"))

    print("This sentence should be beetwen First and Second")

    await async_task_1
    await async_task_2

    end = time.time()
    print(f"End time: {time.strftime('%X')}")
    print(f"Run time: {end-start} s")

if __name__ == '__main__':
    asyncio.run(main())

