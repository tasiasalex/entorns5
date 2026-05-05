import pytest

"""
Exercici 2 (3 punts)
Escriu una funció trobar_edat_maxima(persones) que rebi una llista de diccionaris amb claus 'nom' (string) i 'edat' (int), 
i retorni l'edat més alta. Valida que la llista no sigui buida i que tots els diccionaris tinguin les claus correctes, sinó retorna -1. 
Dóna la sortida de les crides de prova.
def trobar_edat_maxima(persones):
# El teu codi aquí
"""

def trobar_edat_maxima(persones):
    """
    Rep una llista de diccionaris amb les claus 'nom' i 'edat'
    i retorna l'edat més alta.

    Retorna -1 si:
    - la llista és buida
    - algun element no és un diccionari
    - falta alguna clau obligatòria
    """
    if not persones:
        return -1

    for persona in persones:
        if (
            not isinstance(persona, dict)
            or "nom" not in persona
            or "edat" not in persona
            or not isinstance(persona["edat"], int)
        ):
            return -1

    #Obtenir totes les edats
    edats = [persona["edat"] for persona in persones]
    return max(edats)


@pytest.mark.parametrize(
    "persones, resultat_esperat",
    [
        (
            [
                {'nom': 'Anna Garcia', 'edat': 25},
                {'nom': 'Marc Puig', 'edat': 42},
                {'nom': 'Laura Martí', 'edat': 35},
                {'nom': 'Jordi Soler', 'edat': 58},
                {'nom': 'Marta Vidal', 'edat': 29},
                {'nom': 'Pere Català', 'edat': 67},
                {'nom': 'Sofia Roca', 'edat': 31}
            ],
            67
        ),
        ([], -1),
        (
            [
                {'nom': 'Anna Garcia', 'edat': 25},
                {'nom': 'Marc Puig'},
                {'nom': 'Laura Martí', 'edat': 35}
            ],
            -1
        ),
        (
            [
                {'nom': 'Anna Garcia', 'edat': 25},
                {'nom': 'Marc Puig', 'edat': '42'},
                {'nom': 'Laura Martí', 'edat': 35}
            ],
            -1
        )
    ]
)
def test_trobar_edat_maxima(persones, resultat_esperat):
    """
    Test parametritzat de trobar_edat_maxima.
    """
    assert trobar_edat_maxima(persones) == resultat_esperat


"""
Exercici 3 (2 punts)
Fes una funció trobar_producte_mes_car() que retorni el diccionari del producte amb el preu més alt de la variable global productes.
Si la llista global està buida, retorna None.
# Variable global
"""

productes = [
    {
        'nom': 'Portàtil Dell XPS 15',
        'preu': 1299.99,
        'categoria': 'Informàtica',
        'stock': 5
    },
    {
        'nom': 'Ratolí Logitech MX Master',
        'preu': 89.99,
        'categoria': 'Perifèrics',
        'stock': 15
    },
    {
        'nom': 'Monitor Samsung 27"',
        'preu': 349.50,
        'categoria': 'Monitors',
        'stock': 8
    }
]


def trobar_producte_mes_car():
    """
    Retorna el diccionari del producte amb el preu més alt
    de la variable global 'productes'.

    Retorna None si la llista està buida.
    """
    global productes

    if not productes:
        return None

    producte_mes_car = productes[0]

    for producte in productes:
        if producte["preu"] > producte_mes_car["preu"]:
            producte_mes_car = producte

    return producte_mes_car


@pytest.mark.parametrize(
    "llista_productes, resultat_esperat",
    [
        (
            [
                {
                    'nom': 'Portàtil Dell XPS 15',
                    'preu': 1299.99,
                    'categoria': 'Informàtica',
                    'stock': 5
                },
                {
                    'nom': 'Ratolí Logitech MX Master',
                    'preu': 89.99,
                    'categoria': 'Perifèrics',
                    'stock': 15
                }
            ],
            'Portàtil Dell XPS 15'
        ),
        ([], None)
    ]
)
def test_trobar_producte_mes_car(llista_productes, resultat_esperat):
    """
    Test parametritzat de trobar_producte_mes_car.
    """
    global productes
    productes = llista_productes

    resultat = trobar_producte_mes_car()

    if resultat_esperat is None:
        assert resultat is None
    else:
        assert resultat["nom"] == resultat_esperat


"""
Exercici 4 (3 punts)
Escriu una funció comptar_empleats_per_departament(empresa) que rebi una diccionari amb claus 'nom' i 'departaments' 
on departaments és una llista de diccionaris amb 'nom' i 'empleats', i retorni un diccionari amb el nom de cada departament 
i el seu número d'empleats. Fes un exemple de crida de la funció i dóna la sortida per les dades de prova empresa_de_prova.
"""

def comptar_empleats_per_departament(empresa):
    """
    Rep un diccionari empresa amb una llista de departaments
    i retorna un diccionari amb el nombre d'empleats per departament.
    """
    resultat = {}

    for departament in empresa.get("departaments", []):
        resultat[departament["nom"]] = len(departament["empleats"])

    return resultat


@pytest.mark.parametrize(
    "empresa, resultat_esperat",
    [
        (
            {
                'nom': 'TechCorp',
                'departaments': [
                    {
                        'nom': 'Informàtica',
                        'empleats': [
                            {'nom': 'Anna Garcia'},
                            {'nom': 'Marc Puig'},
                            {'nom': 'Laura Martí'}
                        ]
                    },
                    {
                        'nom': 'Recursos Humans',
                        'empleats': [
                            {'nom': 'Jordi Soler'},
                            {'nom': 'Marta Vidal'}
                        ]
                    }
                ]
            },
            {
                'Informàtica': 3,
                'Recursos Humans': 2
            }
        ),
        (
            {
                'nom': 'Empresa Buida',
                'departaments': []
            },
            {}
        )
    ]
)
def test_comptar_empleats_per_departament(empresa, resultat_esperat):
    """
    Test parametritzat de comptar_empleats_per_departament.
    """
    assert comptar_empleats_per_departament(empresa) == resultat_esperat