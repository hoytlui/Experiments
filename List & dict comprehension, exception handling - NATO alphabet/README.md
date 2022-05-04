#### Notes:


- List comprehension
  - `[new_item for item in list]`

- Dictionary comprehension
  - `{new_key:new_value for (index, row) in df.iterrows()}`

- Exception handling
  - Try... except... else
  - Function iteration in `except` clause
  ```
  def generate_phonetic():
    .
    try:
        output_list = [nato_dict[char] for char in word]
    except KeyError:
        print('Enter letters only')
        generate_phonetic()
    else:
        print(output_list)
  ```
