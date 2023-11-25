from uuid import uuid4

import requests
from telegram import Update, InlineQueryResultPhoto
from telegram.ext import ContextTypes


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.inline_query.query

    if not username:
        return

    temp_id = str(uuid4())
    response = requests.post(
        'https://lastcollage.io/api/collage',
        json={
            "colNum": 3,
            "hideMissing": "false",
            "period": "1week",
            "rowNum": 3,
            "showName": "true",
            "type": "albums",
            "username": "miloszowi"
        },
        headers={
            "content-type": "application/json;charset=UTF-8"
        }
    )

    if response.status_code != 200:
        await update.inline_query.answer([], cache_time=48000)

    collage_url = f"https://lastcollage.io/{response.json()['downloadPath']}"

    await update.inline_query.answer(
        [
            InlineQueryResultPhoto(
                id=temp_id,
                photo_url=collage_url,
                thumbnail_url=collage_url,
                photo_width=500,
                photo_height=500
            )
        ],
        cache_time=3600
    )
