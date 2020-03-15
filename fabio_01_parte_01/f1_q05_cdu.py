#01
numero =int(input("qual o numero ? "))

#02
v1 = numero // 100 #123 
v2 = numero % 100 #23
v3 = v2 // 10  #2
v4 = v2 % 10   #
v5 = v4 // 1

#03
soma = v1 + v3 + v5
print(f'a soma dos digitos {v1} + {v3} + {v5} = {soma} ')