import urllib

class Payment:

	def postToService(self):
		params = {}
	
		params['MERCHANT'] = 'OPU_TEST'
		params['ORDER_REF'] = '1441505216094771'
		params['ORDER_DATE'] = 'b602462e2eda02b449d2644debc56688'
		params['PAY_METHOD'] = 'long-lived-token'
		params['ORDER_HASH'] = 'client_credentials'
		params['BACK_REF'] = '1441505216094771'
		params['ORDER_PNAME[0]'] = 'b602462e2eda02b449d2644debc56688'
		params['ORDER_PCODE[0]'] = 'long-lived-token'
		params['ORDER_PRICE[0]'] = 'client_credentials'
		params['ORDER_QTY[0]'] = '1441505216094771'
		params['PRICES_CURRENCY'] = 'b602462e2eda02b449d2644debc56688'
		params['BILL_LNAME'] = 'long-lived-token'
		params['BILL_FNAME'] = 'client_credentials'
		params['BILL_EMAIL'] = '1441505216094771'
		params['BILL_PHONE'] = 'b602462e2eda02b449d2644debc56688'
		params['BILL_COUNTRYCODE'] = 'long-lived-token'
		params['CC_NUMBER'] = 'client_credentials'
		params['EXP_MONTH'] = '1441505216094771'
		params['EXP_YEAR'] = 'b602462e2eda02b449d2644debc56688'
		params['CC_CVV'] = 'long-lived-token'
		params['CC_OWNER'] = 'long-lived-token'
		params['CLIENT_IP'] = 'long-lived-token'
		params['CLIENT_TIME'] = 'long-lived-token'

		params = urllib.urlencode(params)
		f = urllib.urlopen("https://secure.payu.com.tr/order/alu/v2", params)
		print f.read()	
		return f.read()

		'''
	if __name__ =="__main__":
		print "Mert"
		postToService()
		'''