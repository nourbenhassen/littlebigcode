
import pandas
import json


def merge_drugs_publications (drugs_publications_clinical, drugs_publications_pubmed):

    """
    Merge two lists: drugs_publications_clinical and drugs_publications_pubmed

    Parameters
    ----------
        drugs_publications_clinical : list<dict>
            value returned by drugs_in_publications function with 'clinical_trials' as parameter for df_publication_file 
         drugs_publications_pubmed : list<dict>
            value returned by drugs_in_publications function with 'pubmed' as parameter for df_publication_file 

    Return
    ------
        merged_drugs_publications: json
    """
    
    merged_drugs_publications = [*drugs_publications_clinical, *drugs_publications_pubmed]
    merged_drugs_publications = json.dumps(merged_drugs_publications)

    return merged_drugs_publications