#Yocheved Glazer
#This is on a github repo that is public and therefore can be viewed by anyone
#accepts a digit and returns the corresponding text number
def digit_to_text_number(digit):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if digit == 0:
        return ones[digit]
    elif 1 <= digit <= 9:
        return ones[digit]
    elif 11 <= digit <= 19:
        return teens[digit - 11]
    elif digit % 10 == 0:
        return tens[digit // 10 - 1]
    else:
        return tens[digit // 10 - 1] + ' ' + ones[digit % 10]

#splits the string and calls the other method to swap the digit representation
def replace_digits_with_text_number(input_string):
    words = input_string.split()
    result = []

    for word in words:
        if word.isdigit():
            result.append(digit_to_text_number(int(word)))
        else:
            result.append(word)

    return ' '.join(result)

# Get user input
user_input = input("Enter a string: ")

# replace digits with text numbers and print the result
output = replace_digits_with_text_number(user_input)
print("Output:", output)




