'''
conditional statements are very smilar in Python to other languages,
they execute a block of code depending on whether a condition evaluates True or False
if True:
    code block, defined by indent, immediately following is executed
if False:
    skipped

an else block has NO condition and means, really ANYTHING else

you can test multiple conditions using if elif else

following execution of a branch the interpreter steps out of the statement structure, like a break

so when using ranges of values, if..elif blocks should be arranged with care to avoid unreachable code

Since recently in Python 3.10 there is another decision control statement
Called Structural Pattern Matching or match case
This mimicks the behaviour of switch in Java and JS, which traditionally has had no equivalent in Python
The match statement tests a single variable or expression for equality

'''
# single branch IF
if True:
    print("True path in standalone IF executed")

# two separate IF statements - nothing to do with one another
if False:
    # unreachable code
    # pass IndentationError: expected an indented block after 'if' statement on line 28
    pass

# two branch IF - ELSE
if False:
    print("True path in IF - ELSE executed")
else:
    print("ELSE path in IF - ELSE executed")

# three or more branches IF - ELIF - ELSE
if False:
    print("FIRST True path in IF - ELIF - ELSE executed")
elif True:
    print("SECOND True path in IF - ELIF - ELSE executed")
else:
    print("ELSE path in IF - ELSE executed")

# back to LH margin

# unhealthy diagnosis
hr = 150
bp = {"diastolic": 160, "systolic": 90}
# borderline diagnosis
# hr = 120
# bp = {"diastolic": 150, "systolic": 80}
# healthy diagnosis
# hr = 105
# bp = {"diastolic": 110, "systolic": 75}

if hr > 140 and (bp["diastolic"] > 150 and bp["systolic"] > 80):
    print("you are unhealthy - go to A&E")
elif hr > 110 and (bp["diastolic"] > 120 and bp["systolic"] > 70):
    print("you are borderline - go for a checkup")
else:
    print("You are healthy - no action needed")

# an if - else may be written on one line
# Pythonesque
# equivalent to "ternary operator" in other languages
# important concept: its one thing or the other, no thrid option
# an "exclusive OR"
temp = "cold"
temp = "scorchio"
clothing = "jumper" if temp == "cold" else "T-shirt"
print(f"It is {temp} so I should wear a {clothing}")
