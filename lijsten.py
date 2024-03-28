import random


getallenlijst=[]
for teller in range(1000):
    getallenlijst.append(random.randint(0,1000))

print(getallenlijst)


#deze functie geeft de kleinst waarde uit een reeks getallen terug(returnvalue)
# de input is dus een lijst met getallen.



def kleinsteWaardeUitLijst(getallen):
    getallen.sort()
    #print("de lijst is : ",getallen)
    return getallen[0]

print("de kleinste waarde is: ", kleinsteWaardeUitLijst(getallenlijst)) 

