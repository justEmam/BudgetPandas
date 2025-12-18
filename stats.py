def get_col_max(col:list):
    result = float('-inf')
    for element in col:
        try:
            if element == None:
                continue
            elif element > result:
                result = element
        except TypeError:
            print('Please enter a list of integers or floats (numeric)')
            return
    return(result)

    """
    Compute the maximum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The maximum value in the column (numeric type).
    """


def get_col_min(col:list):
    result = float('inf')
    for element in col:
        try:
            if element == None:
                continue
            elif element < result:
                result = element
        except TypeError:
            # print('Please enter a list of integers or floats (numeric)')
            return
    return(result)
    """
    Compute the minimum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The minimum value in the column (numeric type).
    """

def get_col_mean(col:list):
    sum = 0
    count = 0
    for element in col:
        try:
            if element == None:
                continue
            else:
                float(element)
                sum += element
                count += 1
        except ValueError:
            # print('Please enter a list of integers or floats (numeric)')
            return
    return(sum/count)
    
    """
    Compute the mean (average) value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The mean value of the column (float).
    """
    pass

def get_col_median(col:list):
    """
    Compute the median value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The median value of the column (numeric type).
    """
    result = 0
    cleanList = sorted([x for x in col if x is not None])    
    length = len(cleanList)
    for element in cleanList:
        try:
            float(element)
        except ValueError:
            # print('Please enter a list of integers or floats (numeric)')
            return
    
    if length % 2 == 0:
        element1 = cleanList[length//2]
        element2= cleanList[(length//2)-1]
        return((element1+element2)/2)
    else:
        return cleanList[length//2]
        

    
def get_col_mode(col:list):
    """
    Compute the mode (most frequent value) of a column.

    Args:
        col (list): A list of values. `None` values are ignored.

    Returns:
        The mode value of the column. If multiple values have the same
        frequency, the first encountered is returned.
    """
    result = 0
    max_freq = 0
    mymap = {}
    for element in col:
        if element is None:
            continue
        if element in mymap:
            mymap[element]+=1
        else:
            mymap[element]=1
        

    for value in mymap.values():
        if value > max_freq:
            max_freq = value
    
    for key,value in mymap.items():
        if value == max_freq:
            result = key
            break #first occurrence only in multimodal cases.
    
    return result


        
def get_stat(data:dict, dtypes:dict, function):
    """
    Apply a statistical function to all numerical columns in a dataset.

    Args:
        data (dict): Dictionary where keys are column names and values are lists of column values.
        dtypes (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        function (function): A function to apply to each numerical column (e.g., get_col_max, get_col_mean).

    Returns:
        dict: A dictionary where keys are column names and values are the result
        of applying the function to that column. Only numerical columns are processed.
    """
    result = {}
    for key in data:
        if dtypes[key] in ['int','float']:
            result[key] = function(data[key])
        # else:
        #     print(f"Unsupported Datatype for column {key}") 

    return result


# df = {"test":[1,2,3,4],
#       "anothertest": [5,6,7,9,'z']}
# print(get_stat(df,{"test":'int',"anothertest": 'str'},get_col_mean))



