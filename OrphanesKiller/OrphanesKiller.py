import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="--", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        await bot.tree.sync()
        print("✅ Slash commands synced for all servers!")
    except Exception as e:
        print(f"❌ Failed to sync slash commands: {e}")


async def delete_uncategorized_channels(guild):
    """Deletes uncategorized channels and reports what was deleted and what failed."""
    deleted_channels = []
    failed_channels = []

    for channel in guild.channels:
        if isinstance(channel, (discord.TextChannel, discord.VoiceChannel)) and channel.category is None:
            try:
                await channel.delete()
                deleted_channels.append(channel.name)
            except discord.Forbidden:
                failed_channels.append(f"❌ I don't have permission to delete {channel.name}.")
            except discord.HTTPException:
                failed_channels.append(f"⚠️ Failed to delete {channel.name} due to an error.")

    # Build response message
    response = ""
    if deleted_channels:
        response += f"✅ Deleted the following **uncategorized** channels:\n" + "\n".join(deleted_channels) + "\n"
    if failed_channels:
        response += "\n".join(failed_channels)

    return response if response else "✅ No uncategorized channels found."


@bot.command(name="cleanup")
async def cleanup(ctx):
    result = await delete_uncategorized_channels(ctx.guild)
    await ctx.send(result)


@bot.tree.command(name="cleanup", description="Deletes all orphaned text and voice channels.")
async def cleanup_slash(interaction: discord.Interaction):
    result = await delete_uncategorized_channels(interaction.guild)
    await interaction.response.send_message(result, ephemeral=True)


HELP_TEXT = """**Available Commands:**
- `--cleanup` → Deletes all orphaned channels.
- `/cleanup` → Slash command for the same task.
- `/cmd` or `--cmd` → Shows this help message."""


@bot.command(name="cmd")
async def cmd_prefix(ctx):
    await ctx.send(HELP_TEXT)


@bot.tree.command(name="cmd", description="Shows help information")
async def cmd_slash(interaction: discord.Interaction):
    await interaction.response.send_message(HELP_TEXT, ephemeral=True)


bot.run(TOKEN)
