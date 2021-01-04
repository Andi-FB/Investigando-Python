#The aim of this exercise is to write a program to convert a distance in Kilometres
#into a distance in miles.
#1. Take input from the user for a given distance in Kilometres. This can be done
#using the input() function.
#2. Convert the value returned by the input() function from a string into an
#integer using the int() function.
#3. Now convert this value into miles—this can be done by dividing the kilometres
#by 0.6214
#4. Print out a message telling the user what the kilometres are in miles.

kilometres = int(input('Enter the # of Km you want to convert: '))
print(kilometres)
km_to_miles = kilometres / 0.6214
print('{0} km are {1} miles'.format(kilometres, km_to_miles))
