# CQRT - Backend

## Index
- [Pourquoi?](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#pourquoi)
- [Objectif](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#objectif)
- [Versions](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#versions)
- [Comment l'installer et l'utiliser?](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#comment-linstaller-et-lutiliser)
- [Description fichier par fichier](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#description-fichier-par-fichier)
- [Comment contribuer?](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#comment-contribuer)
- [FAQ](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#faq)
- [Nous contacter](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#nous-contacter)
- [License](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#license)
- [Dernière mise à jour de la documentation](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md#dernière-mise-à-jour-de-la-documentation)

## Pourquoi?
Dans le première école dans laquelle j'étais, l'EPSI, on nous avais confié la tâche de faire un projet innovant. J'ai parlé à mon équipe de mon framework Kivy et l'un d'eux particulièrement épris de cybersécurité m'a demandé un réseau social sécurisé. Fort de ma lecture d'un vieux livre sur PGP et de l'AFIT (projet de premier semestre à l'EPITA), je me suis mis à codé et voilà ce que ça a donné. L'objectif de base était d'implémenter la RFC 4880: OpenPGP mais l'implémentation s'est vite révélée extrêmement complexe et je me suis mis à juste coder mon propre truc.

## Objectif
L'objectif de ce projet est d'être un backend universel pour rendre tous les réseau sociaux, tous les tchats de jeu et de manière plus générale toutes les communications compatibles entre elles qu'on ai pas le problème de se trouver à chaque fois un réseau social en commun. Un autre des objectifs de CQRT est de remettre de l'éthique dans nos communications car je suis nostalgique des années 201X durant lesquelles les communications étaient grandement plus éthiques que de nos jours. Bien sûr il va s'en dire qu'un autre objectif très important de ce backend est la sécurité à son apogée et la gestion, le contrôle pour les utilisateurs et développeurs. Un dernier objectif qui me vient en tête sera la rétrocompatibilité qui sera assurée à partir de la première version de déploiement c'est à dire la version 3.0.0 pour le moment.

## Versions
Pour le versionnage le protocole de nommage est le suivant:<br>
[nombre de présentations annuelles passées à l'EPSI].[nombre de nouvelles fonctionnalités depuis la dernière présentation].[nombre d'optimisations et de bugs réglés depuis la dernière fonctionnalité]

Une rétrocompatibilité maximale sera assurée à partir de la version 3.0.0.<br>
Une version est considérée comme ayant pour source officielle le commit du même nom (sauf si explicitement dit autrement) et comme ayant pour versions compilées officielles la release du même nom.

Objectifs:<br>
1.0.0: Exister<br>
2.0.0: Être stable et utilisable + traduction en C# + premier frontend<br>
3.0.0: Déploiement + traduction en Java + second frontend<br>
4.0.0: Première couverture d'un autre réseau social + traduction en Swift + troisième frontend<br>
5.0.0: Finitions en tout genre

Versions:<br>
1.0.0: Existe

## Comment l'installer et l'utiliser?
A partir des versions de déploiement, tous les liens de téléchargement seront accessibles depuis notre site web mais jusque là il va falloir télécharger des releases sur la page github du frontend désiré.<br>
Il est à noter que les dossiers vides ne passent pas sur github donc il va vous falloir les recréer vous-même si vous voulez recompiler de votre côté ou utiliser une version interprétée.

## Description fichier par fichier
- [LICENSE](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/LICENSE): Fichier administratif listant vos droits et devoirs vis-à-vis de notre travail.
- [README.en.md](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.en.md): Fichier expliquant le projet en anglais.
- [README.fr.md](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.fr.md): Fichier expliquant le projet en français. C'est le fichier que vous êtes actuellement en train de lire.
- [README.md](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/README.md): Fichier reliant les README de toutes les langues.
- [.gitignore](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/.gitignore): Fichier listant les différents fichiers et dossiers que vous ne voulez pas mettre sur git / github (caches, fichiers secret, ...) (Principalement utile quand l'upload est automatisé avec des logiciels comme Github Desktop pour pas qu'ils incluent ces fichiers dans vos commits).
- [TESTS.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/TESTS.py): Script permettant d'executer tous les tests unitaires.

### Dossier "TESTS":
- [test_arith.json](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/TESTS/test_arith.json): Fichier contenant des tests unitaires concernant les opérations arithmétiques.
- [test_bytestrings.json](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/TESTS/test_bytestrings.json): Fichier contenant des tests unitaires concernant l'implémentation du type bytestring.

### Dossier "CLIENT":
- SOUS-DOSSIER "data": Dossier contenant toutes les ressources et images de l'application (provient du framework).
- SOUS-DOSSIER "home": Dossier contenant l'architecture de fichiers de l'utilisateur.
- [connexions.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/connexions.py): Fait partie de mon [framework kivy](https://github.com/reza0310/Framework-Kivy) section bonus. Permet d'échanger avec un serveur.
- [CQRT.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/CQRT.py): Fait partie de mon [framework kivy](https://github.com/reza0310/Framework-Kivy). Fichier principal du frontend.
- [framework.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/framework.py): Fait partie de mon [framework kivy](https://github.com/reza0310/Framework-Kivy). Fichier principal de ce dernier. Contient toutes les fonctions et classes principales du framework.
- [globals.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/globals.py): Fait partie de mon [framework kivy](https://github.com/reza0310/Framework-Kivy). Contient les variables ultra-globales.
- [main.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/main.py): Fait partie de mon [framework kivy](https://github.com/reza0310/Framework-Kivy). Fichier d'entrée de l'interprétation et de la compilation. Lie les autres fichiers et initialise l'application.
- [structures.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/structures.py): Fait partie de mon [framework kivy](https://github.com/reza0310/Framework-Kivy). Utilisée pour les classes définies par l'utilisateur, dans ce projet ce fichier contient la classe qui interprète les commandes et appelle commandes.py.
- [bytes.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/bytes.py): Implémente un type bytestring pour pouvoir manipuler et chiffrer facilement les données.
- [commandes.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/CLIENT/commandes.py): Implémentations officielles de toutes les commandes composant CQRT. Fichier commun à toutes les versions, frontends et traductions de CQRT. Fichier crucial.

### Dossier "SERVEUR_COMPTES":
- SOUS-DOSSIER "accounts": Dossier contenant toutes les informations stockées par ce serveur.
- [serveur.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/SERVEUR_COMPTES/serveur.py): Script du serveur de comptes.

### Dossier "SERVEUR_MESSAGES":
- SOUS-DOSSIER "messages": Dossier contenant toutes les informations stockées par ce serveur.
- [serveur.py](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/SERVEUR_MESSAGES/serveur.py): Script du serveur de messages.

## Comment contribuer?
Vous pouvez vous servir de ce dépôt pour vous entraîner à l'open source. Pour contribuer, suivez juste [ce tutoriel](https://github.com/reza0310/Tutorials/blob/contribute/README.fr.md) et commentez toute issue ou pull request (ne mettez pas juste un titre).

## FAQ
Aucune question ne nous a encore été posée.

## Nous contacter
Commanditaire: Azrael: Azrael#002 sur discord.<br>
Coordinateur: reza0310: [page de contact](https://github.com/reza0310#a-propos-de-mon-profil).

## License
Lisez le [fichier "LICENSE"](https://github.com/reza0310/Appli_Kivy_7-CQRT/blob/main/LICENSE) (en anglais).

### Dernière mise à jour de la documentation 
Jeudi 15 septembre 2022
