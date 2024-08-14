year = int(input("Enter your birth year"))
if year < 1946:
    print("uncategorised")
elif year >= 1946 and year <= 1965:
    print(f"Born in: {year} : Baby Boomer")
elif year >= 1966 and year <= 1976:
    print(f"Born in: {year} : Gen X")
elif year >= 1977 and year <= 1994:
    print(f"Born in: {year} : Millenial")
elif year >= 1995:
    print(f"Born in: {year} : Gen Z")

# could refactor to use lower/higher boundaries only