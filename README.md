### **OrphanesKiller**  

**Why?**  
I hate when I delete a category on a Discord server, and all the channels move up instead of being deleted. So, I made this bot to remove those channels automatically.  




### **What It Does**  
OrphanesKiller helps manage your Discord server by **deleting uncategorized text and voice channels** (those not inside a category). It supports both:  
 **Normal commands** (e.g., `--cleanup`, `--cmd`)  
 **Slash commands** (e.g., `/cleanup`, `/cmd`)  

### **Available Commands:**  
- `--cleanup` → Deletes all orphaned channels.  
- `/cleanup` → Slash command for the same task.  
- `/cmd` or `--cmd` → Shows this help message.  

### **Implementation Steps**  
1. Add the following files: `.env`, `OrphanesKiller.py`.  
2. The `.env` file should contain your bot token. Obtain a bot token from the [Discord Developer Portal](https://discord.com/developers/applications) or use an existing bot token.  
3. Run `OrphanesKiller.py` to start the bot.
