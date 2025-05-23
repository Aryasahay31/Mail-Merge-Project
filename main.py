#TODO: Create a letter using starting_letter.txt
with open ("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
# therefore, readlines() function helps us to convert the contents in the txt file into a list

#TODO: for each name in invited_names.txt, Replace the [name] placeholder with the actual name. Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open ("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode= "w") as completed_letter:
            completed_letter.write(new_letter)

    #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp