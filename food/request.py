import json
import sqlite3
from models import Food


def get_all_food():
    with sqlite3.connect("./pantry.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        # The messenger for the db
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            f.id,
            f.name,
            f.quantity,
            f.barcode,
            f.on_grocery_list,
            f.category_id
        FROM Food f
        """)

        # Initialize an empty list to hold all animal representations
        food_list = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
            
        for row in dataset:
            food = Food(row['id'], row['name'], row['quantity'], row['barcode'], row['on_grocery_list'], row['category_id'])

            food_list.append(food.__dict__)

    return json.dumps(food_list)