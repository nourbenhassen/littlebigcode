import pandas as pd

# [{
#                     "drug_name": drug_name
#                     "publication_type": publication_type,
#                     "journal": journal,
#                     "publication_date": publication_date,
# }]


#Extraire depuis le json produit par la data pipeline le nom du journal qui mentionne le plus de médicaments différents

def journal_with_most_drugs(drugs_publications):
    df_drugs_publications = pd.Dataframe(drugs_publications)

    result = df_drugs_publications.groupby('journal').agg({"drug_name": "nunique"}).sort_values(by=['drug_name'], inplace=True, ascending=False))[0]['journal']

    return result
