# LastFM collage generator telegram bot

## Installation

copy the env file
```bash
cp .env .env.local
```

enter your BOT_TOKEN variable received from BotFather into env file
```bash
echo "your bot token here" >> .env.local
```

run the bot

```bash
python -m venv venv
source venv/bin/activate

pip install .
run-bot
```