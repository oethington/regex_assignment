f = open("./regex_test.txt")
data = f.readlines()
# print(data)

# """
# Expected Output
# Abraham Lincoln
# Andrew P Garfield
# Connor Milliken
# Jordan Alexander Williams
# None
# None
# """

# always capital A-Z forst and last name
# data = f.readlines()
# read takes all data
# print(data)
# regex for middle name but not print [A-Za-z]+

pattern = re.compile('([A-Z][a-z]+) ([A-Z][a-z]+)')
for person in data:
    match = pattern.search(person)

    if match:
        print(f"{match.group(1)} {match.group(2)}")
 
    else:
        print("none")