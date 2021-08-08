def reverse(string):
    # initialising an empty list
    rev = ''
    # iterating over the entire string character by character
    # in reverse order
    for i in range(len(string) - 1, -1, -1):
        # adding characters from the end in the empty list
        rev += string[i]
    # could also be done simply with : return string[::-1]
    return rev


def countWords(string):
    # splitting the string around whitespaces
    words = string.split()
    # returning the number of words obtained by splitting
    return len(words)


def count(string):
    # variable initializations
    vowels = 0
    consonants = 0
    special = 0
    # iterating over the entire string character by character
    for letter in string:
        # checking if the character is an alphabet
        if letter.isalpha():
            # checking for vowel
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                vowels += 1
            # since its not a vowel so its a consonant
            else:
                consonants += 1
            # if is not a digit its a special character
        elif not(letter.isdigit()):
            special += 1

    # print the corresponding results
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Special Characters: {special}")


def reverseWords(string):
    # splitting the string around whitespaces
    words = string.split()
    # iterating over the entire string character by character
    # through the control variable i
    for i in range(len(words)):
        # taking the reverse of each word and replacing it with
        # previous value
        words[i] = words[i][::-1]
    # joining the list of strings around whitespaces
    return " ".join(words)


def largestWord(string):
    # splitting the string around whitespaces
    words = string.split()
    # taking the length of the words by list comprehension
    # in a list
    lengths = [len(x) for x in words]
    # getting the index of max length
    index = lengths.index(max(lengths))
    # returning the word stored at the index of max length
    return words[index]


string = input("Enter a String: ")
print("Enter What you Wanna Do")
print("1. Reverse of the String")
print("2. Count Words in the String")
print("3. Count Vowels, Consonants, and Special Characters in the String")
print("4. Reverse the words of the String")
print("5. Find the largest Word in the String")
option = input("Your Choice: ")
if option == '1':
    print(f"Reverse of the String: {reverse(string)}")
elif option == '2':
    print(f"Words: {countWords(string)}")
elif option == '3':
    count(string)
elif option == '4':
    print(f"String After Reversing Words: {reverseWords(string)}")
elif option == '5':
    print(f"Largest Word: {largestWord(string)}")
else:
    print("Invalid Option!")
