#TASCA ESCRITA 1:

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
"""
Exercici 1: Funció de visualització (1,5 punts)
Escriu una funció que rep un diccionari joc i mostra:
Títol en majúscules
Any entre parèntesis
Puntuació amb estrelles
Preu amb €
Exemple: 🎮 THE LEGEND OF ZELDA (2017) - ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ - 59.99€
"""
def mostrar_videojoc(joc):
    #Escriu aquí el teu codi (3-4 línies)
   
#Exemple: 🎮THE LEGEND OF ZELDA (2017) - ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ - 59.99€
    
    titol = joc["titol"].upper()
    any_llancament = joc["any_llancament"]
    puntuacio = int(joc["puntuacio"])
    preu = joc["preu"]
    
    print(f"🎮 {titol} ({any_llancament}) - {'⭐' * int(puntuacio)} - {preu}€")

#Exercici 2: Funció de cerca (2,5 punts)
#Escriu una funció que busqui un videojoc pel títol (insensible a majúscules) i el retorni (el diccionari). #Si no el troba, retorna None.
def buscar_per_titol(titol, videojocs):
    # Escriu aquí el teu codi (4-5 línies)
    
    for joc in videojocs:
        if joc["titol"].upper() == titol.upper():
            return joc
        
    return None
    
#Exercici 3: Gestió de biblioteca (3 punts)
#Escriu una funció afegir_a_biblioteca(titol, videojocs, biblioteca) que:
#Busqui el joc utilitzant buscar_per_títol()
#Si el joc no existeix, retorni "❌ Joc no trobat"
#Si el joc ja està a la biblioteca, retorni "⚠️ Ja està a la biblioteca" 
#Si tot va bé, l'afegeixi i retorni "✅ Joc afegit!"


def afegir_a_biblioteca(titol, videojocs, biblioteca):
    #Escriu aquí el teu codi (8-10 línies)
    
    joc = buscar_per_titol(titol, videojocs)
    
    if joc is None:
        return "❌ Joc no trobat"
    
    if joc in biblioteca:
        return "⚠️ Ja està a la biblioteca"
    
    biblioteca.append(joc)
    return "✅ Joc afegit!"
    

#Exercici 4: Estadístiques (1,5 punts)
#Escriu una funció joc_mes_car() que retorni el videojoc (diccionari) amb el preu més alt de la llista videojocs.
def joc_mes_car(videojocs):
    #Escriu aquí el teu codi (5-6 línies) 
    
    preu_max = videojocs[0]["preu"]
    joc_mes_car = None
    
    for joc in videojocs:
        if joc["preu"] > preu_max:
            preu_max = joc["preu"]
            joc_mes_car = joc
            
    return joc_mes_car


#Exercici 5: Funció Main (1,5 punts)
#Omple els buits amb les crides correctes a les funcions anteriors, recorda que tens accés a les variables videojocs i biblioteca_personal
def main():
    print("=== GESTIÓ DE VIDEOJOCS ===\n")
   
    # 1. Mostrar tots els videojocs
    print("1. CATÀLEG DE VIDEOJOCS:")
    for joc in videojocs:
        mostrar_videojoc(joc) # BUIT 1: Crida per mostrar cada videojoc
    
    print("\n" + "="*50)
    
    print("\n2. CERCA DE VIDEOJOC:")
    # BUIT 2: Buscar "cyberpunk 2077" (insensible a majúscules)
    joc_trobat = buscar_per_titol("cyberpunk 2077", videojocs)
    if not joc_trobat:
        print("Joc trobat:")
        mostrar_videojoc(joc_trobat) # BUIT 3: Mostrar el joc trobat
    else:
        print("Joc no trobat")
    
    print("\n" + "="*50)
    
    print("\n3. GESTIÓ DE BIBLIOTECA PERSONAL:")
    
    # BUIT 4: Afegir "FIFA 24" a la biblioteca
    resultat1 = afegir_a_biblioteca("FIFA 24", videojocs, biblioteca_personal)
    print(resultat1)

    print("\n" + "="*50)
    
    # 4. Mostrar estadístiques
    print("\n4. ESTADÍSTIQUES:")
    # BUIT 5: Trobar el joc més car
    joc_car = joc_mes_car(videojocs)
    print("El joc més car és:")
    # BUIT 6: Mostrar el joc més car
    mostrar_videojoc(joc_car)
    
    print("\n" + "="*50)
    
    # 5. Mostrar biblioteca personal
    print("\n5. LA MEVA BIBLIOTECA:")
    if biblioteca_personal:
        for joc in biblioteca_personal:
            # BUIT 7: Mostrar cada joc de la biblioteca
            mostrar_videojoc(joc)
    else:
        print("La biblioteca està buida")


if __name__ == "__main__":
    # BUIT 8: Crida a la funció principal
    main()           
    

#TASCA ESCRITA 2:

"""
Exercici 1 (2 punts)
Escriu una funció crear_sequencia(inici, final) que generi una llista amb tots els números des de inici fins a final (ambdós inclosos). Valida que inici i final siguin dos enters positius i inici sigui més petit que final, sinó és així retorna una llista buida.
"""
def crear_sequencia(inici, final):
    l = []
    if isinstance(inici, int) and isinstance(final, int) and inici < final and inici >= 0:
        l = [i for i in range(inici, final + 1)]
    return l

