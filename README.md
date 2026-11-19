# Cheker-de-mots-de-passe-Python

Un outil cheker de mots de passe en python, qui lit un fichier de mots de passe et évalue la solidité de chacun selon une politique de sécurité de 5 règles.

-fonctionnalité:

  Politique de Sécurité (5 règles) : Chaque mot de passe est vérifié sur la longueur minimale (12 caractères), la présence d'une minuscule, d'une majuscule, d'un chiffre et d'un caractère spécial. 
  Les règles sont indépendantes : on sait exactement lesquelles sont respectées.

  Score sur 5 : Chaque mot de passe obtient une note de 0 à 5 (une règle respectée = un point), avec la mention "OK" s'il valide les cinq règles, "FAIBLE" sinon.

  Analyse par lot : Le programme traite tout un fichier en une seule commande, une ligne par mot de passe, et conserve l'ordre du fichier.

  Statistiques globales : Affichage du nombre total de mots de passe, du nombre de mots de passe solides et faibles, et du score moyen de l'ensemble.
    

-Technique

  Langage : Python 3

  Bibliothèques : Aucune (modules natifs uniquement)

  Interface : Terminal 

