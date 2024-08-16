# created by Musie Beyene
# StayAhead Training Company
# Dec 12 2019

# import database package
import sqlite3

# declare a connection object
conn = sqlite3.connect('my_database.db')

# declare a context manager (removing the need to close db)
# with conn:
    # declare a cursor object
    # c = conn.cursor()

    # c.execute("""DROP TABLE products""")  #reset

    # comment out CREATE TABLE after first run
    # from HERE
    # c.execute("""CREATE TABLE products  (
    #         prodId text,
    #         description text,
    #         price float
    #         )""")

    # c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
    #     'prodId': '111',
    #     'description': 'Earl grey',
    #     'price': 1.99
    # })

    # c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
    #     'prodId': '222',
    #     'description': 'Americano',
    #     'price': 2.50
    # })

    # c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
    #     'prodId': '333',
    #     'description': 'Capuccino',
    #     'price': 3.00
    # })

    # c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
    #     'prodId': '444',
    #     'description': 'Caffe Late',
    #     'price': 3.50
    # })

    # c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
    #     'prodId': '555',
    #     'description': 'Flat white',
    #     'price': 3.50
    # })

    # c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
    #     'prodId': '666',
    #     'description': 'Hot chocolate',
    #     'price': 3.65
    # })
    # to HERE

# whole of query_db.py script pasted in to main
m = 100

# with sqlite3.connect('my_database.db') as conn:
#   c = conn.cursor()
#   print(type(conn))  #¢ <class 'sqlite3.Connection'>
#   print(type(c))  # <class 'sqlite3.Cursor'>

#   c.execute("SELECT * FROM products")
#   all_items = c.fetchall()
#   print(type(all_items))  # list

#   print('All items in database')
#   for item in all_items:
#     print(item)
#   print("*" * m)

#   c.execute("SELECT * FROM products WHERE price > :price", {'price': 3.00})
#   price_23 = c.fetchall()
#   # print('All items costing more than £3 ',price_23)
#   print('All items costing more than £3 ')
#   for item in price_23:
#     print(item)
#   print("*" * m)

#   c.execute(
#       """UPDATE products SET price = :price
#         WHERE prodId = :prodId""", {
#           'prodId': '111',
#           'price': 10.50
#       })

#   c.execute(
#       """DELETE from products
#                 WHERE description = :description""",
#       {'description': 'Flat white'})

#   c.execute("SELECT * FROM products")

#   all_items = c.fetchall()
#   print(
#       'All items after 1.updating product id "111" 2.deleting "Flat white" in database'
#   )
#   for item in all_items:
#     print(item)
#   print("*" * m)

# whole rollback script pasted into main
with sqlite3.connect('my_database.db') as conn:
  c = conn.cursor()

  c.execute("SELECT * FROM products")
  all_items = c.fetchall()
  print(type(all_items))
  print(all_items)

  print('All items in database')
  for item in all_items:
    print(item)
  print("*" * m)

  c.execute(
      """UPDATE products SET price = :price
      WHERE prodId = :prodId""", {
          'prodId': '111',
          'price': 1.99
      })

  c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", {
      'prodId': '555',
      'description': 'Flat white',
      'price': 3.50
  })

c.execute("SELECT * FROM products")
all_items = c.fetchall()
print(
    'All items after rolling back 1.updating product id "111" 2 "Flat white" delete in database'
)
for item in all_items:
  print(item)
print("*" * m)
