import pandas as pd


# DATA CLEANING METHODS
def drop_duplicate_columns(df):
    df.drop(columns=['the_geom',
                     'spc_latin',
                     'problems',
                     'zip_city',
                     'borocode',
                     'boroname',
                     'cb_num',
                     'cncldist',
                     'st_assem',
                     'st_senate',
                     'nta',
                     'nta_name',
                     'boro_ct',
                     'state',
                     'x_sp',
                     'y_sp',
                     'address'],
            inplace=True)


def combine_columns_treedbh_stumpdiam(df):
    tree_dbh = df['tree_dbh']
    stump_diam = df['stump_diam']
    diam = tree_dbh + stump_diam
    df.drop(columns=['tree_dbh', 'stump_diam'], inplace=True)
    df['diam'] = diam


def strip_strings_in_whole_dataset(df):
    for column in df.columns:
        try:
            df[column] = df[column].str.strip()
        except:
            continue


def strings_to_lower_in_whole_dataset(df):
    for column in df.columns:
        try:
            df[column] = df[column].str.lower()
        except:
            continue


def convert_created_at_to_datetime(df, column):
    df[column] = pd.to_datetime(df[column])
    # df[column] = df[column].dt.strftime('%m/%d/%Y')


def convert_binary_string_columns_to_int(df):
    # dtype is automatically changes from object to int64
    for column in df.columns:
        if df[column].dtype == object:
            if len(df[column].unique()) in [2, 3]:  # take into account nan as a third unique value
                # sidewalk
                if 'nodamage' in df[column].unique():
                    df[column] = df[column].replace('nodamage', 0)
                df[column] = df[column].replace('damage', 1)

                # curb_loc
                df[column] = df[column].replace('oncurb', 1)
                df[column] = df[column].replace('offsetfromcurb', 0)

    take_measures_for_nan_in_sidewalk(df)


def take_measures_for_nan_in_sidewalk(df):
    df['sidewalk'].fillna(-1, inplace=True)
    df['sidewalk'] = df.sidewalk.astype(int)


def convert_binary_string_columns_to_bool(df):
    for column in df.columns:
        if df[column].dtype == object:
            if len(df[column].unique()) in [2, 3]:  # take into account nan as a third unique value
                # problem columns
                df[column] = df[column].replace('yes', True)
                df[column] = df[column].replace('no', False)


def convert_steward_to_string_of_numbers(df):
    # still a string, a bit easier to extract
    df.steward = df.steward.replace('none', '0')
    df.steward = df.steward.replace('1or2', '1, 2')
    df.steward = df.steward.replace('3or4', '>=3')  # overlapping
    df.steward = df.steward.replace('4ormore', '>=3')  # overlapping


def fill_nan_health_alive_tree(df):
    condition_one = (df.status == 'alive')
    condition_two = (df.health.isnull())
    index_to_change = df[condition_one & condition_two].index
    df.loc[index_to_change, 'health'] = 'unknown'


# METHODS TO GET TO KNOW THE DATAFRAME
def print_dataset_basics(df):
    print(df)
    print(df)
    print(df.head())
    print(df.describe())
    print(df.dtypes)
    df.info()


def print_check_duplicates(df):
    print('Check whole dataframe for duplicates\n'
          '####################################')
    print(df.duplicated().value_counts())


def print_valuecounts_whole_dataset(df):
    print('Value counts for all columns\n'
          '############################')
    for column in df.columns:
        print('COLUMN', column)
        print('how many unique values:', len(df[column].unique()))
        print(df[column].value_counts())


def print_check_nulls(df):
    print('Total missing data:', end=' ')
    print(df.isnull().sum().sum())
    print('Missing values per column:')
    print(df.isnull().sum())


def print_check_unique_values(df):
    for column in df.columns:
        print('UNIQUE VALUES IN:', column)
        print(df[column].unique())
