import discord, time, colorama, random, os, sys
from discord.ext import commands
from colorama import Fore, init
init()

client = commands.Bot('>', self_bot = True)


token = input("Enter Your Token: ")
client.remove_command('help')

os.system(f'cls & mode 30,8 & title [Cult Auto Pressure!]')


@client.event
async def on_connect():
    
    
    print(f'''{Fore.RED}  
    ╔═╗╦ ╦╦ ╔╦╗
    ║  ║ ║║  ║ 
    ╚═╝╚═╝╩═╝╩ auto pressure 

    logged in {client.user}
    ''')

PACK_MESAGES = ["LOOK AT YOU NIGGER BOY https://tenor.com/view/funny-monkey-eat-hungry-adorable-cute-gif-16750529", "YOU FUCKING SUCK NIGGA KYS HAHAHHAHAHAHA", "HAHHHA UR ASS KID", "UR SO BAD U CANT EVEN DEFINE A XSS SCAN U FUCKING APE BITCH", "https://cdn.discordapp.com/attachments/919752987616882799/919849977579175956/unknown.png UNKNOWN FUCK HAHAHAHAHAHAHAHHAHAHAHAHHAHAHA", "WHAT THE FUCK KID UR SO ASS SON UR MY SEEED NIGGA HAHA", "HHAHAH WHAT UR SUCH A LARP PACKER GET HOED NIGGER", "UR SO BAD SON I OWN YOU AND UR EBITCH FAGGOT NIGGER FUCK", "HAAHHA UR FOLDING UR TOO SLOW AND IM GETTING RATELIMITED NIGGA HAHAHA", "https://tenor.com/view/spongebob-gay-gif-22490381 this u nigga ?", "HELLO BITCH BOY PAY ATTENTION", "LOLOLOLOL", "VEIL FUCKING ENDED YOU ALL @everyone", "DROP DOWN AND GIVE ME 30 PUSSY NIGGA", "YOUR FUCKING POOR SHOW ME FUNDS U SKID", "DEFINE OPCODE RIGHT NOW DONT FAIL NIGGA HAHAHAHAHHAH LOSER", "@everyone IM HOEING ALL YOU NIGGAS ON GD"]
    
           
@client.command()
async def pack(ctx):
    await ctx.message.delete()
    global end
    end = False
    while True:
        await ctx.send(random.choice(PACK_MESAGES))
        if end == True:
            break

@client.command()
async def stop(ctx):
    await ctx.message.delete()
    global end
    end = True
    if end == True:
        await ctx.send("`Bot Status:` **Offline**")






client.run(token, bot=False)