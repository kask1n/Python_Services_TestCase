from random import randint

import aiohttp

import asyncio

from main import conn, sql


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text()


async def save_to_file(data):
    with open('data.txt', 'a') as file:
        file.write(data + '\n')


async def background_task():
    url = 'http://127.0.0.1:8000/api/data'
    while True:
        async with aiohttp.ClientSession() as session:
            curr = conn.cursor()
            curr.execute(sql.SQL("""
                SELECT COUNT(*)
                FROM test_db.test_schema.test_table;
            """))
            row = curr.fetchone()
            count = row[0]

            data = await fetch_data(session, url + f'?position={randint(1, int(count))}&strings_count={randint(1, 5)}')
            await save_to_file(data)

        await asyncio.sleep(7)


async def main():
    await background_task()


if __name__ == '__main__':
    asyncio.run(main())
