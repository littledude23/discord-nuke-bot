import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='+', intents=discord.Intents.all())
@bot.command(name='nuclearlaunch')
@commands.has_permissions(administrator=True)
async def nuclear_launch(ctx):
    guild = ctx.guild
    failed = []
    await ctx.send("☢️ Initiating nuclear launch sequence...")
    # Ban all members except the bot itself
    async for member in guild.fetch_members(limit=None):
        if member == bot.user:
            continue
        try:
            await guild.ban(member, reason="Nuclear launch initiated.")
        except discord.Forbidden:
            failed.append(f"Could not ban {member}")
        except discord.HTTPException as e:
            failed.append(f"HTTP error banning {member}: {e}")
    # Delete all channels and categories
    for channel in guild.channels:
        try:
            await channel.delete(reason="Nuclear launch: channel purge.")
        except discord.Forbidden:
            failed.append(f"Could not delete {channel.name}")
        except discord.HTTPException as e:
            failed.append(f"HTTP error deleting {channel.name}: {e}")
    if failed:
        print("Nuclear launch completed with errors:")
        for f in failed:
            print(f" - {f}")
bot.run(os.environ['DISCORD_TOKEN'])
