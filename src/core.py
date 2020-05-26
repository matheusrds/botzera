from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

# from conf.settings import BASE_API_URL, TELEGRAM_TOKEN


def start(bot, update):
    response_message = "Olá serei seu intérprete do Octave aqui no Telegram :)"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo="BASE_API_URL" + args[0]
    )


def unknown(bot, update):
    response_message = "Desculpe, não entendi o que voce disse :("
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token="TELEGRAM_TOKEN")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        CommandHandler('octave', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()