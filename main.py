from notaciones import *

cad = "\tEscoge de que notación quieres partir:\n"
cad += "1.- Infija - Infix\n"
cad += "2.- Postfija - Postfix - Polaca Inversa\n"

cad2 = "Ingresa la notación que convertiremos:\n> "

strFromTo = lambda num, origin, to: str(num) + ".- Transformar de " + origin + " a " + to

resp = True
while True:
    print(cad)
    typeNotation = int(input("> "))
    resp = True
    if typeNotation == 1:
        notationIn = input("\n" + cad2)
        infija = notationConversion(notationIn)
        while resp:
            print("\n\t¿Que quieres hacer?")
            print(strFromTo(1, "Infija", "Postfija"))
            print(strFromTo(2, "Infija", "Prefija"))
            opc = int(input("> "))
            if opc == 1:
                print("\n\tNotacion Postfija: " + " ".join(infija.infixToPostfix()))
            elif opc == 2:
                print("\n\tNotacion Prefija: " + " ".join(infija.infixToPrefix()))
            else:
                print("¡Esa opcion no existe, verifica bien!")
            a = int(input("\n¿Quieres realizar otra operación desde Infijo?\n1.- Si\nOtro numero.- No\n> "))
            resp = True if a == 1 else False

    elif typeNotation == 2:
        notationIn = input("\n" + cad2)
        postfija = notationConversion(notationIn)
        while resp:
            print("\n\t¿Que quieres hacer?")
            print(strFromTo(1, "Postfija", "Infija"))
            print(strFromTo(2, "Postfija", "Prefija"))
            opc = int(input("> "))
            if opc == 1:
                print("\n\tNotacion Infija: " + " ".join(postfija.postfixToInfix()))
            elif opc == 2:
                print("\n\tNotacion Prefija: " + " ".join(postfija.postfixToPrefix()))
            else:
                print("¡Esa opcion no existe, verifica bien!")
            a = int(input("\n¿Quieres realizar otra operación desde Infijo?\n1.- Si\nOtro numero.- No\n> "))
            resp = True if a == 1 else False
    else:
        print("\n\t¡No existe esa opción!")
        continue
