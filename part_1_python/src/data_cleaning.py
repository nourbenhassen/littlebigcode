import pandas as pd
import numpy as np
from conf import FILE_SCHEMAS
import nltk
from nltk.corpus import stopwords


def to_dataframe(file_source, *files):

    """
    Return a pandas.DataFrame object from one or a combination of csv and json files.

    Parameters
    ----------
        file_source : str
            values --> 'pubmed', 'drugs' or 'clinical_trials'
        files: str
            values --> path(s) of the csv and json files

    Return
    ------
        df: pandas.DataFrame
    """

    file_schema = FILE_SCHEMAS[file_source]
    df = pd.DataFrame(file_schema)

    for file in files:
        if (file.endswith('.csv')):
            df_newfile = pd.read_csv(file)
        elif (file.endswith('.json')):
            df_newfile = pd.read_json(file)
        else:
            raise Exception('File must be csv or json')

        df = df.append(df_newfile)

    return df


def data_cleaning(df, file_source):

    """
    Takes a pandas.DataFrame object as input, cleans it and returns it. 
    The cleaning operations are: removing duplicate rows, replacing empty strings by NaN values, removing stop words when needed.

    Parameters
        ----------
        df : pandas.DataFrame
        file_source : str
            values --> 'pubmed', 'drugs' or 'clinical_trials'

        Return
        ------
        df_copy: pandas.DataFrame
        A cleaned copy of the pandas dataframe object is returned
    """

    df_copy = df
    df_copy.drop_duplicates()

    if (file_source=="drugs"):
        df_copy["drug"]=df_copy["drug"].str.lower()    
    else:
        df_copy = df_copy.replace(r'^\s*$', np.NaN, regex=True) 
        df_copy['date'] = pd.to_datetime(df_copy['date'], errors='coerce') 

        stop = stopwords.words('english')
        
        if file_source=="pubmed":
            df_copy["title"] = df_copy["title"].astype(str).apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)])).str.lower()  
        elif file_source=="clinical_trials":
            df_copy["scientific_title"] = df_copy["scientific_title"].astype(str).apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)])).str.lower()
    
    return df_copy