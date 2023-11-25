import asyncio
import time
import aiohttp

async def fetch(client):
    async with client.get('http://python.org') as resp:
        assert resp.status == 200
        return await resp.text()

async def main1():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html[0])

async def some1():
    await asyncio.sleep(0.2)
    print('done2')

async def some2():
    await asyncio.sleep(0.1)
    print('done3')


async def main():
    t = asyncio.create_task(main1())
    t1 = asyncio.create_task(some1())
    t2 = asyncio.create_task(some2())
    print(type(t).__base__)
    await t2
    await t1
    await t



start = time.time()

asyncio.run()

print(time.time() - start)