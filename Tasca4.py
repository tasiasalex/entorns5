#Óscar Benítez Uroz

import sys #Importar el mòdul sys per poder llegir arguments de la línia de comandes

def mostrar_ajuda(): #Funció per mostrar la pantalla d'ajuda
    help_text = """
Ús: python ex4.py file [c] [-i -p -f] [--help]

Funcionalitats:
1. Comptar el nombre de línies d'un fitxer de text:
   python ex4.py fitxer.txt

2. Comptar línies que contenen un caràcter específic:
   python ex4.py fitxer.txt a

3. Comptar línies que NO contenen un caràcter específic (-i):
   python ex4.py fitxer.txt a -i

4. Comptar línies que comencen pel caràcter específic (-p):
   python ex4.py fitxer.txt a -p
   Amb -i compta línies que NO comencen pel caràcter:
   python ex4.py fitxer.txt a -p -i

5. Guardar la sortida en un fitxer (-f):
   python ex4.py fitxer.txt a -f
   python ex4.py fitxer.txt a -p -f

6. Mostrar ajuda:
   python ex4.py --help

Notes:
- L'argument c (caràcter) és necessari per a -i i -p.
- La combinació incorrecta d'arguments mostrarà un missatge d'error i aquesta ajuda.
"""
    print(help_text) #Mostrar el text d'ajuda per pantalla

def comptar_linies(file_name, caracter=None, invertir=False, principi=False): #Funció que compta les línies segons condicions
    comptador = 0 #Inicialitzar el comptador a 0
    try:
        with open(file_name, 'r', encoding='utf-8') as f: #Obrir el fitxer en mode lectura
            for linia in f: #Recorrer cada línia del fitxer
                linia = linia.rstrip('\n') #Eliminar el salt de línia al final
                if caracter: #Si s'ha especificat un caràcter c
                    if principi: #Si s'esta comprovant que comenci pel caràcter
                        condicio = linia.startswith(caracter) #True si la línia comença pel caràcter
                    else:
                        condicio = caracter in linia #True si el caràcter està en qualsevol lloc de la línia
                    if invertir: #Si s'ha activat l'opció -i
                        condicio = not condicio #Invertir la condició
                    if condicio: #Si es compleix la condició
                        comptador += 1 #Sumar 1 al comptador
                else:
                    comptador += 1 #Si no hi ha caràcter, comptem totes les línies
        return comptador #Retornar el total de línies comptades
    except FileNotFoundError: #Captura error si el fitxer no existeix
        print(f"Error: el fitxer '{file_name}' no existeix.") #Mostrar missatge d'error
        sys.exit(1) #Sortir del programa amb codi d'error 1
    except Exception as e: #Captura qualsevol altre error
        print(f"S'ha produït un error llegint el fitxer: {e}") #Mostrar missatge amb l'error
        sys.exit(1) #Sortir del programa amb codi d'error 1

def main(): #Funció principal del programa
    args = sys.argv[1:] #Obtenir tots els arguments passats per la línia de comandes, excepte el nom del fitxer Python

    if not args: #Si no hi ha arguments
        print("Error: no s'han especificat arguments. Utilitza '--help' per obtenir informació.") #Mostrar missatge d'error
        sys.exit(1) #Sortir del programa

    if '--help' in args: #Si hi ha l'argument --help
        mostrar_ajuda() #Cridar la funció que mostra ajuda
        sys.exit(0) #Sortir del programa

    file_name = args[0] #El primer argument és el nom del fitxer
    caracter = None #Inicialitzar el caràcter a None
    invertir = False #Inicialitzar la variable -i a False
    principi = False #Inicialitzar la variable -p a False
    fitxer_sortida = False #Inicialitzar la variable -f a False

    #Processar arguments opcionals
    for arg in args[1:]: #Recorrer la resta d'arguments
        if arg == '-i': #Si és -i
            invertir = True #Activar l'opció invertir
        elif arg == '-p': #Si és -p
            principi = True #Activar l'opció principi
        elif arg == '-f': #Si és -f
            fitxer_sortida = True #Activar l'opció fitxer de sortida
        elif len(arg) == 1: #Suposar que és el caràcter c
            if caracter is not None: #Si ja hi havia un caràcter especificat
                print("Error: només es pot especificar un caràcter c.") #Mostrar error
                mostrar_ajuda() #Mostrar ajuda
                sys.exit(1) #Sortir
            caracter = arg #Assignar el caràcter
        else: #Si és un argument desconegut
            print(f"Argument desconegut: {arg}") #Mostrar missatge
            mostrar_ajuda() #Mostrar ajuda
            sys.exit(1) #Sortir

    #Comprovacions de combinacions d'arguments
    if (invertir or principi) and not caracter: #Si s'ha posat -i o -p però no hi ha caràcter
        print("Error: l'argument '-i' o '-p' requereix especificar un caràcter c.") #Mostrar error
        mostrar_ajuda() #Mostrar ajuda
        sys.exit(1) #Sortir

    total = comptar_linies(file_name, caracter, invertir, principi) #Cridar la funció per comptar línies

    sortida_text = f"Nombre de línies comptades: {total}" #Preparar el text de sortida

    if fitxer_sortida: #Si s'ha especificat -f
        try:
            with open("sortida.txt", 'w', encoding='utf-8') as f: #Obrir fitxer de sortida en mode escriptura
                f.write(sortida_text + '\n') #Escriure el resultat
        except Exception as e: #Captura errors en escriptura
            print(f"S'ha produït un error escrivint el fitxer de sortida: {e}") #Mostrar missatge
            sys.exit(1) #Sortir
    else:
        print(sortida_text) #Si no hi ha -f, mostrem el resultat per pantalla

if __name__ == "__main__": #Punt d'entrada del programa
    try:
        main() #Cridar la funció principal
    except Exception as e: #Captura qualsevol error inesperat
        print(f"S'ha produït un error inesperat: {e}") #Mostrar missatge
        sys.exit(1) #Sortir amb error