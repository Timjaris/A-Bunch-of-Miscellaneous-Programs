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
    #tassets = int(float(tassets))
    
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
    print "cassets=", cassets
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
def Divpaid(stock):
    url = urllib2.urlopen("http://finance.yahoo.com/q/cf?s="+stock+"+Cash+Flow&annual")
    page = url.read()
    n=0
    k=0
    divpaid = []
    for item in page:
        if page[n:n+14] == "Dividends Paid":
            while page[n+k+38] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                if page[n+k+38] != ',':
                    divpaid.append(page[n+k+38])
                k+=1
        n+=1


    divpaid = ''.join(divpaid)
    divpaid = int(float(divpaid))
    
    return divpaid

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
def Output(tassets, cassets, tliab, cliab, p_e, eps, nincome, div, divpaid, trev, stockp, Ip_e, tnx):
    print "Total Assets = ", '%24s' %('$'+str(tassets))
    print "Total Current Assets = ", '%16s' %('$'+str(cassets))
    print "Total Liabilities =", '%20s' %('$'+str(tliab))
    print "Total Current Liabilities =", '%12s' %('$'+str(cliab))
    if p_e == "N/A":
        print "P/E", '%36s' %p_e
    else:
        print "P/E = ", '%33s' %(p_e)
    print "EPS = ", '%33s' %(str(eps))
    print "Net Income =", '%27s' %('$'+str(nincome))
    if div == "N/A":
        print "Dividend =", '%29s' %div
    else:
        print "Dividend =", '%29s' %(str(div))
    print "Dividends Paid =", '%23s' %('$'+str(divpaid))
    print "Total Revenue =", '%24s' %('$'+str(trev))
    print "Stock Price =", '%26s' %('$'+str(stockp))
    print "\nIndustry P/E =",'%25s' %Ip_e
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

        por = float(divpaid) / float(nincome)
        if por >= .4:
            p = 1
        else:
            p=0
        print "Pay out Ratio = ", '%23s' %('{0:.0%}'.format(por)), '%10s' %(p*'(+1.00)'+(1-p)*'(0.00)')
        
        buy_value = h+i+j+k+l+m+n+o+p
        if buy_value >=12:
            buy = ' '
        else:
            buy = ' NOT '

        print "\nTotal buy value = ", '{0:.2f}'.format(buy_value), '\n'
        print "You should"+buy+"buy this!"
        if buy == ' ':
            amounttospend = float(raw_input("How many dollars do you want to invest? "))
            print "With $"+'{0:.2f}'.format(amounttospend)+", you could buy",
            print '{0:.0f}'.format(round(amounttospend/stockp)),
            print "shares and would have an annual income of $"+'{0:.2f}'.format(round(amounttospend/stockp)*div)+'.'
        print "\n*Accuracy dependent on Chad's formula, if it doesn't work, it's his fault"
    return buy_value

#End of Functions 

again = 'y'
tassets = 0
x=-1
while 1: #again == 'y' or again == 'Y':
    stocklist = ['BA','CAT','COP','CSCO','CVX','DD','DIS','DE','GE','GS','GIS','HD','K','T','VZ','S','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MSFT','NKE','NEM','PFE','PG','UNH','WMT','XOM','WY','TSLA','FSLR','WFC','BUD','BAC','YUM','KHC','K','KMI','F','GM','UPS','FDX']
    #aa, axp
    x+=1
    stock = stocklist[x]
    url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
    page = url.read()
    print stock, len(page)
    if len(page) < 77500:
        print "\nThis stock does not appear to exist."
        again = 0#raw_input("\nEnter another stock? (Enter 'y' for yes)")
    else:
        #Inputs
        tassets = Tassets(stock)

        cassets = Cassets(stock)

        tliab = Tliab(stock)
    
        cliab = Cliab(stock)

        p_e = P_E(stock)

        eps = EPS(stock)
    
        nincome = Nincome(stock)
    
        div = Div(stock)

        divpaid = Divpaid(stock)
            
        trev = Trev(stock)
    
        #yiel = Yield(stock)
        #print "Yield =", yiel

        stockp = Stock(stock)
   
        Ip_e = IndusP_E(stock)    

        tnx = TNX()    

        Output(tassets, cassets, tliab, cliab, p_e, eps, nincome, div, divpaid, trev, stockp, Ip_e, tnx)

        #again = raw_input("\nEnter another stock? (Enter 'y' for yes)")

