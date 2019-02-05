import urllib
import urllib2
import string

def EPS(stock):
    ups = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = ups.read()
    n=0
    m=0
    k=0
    i=0
    eps = "N/A"
    print len(page)
    for item in page:
        if page[n] == 'E':
            if page[n+1] == 'P':
                if page[n+2] == 'S':
                    if i == 0:
                        i=1
                        while page[n+70] in ['0','1','2','3','4','5','6','7','8','9','-']:
                            if m == 0:
                                eps = []
                                m = 1
                            eps.append(page[n+70])
                            print eps
                            print n
                            n+=1
                            k+=1
                        n-=k
        n+=1   
    return float(eps)
def P_E(stock):
    ups = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = ups.read()
    n=0
    i=0
    p_e = "N/A"
    for item in page:
        if page[n] == 'P':
            if page[n+1] == '/':
                if page[n+2] == 'E':
                    if i == 0:
                        i=1
                        if page[n+70] in ['0','1','2','3','4','5','6','7','8','9','-']:
                            p_e = float(page[n+70:n+75])
                        
        n+=1
    return p_e

stockname = 'vnet' #raw_input()
eps = EPS(stockname)
p_e = P_E(stockname)
print "ESP = ", eps
print "P/E = ", p_e
