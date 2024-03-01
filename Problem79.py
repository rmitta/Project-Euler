#Passcode Derivation

#See Project Euler for Details

with open("Problem79_keylog.txt", "r") as f:
    keylog = f.read()

print(keylog)

logins = keylog.strip('\n').split("\n")


possible_digits = [] 
for i in range(10):
    if str(i) in keylog:
        possible_digits.append(str(i))

#Maybe we can start by easily checking if any number only ever appears in the first or last slot?

def never_not_first_digit(n : str, l : list[str]):
    for string in l:
        if n in string[1:]:
            return False
    return True

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)

#We find that 7 is never not the first digit. This means we can assign 7 as the first digit of the password
# and remove it from our working set.

for i in range(len(logins)):
    if logins[i][0] == "7":
        logins[i] = logins[i][1:]
        
possible_digits.remove('7')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)
        
#Then we find that 3 is never not the first digit. We can repeat the process. 

for i in range(len(logins)):
    if logins[i][0] == "3":
        logins[i] = logins[i][1:]
        
possible_digits.remove('3')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)

#Then we find that 1 is never not the first digit. Repeat again.

for i in range(len(logins)):
    if logins[i][0] == "1":
        logins[i] = logins[i][1:]
        
possible_digits.remove('1')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)
        
#Then 6

for i in range(len(logins)):
    if logins[i]: #? Note that we now have to account for the fact some logins are empty. 
        if logins[i][0] == "6":
            logins[i] = logins[i][1:]
        
possible_digits.remove('6')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)

#Then 2

for i in range(len(logins)):
    if logins[i]:
        if logins[i][0] == "2":
            logins[i] = logins[i][1:]
        
possible_digits.remove('2')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)

#Then 8


for i in range(len(logins)):
    if logins[i]:
        if logins[i][0] == "8":
            logins[i] = logins[i][1:]
        
possible_digits.remove('8')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)

#Then 9

for i in range(len(logins)):
    if logins[i]:
        if logins[i][0] == "9":
            logins[i] = logins[i][1:]
        
possible_digits.remove('9')

for i in possible_digits:
    if never_not_first_digit(i, logins):
        print(i)

#Then 0

#So the smallest possible is 73162890