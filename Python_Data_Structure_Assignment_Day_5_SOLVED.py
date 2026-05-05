
# ============================================================
# Python Data Structures - Day 5 Assignment SOLVED
# ============================================================

# ============================================================
# LISTS
# ============================================================

# --- Q1: Create an empty list named 'a' ---
a = []
print("Value of a:", a)
print("Type of a:", type(a))

# --- Q2: languages list ---
languages = ['R', 'Python', 'SAS', 'Scala', 42]

# Print number of elements
print("\nNumber of elements:", len(languages))

# Iterate and print all elements
for item in languages:
    print(item)

# Select second item 'Python', store in temp
temp = languages[1]
print("\nValue of temp:", temp)
print("Type of temp:", type(temp))

# Append 'Java'
languages.append('Java')
print("\nAfter appending Java:", languages)

# Remove 42 and print
languages.remove(42)
print("After removing 42:", languages)

# --- Q3: colors list ---
colors = ['Red', 'Blue', 'White']

# Append 'Black'
colors.append('Black')
print("\nAfter appending Black:", colors)

# Insert 'Orange' at index 1
colors.insert(1, 'Orange')
print("After inserting Orange at index 1:", colors)

# Create colors2 and extend
colors2 = ['Grey', 'Sky Blue']
colors.extend(colors2)
print("Length of colors:", len(colors))
print("Colors list:", colors)

# Sort and print
colors.sort()
print("Sorted colors:", colors)

# --- Q4: String split, lower, check, remove, slice, join ---
sent = 'Coronavirus Caused Lockdowns Around The World.'

# Split into words
words = sent.split()
print("\nWords list:", words)

# Convert to lower case
words_lower = [word.lower() for word in words]
print("Lowercase words:", words_lower)

# Check if 'country' is in the list
print("Is 'country' in list?", 'country' in words_lower)

# Remove 'the' and print
words_lower.remove('the')
print("After removing 'the':", words_lower)

# Slice first 4 words
x4 = words_lower[:4]
print("First 4 words (x4):", x4)

# Join list into single string
joined = ' '.join(words_lower)
print("Joined string:", joined)


# ============================================================
# SETS
# ============================================================

# --- Q1: stud_grades ---
stud_grades = ['A', 'A', 'B', 'C', 'C', 'F']
print("\nLength of stud_grades:", len(stud_grades))

stud_grades_set = set(stud_grades)
print("stud_grades_set:", stud_grades_set)

print("Type of stud_grades:", type(stud_grades))
print("Type of stud_grades_set:", type(stud_grades_set))
# Note: List allows duplicates, Set removes duplicates automatically

# Add 'G'
stud_grades_set.add('G')
print("After adding G:", stud_grades_set)

# Add 'F' (already present - won't duplicate)
stud_grades_set.add('F')
print("After adding F (already present):", stud_grades_set)

# Remove 'F'
stud_grades_set.remove('F')
print("After removing F:", stud_grades_set)
print("Length of stud_grades_set:", len(stud_grades_set))

# --- Q2: Union, Intersection, Difference ---
colors_list = ['red', 'blue', 'orange']
fruits = ['orange', 'grapes', 'apples']
print("\ncolors:", colors_list)
print("fruits:", fruits)

colors_set = set(colors_list)
fruits_set = set(fruits)
print("colors_set:", colors_set)
print("fruits_set:", fruits_set)

# Union
print("Union:", colors_set.union(fruits_set))

# Intersection
print("Intersection:", colors_set.intersection(fruits_set))

# Difference (fruits but not colors)
print("Fruits but not colors:", fruits_set.difference(colors_set))


# ============================================================
# TUPLES
# ============================================================

# --- Q1: temp list ---
temp = [17, 'Virat', 50.0]

# Iterate and print
print("\nItems in temp:")
for item in temp:
    print(item)

# Replace first element with 11
temp[0] = 11

# Convert to tuple
temp1 = tuple(temp)

# Iterate through temp1
print("Items in temp1:")
for item in temp1:
    print(item)

# Try to replace first element of tuple (will give error)
try:
    temp1[0] = 17
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable - you cannot change their values!")

# --- Q2: Nested Tuples ---
city = ("Bangalore", 28.9949521, 72)
print("\nFirst element of city:", city[0])

city2 = ('Chennai', 30.01, 74)
cities = (city, city2)
print("cities:", cities)
print("Type of first element in cities:", type(cities[0]))
print("Type of cities:", type(cities))


# ============================================================
# DICTIONARY
# ============================================================

# --- Q1: Dictionary operations ---
d = {"actor": "amir", "animal": "cat", "earth": 2, "list": [23, 32, 12]}

# Try d[0] - will give KeyError
try:
    print(d[0])
except KeyError as e:
    print("\nKeyError:", e, "- Key 0 doesn't exist in dictionary!")

# Store d['actor'] in variable actor
actor = d['actor']
print("actor:", actor)
print("Type of actor:", type(actor))

# Store d['list'] in List
List = d['list']
print("Type of List:", type(List))

# Create d1 and merge into d
d1 = {'singer': 'Kr$na', 'album': 'Still here', 'genre': 'hip-hop'}
d.update(d1)
print("Merged dictionary d:", d)

# Print all keys
print("Keys:", list(d.keys()))

# Print all values
print("Values:", list(d.values()))

# Iterate and print key-value pairs
print("\nKey-Value pairs:")
for key, value in d.items():
    print(f"{key} ----> {value}")

# Count character occurrences in 'sent'
sent = 'Coronavirus Caused Lockdowns Around The World.'
char_count = {}
for char in sent:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("\nCharacter count in sent:")
print(char_count)
