from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import sqlite3 as sql
import asyncio

TOKEN = "token del bot aqui"
CHAT_ID = "tu id de telegram"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/f", StaticFiles(directory="frontend"), name="f")


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)
    writeTxt()

def writeTxt():
    conn = sql.connect("IPsDatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IPs")
    data = cursor.fetchall()
    with open("ips.txt", "w", encoding="utf-8") as f:
        f.write(f"")
    for ip in data:
        with open("ips.txt", "a", encoding="utf-8") as f:
            f.write(f"{ip[0]}\n")

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/getIp")
async def getIp(
    i: str = Form(...)
):
    response = requests.get(f"http://ip-api.com/json/{i}")
    data = response.json()
    conn = sql.connect("IPsDatabase.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS IPs (ip TEXT, country TEXT)")
    cursor.execute(f"SELECT * FROM IPs WHERE ip = '{i}'")
    message = f"Un nuevo usuario de {data['country']} ha entrado a tu web desde la ip {i}" if cursor.fetchone() is None else f"Un usuario de {data['country']} ha reingresado a tu web desde la ip {i}"
    send_telegram_message(message)
    cursor.execute("CREATE TABLE IF NOT EXISTS IPs (ip TEXT, country TEXT)")
    cursor.execute(f"INSERT INTO IPs (ip, country) VALUES ('{i}', '{data['country']}')")
    cursor.execute(""" DELETE FROM IPs
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM IPs
    GROUP BY ip
);""")
    conn.commit()
    conn.close()
    return {"status": "ok"}
