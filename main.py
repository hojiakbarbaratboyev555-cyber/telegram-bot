import asyncio import json import base64 import os import pymysql from datetime import datetime from aiogram import Bot, Dispatcher from aiohttp import web

API_KEY = '8600632675:AAFX25zNOSXYtAC5JePH4ZbsMMtDi3jYu5' bot = Bot(token=API_KEY) dp = Dispatcher()

DB_HOST = 'localhost' DB_USER = '688f7a15ce9ef_mixco' DB_PASS = 'abdulloh09' DB_NAME = '688f7a15ce9ef_mixco'

connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, charset='utf8mb4') cursor = connect.cursor(pymysql.cursors.DictCursor)

PORT (Render uchun muhim)

PORT = int(os.environ.get("PORT", 10000))

Simple health route (Render port ochilishi uchun)

async def handle(request): return web.Response(text="Bot ishlayapti")

app = web.Application() app.router.add_get("/", handle)

Bot polling

async def start_bot(): print("Bot ishga tushdi...") await dp.start_polling(bot)

Main

async def main(): runner = web.AppRunner(app) await runner.setup() site = web.TCPSite(runner, "0.0.0.0", PORT) await site.start()

# Botni parallel ishga tushiramiz
asyncio.create_task(start_bot())

while True:
    await asyncio.sleep(3600)

if name == 'main': asyncio.run(main())
