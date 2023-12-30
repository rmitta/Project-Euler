#In this problem I used chatGPT to generate all parts of the solution to test it's capabilities.
#I was quite impressed with what it can do. 

file_path = 'Problem22_names.txt'

with open(file_path, 'r') as file:
    file_contents = file.read()

names : list = [name for name in file_contents.split('"') if name.isupper()]

names.sort()

def alphabetical_value(s):

    alphabet_mapping = {letter: ord(letter) - ord('A') + 1 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    value = sum(alphabet_mapping[letter] for letter in s if letter in alphabet_mapping)

    return value

def calculate_positions_times_f(strings):
    result = [i * alphabetical_value(s) for i, s in enumerate(strings, start=1)]
    return result

print(sum(calculate_positions_times_f(names)))
