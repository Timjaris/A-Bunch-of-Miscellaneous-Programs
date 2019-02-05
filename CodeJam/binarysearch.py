import time

def main():
    T = int(input())
    die = False
    for i in range(T):
        pair = input()
        A, B = pair.split(' ')
        A = int(A)
        B = int(B)
        n = int(input()) #Is this just useless?
        correct = False
        attempts = 0
        guess = (A+B) // 2
        while not correct:# and attempts <= n:
            if guess == A: guess += 1
            print(guess, flush=True)
            response = input()
            if response == "CORRECT":
                correct = True
            elif response == "TOO_BIG":
                B = guess
                guess = (A+B) // 2
            elif response == "TOO_SMALL":
                A = guess
                guess = (A+B) // 2
            elif response == "WRONG_ANSWER":
                die = True
                break
                correct = True #not really, but...
            attempts += 1
        if die: break
    
if __name__ == '__main__':
    file = open(str(time.time())+".txt", "w+")
    file.close()
    main()