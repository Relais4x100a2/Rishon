import click
import requests
from terminaltables import AsciiTable
from operator import itemgetter, attrgetter
import csv


@click.group()
def uneCommandePlusOuMoinsVide():
    """Petit outil CLI pour dénicher des des petits-producteurs de victuailles pour apératifs & co. Les ETI et GRANDES ENTREPRISES ont été exclues des résultats. Des améliorations sont à venir.
     
     3 commandes possibles :
     
     -biere

     -fromage

     - code_NAF : Autres productions en tapant entre guillemets: le code NAF - voir liste de l'INSEE : https://entreprise.data.gouv.fr/api-doc/codes_naf

     2 options possibles (cumulables) pour chaque commande:

     - limitation des résultats pour un département (numéro de départemetn à indiquer) : -d numéro_du_département

     - impression dans un fichier csv en tapan entre guillemets: nom_du_fichier.csv : -imp "nom_du_fichier.csv"

     ***Version 2020-12-28 - Relais4x100a2***"""

    return True

@uneCommandePlusOuMoinsVide.command("biere")
@click.option("-d", "--departement",  type=int, default=None,
             help="Sélectionne les résultats dans le numéro de département indiqué classé selon ordre alphabétique des villes")
@click.option("-imp", "--impression", type=click.File(mode="w"), default=None)
def scope_content(departement=None, impression=None):
    #URL de recherche API SIRENE pour les fabricants de bière
    url = "https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?per_page=100&activite_principale=1105Z"
    """avec la variable R, on passera une requête GET sur URL qui est le paramètre de la fonction"""
    r = requests.get(url)
    """avec la variable DATA, on récupera la réponse(le body) au format JSON """
    data = r.json()
    current_page = int(data["page"])
    next_page = current_page + 1
    total_page = int(data["total_pages"])
    """création d'une liste vide avec la varialble SIMPLIFIED"""
    header=[["SIRET", "Enseigne", "Adresse"]]
    simplified=[]
    resultat=[]

    # Comme on connait le nombre total de pages de résultats, on va faire une boucle pour chaque page
    for i in range(1,total_page):
        url = "https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?per_page=100&activite_principale=1105Z&page={}".format(i)
        f = requests.get(url)
        """avec la variable DATA, on récupera la réponse(le body) au format JSON """
        dataf = f.json()
        """pour chaque fabricant de bière dans SIRENE"""
        for item in dataf["etablissement"]:
            """définition des éléments qu'on souhaite récupérer pour chaque item"""
            siret = item["siret"]
            denomination = item["nom_raison_sociale"]
            adresse = item["geo_adresse"]
            enseigne = item["enseigne"]
            categoriejur = item["categorie_entreprise"]
            nom = item["l1_normalisee"]
            num_departement = item["departement"]
            commune = item["libelle_commune"]
            """ajout des éléments dans la liste SIMPLIFIED parès nettoyage qualitatif"""
            # si l'adresse n'est pas renseignée, il y a un grand risque que l'affaire ne marche plus
            if adresse:
                #on ne garde que les PME
                if categoriejur == "PME":
                    if enseigne:
                        simplified.append([num_departement, commune,siret, enseigne, adresse])
                    else:
                        if "*" in denomination:
                            simplified.append([num_departement,commune,siret, nom, adresse])
                        else:
                            # lorsqu'il y a une indivision (succession), il y a un grand risque que l'affaire ne marche plus
                            if "INDIVISION" not in denomination:
                                simplified.append([num_departement,commune,siret, denomination, adresse])
            simplified=sorted(simplified, key=itemgetter(0))


            if departement:
                for etablissement in simplified:
                    if etablissement[0] != str(departement):
                        simplified.remove(etablissement)
                        simplified = sorted(simplified, key=itemgetter(1))

    if impression:
        writer = csv.writer(impression)
        writer.writerow(["SIRET","nom","adresse"])
        for item in simplified:
            writer.writerow([item[2], item[3], item[4]])
        print("Fichier CSV imprimé !")
    else:
        #on crée une nouvelle liste avec les seuls élèments qu'on souhaite afficher
        for entity in simplified:
            resultat.append(entity[2:])
        table = AsciiTable(header+resultat)
        print(table.table)

@uneCommandePlusOuMoinsVide.command("fromage")
@click.option("-d", "--departement",  type=int, default=None,
             help="Sélectionne les résultats dans le numéro de département indiqué classé selon ordre alphabétique des villes")
@click.option("-imp", "--impression", type=click.File(mode="w"), default=None,
              help="Imprime la liste des résultats")
