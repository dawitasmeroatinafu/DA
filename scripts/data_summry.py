import pandas as pd
import numpy as np
class summery:

    def summ_columns(self, df, unique=True):
        """
        shows columns and their missing values along with data types.
        """
        df1 = df.isna().sum().to_frame().reset_index()
        df1.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df1['missing_percent_(%)'] = round(df1['missing_count']*100/df.shape[0])
        data_type_lis = df.dtypes.to_frame().reset_index()
        df1['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df1.shape[0]):
                unique_val.append(len(pd.unique(df[df1.iloc[i,0]])))
            df1['unique_values'] = pd.Series(unique_val)
        return df1