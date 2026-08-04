import httpx
import asyncio

async def test():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://wttr.in/Hyderabad?format=3")
        print(r.text)

asyncio.run(test())