"""
Exercici 2 (2 punts)
Crea una funció numeros_senars_majors(llista, limit) que retorni una nova llista amb només els números senars que siguin majors que limit. Valida que llista sigui una llista no buida i que limit sigui un número enter, sinó retorna una llista buida.
"""
def numeros_imparells_majors(llista, limit):
    l = []
    if isinstance(llista, list) and isinstance(limit, int) and llista:
        l = [i for i in llista if i % 2 != 0 and i > limit]
    return l
"""

Exercici 3 (2 punts)
Fes una funció primera_posicio(llista, element) que trobi la posició de la primera aparició d'un element a la llista. Si no existeix, ha de retornar -1. No pots utilitzar el mètode .index()
"""
def primera_posicio(llista, element):
    posicio = -1
    for i in range(len(llista)):
        if llista[i] == element:
            posicio = i
    return posicio

"""
Exercici 4 (2 punts)
Escriu una funció diagonal_principal(matriu) que retorni una llista amb els elements de la diagonal principal d'una matriu quadrada . Valida que matriu sigui una llista de llistes no buida, que totes les files tinguin la mateixa longitud i que sigui quadrada (mateix número de files i columnes), sinó retorna una llista buida.
"""
def diagonal_principal(matriu):
    l = []
    # penseu una solució més senzilla
    if isinstance(matriu, list) and all(isinstance(fila, list) and len(fila) == len(matriu[0]) for fila in matriu) and len(matriu) == len(matriu[0]):
        l = [matriu[i][i] for i in range(len(matriu))]
    return l


"""
Crida de les funcions (1 punt)
"""
def main():
    #Dades de prova
    llista_prova = [3, -1, 7, 2, -1, 9, 4, 7]
    matriu_prova = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    llista_buida = []
    matriu_no_quadrada = [[1, 2], [3, 4, 5]]

    print("=== PROVES DE LES FUNCIONS ===")

    #Prova 1: crear_sequencia
    print("\n1. Funció crear_sequencia:")
    resultat1a = crear_sequencia(5, 10)  # Cas vàlid
    resultat1b = crear_sequencia(10, 5)  # Cas invàlid
    resultat1c = crear_sequencia(-2, 5)  # Cas invàlid (negatiu)
    print(f"crear_sequencia(5, 10) = {resultat1a}")
    print(f"crear_sequencia(10, 5) = {resultat1b}")
    print(f"crear_sequencia(-2, 5) = {resultat1c}")

    #Prova 2: numeros_imparells_majors  
    print("\n2. Funció numeros_imparells_majors:")
    resultat2a = numeros_imparells_majors(llista_prova, 3)  # Cas vàlid
    resultat2b = numeros_imparells_majors(llista_buida, 3)  # Cas invàlid
    print(f"numeros_imparells_majors({llista_prova}, 3) = {resultat2a}")
    print(f"numeros_imparells_majors([], 3) = {resultat2b}")

    #Prova 3: primera_posicio
    print("\n3. Funció primera_posicio:")
    resultat3a = primera_posicio(llista_prova, 7)   # Cas vàlid
    resultat3b = primera_posicio(llista_prova, 15)  # Cas vàlid
    resultat3c = primera_posicio(llista_buida, 5)   # Cas invàlid
    print(f"primera_posicio({llista_prova}, 7) = {resultat3a}")
    print(f"primera_posicio({llista_prova}, 15) = {resultat3b}")
    print(f"primera_posicio([], 5) = {resultat3c}")

    # Prova 4: diagonal_principal
    print("\n4. Funció diagonal_principal:")
    resultat4a = diagonal_principal(matriu_prova)  # Cas vàlid
    resultat4b = diagonal_principal(matriu_no_quadrada)  # Cas invàlid
    print(f"diagonal_principal({matriu_prova}) = {resultat4a}")
    print(f"diagonal_principal({matriu_no_quadrada}) = {resultat4b}")


if __name__ == "__main__":
    main()

"""
Sortida Esperada per consola (1 punt):
Completa la sortida per consola segons el codi de la funció main()
=== PROVES DE LES FUNCIONS ===

1. Funció crear_sequencia:
crear_sequencia(5, 10) = [5, 6, 7, 8, 9, 10]
crear_sequencia(10, 5) = []
crear_sequencia(-2, 5) = []

2. Funció numeros_imparells_majors:
numeros_imparells_majors([3, -1, 7, 2, -1, 9, 4, 7], 3) = [7, 9, 7]
numeros_imparells_majors([], 3) = []

3. Funció primera_posicio:
primera_posicio([3, -1, 7, 2, -1, 9, 4, 7], 7) = 7
primera_posicio([3, -1, 7, 2, -1, 9, 4, 7], 15) = -1
primera_posicio([], 5) = -1

4. Funció diagonal_principal:
diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = [1, 5, 9]
diagonal_principal([[1, 2], [3, 4, 5]]) = []
"""