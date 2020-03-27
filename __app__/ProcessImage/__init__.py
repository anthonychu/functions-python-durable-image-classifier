from asyncio import sleep
from random import choice

async def main(imageId: str) -> str:
    #await sleep(1)
    return choice(['cat', 'dog'])
