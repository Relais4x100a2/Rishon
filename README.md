Rishon : exploitation tous azimuts de la base SIRENE
===

## APERO
Petit outil CLI pour dénicher des des petits-producteurs de victuailles pour apératifs & co. Les ETI et GRANDES ENTREPRISES ont été exclues des résultats. Des améliorations sont à venir.
     
 ### 3 commandes possibles :
     
     -biere 
     
     -fromage
     
     - code_NAF : Autres productions en tapant entre guillemets: le code NAF - voir liste de l'INSEE : https://entreprise.data.gouv.fr/api-doc/codes_naf

 ### 2 options possibles (cumulables) pour chaque commande:
     
     - limitation des résultats pour un département (numéro de départemetn à indiquer) : -d numéro_du_département
     
     - impression dans un fichier csv en tapan entre guillemets: nom_du_fichier.csv : -imp "nom_du_fichier.csv"

### Installation

Allez dans le repository git puis tapez dans le terminal de ce dossier

```shell
pip3 install -r requirements.txt
```

ou

```shell
pip install -r requirements.txt
```

Tapez désormais

Python(ou Python3) apero.py [commande] [option]

ex: 

```shell
python3 apero.py biere -d 80 -imp "biere_somme.csv"
```
ou

```shell
python apero.py biere -d 80 -imp "biere_somme.csv"
```

### Ressources supplémentaires
API SIRENE : https://entreprise.data.gouv.fr/api_doc/sirene

