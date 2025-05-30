from datos import VETERINARIOS, SERVICIOS, normalizar_nombre

def validar_cantidad(cantidad):
    if cantidad < 0 or cantidad > 10:
        print("Ingresa un numero valido")
        
    else:    
      return cantidad    

def validar_veterinario(nombre):
    
    nombre_norm = normalizar_nombre(nombre)
    for i in range(len(VETERINARIOS)):
        if VETERINARIOS[i] == nombre_norm:
            return nombre_norm
    return None

def validar_servicio(servicio):

    servicio_norm = normalizar_nombre(servicio)
    for i in range(len(SERVICIOS)):
        if SERVICIOS[i] == servicio_norm:
            return servicio_norm
    return None

def validar_cadena(cadena):
    
   
    if len(cadena) == 0:
        return None
    
    i = 0
    while i < len(cadena):
        c = cadena[i]
        if c < '0' or c > '9':
            return None
        i += 1

    valor = 0
    i = 0
    while i < len(cadena):
        valor = valor * 10 + (ord(cadena[i]) - ord('0'))
        i += 1

    if valor >= 1 and valor <= 10:
        return valor
    else:
        return None