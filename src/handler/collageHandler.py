from uuid import uuid4

import requests
from telegram import InlineQueryResultPhoto, Update
from telegram.ext import CallbackContext


class CollageHandler:

    @staticmethod
    def handle(update: Update, context: CallbackContext) -> None:
        nickname = update.inline_query.query

        if not nickname:
            update.inline_query.answer([], cache_time=48000)
            return

        temp_id = str(uuid4())
        collage_url = f'https://lastfm-collage.herokuapp.com/collage?username={nickname}&method=album&period=7day&column=3&row=3&caption=true&scrobble=true&c={temp_id}'
        response = requests.get(collage_url)

        if response.status_code != 200:
            update.inline_query.answer([], cache_time=48000)

        result = [
            InlineQueryResultPhoto(
                id=temp_id,
                photo_url=collage_url,
                thumb_url=collage_url,
                photo_width=500,
                photo_height=500
            )
        ]

        update.inline_query.answer(result, cache_time=3600)
