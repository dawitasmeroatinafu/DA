import numpy as np
def fill_outliers_mean(self, df, cols):
        df_temp = df.copy(deep=True)
        for col in cols:
            ''' Detection '''
            # IQR
            Q1 = df_temp[col].quantile(0.25)

            Q3 = df_temp[col].quantile(0.75)
            IQR = Q3 - Q1

            length=df_temp.shape[0]
            for index in range(length):
                if(df_temp.loc[index,col] >= (Q3+1.5*IQR)):
                    df_temp.loc[index,col] = np.nan

            ''' filling the Outliers '''
            df_temp = self.fill_missing_by_median(df_temp, cols)

        return df_temp
def removeOutliers(self, df,cols):
        df_temp = df.copy(deep=True)
        for col in cols:
            ''' Detection '''
            # IQR
            Q1 = df_temp[col].quantile(0.25)

            Q3 = df_temp[col].quantile(0.75)
            IQR = Q3 - Q1
            rm_lis = []
            length=df_temp.shape[0]
            for index in range(length):
                if(df_temp.loc[index,col] >= (Q3+1.5*IQR)):
                    rm_lis.append(index)

            ''' Removing the Outliers '''
            df_temp.drop(rm_lis, inplace = True)

        return df_temp
