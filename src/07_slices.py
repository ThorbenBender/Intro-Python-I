"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
sFirst = slice(1, 2);
print(a[sFirst]);

# Output the second-to-last element: 9
sSecond = slice(4, 5);
print(a[sSecond]);

# Output the last three elements in the array: [7, 9, 6]
sThird = slice(3, 6);
print(a[sThird]);

# Output the two middle elements in the array: [1, 7]
sFourth = slice(2, 4);
print(a[sFourth]);

# Output every element except the first one: [4, 1, 7, 9, 6]
sFifth  = slice(1, 6);
print(a[sFifth])

# Output every element except the last one: [2, 4, 1, 7, 9]
sSixth = slice(0, 5);
print(a[sSixth]);

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
sSeventh = slice(7, 12);
print(s[sSeventh]);