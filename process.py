import numpy as np

def clean_data(df):
    df.drop_duplicates(subset='SKU', keep='last', inplace=True)
    df['OnHandQty'] = df['OnHandQty'].clip(lower=0)
    df['ReorderQty'] = np.maximum(0, df['ReorderPoint'] - df['OnHandQty'])
    return df
