import aiohttp
import asyncio

async def fetch_status(session, address):
    url = f"https://api.starkurabu.com/get_whitelisted_status?addr={address}"
    async with session.get(url) as response:
        data = await response.json()
        return address, data.get("status", "Unknown")

async def main():
    addresses_file = "addresses.txt"  

    async with aiohttp.ClientSession() as session:
        tasks = []
        with open(addresses_file, "r") as file:
            addresses = file.read().splitlines()

        for address in addresses:
            task = fetch_status(session, address)
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        for address, status in results:
            print(f"{address}: {status}")

if __name__ == "__main__":
    asyncio.run(main())
