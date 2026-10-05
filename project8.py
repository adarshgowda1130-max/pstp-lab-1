# 8 word occurance counter
sentence=input("enter a sentence:")
word=input("enter the word which you need to count:").lower
list_words=sentence.split()
c=0
for words in list_words:
    if word==words:
        c+=1
print(f"{word} repeates {c} times")
