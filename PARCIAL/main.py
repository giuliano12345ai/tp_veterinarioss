from datos import *
from validaciones import *

turnos = []
for i in range(len(VETERINARIOS)):
    fila = []
    for j in range(len(SERVICIOS)):
        fila.append(0)
    turnos.append(fila)

def hay_turnos_cargados():
    
    for i in range(len(turnos)):
        for j in range(len(turnos[0])):
            if turnos[i][j] > 0:
                return True
    return False

def registrar_turno():
    
    print("\n--- REGISTRAR TURNO ---")
    
    while True:
        nombre = input("Ingrese nombre del veterinario: ")
        nombre_valido = validar_veterinario(nombre)
        
        if nombre_valido is not None:
            break
        
        print(" Nombre de veterinario invalido, tenes que intentar denuevo.")
        
    while True:
        servicio = input("Ingrese tipo de servicio (Consulta General, Vacunacion, Control Post-quirurgico): ")
        servicio_valido = validar_servicio(servicio)
        
        if servicio_valido is not None:
            break
        
        print(" Tipo de servicio invalido. Intente de nuevo.")
        
    while True:
        cantidad_str = input("Ingrese cantidad de turnos a reservar (1-10): ")
        # >>> INICIO DE LA CORRECCIÓN <<<
        # Aquí es donde se cambia para usar validar_cadena, que es la que valida el input de texto
        cantidad_valida = validar_cadena(cantidad_str) 
        # >>> FIN DE LA CORRECCIÓN <<<
        
        if cantidad_valida is not None:
            break
          
        print(" Cantidad invalida. Intente de nuevo.")
        
    i = obtener_indice_veterinario(nombre_valido)
    j = obtener_indice_servicio(servicio_valido)
    turnos[i][j] = turnos[i][j] + cantidad_valida
    total = PRECIOS[j] * cantidad_valida
    
    print(f" Turno registrado con éxito. Total a pagar: ${total}")

def visualizar_datos():
    
    print("\n--- Turnos Registrados ---")
    
    indices = list(range(len(VETERINARIOS)))
    
    for i in range(len(indices)-1):
        for j in range(i+1, len(indices)):
            if VETERINARIOS[indices[i]] > VETERINARIOS[indices[j]]:
                temp = indices[i]
                indices[i] = indices[j]
                indices[j] = temp
                
    print(f"{"Veterinario":<22} {"Servicio":<22} {"Precio":<22} {"Cantidad":<22}")
    for idx in indices:
        for s in range(len(SERVICIOS)):
            if turnos[idx][s] > 0:
                print(f"{VETERINARIOS[idx]:<22}{SERVICIOS[s]:<22}${PRECIOS[s]}   {turnos[idx][s]}")
    print("")

