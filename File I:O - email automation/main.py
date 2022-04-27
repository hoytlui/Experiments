import os

# check current working directory
print(os.getcwd())

# store names in list
with open('./Input/invitees.txt', 'r') as name_file:
    name_list = name_file.readlines()

# automate new letters on letter template
with open('./Input/letter_template.txt', 'r') as letter_file:
    letter_content = letter_file.read()
    for name in name_list:
        # trim space
        name = name.strip()
        new_letter_content = letter_content.replace('[name]', name)
        with open(f'./Output/letter_for_{name}.txt', 'w') as output_file:
            output_file.write(new_letter_content)