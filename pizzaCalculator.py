#Naam: Mike Minheere
#Opdracht: Pizza calculator

#dit zijn de variabelen voor de maten van de pizza's
from logging import exception


klein = 4.99
medium = 6.99
groot = 10.99
loop = True

#dit zijn de variabelen voor de hoeveelheid van een specefieke maat van pizza.
aantalPizzaKlein = 0
aantalPizzaMedium = 0
aantalPizzaGroot = 0

#deze loop zorgt ervoor dat je meerdere keren kan bestellen.
while loop == True:
    print('welke maat pizza wilt u?')
    inputt = input('klein(€4.99), medium(€6.99) of groot(€10.99) ')

#hier kijkt de computer eigenlijk naar wat de inputs zijn, en hij voert acties uit op basis van de inputs, hier voert de computer bijv.
#de code uit die vraagt hoeveel pizza's je wilt.
    if (inputt == "klein" or inputt == "Klein"):
        print('Oke, u heeft voor de kleine pizza gekozen')
        aantalPizzaKlein = input("hoeveel pizza's wilt u? ")
        a = True
        while a == True:
            try:
                aantalPizzaKlein = int(aantalPizzaKlein)
                if aantalPizzaKlein <= 0:
                    raise exception
            except:
                print("sorry, de input moet een heel cijfer zijn")
                aantalPizzaKlein = input("hoeveel pizza's wilt u? ")
            else:a = False

    elif(inputt == 'medium' or inputt == 'Medium'):
        print('Oke, u heeft voor de medium pizza gekozen ')
        aantalPizzaMedium = input("hoeveel pizza's wilt u? ")
        a = True
        while a == True:
            try:
                aantalPizzaMedium = int(aantalPizzaMedium)
                if aantalPizzaMedium <= 0:
                    raise exception
            except:
                print("sorry, de input moet een heel cijfer zijn")
                aantalPizzaMedium = input("hoeveel pizza's wilt u? ")
            else:a = False

    elif(inputt == 'groot' or inputt == 'Groot'):
        print('Oke, u heeft voor de groote pizza gekozen ')
        aantalPizzaGroot = input("hoeveel pizza's wilt u? ")
        a = True
        while a == True:
            try:
                aantalPizzaGroot = int(aantalPizzaGroot)
                if aantalPizzaGroot <= 0:
                    raise exception
            except:
                print("sorry, de input moet een heel en positief cijfer zijn.")
                aantalPizzaGroot = input("hoeveel pizza's wilt u? ")
            else:a = False
    else :print('type alstublieft iets ander')

    #hier is het stukje die je vraagt of je nog meer wilt bestellen.
    print("wilt u nog meer bestellen?")
    BestelInput = input('type "ja" om nog een keer te bestelen, type "nee" als u wilt afronden ')
    if (BestelInput == "nee"):
        loop = False
    else :loop == True

#dit hele stuk is het "bonnetje" van je bestelling, hier rekent die alle prijzen uit.
print("<-------------------------------------------------->")
if(inputt == "klein" or inputt == "Klein" or inputt == 'groot' or inputt == 'Groot' or inputt == 'medium' or inputt == 'Medium'):
    print('uw bestelling:')
    if aantalPizzaKlein == 1:
        print(str(aantalPizzaKlein) + " kleine pizza € 4.99")
    elif aantalPizzaKlein > 1:
        print(str(aantalPizzaKlein) + " kleine pizza's €" + str(float(aantalPizzaKlein) * klein))
    if aantalPizzaMedium == 1:
        print(str(aantalPizzaMedium) + " medium pizza €6.99")
    elif aantalPizzaMedium >1:
        print(str(aantalPizzaMedium) + " medium pizza's €" + str(float(aantalPizzaMedium) * medium))
    if aantalPizzaGroot == 1:
        print(str(aantalPizzaGroot) + " grote pizza €10.99")
    elif aantalPizzaGroot >1:
        print(str(aantalPizzaGroot) + " grote pizza's €" + str(float(aantalPizzaGroot) * groot))
    
    print()
    print("totale kosten:")
    print('€' + str(float(aantalPizzaGroot) * groot + float(aantalPizzaMedium) * medium + float(aantalPizzaKlein) * klein))
print("<-------------------------------------------------->")