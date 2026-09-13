# Bot Images Directory

This directory contains images for your Telegram bot.

## Image Files

- **`startup.jpg`** — Image displayed when users start the bot with `/start` command

## Setup Instructions

1. Place your startup image in this directory and name it `startup.jpg`
2. The image should be in JPG format (you can use PNG as well, just rename the extension in `bot.py`)
3. Recommended image size: 800x600 pixels or larger
4. The image will automatically display alongside the welcome message

## How It Works

When a user sends `/start`:
- The bot checks if `images/startup.jpg` exists
- If it exists, the image is sent with the welcome caption
- If it doesn't exist, only the text message is sent (fallback)

## File Size Limits

- Telegram image size limit: 20 MB
- Keep images under 5 MB for optimal performance
- Supported formats: JPG, PNG, GIF, BMP

## Adding Your Image

To add your startup image:
1. Go to the `images/` folder
2. Upload or replace `startup.jpg` with your image
3. Commit and push to GitHub
4. The bot will use it automatically on the next restart
