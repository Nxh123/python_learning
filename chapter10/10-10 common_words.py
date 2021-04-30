def count_word(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')
    else:
        print(
            f'The word "{word.rstrip()}" appears {contents.lower().count(word)} times.'
        )


file_name = 'test.txt'
word = 'the '
count_word(file_name, word)