NAME_PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    with open("./Input/Names/invited_names.txt") as names:
        name_content = names.readlines()
        for name in name_content:
            stripped_name = name.strip()
            changed_name = letter_content.replace(NAME_PLACEHOLDER, stripped_name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
                final_letter.write(changed_name)
