# import string as sts
# sts.ascii_letters
# string = "hello 34567CzechosLovak@ia"
#
# longest = string[0]
# current = string[0]
# for c in string[1:]:
#     if c in sts.ascii_letters:
#         current += c
#         if len(current) > len(longest):
#             longest = current
#     else:
#         current = ''
# print(longest)

import string as sts
string=input()
longest = string[0]
current = string[0]
for c in string[1:]:
    if c in sts.ascii_letters:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = ''
print(longest)