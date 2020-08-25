"""
The project concerns validating a person’s Tax File Number (TFN). A TFN is a 9-digit
identification number issued to tax-payers by the Australian Taxation Office.
An example TFN is “123456782”.

Each digit of the TFN is multiplied by the weight for that digit and the results
are added together. e.g. For a TFN of “123456782”.

If the grand total is a multiple of 11 (i.e. it is evenly divisible by 11), the TFN is valid.
In this case, the grand total is 253 which is indeed a multiple of 11 and hence it is a valid TFN.
"""


def validate_tfn(tfn):
    # Force type conversion of parameter tfn to a string
    if type(tfn) != str:
        tfn = str(tfn)

    # Delete empty spaces from tfn parameter
    tfn = tfn.replace(' ', '')

    # Confirm the Tax File Number is the correct length, i.e. 9 digits
    if len(tfn) != 9:
        return False

    # Weight value for each digit in Tax File Number
    weights = (1, 4, 3, 7, 5, 8, 6, 9, 10)
    grand_total = [int(digit) * weight for digit, weight in zip(tfn, weights)]

    # If grand_total is multiple of 11 the TFN is valid
    return True if sum(grand_total) % 11 == 0 else False


# Testing the function
user_tfn = input('Enter your TFN: ')

if validate_tfn(user_tfn):
    print("The TFN is valid!")
else:
    print("The TFN is not valid.")