def scope_content(departement=None, impression=None):
    #URL de recherche API SIRENE pour les fabricants de bière
    url = "https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?per_page=100&activite_principale=1051C"
    """avec la variable R, on passera une requête GET sur URL qui est le paramètre de la fonction"""
    r = requests.get(url)
    """avec la variable DATA, on récupera la réponse(le body) au format JSON """
    data = r.json()
    current_page = int(data["page"])
    next_page = current_page + 1
    total_page = int(data["total_pages"])
    """création d'une liste vide avec la varialble SIMPLIFIED"""
    header=[["SIRET", "Enseigne", "Adresse"]]
    simplified=[]
    resultat=[]

    # Comme on connait le nombre total de pages de résultats, on va faire une boucle pour chaque page
    for i in range(1,total_page):
        url = "https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?per_page=100&activite_principale=1051C&page={}".format(i)
        f = requests.get(url)
        """avec la variable DATA, on récupera la réponse(le body) au format JSON """
        dataf = f.json()
        """pour chaque fabricant de bière dans SIRENE"""
        for item in dataf["etablissement"]:
            """définition des éléments qu'on souhaite récupérer pour chaque item"""
            siret = item["siret"]
            denomination = item["nom_raison_sociale"]
            adresse = item["geo_adresse"]
            enseigne = item["enseigne"]
            categoriejur = item["categorie_entreprise"]
            nom = item["l1_normalisee"]
            num_departement = item["departement"]
            commune = item["libelle_commune"]
            """ajout des éléments dans la liste SIMPLIFIED parès nettoyage qualitatif"""
            # si l'adresse n'est pas renseignée, il y a un grand risque que l'affaire ne marche plus
            if adresse:
                #on ne garde que les PME
                if categoriejur == "PME":
                    if enseigne:
                        simplified.append([num_departement, commune,siret, enseigne, adresse])
                    else:
                        if "*" in denomination:
                            simplified.append([num_departement,commune,siret, nom, adresse])
                        else:
                            # lorsqu'il y a une indivision (succession), il y a un grand risque que l'affaire ne marche plus
                            if "INDIVISION" not in denomination:
                                simplified.append([num_departement,commune,siret, denomination, adresse])

                    simplified = sorted(simplified, key=itemgetter(0))

            if departement:
                for etablissement in simplified:
                    if etablissement[0] != str(departement):
                        simplified.remove(etablissement)
                        simplified = sorted(simplified, key=itemgetter(1))

    if impression:
        writer = csv.writer(impression)
        writer.writerow(["SIRET","nom","adresse"])
        for item in simplified:
            writer.writerow([item[2], item[3], item[4]])
        print("Fichier CSV imprimé !")
    else:
        #on crée une nouvelle liste avec les seuls élèments qu'on souhaite afficher
        for entity in simplified:
            resultat.append(entity[2:])
        table = AsciiTable(header+resultat)
        print(table.table)

@uneCommandePlusOuMoinsVide.command("code_NAF")
@click.argument("code", type=str)
@click.option("-d", "--departement",  type=int, default=None,
             help="Sélectionne les résultats dans le numéro de département indiqué classé selon ordre alphabétique des villes")
@click.option("-imp", "--impression", type=click.File(mode="w"), default=None,
              help="Imprime la liste des résultats")

def scope_content(code, departement=None, impression=None):
    print("Code de NAF de l'INSEE - pour plus d'aide voir la liste : https://entreprise.data.gouv.fr/api-doc/codes_naf")
    #URL de recherche API SIRENE pour les fabricants de bière
    url = "https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?per_page=100&activite_principale={}".format(code)
    """avec la variable R, on passera une requête GET sur URL qui est le paramètre de la fonction"""
    r = requests.get(url)
    """avec la variable DATA, on récupera la réponse(le body) au format JSON """
    data = r.json()
    current_page = int(data["page"])
    next_page = current_page + 1
    total_page = int(data["total_pages"])
    """création d'une liste vide avec la varialble SIMPLIFIED"""
    header=[["SIRET", "Enseigne", "Adresse"]]
    simplified=[]
    resultat=[]

    # Comme on connait le nombre total de pages de résultats, on va faire une boucle pour chaque page
    for i in range(1,total_page):
        url = "https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?per_page=100&activite_principale={}&page={}".format(code,i)
        f = requests.get(url)
        """avec la variable DATA, on récupera la réponse(le body) au format JSON """
        dataf = f.json()
        """pour chaque fabricant de bière dans SIRENE"""
        for item in dataf["etablissement"]:
            """définition des éléments qu'on souhaite récupérer pour chaque item"""
            siret = item["siret"]
            denomination = item["nom_raison_sociale"]
            adresse = item["geo_adresse"]
            enseigne = item["enseigne"]
            categoriejur = item["categorie_entreprise"]
            nom = item["l1_normalisee"]
            num_departement = item["departement"]
            commune = item["libelle_commune"]
            """ajout des éléments dans la liste SIMPLIFIED parès nettoyage qualitatif"""
            # si l'adresse n'est pas renseignée, il y a un grand risque que l'affaire ne marche plus
            if departement:
                if str(num_departement) == str(departement):
                    if adresse:
                        #on ne garde que les PME
                        if categoriejur == "PME":
                            if enseigne:
                                simplified.append([num_departement, commune,siret, enseigne, adresse])
                            else:
                                if "*" in denomination:
                                    simplified.append([num_departement,commune,siret, nom, adresse])
                                else:
                                    # lorsqu'il y a une indivision (succession), il y a un grand risque que l'affaire ne marche plus
                                    if "INDIVISION" not in denomination:
                                        simplified.append([num_departement,commune,siret, denomination, adresse])
                simplified = sorted(simplified, key=itemgetter(1))

            else:
                if adresse:
                    # on ne garde que les PME
                    if categoriejur == "PME":
                        if enseigne:
                            simplified.append([num_departement, commune, siret, enseigne, adresse])
                        else:
                            if "*" in denomination:
                                simplified.append([num_departement, commune, siret, nom, adresse])
                            else:
                                # lorsqu'il y a une indivision (succession), il y a un grand risque que l'affaire ne marche plus
                                if "INDIVISION" not in denomination:
                                    simplified.append([num_departement, commune, siret, denomination, adresse])
                    simplified = sorted(simplified, key=itemgetter(0))


    if impression:
        writer = csv.writer(impression)
        writer.writerow(["SIRET","nom","adresse"])
        for item in simplified:
            writer.writerow([item[2], item[3], item[4]])
        print("Fichier CSV imprimé !")
    else:
        #on crée une nouvelle liste avec les seuls élèments qu'on souhaite afficher
        for entity in simplified:
            resultat.append(entity[2:])
        table = AsciiTable(header+resultat)
        print(table.table)


if __name__ == "__main__":
    uneCommandePlusOuMoinsVide()
