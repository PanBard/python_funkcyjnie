import asyncio
import time


async def greetings():
    print("Hello!")
    await asyncio.sleep(2)
    print("Bye!")


async def main():

    await asyncio.gather(greetings(),greetings(),greetings())

start = time.perf_counter()

asyncio.run(main())

perform_time = time.perf_counter() - start
print(f"Time: {perform_time:.2f}s")
