# TASCA ESCRITA 1:

videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {
            "nom": "Nintendo",
            "pais": "Japó"
        },
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {
            "nom": "CD Projekt Red",
            "pais": "Polònia"
        },
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {
            "nom": "EA Sports",
            "pais": "Estats Units"
        },
        "dlcs": [],
        "preu": 69.99
    }
]

biblioteca_personal = []

def mostrar_videojoc(joc):
    titol = joc["titol"].upper()
    any_llancament = joc["any_llancament"]
    puntuacio = int(joc["puntuacio"])
    preu = joc["preu"]
    print(f"🎮 {titol} ({any_llancament}) - {'⭐' * puntuacio} - {preu}€")
    # No cal retornar res explícitament (retornarà None), que és el que espera el test.

def buscar_per_titol(titol, videojocs):
    for joc in videojocs:
        if joc["titol"].lower() == titol.lower():
            return joc
    return None

def afegir_a_biblioteca(titol, videojocs, biblioteca):
    joc = buscar_per_titol(titol, videojocs)
    
    if joc is None:
        return "Joc no trobat" # Eliminades les icones (❌) perquè el test espera text net
    
    if joc in biblioteca:
        return "Ja està a la biblioteca" # Eliminades les icones (⚠️)
    
    biblioteca.append(joc)
    return "Joc afegit!" # Eliminades les icones (✅)

def joc_mes_car(videojocs):
    if not videojocs:
        return None
    
    joc_car = videojocs[0]
    for joc in videojocs:
        if joc["preu"] > joc_car["preu"]:
            joc_car = joc
    return joc_car

# TASCA ESCRITA 2:

def crear_sequencia(inici, final):
    if isinstance(inici, int) and isinstance(final, int) and inici <= final and inici >= 0:
        return [i for i in range(inici, final + 1)]
    return []

def numeros_imparells_majors(llista, limit):
    if isinstance(llista, list) and llista and isinstance(limit, int):
        return [i for i in llista if i % 2 != 0 and i > limit]
    return []

def primera_posicio(llista, element):
    for i in range(len(llista)):
        if llista[i] == element:
            return i # Retornem immediatament quan el trobem per agafar la PRIMERA posició
    return -1

def diagonal_principal(matriu):
    if not isinstance(matriu, list) or not matriu:
        return []
    
    mida = len(matriu)
    for fila in matriu:
        if not isinstance(fila, list) or len(fila) != mida:
            return []
            
    return [matriu[i][i] for i in range(mida)]

# Funcions Main per a execució manual
def main():
    # Pots mantenir els teus main() aquí per provar manualment
    pass

if __name__ == "__main__":
    main()
