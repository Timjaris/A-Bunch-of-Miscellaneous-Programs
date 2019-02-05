from yahoo_finance import Share
yahoo = Share('ups')
print float(yahoo.get_price())+1.0



