
"""
Future Ideas:
 make file to store values offline
 Load all needed pages at the beginning, input into functions
 Add up the Cassets
 Import to document
 chad's new variables
 new weighting?

 Have a bunch of "try"s to remove error messages (except) DONE
"""
from yahoo_finance import Share
import urllib
import urllib2
import string
import sys
import math

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

#Start of main program
again = 'y'
tassets = 0
i=0
x = 0
n = 0
stocklist =  ['aa','axp','ba','CAT','COP','CSCO','CVX','DD','DIS','DE','GE','GS','GIS','HD','K','T','VZ','S','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MSFT','NKE','NEM','PFE','PG','UNH','WMT','XOM','WY','TSLA','FSLR','WFC','BUD','BAC','YUM','KHC','K','KMI','F','GM','UPS','FDX']

#stocklist =  ['aa','ba','CAT','COP','CSCO','CVX','DD','DIS','DE','GE','GIS','HD','K','T','VZ','IBM','INTC','JNJ','KO','MCD','MMM','MSFT','NKE','NEM','PFE','PG','WMT','XOM','WY','YUM','K','KMI','F','GM','UPS','FDX']
buyvaluelist = []
while float(x)/float(len(stocklist)) < 1: #again == 'y' or again == 'Y':
    try:
        print "Loading... "+'{0:.2%}'.format(float(x)/float(len(stocklist)))
        
        #Inputting all relevant pages
        stock = 'khc' #stocklist[x]
        url = urllib2.urlopen("http://finance.yahoo.com/q?s="+stock)
        summery = url.read()
        
        url = urllib2.urlopen("http://finance.yahoo.com/q/op?s="+stock+"+Options")
        options = url.read()

        url = urllib2.urlopen("http://finance.yahoo.com/q/co?s="+stock+"+Competitors")
        competitors = url.read()

        url = urllib2.urlopen("http://finance.yahoo.com/q/is?s="+stock+"+Income+Statement&annual")
        incomestatement = url.read()
    
        url = urllib2.urlopen("http://finance.yahoo.com/q/bs?s="+stock+"+Balance+Sheet&annual")
        balance = url.read()

        url = urllib2.urlopen("http://finance.yahoo.com/q/cf?s="+stock+"+Cash+Flow&annual")
        cashflow = url.read()

        url = urllib2.urlopen("http://finance.yahoo.com/q?s=^tnx")
        tnxpage = url.read()

        x+=1
        print stock
        if len(options) < 180000:
            buyvaluelist.append("\nThis stock does not appear to exist.")
            again = 0#raw_input("\nEnter another stock? (Enter 'y' for yes)")
            
        else:
            #Getting the variables from the pages
            tassets = Tassets(balance)
            cassets = Cassets(balance)
            print "yes"
            tliab = Tliab(balance)
            print "yes"
            cliab = Cliab(balance)
            p_e = P_E(summery)
            eps = EPS(summery)
            nincome = Nincome(incomestatement)
            div = Div(summery)
            divpaid = Divpaid(cashflow)
            trev = Trev(incomestatement)
            yiel = Yield(summery)
            
            #This one uses a different method
            yahoo = Share(stock)
            stockp = float(yahoo.get_price())
            
            Ip_e = IndusP_E(competitors, stock)
            tnx = TNX(tnxpage)
            
            #printing the variables
            """
            print "Total Assets = ", '%24s' %('$'+str(tassets))
            print "Total Current Assets = ", '%16s' %('$'+str(cassets))
            print "Total Liabilities =", '%20s' %('$'+str(tliab))
            print "Total Current Liabilities =", '%12s' %('$'+str(cliab))
            print "P/E = ", '%33s' %(p_e)
            print "EPS = ", '%33s' %(str(eps))
            print "Net Income =", '%27s' %('$'+str(nincome))
            print "Dividend =", '%29s' %(str(div))
            print "Dividends Paid =", '%23s' %('$'+str(divpaid))
            print "Total Revenue =", '%24s' %('$'+str(trev))
            print "Stock Price =", '%26s' %('$'+str(stockp))
            print "Yield =", yiel
            print "\nIndustry P/E =",'%25s' %Ip_e
            print "TNX =", '%34s' %(str(tnx)+'%')
            """
            #Calculations

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
            #print '\n', "Debt Ratio =", '%27s' %'{0:.0%}'.format(debtratio), '%10s' %('('+plus+'{0:.2f}'.format(h)+')')

            roa = float(nincome) / float(tassets)
            i = roa*100 - 7
            if i>0:
                plus = '+'
            else:
                plus = ''
            #print "Return on Asset =", '%22s' %('{0:.0%}'.format(roa)), '%10s' %('('+plus+'{0:.2f}'.format(i)+')')
    
            Promar = float(nincome) / float(trev)
            if Promar > .1:
                j=1
            elif Promar < .05:
                j=-1
            if j>0:
                plus = '+'
            else:
                plus = ''
            #print "Profit Margin =", '%24s' %('{0:.0%}'.format(Promar)),'%10s' %('('+plus+'{0:.2f}'.format(j)+')')

            Crat = float(cassets) / float(cliab)
            k = (.1*Crat*100-10)/4
            if k>0:
                plus = '+'
            else:
                plus = ''
            #print "Current Ratio =", '%24s' %('{0:.0%}'.format(Crat)),'%10s' %('('+plus+'{0:.2f}'.format(k)+')')

            fmv = eps*(stockp)*(tnx+2.0)/10.0
            l = 2 * fmv / stockp - 2
            if l>0:
                plus = '+'
            else:
                plus = ''
            #print "Fair Market Value =", '%20s' %('$'+'{0:.2f}'.format(fmv)),'%10s' %('('+plus+'{0:.2f}'.format(l)+')')

            #keep as is
            mos = fmv - stockp
            if mos > 50:
                m=1
            if m>0:
                plus = '+'
            else:
                plus = ''
            #print "Margin of Safety =", '%21s' %('$'+'{0:.2f}'.format(mos)),'%10s' %('('+plus+'{0:.2f}'.format(m)+')')

            divy = 0
            #if div == "N/A":
                #print "Dividend Yield =          N/A"
            #else:
                #divy = div / stockp
                #n = divy*100 - tnx
                #if n>0:
                    #plus = '+'
                #else:
                    #plus = ''
                #print "Dividend Yield =",'%23s' %('{0:.2%}'.format(divy)),'%10s' %('('+plus+'{0:.2f}'.format(n)+')')



            PE_to_Industry = p_e / Ip_e
            o = -10*PE_to_Industry+10
            if o>0:
                plus = '+'
            else:
                plus = ''
            #print "P/E to Industry P/E Ratio =",'%12s'%('{0:.0%}'.format(PE_to_Industry)), '%10s' %('('+plus+'{0:.2f}'.format(o)+')')

            por = float(divpaid) / float(nincome)
            if por >= .4:
                p = 1
            else:
                p=0
            #print "Pay out Ratio = ", '%23s' %('{0:.0%}'.format(por)), '%10s' %(p*'(+1.00)'+(1-p)*'(0.00)')

            buy_value = h+i+j+k+l+m+n+o+p
            if buy_value >=12:
                buy = ' '
            else:
                buy = ' NOT '

            buyvaluelist.append(buy_value)
            

            """
            print "\nTotal buy value = ", '{0:.2f}'.format(buy_value), '\n'
            print "You should"+buy+"buy this!"
            if buy == ' ':
                amounttospend = float(raw_input("How many dollars do you want to invest? "))
                print "With $"+'{0:.2f}'.format(amounttospend)+", you could buy",
                print '{0:.0f}'.format(round(amounttospend/stockp)),
                print "shares and would have an annual income of $"+'{0:.2f}'.format(round(amounttospend/stockp)*div)+'.'
            print "\n*Accuracy dependent on Chad's formula, if it doesn't work, it's his fault"
            #again = raw_input("\nEnter another stock? (Enter 'y' for yes)")
            """
    except ValueError:
        buyvaluelist.append("Value Error")
        print "Value Error"
    except urllib2.HTTPError:
        x-=1
        print "You have a shitty internet connection, luckily I have prepared for this contigency and the program is re-trying."
    except urllib2.URLError:
        x-=1
        print "You have a shitty internet connection, luckily I have prepared for this contigency and the program is re-trying."


    
x = len(buyvaluelist)-1
sortedlist = zip(buyvaluelist, stocklist)
sortedlist = sorted(sortedlist)

print '\n\n'
for item in sortedlist:
    #if sortedlist[x][0] <= 10000 and sortedlist[x][0] >= 10:
    print sortedlist[x][1],  " "*(5-len(sortedlist[x][1])), " = ", '%12s' %(sortedlist[x][0])
    x-=1


x = input()



















