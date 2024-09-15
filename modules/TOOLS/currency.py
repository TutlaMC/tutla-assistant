from ..Module import * 
from ..Utils import *
from assistantdata import db
import requests

def convert_currency(amt, from_cur, to_cur):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][to_cur]
        return amt * rate
    else:
        return None

async def currency_callback(CommandObject, message, self, params, command_data):
    amt = float(params[1])
    from_cur = params[2].upper()
    to_cur = params[3].upper()
    converted_amt = convert_currency(amt, from_cur, to_cur)
    if converted_amt:
        await message.channel.send(
            f"{amt} {from_cur} is equal to {converted_amt:.2f} {to_cur}"
        )
    else:
        await message.channel.send("smoll error, report bug if it happens again")

currency_command = Command("currency", "Convert currency amounts", currency_callback, TOOLS, aliases=["convert"], params=["AMOUNT", "FROM_CURRENCY", "TO_CURRENCY"])
