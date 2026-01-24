from fastapi import FastAPI, Form, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import sqlite3 as sql
import folium
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_USER_ID')

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
    return FileResponse("frontend/index.html")

@app.get("/admin")
def admin():
    return FileResponse("frontend/admin.html")

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
    mapIp()
    writeTxt()
    return {"status": "ok"}

@app.get("/map")
async def mapIp(
    request: Request
):
    conn = sql.connect("IPsDatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ip FROM IPs")
    data = cursor.fetchall()
    conn.commit()
    conn.close()

    ips_coords = []

    def ipInfo(ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return data

    for i in data:
        rData = ipInfo(i[0])
        ips_coords.append((rData["lat"], rData["lon"]))

    response = requests.get(f"https://api.ipify.org?format=json")
    serverIp = response.json()["ip"]
    serverData = ipInfo(serverIp)
    server_coord = (serverData["lat"], serverData["lon"])

    m = folium.Map(location=[20,0], zoom_start=2, tiles="CartoDB dark_matter")

    for lat, lon in ips_coords:
        folium.CircleMarker(
            location=(lat, lon),
            radius=5,
            color="cyan",
            fill=True,
            fill_color="cyan",
            fill_opacity=0.8,
            popup=f"IP: {lat}, {lon}"
        ).add_to(m)

    folium.CircleMarker(
        location=server_coord,
        radius=7,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=1,
        popup="Servidor"
    ).add_to(m)

    m.save("mapa_ips.html")
    return {"message" : f"Mapa generado porfavor visite {request.base_url}/seeMap o vea el html desde la carpeta en la que esta este main.py"}

@app.get("/seeMap")
def seeMap():
    return FileResponse("mapa_ips.html")

@app.get("/seeCountry")
async def seeCountry():
    conn = sql.connect("IPsDatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT country, COUNT(*) as total FROM IPs GROUP BY country")
    data = cursor.fetchall()
    return data

@app.get("/getMap")
async def getMap():
    text = ""
    with open("mapa_ips.html", "r", encoding="utf-8") as f:
        text = f.read()
    return text

@app.post("/alertAdmin")
async def alertAdmin(data: dict = Body(...)):
    message = data["message"]
    send_telegram_message(message)
