

from scripts.data_summry import Summery
class Cleaner: 

    def __init__(self) -> None:
        self.summar = Summery() 

    def fill_missing_by_mode(self, df, cols=None):
        """
        fills missing values by mode
        """
        mod_fill_list = []
        if(cols == None):
            temp = self.summar.summ_columns(df)
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "object"):
                    mod_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                mod_fill_list.append(col)

        for col in mod_fill_list:
            df[col] = df[col].fillna(df[col].mode()[0])

        return df


    def fill_missing_by_mean(self, df, cols=None):
        """
        fills missing values by mean
        """
        temp = self.summar.summ_columns(df)
        mean_fill_list = []

        if cols is None:
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "float64"):
                    mean_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                mean_fill_list.append(col)

        for col in mean_fill_list:
            df[col] = df[col].fillna(df[col].median())

        return df

    def fill_missing_by_median(self, df, cols=None):
        """
        fills missing values by median.
        """
        temp = self.summar.summ_columns(df)
        median_fill_list = []

        if cols is None:
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "float64"):
                    median_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                median_fill_list.append(col)

        for col in median_fill_list:
            df[col] = df[col].fillna(df[col].median())
        return df


    def fill_missing_forward(self, df, cols):
        """
        fills missing values by value from next rows
        """
        for col in cols:
            df[col] = df[col].fillna(method='ffill')
        return df

    def fill_missing_backward(self, df, cols):
        """
        fills missing values by value from previous rows
        """
        for col in cols:
            df[col] = df[col].fillna(method='bfill')
        return df
