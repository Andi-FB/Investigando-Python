#STRINGS
#1 Create a string with words separated by ',' and replace the commas with spaces;
#for example replace all the commas in 'Denyse,Marie,Smith,21,London,UK'
#with spaces. Now print out the resulting string.
string_to_be_replaced = 'Denyse,Marie,Smith,21,London,UK'
replaced_string = string_to_be_replaced.replace(',', ' ')
print('The replaced string is: ', replaced_string)


#Handle user input
#The aim of this exercise is to write a program to ask the user for two strings and
#concatenate them together, with a space between them and store them into a new
#variable called new_string.
#Next:
#• Print out the value of new_string.
#• Print out how long the contents of new_string is.
#• Now convert the contents of new_string to all upper case.
#• Now check to see if new_string contains the string 'Albus' as a substring.
print('-' * 20)
first_string = input('This is the first word: ')
second_string = input('This is the second word: ')
new_string = first_string + " " + second_string
print(new_string)
print('The length of the new string is: ', str(len(new_string)))
print('To UPPER: ', new_string.upper())
print('Contains Albus? ', new_string.__contains__('Albus'))

