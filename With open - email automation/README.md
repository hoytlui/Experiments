#### Tricks explored in the email autmoation project

- Check current working directory
  - `print(os.getcwd())`

- Store names in list calling `readlines()`
  ```
  with open('./Input/invitees.txt', 'r') as name_file:
    name_list = name_file.readlines()
  ```
  
- Trim space
  - `name = name.strip()`
