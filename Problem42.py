#Coded Triangle Numbers

#See Project Euler for Question.

def char_to_num(char):
    return ord(char.lower()) - ord('a') + 1

def word_value(word):
    return sum(char_to_num(char) for char in word)

def triangle_numbers_upto(max_value : int):
    n = 1
    tn = 1
    yield 1
    while tn < max_value:
        n += 1
        tn += n
        yield tn
           
def main():
    with open('Problem42_words.txt', 'r') as f:
        words = f.read().strip('"').split('","')
    
    #We check what the highest value word in words.txt is
    highest_value_word = max(words, key=word_value)
    max_value = word_value(highest_value_word)
    
    #Get the set of all triangle numbers up to max_value
    triangle_numbers = set(triangle_numbers_upto(max_value))
    
    total_triangle_words = 0
    for word in words:
        if word_value(word) in triangle_numbers:
            total_triangle_words += 1
    
    print(total_triangle_words)
    
if __name__ == "__main__":
    main()