import csv

def read_csv_file(file_path, dtypes:dict):

    """
    Read a CSV file and convert each column to the specified data type.

    Args:
        file_path (str): Path to the CSV data file.
        dtypes (dict): Dictionary mapping column names to data types ('int', 'float', 'string').

    Returns:
        dict: A dictionary where keys are column names and values are lists of column values.
              Missing values (empty strings) are replaced with None.
    
    """
    result = {}
    with open(file_path, mode='r') as csvfile:
         reader = csv.DictReader(csvfile)
         for key in dtypes:
             result[key] = []
         for row in reader:
            for key,value in row.items():
                 if dtypes[key] == 'int':
                    if value == '':
                         result[key].append(None)
                    else:
                         result[key].append(int(value))


                 elif dtypes[key] == 'string':
                     if value == '':
                         result[key].append(None)
                     else:
                         result[key].append(str(value))

                    
                 elif dtypes[key] == 'float':
                     if value == '':
                         result[key].append(None)
                     else:
                         result[key].append(float(value))
    
    return(result)


def read_dtype(file_path):
        """
    Read a CSV file containing column names and their data types.

    Args:
        file_path (str): Path to the CSV file containing column names and types.

    Returns:
        dict: A dictionary where keys are column names and values are data types ('int', 'float', 'string').
    """
        
        result = {}
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                col_name = row["column"]
                result[col_name] = row["dtype"].lower()

        return result
                            
                            
def write_file(file_path, data:dict):
    """
    Write a data dictionary to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (dict): Dictionary where keys are column names and values are lists of column values.

    Returns:
        None
    """
    columns = list(data.keys())
    num_rows = len(data[columns[0]])  # assume all columns have the same length

    with open(file_path, mode='w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for i in range(num_rows):
            row = {}
            for col in columns:
                row[col] = data[col][i]
            writer.writerow(row)
    


df = (read_csv_file('data/titanic.csv',read_dtype('data/titanic_dtype.csv')))
# write_file('test.csv',df)