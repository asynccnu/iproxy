import os
import asyncio
import motor.motor_asyncio

HOST = os.getenv('MONGO_HOST')
PORT = int(os.getenv('MONGO_PORT'))

async def setup_db():
    # { db:test, co:ips }
    db = motor.motor_asyncio.AsyncIOMotorClient(HOST, PORT).test
    # await db.ips.insert_one({'_': []}) # create db on demand 
    return db

try:
    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(setup_db())
finally:
    # loop.close()
    pass
