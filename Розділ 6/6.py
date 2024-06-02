#pip install telethon
import pytz
from telethon import TelegramClient
local_tz = pytz.timezone('Europe/Kiev')
api_id = ''
api_hash = ''
username = ''
channel_name = 'laba6andreashka'
phone_number = ''
client = TelegramClient(username, api_id, api_hash)
print('Страп Андріана група 2 лаб 6')

# Вхід в аккаунт
client.start()

# Отримання інформації про канал
async def get_channel_info():
    channel = await client.get_entity(channel_name)
    channel_id = channel.id
    channel_username = channel.username
    channel_title = channel.title
    channel_creation_date = channel.date.astimezone(pytz.utc).astimezone(local_tz)

    # Виведення інформації про канал в консоль
    print("ID каналу:", channel_id)
    print("Ім'я користувача каналу:", channel_username)
    print("Назва каналу:", channel_title)
    print("Дата створення каналу:", channel_creation_date)

async def get_posts_info():
    channel = await client.get_entity(channel_name)
    msgs = client.iter_messages(channel, limit = 4)
    async for i in msgs:
        print("Час публікації:", i.date.astimezone(pytz.utc).astimezone(local_tz))
        print('Публікація:', i.text)
        print("кількість знаків:", len(i.text))
        print("кількість слів:", len(i.text.split())) 

async def get_posts_save():
    channel = await client.get_entity(channel_name)
    msgs = client.iter_messages(channel)
    with open('telegram.txt', 'w+', encoding='UTF-8') as tlg:
        async for i in msgs:
            tlg.write(str(i.date.astimezone(pytz.utc).astimezone(local_tz))+'\n')
            tlg.write(str(i.message)+'\n')
            tlg.write('\n')

async def get_total():
    channel = await client.get_entity('tpolph3_2022')
    msgs = await client.get_messages(channel)
    print("Кількість постів:", msgs.total)

with client:
    client.loop.run_until_complete(get_channel_info())
    client.loop.run_until_complete(get_posts_info())
    client.loop.run_until_complete(get_posts_save())
    client.loop.run_until_complete(get_total())