def consultas():
    
    while True:
        print("""
--- Consultas ---
1. Cantidad total de turnos por veterinario
2. Promedio de turnos por tipo de servicio
3. Recaudación total acumulada
4. Veterinarios ordenados A-Z con total recaudado
5. Porcentaje de cada tipo de servicio sobre el total de turnos
6. Veterinario con menor cantidad de turnos
7. Porcentaje de turnos por veterinario respecto del total
8. Servicio/s más solicitado/s por cada veterinario
9. Volver al menú principal
""")
        
        opcion = input(" Selecciona una opcion: ")
        
        if opcion == "1":
            print("\nCantidad total de turnos por veterinario: ")
            
            for k in range(len(VETERINARIOS)):
                total = 0
                for j in range(len(SERVICIOS)):
                    total = total + turnos[k][j]
                print(f"- {VETERINARIOS[k]}: {total}")
                
                
        elif opcion == "2":
            print("\n Promedio de turnos por tipo de servicio:")
            for j in range(len(SERVICIOS)):
                suma = 0
                for k in range(len(VETERINARIOS)):
                    suma = suma + turnos[k][j]
                promedio = suma // len(VETERINARIOS)  
                print(f"- {SERVICIOS[j]}: {promedio}")
                
        elif opcion == "3":
            
            print("\nRecaudación total acumulada:")
            recaudacion = 0
            
            for k in range(len(VETERINARIOS)):
                for j in range(len(SERVICIOS)):
                    recaudacion = recaudacion + turnos[k][j]*PRECIOS[j]
                    
            print(f" la recaudacion total es de: ${recaudacion}")
              
        elif opcion == "4":
            
            print("\nVeterinarios ordenados A-Z con total recaudado:")
            
            indices = list(range(len(VETERINARIOS)))
            for k in range(len(indices)-1):
                for j in range(k+1, len(indices)):
                    if VETERINARIOS[indices[k]] > VETERINARIOS[indices[j]]:
                        temp = indices[k]
                        indices[k] = indices[j]
                        indices[j] = temp
                        
            for k in indices:
                total = 0
                for s in range(len(SERVICIOS)):
                    total = total + turnos[k][s]*PRECIOS[s]
                print(f"{VETERINARIOS[k]}: ${total}")
                    
        elif opcion == "5":
            print("\nPorcentaje de cada tipo de servicio respecto al total:")
            total_general = 0
            
            for k in range(len(VETERINARIOS)):
                for j in range(len(SERVICIOS)):
                    total_general = total_general + turnos[k][j]
                    
            if total_general == 0:
                print("No tenes turnos cargados.")
                
            else:
                for j in range(len(SERVICIOS)):
                    suma = 0
                    for k in range(len(VETERINARIOS)):
                        suma = suma + turnos[k][j]
                    porc = (suma * 100) // total_general
                    print(f"{SERVICIOS[j]}: {porc}%")
                                    
        elif opcion == "6":
            print("\n Veterinario con menor cantidad total de turnos:")
            menor = None
            idx_menor = -1
            for k in range(len(VETERINARIOS)):
                suma = 0
                for j in range(len(SERVICIOS)):
                    suma = suma + turnos[k][j]
                if menor is None or suma < menor:
                    menor = suma
                    idx_menor = k
            print(f"{VETERINARIOS[idx_menor]} ({menor} turnos)")
    
        elif opcion == "7":
            print("\n Porcentaje de turnos por veterinario respecto del total general:")
            total_general = 0
            for k in range(len(VETERINARIOS)):
                for j in range(len(SERVICIOS)):
                    total_general = total_general + turnos[k][j]
                        
            if total_general == 0:
                print("No tenes turnos cargados...")
            else:
                for k in range(len(VETERINARIOS)):
                    suma = 0
                    for j in range(len(SERVICIOS)):
                        suma = suma + turnos[k][j]
                    porc = (suma * 100) // total_general
                    print(f"{VETERINARIOS[k]}: {porc}%")
                    
                    
        elif opcion == "8":
            print("\n Servicio mas solicitado por veterinario: ")
            
            for k in range(len(VETERINARIOS)):
                max_turnos = 0
                
                for j in range(len(SERVICIOS)):
                    if turnos[k][j] > max_turnos:
                        max_turnos = turnos[k][j]
                        
                        
                if max_turnos == 0:
                    print(f"{VETERINARIOS[k]}: Ningun turno")
                else:
                    print(f"{VETERINARIOS[k]}: ", end="")
                    primero = True
                    for j in range(len(SERVICIOS)):
                        if turnos[k][j] == max_turnos:
                            if not primero:
                                print(", ", end="")
                            print(f"{SERVICIOS[j]} ({max_turnos})", end="")
                            primero = False
                            
                    print("")
                                    
        elif opcion == "9":
            break
        
        else:
            print("Opcion invalida.")

def menu():
    
    while True:
        print("""    
        🐾 Clínica Veterinaria 🐾
        --------------------------
        1- Registrar un turno
        2- Visualizar todos los datos
        3- Consultas
        4- Salir ...
    
    """)
        
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            registrar_turno()
            
        elif opcion == "2":
            
            if not hay_turnos_cargados():
                print("\n -tenes que cargar al menos un turno antes de visualizar datos !! ")
            else:
                visualizar_datos()
                
        elif opcion == "3":
            if not hay_turnos_cargados():
                print("\n -tenes que cargar al menos un turno antes de acceder a consultas.")
            else:
                consultas()
                
        elif opcion == "4":
            print("Nos vemos la proximaa! ")
            break
        
        else:
            print("Opcion invalida !!")


# Dejo esto aca para copiar y pegar :   \ \   no lo puedo escribir.

menu()