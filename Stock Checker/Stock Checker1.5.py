import urllib
import urllib2
import string
import sys
import math

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
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
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

def IndusP_E(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/in?s="+stock)
    page = url.read()
    m=0
    n=0
    i=1
    k=0
    Ip_e = 'N/A'
    for item in page:
        if page[n:n+24] == 'http://biz.yahoo.com/ic/':
            if m == 0:
                url2 = urllib2.urlopen(page[n:n+32])
                page2 = url2.read()
                m = 1
        n+=1
    
    n=0
    m=0
    k=0
    for item in page2:
        if page2[n:n+16] == 'Earnings:</font>':
            while page2[n+k+72] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                if m == 0:
                    Ip_e = []
                    m = 1
                Ip_e.append(page2[n+k+72])
                k+=1
        n+=1
    Ip_e = ''.join(Ip_e)
    Ip_e = float(Ip_e)
    return Ip_e


    
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

    if len(page) < 77500:
        print "\nThis stock does not appear to exist."
        again = 0#raw_input("\nEnter another stock? (Enter 'y' for yes)")
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
            print "P/E = ", '%33s' %(p_e)

        Ip_e = IndusP_E(stock)
        print "Industry P/E =",'%25s' %Ip_e

        
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
            again = 2#raw_input("\nEnter another stock? (Enter 'y' for yes)")
        else:
            buy = 0
            h=0
            i=0
            j=0
            k=0
            l=0
            m=0
            n=0
            plus = ''
            buy = ''
            
            debtratio = float(tliab) / float(tassets)
            h = -.1*debtratio*100+5
            if h>0:
                plus = '+'
            else:
                plus = ''
            print '\n', "Debt Ratio =", '%27s' %'{0:.0%}'.format(debtratio), '%10s' %('('+plus+'{0:.2f}'.format(h)+')')

            roa = float(nincome) / float(tassets)
            i = roa*100 - 7
            if i>0:
                plus = '+'
            else:
                plus = ''
            print "Return on Asset =", '%22s' %('{0:.0%}'.format(roa)), '%10s' %('('+plus+'{0:.2f}'.format(i)+')')
    
            Promar = float(nincome) / float(trev)
            if Promar > .1:
                j=1
            elif Promar < .05:
                j=-1
            if j>0:
                plus = '+'
            else:
                plus = ''
            print "Profit Margin =", '%24s' %('{0:.0%}'.format(Promar)),'%10s' %('('+plus+'{0:.2f}'.format(j)+')')

            Crat = float(cassets) / float(cliab)
            k = (.1*Crat*100-10)/4
            if k>0:
                plus = '+'
            else:
                plus = ''
            print "Current Ratio =", '%24s' %('{0:.0%}'.format(Crat)),'%10s' %('('+plus+'{0:.2f}'.format(k)+')')

            fmv = eps*(stockp)*(tnx+2.0)/10.0
            l = 2 * fmv / stockp - 2
            if l>0:
                plus = '+'
            else:
                plus = ''
            print "Fair Market Value =", '%20s' %('$'+'{0:.2f}'.format(fmv)),'%10s' %('('+plus+'{0:.2f}'.format(l)+')')

            #keep as is
            mos = fmv - stockp
            if mos > 50:
                m=1
            if m>0:
                plus = '+'
            else:
                plus = ''
            print "Margin of Saftey =", '%21s' %('$'+'{0:.2f}'.format(mos)),'%10s' %('('+plus+'{0:.2f}'.format(m)+')')

            divy = 0
            if div == "N/A":
                print "Dividend Yield =          N/A"
            else:
                divy = div / stockp
                n = divy*100 - tnx
                if n>0:
                    plus = '+'
                else:
                    plus = ''
                print "Dividend Yield =",'%23s' %('{0:.2%}'.format(divy)),'%10s' %('('+plus+'{0:.2f}'.format(n)+')')


            PE_to_Industry = p_e / Ip_e
            o = -10*PE_to_Industry+10
            if o>0:
                plus = '+'
            else:
                plus = ''
            print "P/E to Industry P/E Ratio =",'%12s'%('{0:.0%}'.format(PE_to_Industry)), '%10s' %('('+plus+'{0:.2f}'.format(o)+')')

            

            buy_value = h+i+j+k+l+m+n+o
            if buy_value >=12:
                buy = ' '
            else:
                buy = ' NOT '

            print "\nTotal buy value = ", '{0:.2f}'.format(buy_value), '\n'
            print "You should"+buy+"buy this!"
            if buy == ' ':
                print "With $500, you could buy", '{0:.0f}'.format(round(500/stockp)),
                print "stocks and would have an annual income of $"+'{0:.2f}'.format(round(500/stockp)*div)+'.'
            print "\n*Accuracy dependent on Chad's formula, if it doesn't work, it's his fault"
            #again = raw_input("\nEnter another stock? (Enter 'y' for yes)")

