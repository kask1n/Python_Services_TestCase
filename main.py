from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from datetime import datetime
from psycopg import sql
import psycopg
import uuid


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
        log_data = log.log.split()
        ip_address, http_method, uri, http_status_code = log_data

        log_id = uuid.uuid4()
        log_created = datetime.now()

        query = sql.SQL("""
            INSERT INTO test_schema.test_table(log_uuid,
                                               log_datetime,
                                               ip_address,
                                               http_method,
                                               uri,
                                               http_status_code)
            VALUES (%s, %s, %s, %s, %s, %s);
        """)
        data = (log_id, log_created, ip_address, http_method, uri, http_status_code)

        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
        cur.close()
        return "Лог сохранeн"
    except Exception as e:
        print(e)
        raise HTTPException(status_code=418, detail="Что-то пошло не так")


@app.get("/api/data", response_model=List[object])
async def get_logs():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_db.test_schema.test_table;")
        logs = [{"id": row[1],
                 "created": row[2],
                 "log": {"ip": row[3],
                         "method": row[4],
                         "uri": row[5],
                         "status_code": row[6]}
                 } for row in cur.fetchall()]
        cur.close()
        return logs
    except Exception as e:
        print(e)
        raise HTTPException(status_code=418, detail="Что-то пошло не так.")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
