import asyncio
import motor.motor_asyncio

HOST = 'localhost'
PORT = 27017

async def setup_db():
    # { db:test, co:ips }
    db = motor.motor_asyncio.AsyncIOMotorClient(HOST, PORT).test
    # await db.ips.insert_one({'_': []}) # create db on demand 
    return db

loop = asyncio.get_event_loop()
db = loop.run_until_complete(setup_db())