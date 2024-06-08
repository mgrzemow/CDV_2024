import asyncio
import time
import aiohttp


async def get_result(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as resp:
        if resp.status == 200:
            content = await resp.text()
            return len(content)
        else:
            return -9999


async def main():
    async with aiohttp.ClientSession() as session:
        url = f'http://httpbin.org/get'
        lengths = await asyncio.gather(*[get_result(session, url) for _ in range(10_000)])
        print(lengths)
        print(sum(1 for l in lengths if l == -9999))


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
