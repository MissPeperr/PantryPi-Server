import json
import sqlite3
import requests
from models import Food
from key import api_key
from key import app_id


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


def get_food_by_category(cat_id):
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
        WHERE f.category_id = ?
        """, (cat_id,))

        food_list = []

        dataset = db_cursor.fetchall()
            
        for row in dataset:
            food = Food(row['id'], row['name'], row['quantity'], row['barcode'], row['on_grocery_list'], row['category_id'])

            food_list.append(food.__dict__)

    return json.dumps(food_list)


def get_food_by_barcode(barcode):
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
        WHERE f.barcode = ?
        """, (barcode, ))

        row = db_cursor.fetchone()

        food = Food(row['id'], row['name'], row['quantity'], row['barcode'], row['on_grocery_list'], row['category_id'])

    return json.dumps(food.__dict__)

def create_food(food):
    with sqlite3.connect("./pantry.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Food (id, name, quantity, barcode, on_grocery_list, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (food['foodId'], food['label'], food['quantity'], food['barcode'], food['on_grocery_list'], food['category_id'],))

        food = Food(food['foodId'], food['label'], food['quantity'], food['barcode'], food['on_grocery_list'], food['category_id'])

        return food.__dict__


def get_food_from_api(barcode):
    r = requests.get(f'https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={api_key}&upc={barcode}')
    r = r.json()['hints']
    food_dict = r[0]['food']
    food_dict['barcode'] = barcode
    #  setting up default values for later
    food_dict['quantity'] = 1
    food_dict['on_grocery_list'] = 0
    food_dict['category_id'] = 1
    
    created_food = create_food(food_dict)

    return json.dumps(created_food)