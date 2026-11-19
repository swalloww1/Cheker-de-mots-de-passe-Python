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



#Exemple avec mdp.txt

 == Audit de 10 mots de passe ==\
 [FAIBLE] 1/5  azerty\
 [FAIBLE] 4/5  Azerty123!\
 [OK  ] 5/5  MotDePasse2024!\
 [FAIBLE] 2/5  123456789012\
 [OK  ] 5/5  Soleil!Chaud2024\
 [FAIBLE] 4/5  P@ssw0rd\
 [FAIBLE] 3/5  motdepasse123\
 [FAIBLE] 4/5  SUPERMOTDEPASSE1!\
 [OK  ] 5/5  Chien-Chat-2024\
 [FAIBLE] 1/5  qwerty\

Solides : 3/10  |  faibles : 7  |  score moyen : 3.4
