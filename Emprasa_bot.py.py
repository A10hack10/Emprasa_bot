from telegram.ext import Updater, MessageHandler, Filters
import re
import logging
import sys

# Configure logging to show errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout,
    force=True
)
logger = logging.getLogger(__name__)  # Fixed: Use __name__ instead of undefined 'name'

# Your bot token
TOKEN = "7778789876:AAHGtT_SgWzox-uI4Hdn9-j8YIBneyJnN4s"
total = 0

def handle_message(update, context):
    global total
    try:
        message = update.message.text.strip()
        user = update.message.from_user
        logger.info(f"📩 Received: '{message}' from {user.first_name}")

        # Check for +number pattern
        match = re.match(r'^\+\s*(\d+)$', message)
        if match:
            amount = int(match.group(1))
            if amount <= 0:
                update.message.reply_text("⚠️ Please enter a positive number after +")
                return
                
            total += amount
            reply = f"✅ Added +{amount}\n💰 Total: {total}"
            update.message.reply_text(reply)
            logger.info(f"Added +{amount}. New total: {total}")
        else:
            logger.info(f"⛔️ Ignored: '{message}'")
    except Exception as e:
        logger.error(f"🚨 Error: {e}")

def main():
    print("======================================")
    print("       TELEGRAM BOT STARTING          ")
    print("======================================")
    
    try:
        logger.info("🤖 Initializing bot...")
        logger.info(f"🔑 Token: {TOKEN[:10]}...")  # Show first 10 characters
        
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher
        
        # Add message handler
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
        
        logger.info("✅ Bot started successfully!")
        logger.info("🟢 Listening for messages...")
        print("Bot is running. Press CTRL+C to stop.")
        
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.exception(f"🔥 CRITICAL ERROR: {e}")
        print("Bot failed to start. Check logs above.")
        input("Press Enter to exit...")

if __name__ == '__main__':  # Fixed: Corrected syntax for main check
    main()