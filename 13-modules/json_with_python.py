import json

books = [
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
    {'title': 'The Twits', 'author': 'Roald Dahl'},
    {'title': 'The Bippolo Seed', 'author': 'Dr. Seuss'}
]

# python to JSON: json.dumps()
# JSON back into Python: json.loads()

books_json = json.dumps(books)
print(books_json)
print(type(books_json))

books_python_again = json.loads(books_json)
print(books_python_again)
print(type(books_python_again))

with open("widget.json") as widget_file:
    # read contents into python dict
    a_dict = json.load(widget_file)
    print(a_dict)

    # edit data
    a_dict["widget"]["image"]["src"] = "Images/Moon.png"
    a_dict["widget"]["image"]["name"] = "moon1"
    a_dict["widget"]["text"]["onMouseUp"] = "moon1.opacity = (moon1.opacity / 100) * 90;"

with open("modified-widget.json", mode="w") as modified_widget_file:
    # write modified dictionary to a new JSOn file
    json.dump(a_dict, modified_widget_file)

with open("modified-widget.json") as modified:
    print(modified := json.load(modified))

# [{"title": "The Gruffalo", "author": "Julia Donaldson"}, {"title": "The Twits", "author": "Roald Dahl"}, {"title": "The Bippolo Seed", "author": "Dr. Seuss"}]

# [{'title': 'The Gruffalo', 'author': 'Julia Donaldson'}, {'title': 'The Twits', 'author': 'Roald Dahl'}, {'title': 'The Bippolo Seed', 'author': 'Dr. Seuss'}]