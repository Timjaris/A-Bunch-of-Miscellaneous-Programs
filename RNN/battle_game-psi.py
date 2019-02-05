import random, sys
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation 
from keras.layers import SimpleRNN

#RNN input = 
model = Sequential() 
outputDim = 4
#Do we need to return a sequence? All we care about it the current turn. 
model.add(SimpleRNN(outputDim, input_shape = (None, 13), return_sequences = True))
model.compile(loss='mean_squared_error', optimizer = 'sgd')

winPredictor = Sequential()
winPredictor.add(Dense(10, input_shape = (14, )))
#winPredictor.add(Dense(10))
winPredictor.add(Dense(3))
winPredictor.compile(loss='mean_squared_error', optimizer = 'RMSprop')


#[player_health, computer_health, attack_stat, defense_stat, heal_stat, spa_stat, attack_statc, defense_statc, heal_statc, spa_statc, pattack, pdefend, cattack, cdefend, cdamage, pdamage, pturn, cturn, ccharge, pcharge, level]

#output layer = [attack, defend, heal, special]


def verification(wp, X, Y, stage = ""):
    correct = 0
    total = 0
    predictions = wp.predict(X)
    for i in range(len(Y)):
        pred = predictions[i]
        total += 1
        if np.argmax(pred) == np.argmax(Y[i]):
            correct += 1
    print("Accuracy: ", correct, " / ", total, " = ", correct / total)
    return correct / total

#The game state
class g():
    def __init__(self, dmin, dmax):
        self.attack_stat = random.randint(dmin, dmax)
        self.defense_stat = random.randint(dmin, dmax)
        self.heal_stat = random.randint(dmin, dmax)
        self.spa_stat = random.randint(dmin, dmax)
        self.attack_statc = random.randint(dmin, dmax)
        self.defense_statc = random.randint(dmin, dmax)
        self.heal_statc = random.randint(dmin, dmax)
        self.spa_statc = random.randint(dmin, dmax)
        
        self.player_health = 100
        self.computer_health = 100
        self.level = 0
        self.pcharge = 4
        self.ccharge = 4
        
    def getList(self):
        return [self.attack_stat, self.defense_stat,
                self.heal_stat, self.spa_stat, self.attack_statc,
                self.defense_statc, self.heal_statc, self.spa_statc,
                self.player_health, self.computer_health, self.level,
                self.pcharge, self.ccharge]
        
    def getRivalView(self):
        return [self.attack_statc,
                self.defense_statc, self.heal_statc, self.spa_statc,
                self.attack_stat, self.defense_stat, self.heal_stat, 
                self.spa_stat, self.computer_health, self.player_health,  
                self.level, self.ccharge, self.pcharge]

def getTurn():
    return str(random.randint(1, 4))

#minimax?
#Options: simulate a bunch of turns, do what the winPredictor says is best on average
    #simulate 1 turn with the dice = 10.5
def simulateNextTurn(player, gameState):
    #"What would I do in my oppenent's shoes?
    gs = gameState.getList()
    return 0


