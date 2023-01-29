import discord
bot = discord.Bot()

@bot.slash_command()
@discord.default_permissions(kick_members = True, administrator = True)
async def kick_user(bot, ctx, member : discord.Member, *, reason=None):
    try: 
        await member.kick(reason=reason)
        await ctx.respond(f'{member.mention} has been kicked!')
    except:
        await ctx.respond(f'{member.mention} has not been kicked!')