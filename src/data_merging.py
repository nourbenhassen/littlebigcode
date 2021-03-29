
import pandas


def merge_drugs_publications (drugs_publications_clinical, drugs_publications_pubmed):
    merged_drugs_publications = drugs_publications_clinical.extend(drugs_publications_pubmed)
    return merged_drugs_publications