#8. Realizar un programa que permita ingrear una contraseña de por lo menos 7 caracteres. 
#   Luego preguntarla y verificar si es correcta o no , en caso de no serlo, seguir preguntando hasta que se ingrese la correcta.  

continuar=True
pswrd= input("Cree su contraseña de al menos 7 caracteres: ")
if len(pswrd)<7:
    print("Contraseña no cumple con estandares, se cierra programa")
else:
    while continuar:
        contra = input("Ingrese su contraseña: ")
        if contra != pswrd:
            print("Contraseña incorrecta")
        else:
            continuar=False
    print("Contraseña correcta, bienvenido")

