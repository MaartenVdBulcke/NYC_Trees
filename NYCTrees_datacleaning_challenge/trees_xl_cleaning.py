
from trees_cleaning_functions import *


path = 'data_222222.csv'
trees_xl_dataset = pd.read_csv(path)

# column manipulation
drop_duplicate_columns(trees_xl_dataset)
combine_columns_treedbh_stumpdiam(trees_xl_dataset)

# string consolidation
strip_strings_in_whole_dataset(trees_xl_dataset)
strings_to_lower_in_whole_dataset(trees_xl_dataset)

# dtypes conversion
convert_created_at_to_datetime(trees_xl_dataset, 'created_at')
convert_binary_string_columns_to_int(trees_xl_dataset)
convert_binary_string_columns_to_bool(trees_xl_dataset)
convert_steward_to_string_of_numbers(trees_xl_dataset)

# fix nan for column health for one alive tree
fill_nan_health_alive_tree(trees_xl_dataset)

trees_xl_dataset.to_csv('trees_cleaned_xl.csv', index=False)
