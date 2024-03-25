def trocar_valores(a, b):
    
    print(f"valores iniciais: A = {a}, B = {b}")
    a,b = b, a 
    
    print(f"valores após troca: A = {a}, B = {b}")
    
valor_a = int(input("digite o valor para A: "))

valor_b = int(input("digite o valor para B: "))

trocar_valores(valor_a, valor_b)
