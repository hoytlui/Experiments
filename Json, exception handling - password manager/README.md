#### Notes:


- Json - read, write, update
  - Read data `json.load`
  ```
  with open('password.json', 'r') as password_file:
     password_dict = json.load(password_file)
  ```
  - Write new data `json.dump`
  ```
  with open('password.json', 'w') as password_file:
      json.dump(new_data_dict, password_file, indent=4)
  ```
  - Update data `json.update`
  ```
  password_dict.update(new_data_dict)
  ```

- Exception handling
  - Try... except... else... finally
  ```
  try:
      # try to read data
  except FileNotFoundError:
      # if file not found, write new data to create new file
  else:
      # if file found, continue to update data
      # save updated data
  finally:    
      # whether file found or not, clear entry field
  ```
