# URL to download the data from
BASE_URL = "http://data.economie.gouv.fr/explore/dataset/decp_augmente/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"

# Name of the local file used to store the data
LOCAL_DATASET_PATH = "./data/decp_augmente.csv"

# Column types to load the data with pandas
DATASET_TYPES = {
    "idMarche":int,
    "source":str,
    "type":str,
    "natureObjetMarche":str,
    "objetMarche":str,
    "codeCPV_Original":str,
    "codeCPV":str,
    "codeCPV_division":int,
    "referenceCPV":str,
    "dateNotification":str,
    "anneeNotification":str,
    "moisNotification":str,
    "datePublicationDonnees":str,
    "dureeMois":int,
    "dureeMoisEstimee":str,
    "dureeMoisCalculee":str,
    "montant":str,
    "nombreTitulaireSurMarchePresume":float,
    "montantCalcule":float,
    "formePrix":str,
    "lieuExecutionCode":str,
    "lieuExecutionTypeCode":str,
    "lieuExecutionNom":str,
    "codeDepartementExecution":float,
    "codeRegionExecution":float,
    "libelleRegionExecution":str,
    "nature":str,
    "accord-cadrePresume":str,
    "procedure":str,
    "idAcheteur":str,
    "sirenAcheteurValide":str,
    "nomAcheteur":str,
    "codeRegionAcheteur":str,
    "libelleRegionAcheteur":str,
    "departementAcheteur":str,
    "libelleDepartementAcheteur":str,
    "codePostalAcheteur":str,
    "libelleArrondissementAcheteur":str,
    "codeArrondissementAcheteur":"Int64",
    "libelleCommuneAcheteur":str,
    "codeCommuneAcheteur":str,
    "superficieCommuneAcheteur":float,
    "populationCommuneAcheteur":float,
    "geolocCommuneAcheteur":str,
    "typeIdentifiantEtablissement":str,
    "siretEtablissement":str,
    "siretEtablissementValide":str,
    "sirenEtablissement":str,
    "nicEtablissement":str,
    "sirenEtablissementValide":str,
    "categorieEtablissement":str,
    "denominationSocialeEtablissement":str,
    "codeRegionEtablissement":"Int64",
    "libelleRegionEtablissement":str,
    "libelleDepartementEtablissement":str,
    "departementEtablissement":str,
    "libelleArrondissementEtablissement":str,
    "codeArrondissementEtablissement":str,
    "codePostalEtablissement":str,
    "adresseEtablissement":str,
    "communeEtablissement":str,
    "codeCommuneEtablissement":str,
    "codeTypeEtablissement":str,
    "superficieCommuneEtablissement":float,
    "populationCommuneEtablissement":float,
    "distanceAcheteurEtablissement":float,
    "geolocCommuneEtablissement":str
}