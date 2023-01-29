from discord import Option
import discord

bot = discord.Bot()


@bot.slash_command()
@discord.default_permissions(ban_members = True, administrator = True)
async def ban_user(bot, ctx, member: Option(discord.Member, description="Select a member", required=True), reason: Option(str, description="Reason", required=True)):
    try:
        await member.ban(reason=reason)
        await ctx.respond(f'{member.mention} has been banned!')
    except:
        await ctx.respond(f'{member.mention} has not been banned!')