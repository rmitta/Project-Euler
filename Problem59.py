#XOR Decryption

#The encryption key consists of three lower case characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
import string

def containsCommonEnglishWords(string):
    return ("the" in string) and ("be" in string) and ("to" in string) and ("of" in string) and ("and" in string) and ("that" in string)

def decode(cipher, keyCharacters):
    cipherLength = len(cipher)
    keyTryInts = [ord(char) for char in keyCharacters]
    keyTryIntsFull = [keyTryInts[i % 3] for i in range(cipherLength)]
    decodeTry = [c ^ k for (c, k) in zip(cipher,keyTryIntsFull,strict = True)]
    return decodeTry, "".join([chr(char) for char in decodeTry])


with open("Problem59_cipher.txt", "r") as f:
    cipher = f.read()

cipherList = [int(char) for char in cipher.split(",")]

lowercase = string.ascii_lowercase
for x in lowercase:
    for y in lowercase:
        for z in lowercase:
            decodeTry, decodeTryString = decode(cipherList, [x,y,z])

            if containsCommonEnglishWords(decodeTryString):
                print(decodeTryString)
                message = decodeTry

print(sum(message))
