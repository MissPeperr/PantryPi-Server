import json
import sqlite3
from models import Food


def get_all_food():
    with sqlite3.connect("./pantry.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

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

        food_list = []

        dataset = db_cursor.fetchall()
            
        for row in dataset:
            food = Food(row['id'], row['name'], row['quantity'], row['barcode'], row['on_grocery_list'], row['category_id'])

            food_list.append(food.__dict__)

    return json.dumps(food_list)