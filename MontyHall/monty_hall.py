from enum import Enum
import numpy as np

class Strategie(Enum):
    CHANGER = 1
    GARDER = 2

np.random.seed()

def play(strategie, nb_tours):
    '''Simule une suite de tours du jeu.

    Cette fonction renvoie les résultats de plusieurs parties
    du jeu Monty Hall sous forme d'une liste de gains par le
    joueur.

    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours

    Returns:
        list: Liste des gains du joueurs à chaque partie
    '''
	# chaque ligne represente les portes pour une partie
    portes = np.tile([0, 1, 2], [nb_tours, 1])

    bonnes_portes = np.random.randint(0, 3, size=nb_tours)

    premiers_choix = np.random.randint(0, 3, size=nb_tours)

    # <=> portes.remove(premier_choix)
    portes = portes[portes != premiers_choix[:, np.newaxis]].reshape(nb_tours, 2)

	# <=> portes[randint(0, 1)]
    choix_aleatoires = np.apply_along_axis(np.random.choice, 1, portes[bonnes_portes == premiers_choix])
    # <=> if premier_choix == bonne_porte:
    portes[bonnes_portes == premiers_choix] = choix_aleatoires[:,np.newaxis]

    # <=> else:
    portes[bonnes_portes != premiers_choix] = bonnes_portes[bonnes_portes != premiers_choix][:,np.newaxis]

    deuxiemes_choix = np.zeros(nb_tours, dtype=int)

    if strategie == Strategie.CHANGER:
        deuxiemes_choix = portes[:,0]
    elif strategie == Strategie.GARDER:
        deuxiemes_choix = premiers_choix
    else:
        raise ValueError("Stratégie non reconnue!")

    # print(bonnes_portes)
    # print(premiers_choix)
    # print(deuxiemes_choix)

    return (deuxiemes_choix == bonnes_portes).astype(int)