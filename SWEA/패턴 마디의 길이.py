string=input()

for i in range(1,len(string)+1):
    if string[:i]==string[i:i+i]:
        word=string[:i]
        print(word)
        break

print(len(word))