import openhivenpy
import asyncio
import sys
import os

# Simple test to get a simple response from the Hiven API
TOKEN = os.getenv("token") or "TOKEN" #Just to prevent mishaps
client = openhivenpy.UserClient(token=TOKEN, debug_mode=True, print_output=True)

@client.event() 
async def on_init(client):
    print(dir(client))
    print(client)

async def run():
    response = await client.get()

    # If response is 200 that means the program can interact with Hiven
    if response.status_code == 200:
        print("Success!")
    else:
        print(f"The process failed. STATUSCODE={response.status_code}")

    # Starts the Event loop with the a specified websocket => can also be a different websocket
    print(await client.create_connection())


if __name__ == '__main__':
    asyncio.run(run())