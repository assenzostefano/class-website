import discord
from discord.ext import commands

bot = discord.Bot()

@bot.slash_command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear_messages(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.respond('Messages have been cleared!')