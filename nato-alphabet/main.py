import pandas

student_dict = {
    "student": ["Abid", "Maryam", "Ayah"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_list = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        word = input('Enter a word: ').upper()
        letter_list = [w for w in word]
        nato_phonetic = [word for w in word for (letter, word) in phonetic_list.items() if w in letter]
        print(f"Harder way of doing it: {nato_phonetic}")

        nato_phonetic = [phonetic_list[letter] for letter in word]
        print(f"Easier way of doing it: {nato_phonetic}")
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")