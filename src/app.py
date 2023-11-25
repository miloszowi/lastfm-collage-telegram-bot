import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, Application, InlineQueryHandler

from . import collageHandler


class App:
    app: Application

    def run(self) -> None:
        self.app = ApplicationBuilder().token(os.getenv('BOT_TOKEN')).build()

        self.app.add_handler(InlineQueryHandler(collageHandler.handle))
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


def __main__():
    load_dotenv(dotenv_path='.env.local')
    App().run()
