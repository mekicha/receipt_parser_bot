## RECEIPT/BILLS PARSER MICROBOT

This is a micro telegram bot that takes an image of a receipt/bill and extracts
the data therein using the awesome [MINDEE API](https://mindee.com/use-case/expense-management).

### FEATURES

Not many features at the moment, to be honest. But if you insist, here they are.

- extracts bills/receipt data using the Mindee API mentioned above.
- stores the relevant extracted data in an SQLITE database using the [peewee orm](http://docs.peewee-orm.com/en/latest/index.html)
- makes it possible to query the total expenses by calling the `/total` command on the bot.
- That is it, really

### I WANT TO RUN THIS. HOW CAN I DO IT?

Well, here is all you need.

1. An API key/token from [Mindee](https://mindee.com/use-case/expense-management). You can get a free one
   that gives you 50 api calls per month.
2. A telegram bot token. You get that by talking to the [BotFather](https://t.me/botfather). More info [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
3. Fill `MINDEE_API_TOKEN` and `BOT_TOKEN` in `config.py` with the values you got.
4. Run `python bot.py` and then try sending a receipt/bill from your telegram bot.
5. Did it work? Congratulations. Let me know if you have other ideas to add to the bot.
6. It didn't work? Uh oh, can you maybe open an issue with the problem you encountered and I will see how I can help.
