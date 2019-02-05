
"""
30min, 30min, 1hr, 1hr, 1hr, 30min
Future Ideas:
 fix dates
 make file to store values offline
 Import to document
 display relevant years

 Load all needed pages at the beginning, input into functions DONE
 Add up the Cassets DONE
 Have a bunch of "try"s to remove error messages (except) DONE
"""
from yahoo_finance import Share
import urllib
import urllib2
import string
import sys
import math

#Input Functions
def Title(page):
    n=0
    k=0
    i=0
    title = []
    for item in page:
        if page[n:n+11] == "Summary for":
            while page[n+k+12:n+k+20] != "- Yahoo!" :
                title.append(page[n+k+12])
                k+=1
        n+=1


    title = ''.join(title)
    return title
def Tassets(page):
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

def Cassets(page):
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
    if cassets == []:
        CCE = []
        STI = []
        NR = []
        I = []
        OCA = []
        k=0
        n=0
        for item in page:
            if page[n:n+25] == "Cash And Cash Equivalents":
                while page[n+k+48] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+48] != ',':
                        CCE.append(page[n+k+48])
                    k+=1
                CCE = ''.join(CCE)
                try:
                    CCE = int(float(CCE))
                except:
                    CCE = 0
            k=0
            if page[n:n+22] == "Short Term Investments":
                while page[n+k+45] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+45] != ',':
                        STI.append(page[n+k+45])
                    k+=1
                STI = ''.join(STI)
                try:
                    STI = int(float(STI))
                except:
                    STI = 0
            k=0 
            if page[n:n+15] == "Net Receivables":
                while page[n+k+38] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+38] != ',':
                        NR.append(page[n+k+38])
                    k+=1
                NR = ''.join(NR)
                try:
                    NR = int(float(NR))
                except:
                    NR = 0
            k=0
            if page[n:n+9] == "Inventory":
                while page[n+k+32] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+32] != ',':
                        I.append(page[n+k+32])
                    k+=1
                I = ''.join(I)
                try:
                    I = int(float(I))
                except:
                    I = 0
                
            k=0
            if page[n:n+20] == "Other Current Assets":
                while page[n+k+43] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+43] != ',':
                        OCA.append(page[n+k+43])
                    k+=1
                OCA = ''.join(OCA)
                try:
                    OCA = int(float(OCA))
                except:
                    OCA = 0
                
            n+=1
        cassets = CCE + STI + NR + I + OCA
    try:
        cassets = ''.join(cassets)
        cassets = int(float(cassets))
    except:
        "placeholder"


    return cassets
def Tliab(page):
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
def Cliab(page):
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

    if cliab == []:
        AP = []
        SCLTD = []
        OCL = []
        k=0
        n=0

        for item in page:
            k=0
            if page[n:n+16] == "Accounts Payable":
                while page[n+k+39] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+39] != ',':
                        AP.append(page[n+k+39])
                    k+=1
                AP = ''.join(AP)
                try:
                    AP = int(float(AP))
                except:
                    AP = 0

            k=0
            if page[n:n+28] == "Short/Current Long Term Debt":
                while page[n+k+51] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+51] != ',':
                        SCLTD.append(page[n+k+51])
                    k+=1
                SCLTD = ''.join(SCLTD)
                try:
                    SCLTD = int(float(SCLTD))
                except:
                    SCLTD = 0
            k=0 
            if page[n:n+25] == "Other Current Liabilities":
                while page[n+k+48] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                    if page[n+k+48] != ',':
                        OCL.append(page[n+k+48])
                    k+=1
                OCL = ''.join(OCL)
                try:
                    OCL = int(float(OCL))
                except:
                    OCL = 0
            n+=1
        cliab = AP + SCLTD + OCL

    try:
        cliab = ''.join(cliab)
        cliab = int(float(cliab))
    except:
        "placeholder"

    return cliab

def P_E(page):
    n=0
    m=0
    k=0
    i=0
    p_e = 0
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

    if m == 1:
        p_e = ''.join(p_e)
        p_e = float(p_e)
    return p_e

    
