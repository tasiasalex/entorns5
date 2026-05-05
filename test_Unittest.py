# fitxer: tests_tasques.py

"""
Fitxer de tests per a les dues tasques escrites dins tasques.py.
Conté dues classes de test amb mètodes documentats i comentaris de línia.
"""

import unittest
from tasques import (
    videojocs, biblioteca_personal,
    mostrar_videojoc, buscar_per_titol, afegir_a_biblioteca, joc_mes_car,
    crear_sequencia, numeros_imparells_majors, primera_posicio, diagonal_principal
)

class TestTasca1(unittest.TestCase):
    """Tests per a la Tasca Escrita 1: gestió de videojocs."""

    def test_mostrar_videojoc(self):
        """
        Comprova que mostrar_videojoc no llença errors.
        Només imprimeix el contingut del joc; retorn esperat: None.
        """
        for joc in videojocs:
            #Cada joc hauria de ser mostrat sense errors
            self.assertIsNone(mostrar_videojoc(joc))

    def test_buscar_per_titol(self):
        """
        Comprova que buscar_per_titol troba correctament els jocs pel títol.
        També prova insensibilitat a majúscules i joc inexistent.
        """
        #Cerca amb majúscules exactes
        joc = buscar_per_titol("Cyberpunk 2077", videojocs)
        self.assertIsNotNone(joc)
        self.assertEqual(joc["titol"], "Cyberpunk 2077")

        #Cerca insensible a majúscules
        joc2 = buscar_per_titol("cyberpunk 2077", videojocs)
        self.assertIsNotNone(joc2)
        self.assertEqual(joc2["titol"], "Cyberpunk 2077")

        #Cerca d’un joc que no existeix
        self.assertIsNone(buscar_per_titol("Joc Inexistent", videojocs))

    def test_afegir_a_biblioteca(self):
        """
        Comprova l’afegir_a_biblioteca amb diferents casos:
        - Afegir un joc vàlid
        - Afegir el mateix joc de nou
        - Afegir un joc inexistent
        """
        biblioteca_test = []

        #Afegir un joc vàlid
        resultat = afegir_a_biblioteca("FIFA 24", videojocs, biblioteca_test)
        self.assertEqual(resultat, "Joc afegit!")

        #Intentar afegir el mateix joc de nou
        resultat2 = afegir_a_biblioteca("FIFA 24", videojocs, biblioteca_test)
        self.assertEqual(resultat2, "Ja està a la biblioteca")

        #Intentar afegir un joc inexistent
        resultat3 = afegir_a_biblioteca("Joc Inexistent", videojocs, biblioteca_test)
        self.assertEqual(resultat3, "Joc no trobat")

    def test_joc_mes_car(self):
        """
        Comprova que joc_mes_car retorna correctament el joc amb el preu més alt.
        """
        joc_car = joc_mes_car(videojocs)
        #Troba el preu màxim a la llista de videojocs
        preu_max = max(joc["preu"] for joc in videojocs)
        self.assertEqual(joc_car["preu"], preu_max)


class TestTasca2(unittest.TestCase):
    """Tests per a la Tasca Escrita 2: manipulació de llistes i matrius."""

    def test_crear_sequencia(self):
        """
        Comprova crear_sequencia amb casos vàlids i invàlids:
        - Inici < final i positius: retorna llista completa
        - Inici > final: retorna llista buida
        - Inici negatiu: retorna llista buida
        """
        self.assertEqual(crear_sequencia(5, 10), [5, 6, 7, 8, 9, 10])
        self.assertEqual(crear_sequencia(10, 5), [])
        self.assertEqual(crear_sequencia(-2, 5), [])

    def test_numeros_imparells_majors(self):
        """
        Comprova numeros_imparells_majors:
        - Retorna només els nombres senars majors que el límit
        - Cas amb llista buida: retorna llista buida
        """
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        self.assertEqual(numeros_imparells_majors(llista, 3), [7, 9, 7])
        self.assertEqual(numeros_imparells_majors([], 3), [])

    def test_primera_posicio(self):
        """
        Comprova primera_posicio:
        - Retorna la primera aparició de l'element
        - Retorna -1 si l'element no existeix o la llista és buida
        """
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        self.assertEqual(primera_posicio(llista, 7), 2)
        self.assertEqual(primera_posicio(llista, 15), -1)
        self.assertEqual(primera_posicio([], 5), -1)

    def test_diagonal_principal(self):
        """
        Comprova diagonal_principal:
        - Retorna la diagonal principal d'una matriu quadrada
        - Retorna llista buida si la matriu no és quadrada o no vàlida
        """
        matriu_valida = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matriu_invalida = [[1, 2], [3, 4, 5]]
        self.assertEqual(diagonal_principal(matriu_valida), [1, 5, 9])
        self.assertEqual(diagonal_principal(matriu_invalida), [])


if __name__ == "__main__":
    #Executa totes les proves quan s’executa aquest fitxer
    unittest.main()