class Hond:
    def __init__(self, naam, age):
      self.naam = naam
      self.age = age
    def __str__(self):
        return ("Hond heet: {} en leeftijd is {}"  .format(self.naam, self.age ) )
    
    
    def blaf(self):
        print("Woef")

hond1=Hond("Joppie" ,1)
hond2=Hond("Bonnie" , 6)
hond3=Hond("Biko" , 13)

#dit is top!

hond1.blaf()
hond2.blaf()
hond3.blaf()
print(hond1)
print(hond2)
print(hond3)
"""     
def __init(age, name):
        hond1.name = "Joppie"
        hond2.name = "Bonnie"
        hond3.name = "Biko"
        hond1 = Hond("Joppie")
        hond2 = Hond("Bonnie")
        hond3 = Hond("Biko")
        hond1.age = 1
        hond2.age = 6
        hond3.age = 13
        print(hond1)
        print(hond2)
        print(hond3)

        """