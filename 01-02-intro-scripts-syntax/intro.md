## Introduction and history

Python: not named after snakes, but after Monty Python
Guido Van Rossum, creator, was Monty Python fan
References to the show may be found throughout the docs

Python: an object-oriented programming language, arguably easier to learn than Java.
Object-oriented languages:
Favour data encapsulation in object structures (for Python, the dictionary structure is akin to an object literal in other languages)

### Object-Oriented programming 

in other languages, {} denote object literal
literal means not created by a class
in Python this is a dict (dictionary), one of the container structures
(lists, tuples, sets, dicts and strings)

OO languages noun and verb analysis for software engineering

Airway Provides the Customer with radio Infrastructure to allow them to communicate in the field. 

Nouns:
Customer
Infrastrucure
(Airway is a red herring for it represents the whole system)

different types 
backend network
base stations

Verbs:
provide()
communicate()

Nouns would suggest classes
Classes are a blueprint for creating objects

class: 
Customer

attributes:
name
address
id

functions:
provide/setup customer()

class:
Infrastructure (candidate for abstraction)

attributes (only those in common with every type):
type
description
list of customers

functions:
add_customer(customer)
communicate()

class:
BackEndNetwork(Infrastructure)
attributes: (specific/extra ones)
function: (specific/extra ones)

class:
BaseStations(Infrastructure)
attributes: (specific/extra ones)
function: (specific/extra ones)

NOUNS become classes, from classes we make Objects.

Every instantiation of the class has the same properties / attributes
Not necessarily the same values
Verbs become functions, which are props of Objects.

In Python, Objects and Classes are the default, go-to data structures.

Variables may and can change datatypes during an application/script.
Python supports this and is referred to as a Dynamically-typed language.

Python mostly used for either scripting or programming, but not building whole, standalone, deployable apps. 
Scripting is in the main high-level, interpreted code.
Programming is more imperatively-written, low-level machine code, often with a compile-time stage.
Python does both. 

https://byjus.com/gate/difference-between-scripting-and-programming-languages/

https://www.tutorialspoint.com/is-python-a-programming-language-or-simply-a-scripting-language


### Functional Programming, or FP

Immutable data structures are preferred, and transformations over modifications.

Lists and containers are treated AS IF they cannot be changed.

A change results in a new version returned.

Think of OOP as `Save`

Think of FP as `Save As`

Neither OOP or FP are exclusive!



### Versioning

Python was re-written between major releases 2 and 3.
Versions 3 > are breaking changes - NOT backward compatible!

Most of what we do hasn't changed much since version 3.5
Best to install fresh from python.org/downloads

Once installed, run in two ways:
-   1. as a REPL shell (Read Evaluate, Print, Loop), always useful for unit testing as you code bigger Scripts
-   2. script mode: write and execute longer chunks of code. Code persisted to memory.

### Implementations

A Python implementation is not something we should concern iourselves with as it is to do with the underlying language.

Python code, using the standard implementation of CPython (underlying language is C) is interpreted
(no separate compile time stage to check for syntax errors, 
no performance optimisation at low-level machine code, 
but IDE can still use linters with code suggestions)

Other implementations include Jython, which is Java-based, IronPython - at the end of the day, it is the Python interpreter that runs the code.

EDITORS:
PyCharm, Spyder, Idle (used to ship with Python install, aka Eric idle)
Visual Studio, Visual studio Code, IntelliJ IDEA, Webstorm, Eclipse, Sublime, Atom

We use Visual studio Code as it is fully-featured and open source. 

### Documentation

the Python official docs are quite hard to naviagte and read. Though the most exhaustive source of info, they can put off many first time users.

docs.python.org

Excellent resource for thsoe whose Python is not their first language.

Easier on the eye is W3 schools, especially if Python is first language

w3schools.com/python

### Naming conventions

Variables and functions should be named in snake_case (lower case, underscore separated).

Classes should be named in PascalCase (CamelCase).

So, if you EVER see a capital letter in Python it denotes the presence of a class of that name.

Pythin does not support the concept of CONSTANTS (variable that may not be reassigned) but can indicate to the next dev that they should be treated as such by caps lock. SCREAMING_SNAKE_CASE.

Comments should be in whole sentences, sentebce case and terninated with full stop and two spaces. More detail in the manual.

All these things are best practice only, NOT mandatory, but to ignore them is to code in an un-Pythonesque way.

## indenting and line-splitting

Indents are fundamental to Python and each statement in Python is terminated by a newline character.

Multiple statements MAY be written on one line using semicolon terminatro, but, in trainer's opinion SHOULD NOT.

e.g.

`num1 = 1; num2 = 1`

technology_without_an_interesting_name = "TWAIN"

the following are permitted

technology_without_an_interesting_name /
 = "TWAIN"

{technology_without_an_interesting_name 
    = "TWAIN"}

(technology_without_an_interesting_name 
= "TWAIN") # probably the most readable, used with the Walrus operator (see later)