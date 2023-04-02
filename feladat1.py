import math 

f = open("eredmeny.txt", "w")
class Háromszög:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c
    def kerulete(self):
        return (self.a+self.b+self.c)
    def terulete(self):
        s=(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    def szerkezhetoseg(self):
        if a+b > c and b+c > a:
            return "Szerkezhető" 
        else:
            return "Nem szerkezhető"    
    def korsugar(self):    
        s=(a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))/((a+b+c)/2)
    
a = int(input("Adja a oldalt: "))
b = int(input("Adja b oldalt: "))
c = int(input("Adja c oldalt: "))
hlista = []
hszog = Háromszög(a,b,c)
hlista.append(hszog)  


print("Háromszög kerulete: ",hszog.kerulete())
print("Háromszög terulete: ",round(hszog.terulete(),2))
print(hszog.szerkezhetoseg())
print("Háromszögbe írható kör sugara: ",round(hszog.korsugar(),2))
 
f.write("Háromszög kerulete: ",hszog.kerulete(),"\n","Háromszög terulete: ",round(hszog.terulete(),2),"\n",hszog.szerkezhetoseg(),"Háromszögbe írható kör sugara: ","\n",round(hszog.korsugar(),2))
f.close()