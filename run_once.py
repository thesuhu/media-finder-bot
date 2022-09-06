from utils import save_file
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, CHANNELS, USERBOT_STRING_SESSION, USER_SESSION, id_pattern
from pyrogram import Client
import asyncio
import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

logger = logging.getLogger(__name__)
lock = asyncio.Lock()

async def main():
    """Save old files in database with the help of user bot"""
    user_bot = Client(USERBOT_STRING_SESSION, API_ID, API_HASH) # Create user bot, b'cause get_chat_history is not available in bot
    bot = Client(SESSION, API_ID, API_HASH, bot_token=BOT_TOKEN)

    await user_bot.start()
    await bot.start()

    try:
        print('Started')
        for channel in CHANNELS:
            print(f'Checking {channel}')          
            async for user_message in user_bot.get_chat_history(channel):
                print(f'Checking {user_message.id}')
                message = await user_bot.get_messages(channel, user_message.id, replies=0)
                for file_type in ("document", "video", "audio"):
                    media = getattr(message, file_type, None)
                    if media is not None:
                        break
                else:
                    continue
                media.file_type = file_type
                media.caption = message.caption
                await save_file(media)
                print(f'Saved {media.file_name}')
    finally:
        await user_bot.stop()
        await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
