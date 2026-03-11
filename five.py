from  fastapi import FastAPI,APIRouter,BackgroundTasks
import asyncio
import time
app = FastAPI()
router_five = APIRouter(prefix="/Асинхроность",tags=['/Осинхронсть'])


def sync_task():
    time.sleep(3)
    print("Email-нызга код жонотулду")

async def async_task():
    await asyncio.sleep(3)
    print('башка API-ден сураным жонотулду')

@router_five.get('/')
async def some_route(background_tasks: BackgroundTasks):
    background_tasks.add_task(sync_task)
    ...
    asyncio.create_task(async_task())
    return {'Сураным алынды': True}

