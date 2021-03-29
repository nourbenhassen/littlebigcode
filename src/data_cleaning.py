import pandas as pd
import numpy as np
from conf import FILE_SCHEMAS
import nltk
from nltk.corpus import stopwords

#convert and merge csv and json files to pandas Dataframes
def to_dataframe(file_source, *files):
    '''
    '''
    file_schema = FILE_SCHEMAS[file_source]
    df = pd.DataFrame(file_schema)

    for file in files:
        print(file)
        if (file.endswith('.csv')):
            df_newfile = pd.read_csv(file)
        elif (file.endswith('.json')):
            df_newfile = pd.read_json(file)
        else:
            raise Exception('File must be csv or json')

        df = df.append(df_newfile)

    return df

def data_processing(df, file_source):
    '''
    '''
    #date format constant
    #delete repeted rows
    #replace empty strings by NaN
    #TODO: remove stop words from title, scientific_title, journal - remove verbs, adjectives ?
    #TODO: check file schema

    #file_schema = FILE_SCHEMAS.file_source

    df_copy = df
    df_copy.drop_duplicates()

    if (file_source!="drugs"):
    
        df_copy = df_copy.replace(r'^\s*$', np.NaN, regex=True) #replace empty strings by NaN values
        print(df_copy['date'].dtypes)
        df_copy['date'] = pd.to_datetime(df_copy['date'], errors='coerce') #change datatype to datetime
        print(df_copy['date'].dtypes)
        #df_copy = df["date"].dt.strftime("%d/%m/%y") #change datetime format
        stop = stopwords.words('english')
        df_copy['title'] = df_copy['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)])) #remove stop words from title

    return df_copy
    
df_from_source_files = to_dataframe('pubmed', '../data/pubmed.csv', '../data/pubmed.json')
df_cleaned = data_processing(df=df_from_source_files, file_source='pubmed')

print(df_cleaned)