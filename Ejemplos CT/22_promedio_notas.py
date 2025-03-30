#7. Hacer un programa que permita ingresar el nombre de un estudiante y 3 notas con valor de 0 a 5. 
#   Calcular promedio y si es mayor o igual a 3 mostrar "Aprobado", de lo contrario "Reprobado"

nombre =input("Ingrese nombre de estudiante: ")
nota1 = int(input("Ingrese Nota 1: "))
nota2 = int(input("Ingrese Nota 2: "))
nota3 = int(input("Ingrese Nota 3: "))

promedio = (nota1+nota2+nota3)/3
if promedio >=3:
    print(f"Aprobado con promedio {promedio}")
else: 
    print(f"Reprobado con nota {promedio}")
