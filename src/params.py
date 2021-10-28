# URL to download the data from
URL_AUGMENTED = "http://data.economie.gouv.fr/explore/dataset/decp_augmente/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
URL_CONSOLIDATED = "https://www.data.gouv.fr/fr/datasets/r/16962018-5c31-4296-9454-5998585496d2"
URL_CONSOLIDATED_SCHEMA = "https://schema.data.gouv.fr/schemas/139bercy/format-commande-publique/latest/marches.json"
# Name of the local files used to store the data
LOCAL_PATH_AUGMENTED = "./data/decp_augmente.csv"
LOCAL_PATH_CONSOLIDATED = "./data/decp.json"
LOCAL_PATH_CONSOLIDATED_SCHEMA = "./data/decp_schema.json"
LOCAL_PATH_AUDIT_RESULTS = "./data/data_quality_audit_results.json"
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

# Column types to load the data with pandas
COLUMNS_TO_ANALYZE_QUALITY = [
    "codeCPV_Original",
    "codeCPV",
    "dateNotification",
    "datePublicationDonnees",
    "denominationSocialeEtablissement",
    "dureeMois",
    "formePrix",
    "idAcheteur",
    "idMarche",
    "lieuExecutionCode",
    "lieuExecutionNom",
    "lieuExecutionTypeCode",
    "montant",
    "nature",
    "objetMarche",
    "procedure",
    "siretEtablissement",
    "source",
    "type",
    "typeIdentifiantEtablissement"
]

# GitHub repo where the project is
GITHUB_REPO = "pauldes/valorisation-decp"
AUDIT_RESULTS_ARTIFACT_NAME = "data_quality_audit_results.json"