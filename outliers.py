def outliers(df):
    """
    df: DataFrame
    rtype: DataFrame: with outliers
    """
    return df[abs(df - df.mean()) >= (2 * df.std())]
