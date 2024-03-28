
#dit is de eindopdracht P1 - medium
#Naam programmeur: Sil de Vries
#datum 15-11-2023


#getallenraden - versie Medium (max 6 punten)

maxAantalBeurten=10
beurt=1
speler1="Sil de Vries"#input("Speler1, Wat is uw naam? )
speler2=(input("Speler2, Wat is uw naam? "))
teradengetal=int(input(speler1+"voer getal in dat moet worden geraden)"))


    



opgegevengetal=-99

while opgegevengetal!=teradengetal and beurt<=maxAantalBeurten:
    opgegevengetal=int(input(speler2+"geef een getal op: "))
    
    if opgegevengetal==teradengetal:
        print("Gefeliciteerd!")
    elif opgegevengetal>teradengetal:
        print("Het te raden getal is lager. Dit was beurt: ",beurt)
    else:
        print("Het te raden getal is hoger. Dit was beurt: ",beurt)
    beurt+=1
    if beurt>maxAantalBeurten and opgegevengetal!=teradengetal:
        print("Helaas, u heeft het maximale aantal beurten bereik")
    

