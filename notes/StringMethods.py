# NS 1st Strings Mathods Notes

#subject = "Computer Programming 1 !"

#print(subject.upper())

#print(subject.center(100))

# Stupid/idiot Proofing inputs
#color = input("What is your favorite color?").strip().capitalize()
# lower() => all lower case
# upper() => all upper case
# capitalize => capitalize first letter of first word
# title() => capitalizes the first letter of every word
#full_name = input("What is your full name?").strip().title()
#print("That is cool "+ full_name + ". I Like " + color + " too!")
#print("That is cool {full_name} . I Like {color} too!" .format(full_name=full_name, color=color))

#f-strings 
#print(f"That is cool {full_name}. I like {color} too!")

pi = "3.14159"           
#print(f"We all know pi is equal to {pi:. 3f})                                                                                                                                                                                                                                                                                           
#print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog."
word = "jumps"
print(sentence.find(word))
start = sentence.index(word)
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)