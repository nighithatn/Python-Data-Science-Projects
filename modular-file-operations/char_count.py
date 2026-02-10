def count_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return len(text)

