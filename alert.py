def flag_low_stock(df):
    return df[df['ReorderQty'] > 0]
