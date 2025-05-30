VETERINARIOS = [
    "Neiner, Maximiliano",
    "Villegas, Octavio",
    "Cardozo, Marina",
    "Baus, Christian",
    "Luccheta, Giovanni",
    "Fernandez, David",
    "Ochoa, Gonzalo",
    "Gatto, Catriel",
    "Fernandez, Mariano",
    "Bustos Gil, Felipe"
]
SERVICIOS = [
    "Consulta General",
    "Vacunacion",
    "Control Post-quirurgico"
]
PRECIOS = [15000, 20000, 30000]

def normalizar_nombre(texto):
    
    texto = texto.strip().lower()
    resultado = ""
    mayus = True
    for c in texto:
        if mayus and c.isalpha():
            resultado += c.upper()
            mayus = False
        else:
            resultado += c
        if c == " " or c == "," or c == "-":
            mayus = True
    return resultado

def obtener_indice_veterinario(nombre):
    
    for i in range(len(VETERINARIOS)):
        if VETERINARIOS[i] == nombre:
            return i
    return -1

def obtener_indice_servicio(servicio):
    
    for i in range(len(SERVICIOS)):
        if SERVICIOS[i] == servicio:
            return i
    return -1