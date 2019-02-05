import urllib
import urllib2
import string

def EPS(stock):
    ups = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = ups.read()
    n=0
    i=0
    for item in page:
        if page[n] == 'E':
            if page[n+1] == 'P':
                if page[n+2] == 'S':
                    if i == 0:
                        eps = float(page[n+70:n+74])
                        i=1
        n+=1   
    return eps
def P_E(stock):
    ups = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = ups.read()
    n=0
    i=0
    for item in page:
        if page[n] == 'P':
            if page[n+1] == '/':
                if page[n+2] == 'E':
                    if i == 0:
                        p_e = float(page[n+70:n+75])
                        i=1
        n+=1
    return p_e

stockname = 'ups' #raw_input()
eps = EPS(stockname)
p_e = P_E(stockname)
print "ESP = ", eps
print "P/E = ", p_e
