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
    # Force conversion to string and delete any empty spaces
    tfn = str(tfn).replace(' ','')

    if len(tfn) != 9:
        return False

    # Weights given to digits do not change
    weights = (1, 4, 3, 7, 5, 8, 6, 9, 10)
    grand_total = []
    for i in range(len(tfn)):
        x = int(tfn[i]) * weights[i]
        grand_total.append(x)
    # Or with more Pythonic list comprehension
    # grand_total = [int(tfn[i]) * weights[i] for i in range(len(tfn))]

    return True if sum(grand_total) % 11 == 0 else False


# Testing the function
# user_tfn = input('Enter your TFN: ')
#
# if validate_tfn(user_tfn):
#     print("The TFN is valid!")
# else:
#     print("The TFN is not valid.")

# Find the lowest 10 valid TFNs
MIN_TFN = 100000000
MAX_TFN = 999999999

l = [] # Holds the valid TFNs
for i in range(MIN_TFN, MAX_TFN):
    if len(l) < 10:
        if validate_tfn(i):
            print(f'[+] Found valid TFN -> {i}')
            l.append(i)

# Find the highest 10 valid TFNs
# Uncomment the code below to find the highest TFNs
# l = [] # Holds the valid TFNs
# for i in range(MAX_TFN, MIN_TFN, -1):
#     if len(l) < 10:
#         if validate_tfn(i):
#             print(f'[+] Found valid TFN -> {i}')
#             l.append(i)


# Different approach (seems to fix the issue)
l = []
for i in range(MIN_TFN, MAX_TFN):
    if validate_tfn(i):
        print(f'[+] Found valid TFN -> {i}')
        l.append(i)

        # Test how many TFNs already in the list
        if len(l) == 10:
            print('Already found 10 valid TFNs. Exiting now...')
            break

# Output the final list with the lowest valid TFNs
print(l)