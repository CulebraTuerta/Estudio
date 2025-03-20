# La gracia del codigo es poder decir los numeros del 1 al 100 
# pero considerando que en vez de decir los 3 y sus multiplos, se dice Fizz
# los 5 y sus multiplos se dice Buzz
# los multiplos de ambos se dicen FizzBuzz
# -------------------------------

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...

# -----------------------------------------------

# ocupare el operador % el cual me da el residui de la division de dos numeros

for i in range(1,31,1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0 and i%5 != 0:
        print("Fizz")
    elif i%3 != 0 and i%5 == 0:
        print("Buzz")
    else:
        print(i)

