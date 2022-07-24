def find_anagram(word, anagram):
    word_list = list(word)
    anagram_list = list(anagram)
    if len(word_list)!= len(anagram_list):
        return False
    word = sorted(word)
    anagram = sorted(anagram)
    if word == anagram:
        return True

    else:
       return False

word = input("Input the first word:").lower()
anagram = input("Input the second word:").lower()
print(find_anagram(word, anagram))

