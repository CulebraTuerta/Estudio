print("")
print("##########   Calculadora de moneda Chilena ############")
print("")

colombianos = int(input("Cuantos pesos colombianos te quedan? "))
soles=int (input("Cuantos soles? "))
reales=int (input("Cuantos Reales? "))

colombianos=colombianos*0.22501
soles=soles*251.62
reales=reales*161.7
print("colombianos a pesos chilenos:",colombianos)
print("soles a pesos chilenos:",soles)
print("reales a pesos chilenos:",reales)


pesos_chilenos=colombianos+soles+reales

print("")
print("Te quedan:",round(pesos_chilenos),"pesos chilenos")
print("######################################################")