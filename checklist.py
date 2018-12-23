import discord

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(msg):
    # we do not want the bot to reply to itself
    if msg.author == client.user:
        return

    if msg.content.startswith('+createlist'):
        listitems = msg.content.split(',')
        await send_message(msg.channel, 'React with :white_check_mark:(``:white_check_mark:``) '
                                            'to mark a list item as done.')
        for i in range(len(listitems)):
            currentitem = listitems[i].replace('+createlist', '')
            listitems[i] = currentitem
            counter = i+1
            await send_message(msg.channel, str(counter) + '. ' + currentitem)

@client.event
async def on_reaction_add(reaction, user):

    if reaction.emoji.startswith(u"\u2705"):
        if 'React with' in reaction.message.content:
            await client.remove_reaction(reaction.message, u"\u2705", user)
            return
        if reaction.message.author == client.user:
            fixed_message = '~~' + reaction.message.content + '~~'
            if ' - completed by ' in reaction.message.content:
                await client.remove_reaction(reaction.message, u"\u2705", user)
                return
            await client.edit_message(reaction.message, fixed_message + " - completed by " + user.name)
            await client.remove_reaction(reaction.message, u"\u2705", user)


async def send_message(channel, message):
    await client.send_message(channel, message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)