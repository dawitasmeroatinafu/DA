class Format:
    def format_number(self, df, cols):
        """
        format floating number variables
        """
        float_format_list = []

        for col in cols:
            float_format_list.append(col)
        for col in float_format_list:
            df[col] = df.apply(lambda row : f'{row[col]:,.2f}', axis = 1)

        return df


    def byte_to_mb(self, df, identifier):
        """
        converting byte to megabyte.
        """
        bytes_list = []
        megabyte = 1*10e+5
        temp = self.summar.summ_columns(df)
        
        for i in range(temp.shape[0]):
            if(identifier in temp.iloc[i,0]):
                bytes_list.append(temp.iloc[i,0])
        
        for col in bytes_list:
            df[col] = df[col]/megabyte
            df.rename(columns={col:col.replace(identifier,'(MB)')}, inplace=True)
        return df



    def ms_to_s(self, df, identifier):
        """
        converting ms to s.
        """
        ms_list = []
        second = 1000
        temp = self.summar.summ_columns(df)
        
        for i in range(temp.shape[0]):
            if(identifier in temp.iloc[i,0]):
                ms_list.append(temp.iloc[i,0])
        
        for col in ms_list:
            df[col] = df[col]/second
            df.rename(columns={col:col.replace(identifier,'(S)')}, inplace=True)
        return df