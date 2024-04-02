import pandas as pd
import re
from unidecode import unidecode

def clear_names(df):
    """Rinomina le colonne di un DataFrame in minuscolo, rimuovendo gli accenti e sostituendo
    i caratteri speciali e gli spazi con underscore.

    Args:
        df (pandas.DataFrame): Il DataFrame da elaborare.

    Returns:
        pandas.DataFrame: Un nuovo DataFrame con i nomi delle colonne corretti.
    """
    # Crea una copia del DataFrame per evitare modifiche ai dati originali
    df_copy = df.copy()
    
    # Funzione per pulire i nomi delle colonne
    def clean_column_name(col):
        # Converti il nome della colonna in minuscolo
        col = col.lower()
        # Rimuovi accenti
        col = unidecode(col)
        # Rimuovi caratteri speciali e sostituisci spazi con underscore
        col = re.sub(r'[^a-zA-Z0-9]+', '_', col)
        
        return col
    
    # Rinomina le colonne del DataFrame usando la funzione clean_column_name
    df_copy.columns = map(clean_column_name, df_copy.columns)
    
    return df_copy