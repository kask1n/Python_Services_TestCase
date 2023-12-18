import aiohttp
import asyncio

from random import randint

from webapi.main import conn, sql


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text()


async def save_to_file(data):
    with open('data.txt', 'a') as file:
        file.write(data + '\n')


async def background_task(url):
    while True:
        async with aiohttp.ClientSession() as session:
            curr = conn.cursor()
            curr.execute(sql.SQL("""
                SELECT COUNT(*)
                FROM log_table;
            """))
            row = curr.fetchone()

            count = row[0]
            if not count:
                count = 2

            data = await fetch_data(session, url + f'?position={randint(1, count)}&strings_count={randint(1, 5)}')
            await save_to_file(data)

        await asyncio.sleep(7)


async def main():
    url = 'http://177.77.0.78:8000/api/data'
    await background_task(url)


if __name__ == '__main__':
    asyncio.run(main())
