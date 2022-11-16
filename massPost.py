import asyncio
from pyrogram import Client, filters, types
from datetime import datetime

api_id = 12345  # берем эти данные с
api_hash = "abcde"  # https://my.telegram.org/apps

Client("my_account", api_id=api_id, api_hash=api_hash)

sendall_channel_id = "mychannel"  # сюда username канала из которого будут пересылаться сообщения без @
channels_send_to_id = [-10213454, -10021452467] # сюда id каналов для пересылки

app = Client("my_account", api_id=api_id, api_hash=api_hash)
print('~Activated~')


@app.on_message(filters.chat(sendall_channel_id))
async def send_message_to_channels(client: Client, message: types.Message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Message seen!")
    for to_chat in channels_send_to_id:
        await app.copy_message(to_chat, sendall_channel_id, message.id)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{now}] Sent to chat {to_chat}')
        await asyncio.sleep(1)


app.run()
