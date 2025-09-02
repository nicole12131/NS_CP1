# NS 1st Strings Notes



#string examples 
sentence = "The quick brown fox jumps over the lazy dog!"

first_name = "Nicole"
month = "September"
book = "The Return of the King"
food = "chocolate"

print(month)
#get length of string
length = len(sentence)
print(len(sentence))


print('"Inkheart" is the best book ever!')
print("'Inkheart' is the best book ever!")
#escape characters 
print("\"Inkheart\" is the best book ever!")


#concatnate
last_name = "Salom"
full_name = first_name + " " + last_name

print(full_name)

#index
print(last_name[ :2])
print(last_name[2:-2])
print(sentence[10:15])