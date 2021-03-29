import pandas as pd
from data_cleaning import to_dataframe, data_processing

df_drugs = to_dataframe('drugs','../data/drugs.csv')
df_drugs = data_processing(df=df_drugs, filesource='drugs')
df_pubmed = to_dataframe('clinical_trials', '../data/clinical_trials.csv')
df_pubmed = data_processing(df=df_pubmed, filesource='pubmed')

def drugs_in_publications (df_drugs, df_publication_file):

    '''
    '''

    publication_type = ""
    drugs_publications = []

    if ('scientific_title' in df_publication_file.columns):
        publication_type="clinical_trial"
        df_publication_file.rename({"scientific_title": "title"})
    else:
        publication_type="pubmed"

    for index_drug, row_drug in df_drugs.iterrows():
        drug_name = row_drug["drug"]


        #filter by keeping rows that contain drug_name in title
        df_publication_file = df_publication_file[df_publication_file['title'].str.contains(drug_name)]

        for index_publication_file, row_publication_file in df_publication_file.iterrows():
            journal = row_publication_file["journal"]
            date_mention = row_publication_file["date"]
            drugs_publications.append(
                {
                    "drug_name": drug_name,
                    "publication_type": publication_type,
                    "journal": journal,
                    "date_mention": date_mention,
                }
            )

    return drugs_publications



print(drugs_in_publications(df_drugs, df_pubmed))
 