def EPS(page):
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
def Nincome(page):
    n=0
    i=0
    k=0
    nincome = []
    for item in page:
        if page[n:n+10] == "Net Income":
            if i == 0:
                i=1
                while page[n+k+53] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(']:
                    if page[n+k+53] == '(':
                        nincome.append('-')
                    if page[n+k+53] != ',' and page[n+k+53] != '(':
                        nincome.append(page[n+k+53])
                    k+=1
            i=1
        n+=1

    nincome = ''.join(nincome)
    nincome = int(float(nincome))
    return nincome
def Div(page):
    i=0
    n=0
    k=0
    m=0
    div= 0
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

    
    if m == 1:
        div = ''.join(div)
        div = float(div)
    return div
def Divpaid(page):
    try:
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
    except:
        divpaid = 0
    return divpaid

def Trev(page):
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
"""
#Calculating this manually
def Yield(page):
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
"""

def Equity(page):
    n=0
    k=0
    equity = []
    for item in page:
        if page[n:n+24] == "Total Stockholder Equity":
            while page[n+k+180] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                if page[n+k+180] != ',':
                    equity.append(page[n+k+180])
                k+=1
        n+=1


    equity = ''.join(equity)
    equity = int(float(equity))
    return equity

def CashFlow(page):
    n=0
    k=0
    i=0
    cashflow = []
    for item in page:
        if page[n:n+16] == "Cash Equivalents":
            while page[n+k+173] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                if page[n+k+173] != ',':
                    cashflow.append(page[n+k+173])
                k+=1
        n+=1


    cashflow = ''.join(cashflow)
    cashflow = int(float(cashflow))
    return cashflow

def IndusP_E(page, stock):
    try:
        Ip_e = []
        i=0
        m=1
        n=0
        k=0
        for item in page:
            if page[n:n+16] == 'Operating Margin':
                while i == 0:
                    if page[n+k:n+k+13] == 'align="right"':
                        if m == 20:
                            while page[n+k+37] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                                Ip_e.append(page[n+k+37])
                                k+=1
                                i=1
                        m+=1
                    k+=1
                    if k > 10000:
                        i=1
            n+=1
            
        Ip_e = ''.join(Ip_e)
        Ip_e = float(Ip_e)
    except:
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
    

def TNX(page):
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
def PastTassets(page):
    i=0
    k=0
    m=0
    n=0
    tassets = []
    for item in page:
        if page[n:n+12] == "Total Assets":
            while i < 3:
                if page[n+m:n+m+8] == "<strong>":
                    if i == 2:
                        while page[n+m+k+37] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                            if page[n+m+k+37] != ',':
                                tassets.append(page[n+m+k+37])
                            k+=1
                    
                    i+=1
                m+=1
        n+=1


    tassets = ''.join(tassets)
    #tassets = int(float(tassets))

    return tassets
def PastTliab(page):
    i=0
    k=0
    m=0
    n=0
    tliab = []
    for item in page:
        if page[n:n+17] == "Total Liabilities":
            while i < 3:
                if page[n+m:n+m+8] == "<strong>":
                    if i == 2:
                        while page[n+m+k+37] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                            if page[n+m+k+37] != ',':
                                tliab.append(page[n+m+k+37])
                            k+=1
                    
                    i+=1
                m+=1
        n+=1


    tliab = ''.join(tliab)
    tliab = int(float(tliab))

    return tliab

def PastTrev(page):
    i=0
    k=0
    m=0
    n=0
    trev = []
    for item in page:
        if page[n:n+13] == "Total Revenue":
            while i < 3:
                if page[n+m:n+m+8] == "<strong>":
                    if i == 2:
                        while page[n+m+k+37] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                            if page[n+m+k+37] != ',':
                                trev.append(page[n+m+k+37])
                            k+=1
                    
                    i+=1
                m+=1
        n+=1


    trev = ''.join(trev)
    trev = int(float(trev))

    return trev

def PastNincome(page):
    i=0
    k=0
    m=0
    n=0
    nincome = []
    for item in page:
        if page[n:n+10] == "Net Income":
            while i < 4:
                if page[n+m:n+m+8] == "<strong>":
                    if i == 3:
                        while page[n+m+k+37] in ['0','1','2','3','4','5','6','7','8','9','-','.',',','(',')']:
                            if page[n+m+k+37] == '(':
                                nincome.append('-')
                            elif page[n+m+k+37] not in [',','(',')']:
                                nincome.append(page[n+m+k+37])
                            k+=1
                    
                    i+=1
                m+=1
        n+=1


    nincome = ''.join(nincome)
    #nincome = int(float(nincome))

    return nincome

def PastCashFlow(page):
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

    return cashflow

def GetOptionsMonth(stock):
    #input is not a webpage
    #THE DATE NEEDS TO BE FIXED!
    url = urllib2.urlopen("http://finance.yahoo.com/q/op?s=UPS+Options")
    page = url.read()
    
    n=0
    i=0
    date = ""
    monthurl = ""
    for item in page:
        if page[n:n+11] == "option data":
            if i == 3:
                monthurl = "http://finance.yahoo.com/q/op?s=" + stock + page[n+39:n+55]
                date = page[n+78:n+92]
      
            i+=1
        n+=1
    return (monthurl, date)

""" # I don't think this strategy will work
def GetStrikeInterval(page):
    print page
"""

def GetAllSprices(page,stock):
    #There are inconsistent number of strike prices
    #print page
    n=0
    k=0
    i=0
    sprice = []
    spricelist = []
    for item in page:
        if page[n:n+54] == '<strong data-sq=":value" data-raw=""><a href="/q/op?s=':
            sprice = []
            while page[n+k+len(stock)+62] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                sprice.append(page[n+k+len(stock)+62])
                k+=1
            k=0
            sprice = ''.join(sprice)
            sprice = float(sprice)
            spricelist.append(sprice)
            
        n+=1

    return spricelist

def GetBidPrice(page,sprice):
    n=0
    m=0
    i=0
    k=0
    sprice = str(sprice)
    bidp = []
    for item in page:
        if page[n:n+len(sprice)+1] == sprice+'0' and i == 0:
            for item in page[n:n+500]:
                if page[n+m:n+m+32] == '<div class="option_entry Fz-m" >':
                    if i == 2:
                        while page[n+m+k+32] in ['0','1','2','3','4','5','6','7','8','9','-','.',',']:
                            bidp.append(page[n+m+k+32])
                            k+=1
                    i+=1
                m+=1
        n+=1
    bidp = ''.join(bidp)
    bidp = float(bidp)
    
    return bidp
    
#Start of main program
again = 'y'
tassets = 0
x = 0
n = 0
#stocklist =  ['aa','axp','ba','CAT','COP','CSCO','CVX','DD','DIS','DE','GE','GS','GIS','HD','K','T','VZ','S','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MSFT','NKE','NEM','PFE','PG','UNH','WMT','XOM','WY','TSLA','FSLR','WFC','BUD','BAC','YUM','KHC','K','KMI','F','GM','UPS','FDX']

buyvaluelist = []
while again == 'y' or again == 'Y': #float(x)/float(len(stocklist)) < 1: #
    try:
        stock = raw_input("\nEnter stock symbol (e.g. ups): ")
        outputlist = []
        bestdeal = []
        numopt = 1
        b = 0
        i = 0
        
        
        url = urllib2.urlopen("http://finance.yahoo.com/q/op?s="+stock+"+Options")
        options = url.read()

        url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
        summary = url.read()

        (monthurl, date) = GetOptionsMonth(stock)

        url = urllib2.urlopen(monthurl)
        futureoptions = url.read()             
        
        if len(options) < 180000:
            print("\nThis stock does not appear to exist.")
            #buyvaluelist.append("\nThis stock does not appear to exist.")    
        else:
            title = Title(summary)
            
            #This one uses a different method
            yahoo = Share(stock)
            stockp = float(yahoo.get_price())

            spricelist = GetAllSprices(futureoptions,stock)

            #trims dupicates from list
            a =  len(spricelist)
            spricelist.reverse()
            while len(spricelist) > a / 2:
                spricelist.remove(spricelist[0])
            spricelist.reverse()

            #finds strike price nearest stock price
            while stockp > spricelist[i]:
                i+=1
            if spricelist[i] - stockp > stockp - spricelist[i-1]:
                i-=1

            print title
            print "For ", date, '\n'

            while b < 5:
                sprice = spricelist[i + b - 2]
                bidp = GetBidPrice(futureoptions, sprice)
                amountneeded = stockp*numopt*100.0
                selprof = sprice*numopt*100.0 - amountneeded - 16 - .75*numopt+bidp*numopt*100
                nonselprof = bidp * numopt * 100 - 8 - numopt*.75
                
                outputlist.append([stockp, sprice, numopt, bidp, amountneeded, selprof, nonselprof])
                b+=1

            b = 0
            while b < 5:
                bestdeal.append(min(outputlist[b][5],outputlist[b][6]))
                b+=1

            b = 0
                

            while b < 5:
                print "Current Price =", '%26s' %('$'+str('{0:.2f}'.format(stockp)))
                print "Strike Price =",  '%27s' %('$'+str('{0:.2f}'.format(outputlist[b][1])))
                print "# of Options =",  '%27s' %(outputlist[b][2])
                print "Bid Price =",     '%30s' %('$'+str('{0:.2f}'.format(outputlist[b][3]))), '\n' #has to be here for 1 space
                
                print "  Amount Needed =", '%24s' %('$'+str('{0:.2f}'.format(outputlist[b][4])))
                print "  Selected Profit =", '%22s' %('$'+str('{0:.2f}'.format(outputlist[b][5]))),
                if outputlist[b][5] == max(bestdeal):
                    print "   !!!"
                else:
                    print '\n',
                print "  Non-Selected Profit =", '%18s' %('$'+str('{0:.2f}'.format(outputlist[b][6]))),
                if outputlist[b][6] == max(bestdeal):
                    print "   !!!"
                else:
                    print '\n',
                print '\n' #2 spaces
                b+=1

    except ValueError:
        #buyvaluelist.append("Value Error")
        print "Value Error"
    except urllib2.HTTPError:
        x-=1
        print "You have a shitty internet connection, luckily I have prepared for this contigency and the program is re-trying."
    except urllib2.URLError:
        x-=1
        print "You have a shitty internet connection, luckily I have prepared for this contigency and the program is re-trying."



    again = 'y'





