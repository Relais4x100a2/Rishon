Rishon : exploitation tous azimuts de la base SIRENE
===

## APERO.PY

Petit outil CLI pour dénicher des des petits-producteurs de victuailles pour apératifs & co (bière et fromage mais possible avec d'autres en précisant le code NAF). 
Affiche le numéro de SIRET, l'enseigne, l'adresse et la date de création de l'entreprise.
Les ETI et GRANDES ENTREPRISES ont été exclues des résultats. Des améliorations sont à venir.

3 commandes possibles :
     
- biere

- fromage

- code_NAF : Autres productions en tapant le code NAF - voir liste de l'INSEE : https://entreprise.data.gouv.fr/api-doc/codes_naf

2 options possibles (cumulables) pour chaque commande:

- limitation des résultats pour un département (numéro de département à indiquer) : -d numéro_du_département

- impression dans un fichier csv en indiquant nom_du_fichier.csv : -imp nom_du_fichier.csv

     **Version 2020-12-29 - Relais4x100a2**

### Installation

Allez dans le repository git puis tapez en fonction dans le terminal de ce dossier :

```shell
pip3 install -r requirements.txt
```

Tapez ensuite

Python(ou Python3) apero.py [commande] [option]

ex: 

```shell
python3 apero.py code_NAF 0126Z -d 34 -imp resultatolive.csv
```


### Ressources supplémentaires
API SIRENE : https://entreprise.data.gouv.fr/api_doc/sirene

