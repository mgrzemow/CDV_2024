import asyncio
import time


def count_sync():
    print("One")
    time.sleep(1)
    print("Two")
    return 'result'


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    return 'result'


async def main():
    # r1 = await count()
    # r2 = await count()
    # r3 = await count()
    results = await asyncio.gather(count(), count(), count())
    # print(results)


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    # s = time.perf_counter()
    # count_sync()
    # count_sync()
    # count_sync()
    # elapsed = time.perf_counter() - s
    # print(f"{__file__} executed in {elapsed:0.2f} seconds.")