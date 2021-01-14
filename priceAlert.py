from pushover import init, Client
from coinbase.wallet.client import Client as c
import time
#midnight = "00:00:00"
pushClient = Client("<user-key>", api_token="<api-token>")
api_key = "<API key>"#just leave it as API key, you don't need to generate a new key to query price
api_secret = "<API secret>"#same here
client = c(api_key, api_secret)
initialPrice = client.get_spot_price(currency_pair = 'ETH-USD').get("amount","none")
print("Initialized\nTime: "+time.strftime("%H:%M:%S", time.localtime())+"\nPrice at $"+initialPrice+"\nStarting...")
pushClient.send_message("Initialization successful",title="Initialized")
while True:
    if (time.strftime("%H:%M:%S", time.localtime())=="00:00:00"):#initialized price will reset at midnight
        initialPrice = client.get_spot_price(currency_pair = 'ETH-USD').get("amount","none")
        print("Price set at: $"+initialPrice)
    price = client.get_spot_price(currency_pair = 'ETH-USD').get("amount","none")
    print(price)
    if ((float)(price) >= (float)(initialPrice)*1.04):#you can change the percentage
        pushClient.send_message("rose 4% today", title="Higher")
        initialPrice = client.get_spot_price(currency_pair = 'ETH-USD').get("amount","none")#reinitialize the set price
        print("Price reinitialized: $"+initialPrice)
        time.sleep(3600)
    elif((float)(price) <= (float)(initialPrice)*0.96):
        pushClient.send_message("dropped 4% today", title="Lower")
        initialPrice = client.get_spot_price(currency_pair = 'ETH-USD').get("amount","none")
        print("Price reinitialized: $"+initialPrice)
        time.sleep(3600)
    time.sleep(180)
