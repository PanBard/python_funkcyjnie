import asyncio
import time

async def add(a,b):
    print("Adding number")
    await asyncio.sleep(3)
    c = a+b
    print("3 second have passed")
    print(f"{a}+{b}={c}")

async def multiplication(a,b):
    print("Multiplication number")
    await asyncio.sleep(4)
    c = a * b
    print("3 second have passed")
    print(f"{a}*{b}={c}")


async def main(a,b):
    await add(a,b)
    print("\nBetween\n")
    await multiplication(a,b)

start = time.perf_counter()

if __name__ == '__main__':
    asyncio.run(main(34,65))

perform_time = time.perf_counter() - start
print(f"Time: {perform_time:.2f}s")
