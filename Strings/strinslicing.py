# Slicing of string -> [start : End : step]
# rules
"""
Start : Default 0 (Optional)
End : Default Last Character (Optional)
Step : Default +1 (Optional)
"""

s = "welcome"

# String Slicing with Positive Indexing
"""
print(s)  # welcome
print(s[3])  # c
print(s[:])  # welcome
print(s[::])  # welcome
print(s[3:])  # come
print(s[3:5])  # co
print(s[3:7])  # come
print(s[3:17])  # come
print(s[:3])  # wel
print(s[::3])  # wce
print(s[::1])  # welcome
print(s[3::3])  # ce
print(s[3:6:3])  # c
"""

# String Slicing with negative Indexing
'''
print(s[-1:])  # e
print(s[-4:])  # come
print(s[:-4])  # wel
print(s[::-4])  # el
print(s[0::-2])  # w
print(s[-3::-2])  # olw
print(s[-3:-6:-2])  # ol
print(s[3::-2])  # ce
print(s[3:-6:-2])  # c
print(s[3:-6:2])  #
print(s[::-1])  # emoclew (reversed string)
'''