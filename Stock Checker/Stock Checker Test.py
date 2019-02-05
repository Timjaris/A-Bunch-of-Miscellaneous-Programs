from yahoo_finance import Share
import urllib
import urllib2
import string
import sys
import math

stock = 'tsla'
url = urllib2.urlopen("http://finance.yahoo.com/q/cf?s=tsla+Cash+Flow&annual")
page = url.read()
i=0
k=0
m=0
n=0
cashflow = []
for item in page:
    if page[n:n+16] == "Cash Equivalents":
        while i < 3:
            if page[n+m:n+m+8] == "<strong>":
                if i == 2:
                    while page[n+m+k+37] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(',')']:
                        if page[n+m+k+37] == '(':
                            cashflow.append('-')
                        elif page[n+m+k+37] not in [',','(',')']:
                            cashflow.append(page[n+m+k+37])
                        k+=1
                
                i+=1
            m+=1
    n+=1

cashflow = ''.join(cashflow)
#cashflow = int(float(cashflow))

print cashflow

