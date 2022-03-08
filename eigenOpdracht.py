
b = True
while b == True:
    a = input('vul iets in: ')
    try:
        a = int(a)
    except:
        print('dat werkt niet dombo, probeer opnieuw!')
    else:b = False
print('gefeliciteerd! je hebt nu een sticker.')