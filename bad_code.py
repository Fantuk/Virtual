summa = 100000
stavka = 20
srok = 4

def credit(summa, stavka, srok):
    month = 1
    try:
        summa = float (summa)
        stavka = float (stavka)
        # srok = float (srok)
        
    except:
        return ('Введены некорректные данные')
        quit()
    if srok == str(srok):
        return ('Введены некорректные данные')
        quit()
    if summa <= 0 or stavka <= 0 or srok <= 0:
        return ('Введите положительное число')
        quit()
    if srok%1 !=0:
        return ('Срок должен быть целым числом')
        exit()

    
    stroka = [] 
    table = []

    dolg = summa / srok
    for i in range (srok):
        procenty = summa * stavka / 100 / 12
        summa_plateja = procenty + dolg
        ostatok = summa - dolg

        procenty=round(procenty, 2)
        summa_plateja = round(summa_plateja, 2)
        dolg = round(dolg, 2)
        ostatok = round(ostatok, 2)

        stroka.append(str(month))
        stroka.append(str(summa))
        stroka.append(str(procenty))
        stroka.append(str(summa_plateja))
        stroka.append(str(dolg))
        stroka.append(str(ostatok))

        summa = ostatok
        month +=1
        stroka1 = ' '.join(stroka)
        # print(stroka1)
        table.append(stroka1)
        stroka = []

    return(table)

def present():
    print(credit(summa, stavka, srok))
    return 0

print(present())