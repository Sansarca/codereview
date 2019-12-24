text = str(input('Введіть рядок:'))
list = []
text =text.split(" ")
for word in text:
      if (i.isupper() for i in word):
          list.append(word)
print(list)
