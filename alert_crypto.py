import time
import requests
import schedule
import json
import os
from twilio.rest import Client



#schedule when code will run at specific intervals
def perfect_timing():
	schedule.every().day.at("06:00").do(txt_code)
	schedule.every().day.at("07:00").do(txt_code)
	schedule.every().day.at("08:00").do(txt_code)
	schedule.every().day.at("09:00").do(txt_code)
	schedule.every().day.at("10:00").do(txt_code)
	schedule.every().day.at("11:00").do(txt_code)
	schedule.every().day.at("12:00").do(txt_code)
	schedule.every().day.at("13:00").do(txt_code)
	schedule.every().day.at("14:00").do(txt_code)
	schedule.every().day.at("15:00").do(txt_code)
	schedule.every().day.at("16:00").do(txt_code)
	schedule.every().day.at("17:00").do(txt_code)
	schedule.every().day.at("18:00").do(txt_code)
	schedule.every().day.at("19:00").do(txt_code)
	schedule.every().day.at("20:00").do(txt_code)
	schedule.every().day.at("21:00").do(txt_code)
	schedule.every().day.at("22:00").do(txt_code)
	schedule.every().day.at("23:00").do(txt_code)
	schedule.every().day.at("00:00").do(txt_code)


#twilio code to send text message
def txt_code():

	#bitcoin local variables
	response1 = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
	data1 = response1.json()
	currency1 = data1["data"]["base"]
	price1 = data1["data"]["amount"]
	bitcoin_env_amount = float(os.environ.get("bitcoin_amount"))
	pricetofloat1 = float(price1)
	wallet_value1 = pricetofloat1 * bitcoin_env_amount

	#ethereum local variables
	response2 = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
	data2 = response2.json()
	currency2 = data2["data"]["base"]
	price2 = data2["data"]["amount"]
	ethereum_env_amount = float(os.environ.get("ethereum_amount"))
	pricetofloat2 = float(price2)
	wallet_value2 = pricetofloat2 * ethereum_env_amount

	#verbiage to be sent via text message
	output1 = (f"{currency1} {pricetofloat1:.2f}, Bitcoin wallet value is at {wallet_value1:.2f}.\n")
	output2 = (f"\n{currency2} {pricetofloat2:.2f}, Ethereum wallet value is at {wallet_value2:.2f}.")
	
	message_to_send1 = (output1)
	message_to_send2 = (output2)
	receiving_phone_number = os.environ.get("my_phone_number")
	local_time = time.strftime("%A %B %d, %Y and its %X",time.localtime())
	account_sid = os.environ.get("twilio_acct_sid")
	auth_token = os.environ.get("twilio_auth_token")
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
						 body= (message_to_send1 + message_to_send2),
						 from_= os.environ.get("twilio_phone_number"),
						 to= receiving_phone_number
					 )


perfect_timing()


while True:
	schedule.run_pending()
	time.sleep(1)

