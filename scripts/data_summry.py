def summ_columns(self, df, unique=True):
    """
    shows columns and their missing values along with data types.
    """
    df2 = df.isna().sum().to_frame().reset_index()
    df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
    df2['missing_percent_(%)'] = round(df2['missing_count']*100/df.shape[0])
    data_type_lis = df.dtypes.to_frame().reset_index()
    df2['data_type'] = data_type_lis.iloc[:,1]
    
    if(unique):
        unique_val = []
        for i in range(df2.shape[0]):
            unique_val.append(len(pd.unique(df[df2.iloc[i,0]])))
        df2['unique_values'] = pd.Series(unique_val)
    return df2