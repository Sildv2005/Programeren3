

def invoervangebruiker():
    tekst= input("Voer hier uw naam in:")
    return tekst
pad="C:\\logboekje strijder\\"

      

bestandsnaam=pad+"logboek.txt"
print(bestandsnaam)
f = open(bestandsnaam, "a")
f.write(invoervangebruiker()+"\n")
f.close()
f = open("c:\\logboekje strijder\\logboek.txt", "r")
print(f.read())
