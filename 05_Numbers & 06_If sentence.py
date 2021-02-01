a_float = 2.0
an_integer = 3
print(type(a_float))
print(type(an_integer))
sum_float = a_float + an_integer
print(type(sum_float))
div_float = sum_float / an_integer
print(div_float)
print(type(div_float))
div_ = sum_float // a_float
print(type(div_))
print(div_)

"""
The aim of this exercise is to write a program to convert a distance in Kilometres
#into a distance in miles.
#1. Take input from the user for a given distance in Kilometres. This can be done
#using the input() function.
#2. Convert the value returned by the input() function from a string into an
#integer using the int() function.
#3. Now convert this value into miles—this can be done by dividing the kilometres
#by 0.6214
#4. Print out a message telling the user what the kilometres are in miles.
"""
input_ok = False
while not input_ok:
    kilometres = input('Enter the # of Km you want to convert: ')
    if kilometres.isnumeric(): #Already checks if number is greater than 0 (It doesn´t work for negative numbers)
        kilometres = int(kilometres)
        input_ok = True

print(kilometres)
km_to_miles = kilometres / 0.6214
print('{0} km are {1} miles'.format(kilometres, km_to_miles))
"""
In this exercise you should return to the kilometres to miles converter you wrote in
the last chapter.
We will add several new tests to your program:
1. Modify your program such that it verify that the user has entered a positive
distance (i.e. they cannot enter a negative number).
2. Now modify your program to verify that the input is a number; if it is not a
number then do nothing; otherwise convert the distance to miles.
To check to see if a string contains only digits use the method isnumeric()
for example '42'.isnumeric(); which returns True if the string only con-
tains numbers. Note this method only works for positive integers; but this is suf-
ficient for this example.
"""