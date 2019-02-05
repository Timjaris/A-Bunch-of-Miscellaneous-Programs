import urllib
import urllib2
import string
import sys

def Tassets(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
    page = url.read()
    n=0
    k=0
    tassets = []
    for item in page:
        if page[n:n+12] == "Total Assets":
            while page[n+k+168] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                if page[n+k+168] != ',':
                    tassets.append(page[n+k+168])
                k+=1
        n+=1


    tassets = ''.join(tassets)
    tassets = int(float(tassets))
    
    return tassets
def Cassets(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
    page = url.read()
    n=0
    k=0
    i=0
    cassets = []
    for item in page:
        if page[n:n+20] == "Total Current Assets":
            if i == 0:
                i=1
                while page[n+k+176] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+176] != ',':
                        cassets.append(page[n+k+176])
                    k+=1
        n+=1


    cassets = ''.join(cassets)
    cassets = int(float(cassets))
    return cassets
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
        if page[n:n+3] == 'P/E':
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
    if m == 1:
        p_e = float(p_e)
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
        if page[n:n+3] == 'EPS':
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
    eps = ''.join(eps)
    eps = float(eps)
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
    m=0
    div='N/A'
    for item in page:
        if page[n:n+5] == "Div &":
            if i == 0:
                i=1
                while page[n+k+49] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if m == 0:
                        div = []
                        m=1
                    if page[n+k+49] != ',':
                        div.append(page[n+k+49])
                    k+=1
            i=1
        n+=1

    div = ''.join(div)
    if m == 1:
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
    m=0
    yiel = 'N/A'
    for item in page:
        if page[n:n+5] == "Div &":
            if i == 0:
                i=1
                while page[n+k+55] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(']:
                    if m==0:
                        yiel = []
                        m=1
                    if page[n+k+55] != ',' and page[n+k+55] != '(':
                        yiel.append(page[n+k+55])
                    k+=1
            i=1
        n+=1

    yiel = ''.join(yiel)
    if m == 1:
        yiel = float(yiel)
    return yiel

def Stock(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
    n=0
    i=0
    k=0
    chad = 0 
    stockp = []
    if stock == 't' or stockp == 'T':
        chad = 20
    elif len(stock) == 1:
        chad = 5
    for item in page:
        if page[n:n+len(stock)+2] == stock+'">':
            if i == chad:
                
                i += 1
                while page[n+k+len(stock)+2] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(']:
                    if page[n+k+len(stock)+2] != ',':
                        stockp.append(page[n+k+len(stock)+2])
                    k+=1
            else:
                i +=1
        n+=1
    stockp = ''.join(stockp)
    stockp = float(stockp)
    return stockp
def TNX():
    url = urllib2.urlopen("http://finance.yahoo.com/q?s=^tnx")
    page = url.read()

    n=0
    k=0
    i=0
    tnx = []
    for item in page:
        if page[n:n+5] == 'tnx">':
            if i == 0:
                i=1
                while page[n+k+5] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+5] != ',':
                        tnx.append(page[n+k+5])
                    k+=1
        n+=1
    tnx = ''.join(tnx)
    tnx = float(tnx)
    return tnx
again = 'y'
tassets = 0
while 1: #again == 'y' or again == 'Y':
    stock = raw_input("\nEnter stock symbol (e.g. ups): ")
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()

    if len(page) < 78000:
        print "\nThis stock does not appear to exist."
        again = raw_input("\nEnter another stock? (Enter 'y' for yes)")
    else:
        #Inputs
        tassets = Tassets(stock)
        print "Total Assets = ", '%24s' %('$'+str(tassets))

        cassets = Cassets(stock)
        print "Total Current Assets = ", '%16s' %('$'+str(cassets))

        tliab = Tliab(stock)
        print "Total Liabilities =", '%20s' %('$'+str(tliab))

        cliab = Cliab(stock)
        print "Total Current Liabilities =", '%12s' %('$'+str(cliab))

        p_e = P_E(stock)
        if p_e == "N/A":
            print "P/E", '%36s' %p_e
        else:
            print "P/E = ", '%33s' %(str(p_e))

        eps = EPS(stock)
        print "EPS = ", '%33s' %(str(eps))

        nincome = Nincome(stock)
        print "Net Income =", '%27s' %('$'+str(nincome))

        div = Div(stock)
        if div == "N/A":
            print "Dividend =", '%29s' %div
        else:
            print "Dividend =", '%29s' %(str(div))

        trev = Trev(stock)
        print "Total Revenue =", '%24s' %('$'+str(trev))

        #yiel = Yield(stock)
        #print "Yield =", yiel

        stockp = Stock(stock)
        print "Stock Price =", '%26s' %('$'+str(stockp))

        tnx = TNX()
        print "TNX =", '%34s' %(str(tnx)+'%')

        #Calculations
        if p_e == "N/A" or div == "N/A":
            print "\nSome values are not applicable."
            again = raw_input("\nEnter another stock? (Enter 'y' for yes)")
        else:
            buy = 0
            h=0
            i=0
            j=0
            k=0
            l=0
            m=0
            n=0
            debtratio = float(tliab) / float(tassets)
            if debtratio < .4:
                h=1
            elif debtratio >.71:
                h=-1
            print '\n', "Debt Ratio =", '%16s' %'{0:.0%}'.format(debtratio), '%10s' %(h*"Good"+(-1)*h*"Bad")

            ros = float(nincome) / float(tassets)
            if ros > .15:
                i=1
            elif ros < .09:
                i=-1
            print "Return on Asset =", '%11s' %('{0:.0%}'.format(ros)), '%10s' %(i*"Good"+(-1)*i*"Bad")
    
            Promar = float(nincome) / float(trev)
            if Promar > .15:
                j=1
            elif Promar < .09:
                j=-1
            print "Profit Margin =", '%13s' %('{0:.0%}'.format(Promar)),'%10s' %(i*"Good"+(-1)*i*"Bad")

            Crat = float(cassets) / float(cliab)
            if Crat > 1.3:
                k=1
            elif Crat < 1:
                k=-1
            print "Current Ratio =", '%13s' %('{0:.0%}'.format(Crat)),'%10s' %(k*"Good"+(-1)*k*"Bad")

            fmv = 11.0*eps*stockp/25.0
            if fmv > stockp:
                l=1
            elif fmv < stockp:
                l=-1
            print "Fair Market Value =", '%9s' %('$'+'{0:.2f}'.format(fmv)),'%10s' %(l*"Good"+(-1)*l*"Bad")

            mos = fmv - stockp
            if mos > 50:
                m=1
            else:
                m=-1
            print "Margin of Saftey =", '%10s' %('$'+'{0:.2f}'.format(mos)),'%10s' %(m*"Good"+(-1)*m*"Bad")

            divy = 0
            if div == "N/A":
                print "Dividend Yield =          N/A"
            else:
                divy = div / stockp
                if divy*100 > tnx:
                    n = 1
                elif divy*100 < tnx:
                    n = -1
                print "Dividend Yield =", '%12s' %('{0:.0%}'.format(divy)),'%10s' %(n*"Good"+(-1)*n*"Bad"), '\n'


            if h+i+j+k+l+m >= 5:
                print "BUY!"
            else:
                print "DO NOT BUY!"
            print "*Accuracy dependent on Chad's formula, if it doesn't work, it's his fault"
            again = raw_input("\nEnter another stock? (Enter 'y' for yes)")

