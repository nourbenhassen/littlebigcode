
import pandas
from data_cleaning import to_dataframe, data_processing
from data_processing import drugs_in_publications



def merge_drugs_publications (drugs_publications_clinical, drugs_publications_pubmed):
    merged_drugs_publications = drugs_publications_clinical
    merged_drugs_publications.append(drugs_publications_pubmed)
    return merged_drugs_publications


df_drugs = to_dataframe('drugs','../data/drugs.csv')
df_drugs = data_processing(df=df_drugs, file_source='drugs')

df_clinical = to_dataframe('clinical_trials', '../data/clinical_trials.csv')
df_clinical= data_processing(df=df_clinical, file_source='clinical_trials')

df_pubmed = to_dataframe('pubmed', '../data/pubmed.csv', '../data/pubmed.json')
df_pubmed = data_processing(df=df_pubmed, file_source='pubmed')

drugs_in_publications_pubmed = drugs_in_publications(df_drugs, df_pubmed)
drugs_in_publications_clinical = drugs_in_publications(df_drugs, df_clinical)

merged_data = merge_drugs_publications(drugs_in_publications_clinical, drugs_in_publications_pubmed)

print(merged_data)
