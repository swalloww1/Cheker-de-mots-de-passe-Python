

from __future__ import annotations

import sys

LONGUEUR_MIN = 12

def lire_mots(chemin: str) -> list[str]:
    """Renvoie le fichier ligne par ligne (sans lignes vides)."""
    mots = []
    with open(chemin, encoding="utf-8") as fichier:
        for ligne in fichier:
            mot = ligne.strip()
            if mot:
                mots.append(mot)
    return mots


def criteres(mdp: str) -> dict[str, bool]:
    """Vérifie les 5 règles de la politique de sécurité.

    Retourne un dictionnaire avec exactement ces 5 clés :
      "longueur"  : au moins 12 caractères          (len(mdp) >= 12)
      "minuscule" : au moins une lettre minuscule   (a, b, ...)
      "majuscule" : au moins une lettre majuscule   (A, B, ...)
      "chiffre"   : au moins un chiffre             (0-9)
      "special"   : au moins un caractère qui n'est ni une lettre ni un chiffre     (!, @, -, ...)"""

    resultat = {
        "longueur": len(mdp) >= LONGUEUR_MIN,
        "minuscule": False,
        "majuscule": False,
        "chiffre": False,
        "special": False,
    }

    for caractere in mdp:
        if caractere.islower():
            resultat["minuscule"] = True
        if caractere.isupper():
            resultat["majuscule"] = True
        if caractere.isdigit():
            resultat["chiffre"] = True
        if not caractere.isalnum():
            resultat["special"] = True

    return resultat

  
def score(criteres_mdp: dict[str, bool]) -> int:
    """Renvoie le nombre de règles respectées : de 0 à 5."""
    return sum(criteres_mdp.values())



def est_solide(mdp: str) -> bool:
    """True si le mot de passe respecte les 5 règles, False sinon."""
    return score(criteres(mdp)) == 5


def analyser(mots: list[str]) -> list[tuple[str, int]]:
    """Note chaque mot de passe : [(mot_de_passe, score), ...]."""
    resultats = []
    for mdp in mots:
        resultats.append((mdp, score(criteres(mdp))))
    return resultats


def rapport(mots: list[str]) -> dict:
    """Assemble les statistiques sous forme de dictionnaire.

    Clés attendues :
      "total"       : nombre de mots de passe (int)
      "solides"     : combien respectent les 5 règles (int)
      "faibles"     : total - solides (int)
      "score_moyen" : score moyen, en nombre à virgule (float)
    """
    total = len(mots)
    solides = 0
    score_total = 0
    for mdp in mots:
        if est_solide(mdp):
            solides += 1
        score_total += score(criteres(mdp))

    faibles = total - solides
    if total > 0:
        score_moyen = score_total / total
    else:
        score_moyen = 0.0

    return {
        "total": total,
        "solides": solides,
        "faibles": faibles,
        "score_moyen": score_moyen,
    }


def afficher_mots(resultats: list[tuple[str, int]]) -> None:
    """Affiche le score de chaque mot de passe."""
    for mdp, note in resultats:
        etat = "OK  " if note == 5 else "FAIBLE"
        print(f"  [{etat}] {note}/5  {mdp}")


chemin = sys.argv[1] if len(sys.argv) > 1 else "mdp.txt"
mots = lire_mots(chemin)
stats = rapport(mots)

print(f"== Audit de {stats['total']} mots de passe ==")
afficher_mots(analyser(mots))

print(
    f"\nSolides : {stats['solides']}/{stats['total']}"
    f"  |  faibles : {stats['faibles']}"
    f"  |  score moyen : {stats['score_moyen']}"
)
