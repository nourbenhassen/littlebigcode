import pandas as pd


def drugs_in_publications (df_drugs, df_publication_file):

    """
    Return a list of dictionaries. Each element of the list contains the information 
    about a publication: "drug_name", "publication_type", "journal", "date_mention"

    Parameters
    ----------
        df_drugs : pandas.DataFrame
            This is the output of the data_cleaning function with 'drugs' as file_source
        df_drugs : pandas.DataFrame
            This is the output of the data_cleaning function with 'pubmed' or 'clinical_trials' as file_source

    Return
    ------
        drugs_publications: list<dict>
    """

    publication_type = ""
    drugs_publications = []

    if ('scientific_title' in df_publication_file.columns):
        publication_type="clinical_trial"
        df_publication_file.rename(columns= {"scientific_title": "title"}, inplace=True)
    else:
        publication_type="pubmed"

    for index_drug, row_drug in df_drugs.iterrows():
        drug_name = row_drug["drug"]

        df_publication_file_filtered = df_publication_file[df_publication_file['title'].str.contains(drug_name)]

        for index_publication_file, row_publication_file in df_publication_file_filtered.iterrows():
            journal = row_publication_file["journal"]
            date_mention = str(row_publication_file["date"])
            drugs_publications.append(
                {
                    "drug_name": drug_name,
                    "publication_type": publication_type,
                    "journal": journal,
                    "date_mention": date_mention,
                }
            )

    return drugs_publications 