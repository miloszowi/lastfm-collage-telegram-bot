from telegram.ext import InlineQueryHandler, Updater
from telegram.ext.dispatcher import Dispatcher

from config.envs import BOT_TOKEN, PORT, WEBHOOK_URL
from handler.collageHandler import CollageHandler


class App:
    updater: Updater
    dispatcher: Dispatcher

    def __init__(self):
        self.updater = Updater(BOT_TOKEN)

    def run(self) -> None:
        self.register_inline()
        self.register_webhook()

        self.updater.idle()

    def register_inline(self) -> None:
        self.updater.dispatcher.add_handler(InlineQueryHandler(CollageHandler.handle))

    def register_webhook(self) -> None:
        self.updater.start_webhook(
            listen="0.0.0.0",
            port=int(PORT),
            url_path=BOT_TOKEN,
            webhook_url="/".join([WEBHOOK_URL, BOT_TOKEN])
        )


if __name__ == "__main__":
    app = App()
    app.run()
