from . import btcapipuller

try:
	import urllib.request as url, json
except:
	import urllib as url, json

class API_BlockChain(btcapipuller.BtcApiPuller):

	def get_name(self):
		return "BlockChain"

	def get_price(self, country):
		response = url.urlopen("https://blockchain.info/ticker");
		data = json.loads(response.read().decode('utf-8'))

		if country in data:
			return data[country]['15m']