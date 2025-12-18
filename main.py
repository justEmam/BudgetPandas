from dataframe import *
def main():
    df1 = DataFrame.read_csv(data_path = 'data/titanic.csv', dtype_path = 'data/titanic_dtype.csv')
    # TODO: Read data

    # TODO: Fill missing values
    # Numeric columns → mean
    # Categorical columns → mode
    df1.fillna(num_strategy=get_col_mean,cat_strategy=get_col_mode)



    # TODO:Generate statistics file
    df1.describe('describertest.csv')


    # TODO:Write cleaned data to CSV
    df1.to_csv('testtyfinal.csv')




if __name__ == "__main__":
    main()
