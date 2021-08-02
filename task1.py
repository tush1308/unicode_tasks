n=input()                            #inputting no. of lines "n"
num = int(n)                         
counter_dict = {}
words_list = []
for i in range(num):
  word = input()                    #inputting "n" lines each containing a word
  words_list.append(word)
  if word in counter_dict:
    counter_dict[word] += 1
  else:
    counter_dict[word] = 1

l=len(counter_dict)
print(len(counter_dict))
print(' '.join([str(counter_dict[word]) for word in counter_dict]))

# Bonus
sort_dict=sorted(counter_dict.items(),key=lambda x: x[1],reverse=True)    #Arranging each distinct word in the inout in decreasing order of their no. ofappearances
a=dict(sort_dict)     
for b in a:           #printing each distinct word in the inout according to their occurences in descending order
  print(b)
print("The most repeated word is: ",sort_dict[0][0])
print("The least repeated word is:",sort_dict[l-1][0])