import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class Summery:
    def _init(self) -> None:
       pass
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
    def show_col_distribution(self, df, cols, colors):
        for index in range(len(cols)):
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(8,6))
            sns.displot(data=df, x=cols[index], color=colors[index], kde=True, height=4, aspect=2)
            plt.title(f'Distribution of'+cols[index]+ 'data volume', size=20, footweight='bold')
            plt.show

            
    