def battle(human):
    result = []
    win = [];
        
    #dice setting
    dmin = 1
    dmax = 20
    #intro
    print("Welcome to the battle game!")
    name = "bot" 
    if human:
        name = input("What is your characters name?")
        print("Hello",name,",it is time to roll for stats.")
    else:
        print("Hello bot,it is time to roll for stats.")
    print("Rolling the dices...")
    print("The values are:")
    gameState = g(dmin, dmax)
    
    pattack = 0
    pdefend = 0
    cattack = 0
    cdefend = 0
    cdamage = 0
    pdamage = 0
    pturn = 0
    cturn = 0
    print("your attack stat is",gameState.attack_stat,"and your defense stat is",gameState.defense_stat)
    print("Your healing stat is",gameState.heal_stat,"and your Special attack stat is",gameState.spa_stat)
    print("The computer's attack stat is",gameState.attack_statc,"and its defense stat is",gameState.defense_statc)
    print("The computer's healing stat is",gameState.heal_statc,"and Special attack stat is",gameState.spa_statc)
    #begin game

    
    while gameState.player_health > 0 and gameState.computer_health > 0:
        gameState.ccharge = min(4,gameState.ccharge)
        gameState.pcharge = min(4,gameState.pcharge)
        gameState.player_health = min(100,gameState.player_health)
        gameState.computer_health = min(100,gameState.computer_health)
        gameState.level += 1
        #player turn
        print("Round",gameState.level)
        print("player health",gameState.player_health)
        print("computer health",gameState.computer_health)
        
        if human:
            turn = input("Attack(1) Defend(2) Heal(3) Special attack(4)")
        else:
            turn = getTurn()

        while turn not in ['1','2','3','4']:
            print("Invalid input,Please try again")
            turn = input("Attack(1) Defend(2) Heal(3) Special attack(4)")
        turn = int(turn)
        result.append([turn] + gameState.getList())
        if turn == 1:
               pturn = 'Attack'
               aroll = random.randint(dmin, dmax)
               totala = aroll + gameState.attack_stat
               print(name,"rolled",aroll,"for an attack of",totala)
               pattack = totala
               pdefend = gameState.defense_stat
        
        if turn == 2:
                pturn = 'Defend'
                pdefense = random.randint(dmin, dmax)
                ptotaldefense = pdefense + gameState.defense_stat
                print(name,"rolled",pdefense,"for a defense of",ptotaldefense)
                pattack = 0
                pdefend = ptotaldefense
                
        if turn == 3:
                pturn = 'Heal'
                pheal = random.randint(dmin, dmax)
                ptotalheal = pheal + gameState.heal_stat
                print(name,"rolled",pheal,"for a heal of",ptotalheal)
                gameState.player_health += ptotalheal
                pattack = 0
                pdefend = gameState.defense_stat
                
        if turn == 4:
                if gameState.pcharge == 4:
                    pturn =  'Special_Attack'
                    aroll = random.randint(dmin, dmax)
                    totala = (aroll + gameState.attack_stat) + gameState.spa_stat
                    print(name,"rolled",aroll,"for a Special attack of",totala)
                    gameState.pcharge -= 4
                    pattack = totala
                    pdefend = gameState.defense_stat
                elif gameState.pcharge < 4 :
                    pturn =   'Failed_Special_Attack'
                    aroll = random.randint(dmin, dmax)
                    totala = (aroll + gameState.attack_stat) * 0
                    print(name,"rolled",aroll,"for a failed specail attack of",totala)
                    pattack = totala
                    pdefend = gameState.defense_stat
            
        
            
            
        if gameState.computer_health > 0:
            """
            x = 20 + gameState.attack_stat + gameState.spa_stat 
            if gameState.ccharge == 4:
                turnc = 4
            elif 10 < gameState.computer_health < x:
                turnc = 3
            elif gameState.computer_health <= 10:
                turnc = 2
            else:
                turnc = 1
            """
            turnc = int(getTurn())
            
            if turnc == 1:
                   cturn = 'Attack'
                   caroll = random.randint(dmin, dmax)
                   totalac = caroll + gameState.attack_statc
                   print("computer rolled",caroll,"for an attack of",totalac)
                   cattack = totalac
                   cdefend = gameState.defense_statc
            if turnc == 2:
                    cturn = 'Defend'
                    cdefense = random.randint(dmin, dmax)
                    ctotaldefense = cdefense + gameState.defense_statc
                    print("Computer rolled",cdefense,"for a defense of",ctotaldefense)
                    cattack = 0
                    cdefend = ctotaldefense
            if turnc == 3:
                    cturn = 'Heal'
                    cheal = random.randint(dmin, dmax)
                    ctotalheal = cheal + gameState.heal_statc
                    print("computer rolled",cheal,"for a heal of",ctotalheal)
                    gameState.computer_health += ctotalheal
                    cattack = 0
                    cdefend = gameState.defense_stat
            if turnc == 4:
                    if gameState.ccharge == 4:
                        cturn =  'Special_Attack'
                        caroll = random.randint(dmin, dmax)
                        totalac = (caroll + gameState.attack_statc) + gameState.spa_statc
                        print("Computer rolled",caroll,"for a Special attack of",totalac)
                        gameState.ccharge -= 4
                        cattack = totalac
                        cdefend = gameState.defense_statc
                    elif gameState.ccharge <4 :
                        cturn =   'Failed_Special_Attack'
                        caroll = random.randint(dmin, dmax)
                        totalac = (caroll + gameState.attack_statc) * 0
                        print("computer rolled",caroll,"for a failed specail attack of",totalac)
                        cattack = totalac
                        cdefend = gameState.defense_statc
        #results
        print("Results....")
        cdamage = pattack - cdefend
        cdamage = max(0,cdamage)
        pdamage = cattack - pdefend
        pdamage = max(0,pdamage)
        gameState.player_health -=pdamage
        gameState.computer_health -= cdamage
        gameState.pcharge += 1
        gameState.ccharge += 1
        print(name,"used",pturn,"and dealt",cdamage," damage and took",pdamage,"damage")
        print("Computer used",cturn,"and dealt",pdamage," damage and took",cdamage,"damage")
        print("Next Round.....")
        if gameState.computer_health <= 0:
                print("player health",gameState.player_health)
                print("computer health",gameState.computer_health)
                print("Congradulations! You win!")
                win = [1, 0, 0]
                score = gameState.level + gameState.player_health
                print("Your score is",score)
        if gameState.player_health <= 0:
                print("player health",gameState.player_health)
                print("computer health",gameState.computer_health)
                print("Sorry! You lose!")
                win = [0, 1, 0]
                score = gameState.level + gameState.player_health
                print("Your score is",score)
       
        
        
        if gameState.level >= 100:
            #win, loss, draw
            win = [0, 0, 1]
            break
        
        
    return (result, win)

