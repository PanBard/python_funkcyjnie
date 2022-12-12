import asyncio

async def greetings(word_1,word_2):
    print(word_1)
    await asyncio.sleep(3)
    print(word_2)

    return 10

async def main():
    print("Demonstrate async program:")

    async_task_1 = asyncio.create_task(greetings("First","Second"))
    await asyncio.sleep(1)

    print("This sentence should be beetwen First and Second")

    return_value_form_function = await async_task_1
    print(return_value_form_function)

if __name__ == '__main__':
    asyncio.run(main())

