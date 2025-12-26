s1 = "Thirty"
s2 = "Days"
s3 = "Of"
s4 = "Python"
sentence = s1 + " " + s2 + " " + s3 + " " + s4
print(sentence)
s5 = "Coding"
s6 = "For"
s7 = "All"
sentence2 = s5 + " " + s6 + " " + s7
print(sentence2)
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
s8 = company.capitalize()
s9 = company.title()
s10 = company.swapcase()
print(s8, ' ', s9, ' ', s10)
company_slice = company[7:14]
print(company_slice)
print(company_slice.find("Coding"))
company_replace = company.replace("Coding", "Python")
print(company_replace)
company_replace_all = company_replace.replace(
    "Python For All", "Python For Everyone")
print(company_replace_all)
company_split = company.split()
print(company_split)
# Split the string at the comma and change it to a list
s11 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = s11.split(", ")
print(companies)
print(company[0])
print(len(company))
print(f"'{company[10]}'")


# Abbreviation
company_replace_all_split = company_replace_all.split()
acronym_company_replace_all = ''
for word in company_replace_all_split:
    acronym_company_replace_all += word[0]
print(acronym_company_replace_all)

# Abbreviation
acronym_company = ''
for word in company_split:
    acronym_company += word[0]
print(acronym_company)
print("C at index:", company.index("C"))
print("F at index:", company.index("F"))
print("Last occurrence of l at index: ", company.rindex("l"))


s12 = "You cannot end a sentence with because because because is a conjunction"
s12_because_start = s12.find("because")
print(s12.find("because"))  # using find method
print(s12.index("because"))  # using index method

s12_because_end = s12.rfind("because") + len("because")
print(s12.rfind("because"))  # using find method
print(s12.rindex("because"))  # using index method

# slicing because because because
s12_slice = s12[s12_because_start:s12_because_end]
print(s12_slice)

# Substrinng check by startswith() and endswith() methods
print("Does \"Coding For All\"start with a substring Coding -> ",
      company.startswith("Coding"))
print("Does \"Coding For All\" end with a substring Coding -> ",
      company.endswith("Coding"))

# Removing whitespaces
s13 = "   Coding For All      "
print(s13.strip())
print(s13.lstrip())

# Check if the string contains only alphanumeric characters
s14 = "30DaysOfPython"
s15 = "thirty_days_of_python"
print(s14.isidentifier())
print(s15.isidentifier())

# Joining a list of strings
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '# '.join(libraries)
print(joined_libraries)
