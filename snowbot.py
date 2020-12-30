import discord
import random
import snowbot_commands

TOKEN = "TOKEN HERE"
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


    if str(message.content).lower() in snowbot_commands.command_question:
        await message.channel.send(snowbot_commands.command_list[str(message.content).lower()])

    if 'snowbot' == str(message.content).lower():
        randomessage = random.choice(snowbot_commands.random_reply_list)
        await message.channel.send(randomessage)
    
    if 'snowbot ' in str(message.content).lower():
        if 'on' in str(message.content).lower():
            autosend_delmsg = True
            await message.channel.send('turned on')
        elif 'off' in str(message.content).lower():
            autosend_delmsg = False
            await message.channel.send('turned off')
        elif message.author != 454755817179054081:
            await message.channel.send('you cant do that noob')
        else:
            await message.channel.send('missing an argument')





@client.event
async def on_message_delete(message_del):
    global autosend_delmsg
    deleted_message = (f'{message_del.content} {message_del.author} {message_del.channel} {message_del.guild}')
    prGreen(deleted_message)
    if autosend_delmsg == True:
        if message_del.channel == 777795314706939915:
            return
        else:
            await message_del.channel.send(deleted_message)


client.run(TOKEN,bot=False)
