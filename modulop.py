# archivo del modulo

#def par(resultado):
#    if resultado % 2 == 0:
#        print(f"el {resultado} es par")
#    else:
#        print(f"el {resultado} es impar")
#    return resultado

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

def division(num1, num2):
    try:
        resultado = num1  // num2
    except Exception as e:
        print(f"error de sistema! {e}")
    return resultado

def potenciacion(num1, num2):
    resultado = num1 ** num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado


        



