import asyncio
from time import time

import aiohttp

URL = "https://picsum.photos/200/300"


def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True, ssl=False) as response:
        data = await response.read()
        write_image(data)


async def main():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(URL, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)
