from file_handler import *
from stats import *

class DataFrame:
    def __init__(self, data:dict, dtype:dict):
        self.data = data
        self.dtypes = dtype

    @classmethod
    def read_csv(cls,data_path,dtype_path):  #define read_csv(data_path, dtype_path)
        dtypes = read_dtype(dtype_path)
        data = read_csv_file(data_path,dtypes)
        return cls(data,dtypes)
    
    
    #TODO: define count_nulls()
    def count_nulls(self):
        NoneDict = {}
        for columnName in self.dtypes:
            NoneDict[columnName] = 0

        for key in self.data:
            for element in self.data[key]:
                if element is None:
                    NoneDict[key]+=1


        # for key,value in NoneDict.items():
        #    print(f"**{key}** Number of Nones: {value}")
        
        return NoneDict



    
    #TODO: define describe()
    def describe(self,path='data/describe.csv'):
            min = get_stat(self.data, self.dtypes, get_col_min)
            max = get_stat(self.data, self.dtypes, get_col_max)
            mean = get_stat(self.data, self.dtypes, get_col_mean)
            median = get_stat(self.data, self.dtypes, get_col_median)
            mode = get_stat(self.data, self.dtypes, get_col_mode)
            nulls = self.count_nulls()

            headers = ["column", "nulls", "max", "min", "mean", "median", "mode"]
            with open(path, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(headers)

                for col in self.data.keys():
                    writer.writerow([
                        col,
                        nulls.get(col, ""),
                        max.get(col, ""),
                        min.get(col, ""),
                        mean.get(col, ""),
                        median.get(col, ""),
                        mode.get(col, "")
                    ])




        
    #TODO: define fillna()
    def fillna(self,num_strategy, cat_strategy):
        if num_strategy == get_col_mean:
            for key,value in self.data.items():
                for i,record in enumerate(value):
                    if record is None:
                        self.data[key][i] = get_col_mean(self.data[key])

            
        if num_strategy == get_col_median:
            for key,value in self.data.items():
                for i,record in enumerate(value):
                    if record is None:
                        self.data[key][i] = get_col_median(self.data[key])
            
        if cat_strategy == get_col_mode:
            for key,value in self.data.items():
                for i,record in enumerate(value):
                    if record is None:
                        self.data[key][i] = get_col_mode(self.data[key])


        
    #TODO: define to_csv()
    def to_csv(self,path='data/out.csv'):
        write_file(path,self.data)


                       
    
    
    
