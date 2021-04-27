
def dod (a, b): 
    c = a + b
    print(str(a) + " + " + str(b) + " = " + str(c))
    
def odej (a, b): 
    c = a - b
    print(str(a) + " - " + str(b) + " = " + str(c))
    
def mno (a, b): 
    c = a * b
    print(str(a) + " * " + str(b) + " = " + str(c))

def dziel (a, b):
         
    
             try:
                    c = a / b
                    print(str(a) + " / " + str(b) + " = " + str(c))
                    
             except ZeroDivisionError:
          
                 print("Nastąpiło dzielenie przez zero  !!!")  
             
      
          
      
def dzielcal (a, b): 

   
             try:
                    c = a // b
                    print(str(a) + " // " + str(b) + " = " + str(c))
                    
             except ZeroDivisionError:
          
                 print("Nastąpiło dzielenie przez zero!!!")  
         
 
def modulo (a, b):
    
             try:
                    c = a % b
                    print(str(a) + " %" + str(b) + " = " + str(c))
                    
             except ZeroDivisionError:
          
                 print("Nastąpiło dzielenie przez zero!!!")
                       
                       
    
def potega (a, b):
    c = a ** b
    print(str(a) + " ^ " + str(b) + " = " + str(c))


odp = -1

while True: 
    print()
    print()
    print(" *** LICZYDŁO ***") 
    print()
    print("1. dodawanie")
    print("2. odejmownaie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("5. dzielenie całkowite")
    print("6. reszta z dzielenia")
    print("7. potęgowanie")
    print("8. koniec")
    print()
    print("----------------------")
    odp=int(input("Podaj nr działania: "))
    
    if odp == 8: break
  
    print()
    print("Wprowadź dane :")
    print()
    
    while 1:
            try:
                a=float(input("Podaj pierwszą liczbę : "))
                b=float(input("Podaj drugą liczbę : "))
                print()
                break
            except ValueError:
                print()
                print("podaj liczbę!!!")
   
    

    if odp == 1:
        dod(a,b)
        
    if odp == 2:
        odej(a,b)
        
    if odp == 3:
        mno(a,b)
        
    if odp == 4:
        dziel(a,b)
        
    if odp == 5:
        dzielcal(a,b)
        
    if odp == 6:
        modulo(a,b)
        
    if odp == 7:
        potega(a,b)
       

print("Koniec..........")
   
      
    
