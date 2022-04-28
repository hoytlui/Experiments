import pandas as pd


# open file
nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
print(nato_df)

# create dict using dict comprehension
# {new_key:new_value for (index, row) in df.iterrows()}
nato_dict = {row['letter']:row['code'] for (idx, row) in nato_df.iterrows()}
print(nato_dict)

# prompt user for word
word = input("Enter a word: ").upper()

# output the associated nato alphabet using list comprehension
# [new_item for item in list]
output_list = [nato_dict[char] for char in word]
print(output_list)