print("***************bienbenido a la sala de bliblioteca donde consigira todo tipo de libro*******************")
input("en que le podemos ayudar   :")
print("locentimos ese libro esta en utilidad pero le podemos ofreser 5 libros parecidos")
print("(1.)Mi isla, Elísabet Benavent")
print("(2.)Culpa mía, Mercedes Ron")
print("(3.)Rompe el círrculo, Colleen Hoover")
print("(4.)Odisea - Homero. .. ")
print("(5.)Diez negritos - Agatha Christie. ... ")
libros=int(input("cual le parece mas interesante : "))
def switch_case(libros):
    match libros :
        case 1:
            print("elegiste mi isla,elisabet benavent")
        case 2:
            print("elegiste culpa mia,mercedes room")
        case 3:
            print("elegiste rompe el circulo,collen hoover ")
        case 4:
            print("odisea-homero..")
        case 5:
            print("diez negritos-agatha christie..")
switch_case(libros)
    
