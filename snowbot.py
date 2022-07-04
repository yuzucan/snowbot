import discord
import random
import snowbot_commands

TOKEN = "Your TOKEN here"
client = discord.Client()

autosend_delmsg = False

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 


@client.event
async def on_ready():
    print('logged in')
    await client.change_presence(activity=discord.Game('snowman'))



@client.event
async def on_message(message):
    global autosend_delmsg
    if message.author.bot:
        return
    
    if message.channel == 777795314706939915:
        return


    if (message.content).lower() in snowbot_commands.command_list :
        await message.channel.send(snowbot_commands.command_list[str(message.content).lower()])

    if 'snowbot' == str(message.content).lower():
        randomessage = random.choice(snowbot_commands.random_reply_list)
        await message.channel.send(randomessage)
    
    if 'snowbot allsnipe' in str(message.content).lower():
        if 'on' in str(message.content).lower() and message.author.id in snowbot_commands.authorised:
            autosend_delmsg = True
            await message.channel.send('turned on')
        elif 'off' in str(message.content).lower() and message.author.id in snowbot_commands.authorised:
            autosend_delmsg = False
            await message.channel.send('turned off')
        else:
            await message.channel.send("you can't do that Noob")

 



@client.event
async def on_message_delete(message_del):
    global autosend_delmsg
    global deleted_message
    deleted_message = (f'{message_del.content} {message_del.author} {message_del.channel} {message_del.guild} ')
    prGreen(deleted_message)
    if autosend_delmsg == True:
        if message_del.channel == 777795314706939915 or '-sniped by snowbot' in message_del.content:
            return
        else:
            await message_del.channel.send('`' + deleted_message + ' -sniped by snowbot`')

#@client.event
#async def on_message_edit()#
client.run(TOKEN,bot=False)
