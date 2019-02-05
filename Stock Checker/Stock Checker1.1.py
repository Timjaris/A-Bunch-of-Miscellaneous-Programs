import urllib
import urllib2
import string

def Tassets(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
    page = url.read()
    n=0
    k=0
    Tassets = []
    for item in page:
        if page[n:n+12] == "Total Assets":
            while page[n+k+168] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                if page[n+k+168] != ',':
                    Tassets.append(page[n+k+168])
                k+=1
        n+=1


    Tassets = ''.join(Tassets)
    Tassets = int(float(Tassets))
    return Tassets
def Cassets(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
    page = url.read()
    n=0
    k=0
    i=0
    Cassets = []
    for item in page:
        if page[n:n+20] == "Total Current Assets":
            if i == 0:
                i=1
                while page[n+k+176] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+176] != ',':
                        Cassets.append(page[n+k+176])
                    k+=1
        n+=1


    Cassets = ''.join(Cassets)
    Cassets = int(float(Cassets))
    return Cassets
def Tliab(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
    page = url.read()
    n=0
    k=0
    i=0
    tliab = []
    for item in page:
        if page[n:n+17] == "Total Liabilities":
            if i == 0:
                i=1
                while page[n+k+173] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+173] != ',':
                        tliab.append(page[n+k+173])
                    k+=1
        n+=1


    tliab = ''.join(tliab)
    tliab = int(float(tliab))
    return tliab
def Cliab(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
    page = url.read()
    n=0
    k=0
    i=0
    cliab = []
    for item in page:
        if page[n:n+25] == "Total Current Liabilities":
            if i == 0:
                i=1
                while page[n+k+181] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+181] != ',':
                        cliab.append(page[n+k+181])
                    k+=1
        n+=1

    cliab = ''.join(cliab)
    cliab = int(float(cliab))
    return cliab
    




def P_E(stock):
    ups = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = ups.read()
    n=0
    m=0
    k=0
    i=0
    p_e = "N/A"
    for item in page:
        if page[n] == 'P':
            if page[n+1] == '/':
                if page[n+2] == 'E':
                    if i == 0:
                        i=1
                        while page[n+70] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                            if m == 0:
                                p_e = []
                                m = 1
                            p_e.append(page[n+70])
                            n+=1
                            k+=1
                        n-=k
        n+=1
    p_e = ''.join(p_e)
    return p_e
def EPS(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
    n=0
    m=0
    k=0
    i=0
    eps = "N/A"
    for item in page:
        if page[n] == 'E':
            if page[n+1] == 'P':
                if page[n+2] == 'S':
                    if i == 0:
                        i=1
                        while page[n+70] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                            if m == 0:
                                eps = []
                                m = 1
                            eps.append(page[n+70])
                            n+=1
                            k+=1
                        n-=k
        n+=1
    #try
    eps = ''.join(eps)
    return eps
def Nincome(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/is?s="+stock+"+Income+Statement&annual")
    page = url.read()
    n=0
    i=0
    k=0
    nincome = []
    for item in page:
        if page[n:n+10] == "Net Income":
            if i == 0:
                i=1
                while page[n+k+53] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(']:
                    if page[n+k+53] != ',' and page[n+k+53] != '(':
                        nincome.append(page[n+k+53])
                    k+=1
            i=1
        n+=1

    nincome = ''.join(nincome)
    nincome = int(float(nincome))
    return nincome
def Div(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
    i=0
    n=0
    k=0
    div=[]
    for item in page:
        if page[n:n+5] == "Div &":
            if i == 0:
                i=1
                while page[n+k+49] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+49] != ',':
                        div.append(page[n+k+49])
                    k+=1
            i=1
        n+=1

    div = ''.join(div)
    div = float(div)
    return div
def Trev(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/is?s="+stock+"+Income+Statement&annual")
    page = url.read()
    i=0
    n=0
    k=0
    trev = []
    for item in page:
        if page[n:n+13] == "Total Revenue":
            if i == 0:
                i=1
                while page[n+k+169] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+169] != ',':
                        trev.append(page[n+k+169])
                    k+=1
            i=1
        n+=1

    trev = ''.join(trev)
    trev = int(float(trev))
    return trev
def Yield(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
    i=0
    n=0
    k=0
    yiel = []
    for item in page:
        if page[n:n+5] == "Div &":
            if i == 0:
                i=1
                while page[n+k+55] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(']:
                    if page[n+k+55] != ',' and page[n+k+55] != '(':
                        yiel.append(page[n+k+55])
                    k+=1
            i=1
        n+=1

    yiel = ''.join(yiel)
    yiel = float(yiel)
    return yiel

def Stock(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
    print page
    


stock = 'vnet' #raw_input("Enter stock symbol (e.g. ups): ")

Tassets = Tassets(stock)
print "Total Assets = ", Tassets

Cassets = Cassets(stock)
print "Total Current Assets = ", Cassets

Tliab = Tliab(stock)
print "Total Liabilities =", Tliab

Cliab = Cliab(stock)
print "Total Current Liabilities =", Cliab

p_e = P_E(stock)
print "P/E = ", p_e

eps = EPS(stock)
print "ESP = ", eps

Nincome = Nincome(stock)
print "Net Income =", Nincome

div = Div(stock)
print "Dividend =", div

trev = Trev(stock)
print "Total Revenue", trev

yiel = Yield(stock)
print "Yield =", yiel

stockp = Stock(stock)
print "Stock Price =", stockp


debtratio = Tliab / Tassets
print '\n', "Debt Ratio =", debtratio






yiel = Yield(stock)
print "Yield =", yiel