"""
if __name__ == "__main__":    
    again = "y"
    while again[0]=="y":
        if __name__ == "__main__":
            fight(True, True)
        again = input("run again? (y/n): ")
    print("Goodbye") 
"""

def getFights(n):
    fights = []
    for i in range(n):
        if not i % 10:
            print("Progress: ", i, " / ", n)
        
        orig_stdout = sys.stdout
        f = open('log.txt', 'w')
        sys.stdout = f
        
        fights.append(battle(False))
        
        print("\n\n\n")
        sys.stdout = orig_stdout
        f.close()
        
        rounds = fights[i][0][len(fights[i][0])-1][11] #Jesus fuck why did I pick this archetecture
        print("    Rounds: ", rounds)
    X = []
    Y = []
    for fight in fights:
        for rownd in fight[0]:
            X.append(rownd)
            Y.append(fight[1])
    X = np.array(X)
    Y = np.array(Y)
    return X, Y
    
"""
fights = getFights(1000)
wins = 0
draws= 0
for i in range(len(fights)):
    if (fights[i][1] == [1,0,0]):
        wins += 1
    elif(fights[i][1] == [0,0,1]):
        draws+= 1
        
print("Win %: ", wins / len(fights))
print("Draw %: ", draws / len(fights))
"""
#horray formating 

Xt, Yt = getFights(1000)
Xv, Yv = getFights(100)
acc = 0
bestAcc = 0
didntImprove = 0
while didntImprove < 5:
    winPredictor.fit(Xt, Yt, 5)
    acc = verification(winPredictor, Xv, Yv)
    if bestAcc > acc:
        didntImprove += 1
    else:
        bestAcc = acc
        didntImprove = 0
        
#2 layers, 10, 3: 81, 81, 79
#3 layers, 10, 10, 3: 78, 84, 82

#Shapes for the RNN
"""
X.reshape(2, 1, 13) #2 = batches?, 1 = timestep??, 13= features
Y.reshape(2, 1, 4)
"""
