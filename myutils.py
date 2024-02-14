# @desc   It supports data wrangling
# @author Magic Magg
# @date   Oct 30, 2023

# for infering dtype
from pandas.api.types import infer_dtype
from pandas import notnull
import pandas as pd
import os.path


'''
    detect mixed types in a dataframe
    @param df_ Dataframe
    @param col_ The column (number)
    @return the list of pairs: (row, dtype, value) if the list has only one element
            one dtype omnipresent, nan values are skipped

'''
def detect_mixed_values(df_, col_, ):
    if (len(df_.index) == 0):
        return
    
    output = []
    for i in range(0,len(df_.index)):        

        if notnull(df_.iloc[i, col_]):
            val = df_.iloc[i, col_]
            curr = infer_dtype( [ val ])
            if len(output) == 0:
                output.append((i,curr, val))
            elif output[-1][1] != curr:
                output.append((i, curr, val))
            
    return output

'''
    Print missing data
    @param df_ Data frame
    @param dig_prec_ How many precision digits
    @return pandas.core.frame.DataFrame with
            the nonull values ('s1'), and null values ('s2')
            and their sum
'''
def count_missing(df_, digi_prec_=2):
    s1 = df_.notnull().sum()
    s2 = df_.isnull().sum()
    
    d = pd.concat([s1, s2], axis=1).reset_index()    
    d['Total'] = d[0] + d[1]
    d.rename(columns={'index' : 'Attribute', 0: '#NotNull', 1:'#Missing'}, inplace=True)
    d['%Missing'] = round(d['#Missing']/d['Total']*100, digi_prec_)

    return d

'''
    It checks if the columns are only integers. It uses is_integer()
    The NA values are ignored.

    @param df_ Dataframe
    @param col_ the column that need to be checked
    @return [] if the column is an integer column
            [idx, val] the index and the value of the first observation that is
            not an integer
'''
def is_col_int(df_, col_):
    df = df_[df_[col_].notnull()]
    for idx in df.index:
        val = df.loc[idx][col_]
        if (not val.is_integer()):
            return [idx, val]
    return []

'''
    It checks if the columns are only integers. It uses modulo operation
    The NA values are ignored. It is assumed that the column is a numeric column.
    It is probably slower than using is_integer(), but tests show
    it might be faster. 

    @param df_ Dataframe
    @param col_ the column that need to be checked
    @return [] if the column is an integer column
            [idx, val] the index and the value of the first observation that is
            not an integer
'''
def is_col_int_modulo(df_, col_):
    df = df_[df_[col_].notnull()]
    for idx in df.index:
        val = df.loc[idx][col_]
        if (val % 1 != 0):
            return [idx, val]
    return []

'''
    Checks whether a list of columns contains only integer values
    @param df_ The frame
    @param cols_ The list of columns names to be checked
    @return [] - The list of columns that are integer columns
'''
def check_ints(df_, cols_):
    res = []
    for c in cols_:
        l = is_col_int(df_, c)
        if len(is_col_int(df_, c)) == 0:
            res.append(c)
    
    return res

'''
    Transforms a list of columns' names in a given dataframe to 
    integers

    @param df_ A dataframe
    @param cols_ A list of columns names
    @param type_ A type an integer type if not specified 'Int64' is assumed

    @return  A dataframe with changed types of the columns to an integer
'''
def transform_to_ints(df_, cols_, type_ = 'Int64'):
    for c in cols_:
        # this still have float64
        # df_[c] = pd.to_numeric(df_[c], downcast='integer', errors='coerce')
        df_[c] = df_[c].astype(type_)
    return df_

'''
    Check whether the dataframe contains duplicates

    @param df_ data frame to be checked
    @return series showing the duplicates
'''
def are_there_duplicates(df_):
    s = df_.duplicated()
    return s[s == True]

'''
    Write a dataframe to a csv file

    @param df_ dataframe
    @param fname_ the output file name
    @param compression_ The compression method as to pandas.to_csv()
    @return (success, str) boolean value for success or failure
                           str string for description
'''
def wrt_to_csv(df_, fname_, compression_='zip'):
    # get the name of the directory path without the name of the file
    head, tail = os.path.split (fname_)
    # indicates if there is an error
    success = False
    str = ""

    try:
        os.makedirs(head, exist_ok = True)
        # Directory head,  created successfully or existed )
        if os.path.isfile(fname_):
            str = f"WARN: File exists in location: {fname_}. No write ..."            
        else:
            df_.to_csv(fname_, index = False, compression=compression_)
            str = f"INFO: File written to {fname_}"
            success = True            
    
    except OSError as error:
        str = f"ERROR: Directory {head}  cannot be created ... File NOT written ... {fname_}"
    
    return (success, str)

'''
    Reads the csv to the dataframe file

    @param fname_ the file name to be read from
    @param print_info_ whether the print info should be displayed or not
    
    @return  dataframe
'''
def read_to_df(fname_, print_info_=True):
    # values in col 6 are formatted with comma separating thousands `1,049`
    # that is why I added thousands parameter
    # parse_dates argument fixes the warning for column 10 for dates.
    df = pd.read_csv(fname_, thousands=',', 
                        parse_dates= ['AppliedDate', 'IssuedDate', 'ExpiresDate', 'CompletedDate'], dtype={'OriginalZip' : 'object'}
                    )
    if print_info_:
        print(df.info())
        #print(f"After reading {fname_}:\n{df.head()}")
    
    return df