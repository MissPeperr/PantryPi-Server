import sqlite3
import json
from models import Category

def get_all_categories():
    with sqlite3.connect("./pantry.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM Category c
        """)

        category_list = []

        dataset = db_cursor.fetchall()
            
        for row in dataset:
            category = Category(row['id'], row['name'])

            category_list.append(category.__dict__)

    return json.dumps(category_list)