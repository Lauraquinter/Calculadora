import modulop
import conectbd

def calcular(resultadofinal=True):
    
    contador = 0

    while True:

        opcion = str(input("seleccione la operación que desea realizar: \n"
                            "1. multiplicacion \n"
                            "2. division \n"
                            "3. resta \n"
                            "4. suma \n"
                            "5. potenciación \n"
                            "6. operación mas repetitiva \n"
                            "7. Historial \n"
                            "8. salir \n"))
        
        num3 = int(input("ingrese el primer numero: "))
        num4 = int(input("ingrese el segundo numero: "))

        if opcion == "1":
            resultadofinal = modulop.multiplicacion(num3, num4)
            #num_par = modulop.par(resultadofinal)
        elif opcion == "2":
            resultadofinal = modulop.division(num3, num4)
            #num_par = modulop.par(resultadofinal)
        elif opcion == "3":
            resultadofinal = modulop.resta(num3, num4)
            #num_par = modulop.par(resultadofinal)
        elif opcion == "4":
            resultadofinal = modulop.suma(num3, num4)
            #num_par = modulop.par(resultadofinal)
        elif opcion == "5":
            resultadofinal = modulop.potenciacion(num3, num4)
            #num_par = modulop.par(resultadofinal)
        elif opcion == "6":
            contador += 1
            print(f"Numero de veces que has entrado {contador}")
        elif opcion == "7":
            resultados = conectbd.consulta()
            # Haz algo con los resultados si es necesario
            print(resultados)
        elif opcion == "8":
            print("fin del programa")
            break
        else:
            print("Opcion incorrecta")

        conectbd.agregar(opcion, num3, num4, resultadofinal)

    return resultadofinal