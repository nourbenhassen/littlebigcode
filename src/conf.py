import pandas as pd

PUBMED_SCHEMA = {
    'id': pd.Series([], dtype='int'),
    'title': pd.Series([], dtype='str'),
    'date': pd.Series([], dtype='object'),
    'journal': pd.Series([], dtype='string'),
    }

DRUGS_SCHEMA = {
    'atccode': pd.Series([], dtype='string'),
    'drug': pd.Series([], dtype='string'),
}

CLINICAL_TRIALS_SCHEMA = {
    'id': pd.Series([], dtype='int'),
    'scientific_title': pd.Series([], dtype='str'),
    'date': pd.Series([], dtype='object'),
    'journal': pd.Series([], dtype='string'),
}

FILE_SCHEMAS = {
    'pubmed': PUBMED_SCHEMA,
    'drugs': DRUGS_SCHEMA,
    'clinical_trials': CLINICAL_TRIALS_SCHEMA,
}