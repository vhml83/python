# =======================================================================================================
# Write a function that receives a list and returns a tupple with the first and last elements of the list.
# Throws an exception when:
#  - Parameter is not a list
#  - List has less than 2 elements
# =======================================================================================================

def first_and_last(list):
    if list: 
        if len(list) >= 2:
            return (list[0], list[-1])    
        raise ValueError('List must have two or more items.')
    raise ValueError('Parameter is not a list.')

# CP1: List with many elements.
list1 = [1, 2, 3, 4, 5]
print('\nCP1:', first_and_last(list1))

# CP2: List with 2 elements.
list2 = [1, 2]
print('CP2:', first_and_last(list2))

# CP3: List with only 1 element.
list3 = [0]
try:
    print('CP3:', first_and_last(list3))
except Exception as error:
    print('CP3:', error)

# CP4: Not a list.
list4 = None
try:
    print('CP4:', first_and_last(list4))
except Exception as error:
    print('CP4:', error)

# =======================================================================================================
# Write a function that opens & reads a text file.
# Returns a list with the contents from the text file.
# Throws an exception if it is unable to open the file.
# =======================================================================================================

def create_list(file_name):
    try:
        result = []
        with open(file_name, 'r') as file:
            for data in file:
                result.append(data.strip()) #removes break line
            return result
    except FileNotFoundError:
        raise FileNotFoundError("File couldn't be oppened.".upper())
    
# CP5: File name with valid values.
writers = "others\writers.txt"
list5 = create_list(writers)
print('\nCP5:', list5)

# =======================================================================================================
# Write a function that receives a list.
# Returns total number of positive numbers.
# Throws an exception if the received parameter is not a list.
# =======================================================================================================

def count_positive(list):
    if list:
        positives = 0
        for number in list:
            if  type(number) != str:
                if number > 0:
                    positives += 1
            continue
        return positives
    raise ValueError('Data error: parameter is not a list!')

# CP6: a list of integers
list6 = [405,-107,210,5,-23,-45,87]
print('CP6: Total positive numbers:', count_positive(list6))

# CP7: a list of with negative numbers
list7 = [-35.61,-10.17,-15.99,-8.5]
print('CP7: Total positive numbers:', count_positive(list7))

# CP8: a list of with strings
list8 = ['Costa Rica', 'Colombia', 'Canada', 'Chile']
print('CP8: Total positive numbers:', count_positive(list8))

# CP9: not a list
list9 = None
try:
    print('CP9: Total positive numbers:', count_positive(list9))
except ValueError as error:
    print('CP9:', error)

# CP10: a list with numbers and strings
list10 = [405,-107,'Costa Rica',210,'Colombia',5,-23,'Chile',-45,87,'Canada']
print('CP10: Total positive numbers:', count_positive(list10))

# =======================================================================================================
# Write a function that receives two lists (only numbers).
# Returns 'TRUE' if both lists are the same size AND the first element of List 1 is a multiple of 
# the first element of List 2, second element of List 1 is a multiple of the second element of List 2, 
# and so on. 
# Returns 'false' if one of the conditions is not met.
# =======================================================================================================
def determine_multiples(list1, list2):
    if len(list1) == len(list2):
        limit = len(list1)
        index = 0
        while index < limit and list1[index] % list2[index] == 0:
            index += 1
        answer = index == limit
    else:
        answer = False
    return answer

# CP11: Two lists that match the conditions
list11 = [9, 16, 15, 8, 21]
list12 = [3, 2, 5 , 8, 7]

if determine_multiples(list11, list12):
    print('CP11: Conditions are met.')
else:
    print('CP11: Conditions are not met.')

# CP12: Two lists with different size.
list13 = [3, 2, 5, 8]

if determine_multiples(list11, list13):
    print('CP12: Conditions are met.')
else:
    print('CP12: Conditions are not met.')

# CP13: Two lists with same size, but not all numbers are multiples.
list14 = [4, 2, 5, 8, 7]

if determine_multiples(list11, list14):
    print('CP13: Conditions are met.')
else:
    print('CP13: Conditions are not met.')

# =======================================================================================================
# Function 2: Receives a list (only numbers) and a positive integer number 'n'. Returns the average of 
# the numbers that occupy multiples of 'n'.
# Throws an exception if the received parameters are not lists.
# =======================================================================================================
def calculate_average(list, n):
    sum = 0
    counter = 0
    for i, element in enumerate(list):
        if i % n == 0:
            sum += element
            counter += 1
    try:
         average = sum / counter
         return  average
    except:
        raise ArithmeticError('Average number cannot be calculated.')

# CP14: a list with integer numbers.
list15 = [11, -20, -7, 45, 10, -16, 14, 17]
average1 = calculate_average(list15, 2)
print('CP14 -> Average =', average1)

# CP15: a list with real numbers.
list16 = [3.5, -2.8, 2.4, 1.5, -2.3, -3.1, -4.5, 5.2, 3.8, 6.0]
average2 = calculate_average(list16, 3)
print('CP15 -> Average =', average2)

# CP16: an empty list.
list17 = []
average3 = calculate_average(list17, 3)
print('CP16 -> Average =', average3)