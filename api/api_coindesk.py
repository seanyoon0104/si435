from . import btcapipuller

try:
	import urllib.request as url, json
except:
	import urllib as url, json

class API_CoinDesk(btcapipuller.BtcApiPuller):

	def get_name(self):
		return "CoinDesk"

	def get_price(self, country):
		response = url.urlopen("http://api.coindesk.com/v1/bpi/currentprice/"+country+".json");
		data = json.loads(response.read().decode('utf-8'))

		if "bpi" in data:
			return data["bpi"][country]["rate"]