import asyncio


async def print_taask(i):
    print("Task:",i)


async def main():

    N = 10
    print("Demonstrate create 10 async task with for loop")

    for i in range(N):
        task = asyncio.create_task(print_taask(i))
        await task


if __name__ == '__main__':
    asyncio.run(main())

