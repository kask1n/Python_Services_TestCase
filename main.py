from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from typing import List
import psycopg


class Log(BaseModel):
    log: str


app = FastAPI()

conn = psycopg.connect(
    dbname="test_db",
    user="test_user",
    password="qwerty",
    host="localhost",
    port="5432"
)


@app.post("/api/data", status_code=201)
async def save_log(log: Log):
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO test_schema.test_table(ip_address, http_method, uri, http_status_code) VALUES (%s, %s, %s, "
            "%s);",
            ("http://127.0.0.1:8000/", "hello/", "Alexey", 201))
        conn.commit()
        cur.close()
        return "Лог сохранён."
    except Exception as e:
        raise HTTPException(status_code=418, detail="Что-то пошло не так.")


@app.get("/api/data", response_model=List[Log])
async def get_logs():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_db.test_schema.test_table;")
        logs = [{"log": row[0], "ip_address": row[1], "http_method": row[2], "uri": row[3], "http_status_code": row[4]}
                for row in cur.fetchall()]
        cur.close()
        return logs
    except Exception as e:
        raise HTTPException(status_code=418, detail="Что-то пошло не так.")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
