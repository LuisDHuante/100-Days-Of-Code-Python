import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")


#Or phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
nato_dict = dict(zip(df.letter, df.code))





#Or nato_dict.get(letter)
def nato_coding():
    try:
        word_to_cypher = input("Enter a word to encode: ").upper()
        code_words_list = [nato_dict[letter] for letter in word_to_cypher]
    except KeyError:
        print("You can only enter letters. ")
        nato_coding()
    else:
        print(code_words_list)


nato_coding()