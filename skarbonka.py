
def wpłata():   
    kwota=float(input("podaj kwotę transakcji: "))
    skarbonka.append(kwota)
    
    
def wypłata():   
    kwota=float(input("podaj kwotę transakcji: "))
    skarbonka.append(-kwota)
    
    

def raport():
    for i in range(len(skarbonka)):
        print("transakcja nr: " + str(i+1) + "  " + str(skarbonka[i]))
       


def saldo():
    s=sum(skarbonka)
    print("---------------------------")
    print("saldo wynosi: " + str(s) + " zł")
    print("---------------------------")



def uznania():
    uz=[kwota for kwota in skarbonka if kwota >0]
    s=sum(uz)
    print("---------------------------")
    print("Suma wpłat: " + str(s) + " zł")
    print("---------------------------")
    
    
def wydatki():
    uz=[kwota for kwota in skarbonka if kwota < 0]
    s=sum(uz)
    print("---------------------------")
    print("Suma wypłat: " + str(s*-1) + " zł")
    print("---------------------------")






skarbonka=[]


odp = -1

while True: 
    print()
    print()
    print("        SKARBONKA          ") 
    print("---------------------------")
    print("1. Dodaj wpłatę")
    print("2. Dodaj wypłatę")
    print("3. Saldo")
    print("4. Suma wpłat")
    print("5. Suma wypłat")
    print("6. Lista wszystkich transkacji")
    print("7. Koniec")
    print("-----------------------------")
    odp=int(input("Podaj nr działania: "))
    print()
    
    
    
    if odp==1:
      
        while 1:
                try:
                    wpłata()
                    print()
                    break
                except ValueError:
                    print()
                    print("podaj liczbę!!!")
       
    if odp==2:
        
         while 1:
                try:
                    wypłata()
                    print()
                    break
                except ValueError:
                    print()
                    print("podaj liczbę!!!")
         
                              
    if odp==3:
            print()
            saldo() 
                     
    if odp==4:
            print()
            uznania()                  
            
    if odp==5:
            
            wydatki()     
            
    if odp==6:
            print("-------------------")
            raport()
            print("-------------------")
          
                   
            
    if odp == 7: break


print("Koniec..........")
   
      