import io
from dateutil import parser
from peewee import fn

import config
from db import Expense


def parse_receipt(image: io.BytesIO):
    """ Sends the image to mindee api for parsing of receipt data """
    import requests

    files = {"file": image.getvalue()}
    headers = {"X-Inferuser-Token": config.MINDEE_API_TOKEN}
    response = requests.post(config.MINDEE_URL, files=files, headers=headers)
    response.raise_for_status()
    return response.json()

    # todo: fallback to Google vision api or setup mechanism to retry later


def start_handler(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


def image_handler(update, context):
    # the last image in the list is the original size sent
    # use the first image if you want a smaller size
    image = [photo.get_file() for photo in update.message.photo][-1]

    # download the image

    im = io.BytesIO(image.download_as_bytearray())
    res = parse_receipt(im)
    prediction = res["predictions"][0]
    date = prediction["date"]["raw"]
    date = parser.parse(date).date()
    amount = float(prediction["total"]["amount"])
    merchant = prediction["merchant"]["name"]
    Expense.create(amount=amount, purchase_date=date, merchant=merchant)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Success! Receipt from {merchant} for {amount} Euros has been processed",
    )


def unknown_handler(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Uhm not sure I got that, sorry :( Try typing /help",
    )


def total_handler(update, context):
    """ Return the total spent so far """
    total = Expense.select(fn.SUM(Expense.amount)).scalar()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Total amount : {total}"
    )


def report_handler(update, context):
    """ Get full report of expenses """

    Expense.select(fn.SUM(Expense.amount)).scalar()
    context.bot.send_message(chat_id=update.effective_chat.id, text="")
