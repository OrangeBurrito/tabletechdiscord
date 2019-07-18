import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Table Tech Discord has been activated.')


@client.command()
async def flip(ctx):
    await ctx.send(f'Flipped a table over in {round(client.latency * 1000)}ms. :table_flipped:')


@client.command()
async def diceshrine(ctx):
    responses = ['Renewed: +4 health',
'Bolstered: +1-2 HP',
'Paid: +60 money',
'Shielded: +2 armor',
'Cleansed: -5 curse',
'Gift: Chest spawns in front of you',
'Reloaded: all ammo refilled',
'Blanked: +6 blanks',
'Pained: -2 hearts',
'Enfeebled: -1 HP',
'Robbed: -60 money',
'Disarmed: -1 gun',
'Limited: -30 percent ammo capacity',
'Deblanked: -6 blanks',
'Cursed: +5 curse up',
'Unsteady: increased reload time',
'Priceless: no effect',
'Shrine Explodes: reduces you to 1 HP, +300 damage up']
    await ctx.send(random.choice(responses))

client.run('NDg4Njk2NzE0NDE3NTM3MDI0.XTCSRA.Ujg6sYtGO2lIiCB2a5NKb8XL0Bg')

# example of numbers in
# @client.command(aliases=['1curseup'])
# async def _1curseup(ctx):
#     await ctx.send('+1 Curse')

# @client.command()
# async def diceshrine(ctx):
#     responses: ['Renewed - +4 health',
#                 'Bolstered - +1-2 HP',
#                 'Paid - +60 money',
#                 'Shielded - +2 armor',
#                 'Cleansed - -5 curse',
#                 'Gift - Chest spawns in front of you',
#                 'Reloaded - all ammo refilled',
#                 'Blanked - +6 blanks',
#                 'Pained - -2 hearts',
#                 'Enfeebled - -1 HP',
#                 'Robbed - -60 money',
#                 'Disarmed - -1 gun',
#                 'Limited -30 percent ammo capacity',
#                 'Deblanked - -6 blanks',
#                 'Cursed - +5 curse up',
#                 'Unsteady - increased reload time',
#                 'Priceless - no effect',
#                 'Shrine Explodes - reduces you to 1 HP, +300 percent damage up']
#     await ctx.send(f'{random.choice(responses)}')

# CONSOLE LOGS JOINING/LEAVING OF USERS
# @client.event 
# async def on_member_join(member): 
#     print(f'{member} has joined the server.')

# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left the server.')

# OLD STUFF FROM OTHER TUT, NOT USING RN

# bot = commands.Bot(command_prefix='.', description='Table Tech Discord is a passive item.')

# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')

# @bot.command()
# async def add(ctx, a: int, b: int):
#     await ctx.send(a+b)

# @bot.command()
# async def multiply(ctx, a: int, b: int):
#     await ctx.send(a*b)

# @bot.command()
# async def flip(ctx):
#     await ctx.send("You flipped a table over. :fliptable:")

# @bot.command()
# async def croc(ctx):
#     await ctx.send("https://bit.ly/2xOoGmj")