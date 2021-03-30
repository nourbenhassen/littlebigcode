import pandas as pd
import numpy as np
from data_cleaning import to_dataframe, data_cleaning
from data_processing import drugs_in_publications
from data_merging import merge_drugs_publications
import json


def journal_with_most_drugs(drugs_publications):

    """
    Extract the journal name(s) from json variable which mention the highest number of distinct drug names.

    Parameters
    ----------
        drugs_publications: json
            value returned by merge_drugs_publications function

    Return
    ------
        journal_max_drug_names: pandas.DataFrame

    """
    
    drugs_publications = json.loads(drugs_publications)
    df_drugs_publications = pd.DataFrame(drugs_publications)

    result = df_drugs_publications.groupby('journal').agg({"drug_name": "nunique"})
    max = result.agg({"drug_name": "max"}).iloc[0]
    journal_max_drug_names = result[result["drug_name"] == max]

    return journal_max_drug_names




df_drugs = to_dataframe('drugs','../data/drugs.csv')
df_drugs = data_cleaning(df=df_drugs, file_source='drugs')

df_clinical = to_dataframe('clinical_trials', '../data/clinical_trials.csv')
df_clinical= data_cleaning(df=df_clinical, file_source='clinical_trials')

df_pubmed = to_dataframe('pubmed', '../data/pubmed.csv', '../data/pubmed.json')
df_pubmed = data_cleaning(df=df_pubmed, file_source='pubmed')

drugs_in_publications_pubmed = drugs_in_publications(df_drugs, df_pubmed)
drugs_in_publications_clinical = drugs_in_publications(df_drugs, df_clinical)

drugs_publications = merge_drugs_publications(drugs_in_publications_clinical, drugs_in_publications_pubmed)


print(journal_with_most_drugs(drugs_publications))