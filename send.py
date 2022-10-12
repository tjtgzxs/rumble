import telegram
from time import sleep
TELEGRAM_BOT_TOKEN="5526396580:AAE_hnLuGBq-uEnUX3ASTYWfERDrgIkDATI"
TELEGRAM_CHAT_ID="610906120"
def main(textMSg,tele_token=TELEGRAM_BOT_TOKEN,tele_chat_id=TELEGRAM_CHAT_ID):
    return True
    while True:
        try:
            bot=telegram.Bot(token=tele_token)
            bot.send_message(chat_id=tele_chat_id,text=textMSg)
            return  True
        except Exception:
            sleep(40)
            continue

def send_img(img_path,tele_token=TELEGRAM_BOT_TOKEN,tele_chat_id=TELEGRAM_CHAT_ID):
    return True
    while True:
        try:
            bot=telegram.Bot(token=tele_token)
            bot.send_photo(chat_id=tele_chat_id,photo=open(img_path,'rb'))
            return  True
        except Exception:
            sleep(40)
            continue
