

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MYSQL CONNECTION

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nothing@12",
    database="business_db"
)

cursor = db.cursor()


# CITY-WISE API

@app.get("/city-wise")
def city_wise():

    query = """
    SELECT city, COUNT(*) as total
    FROM listing_master
    GROUP BY city
    """

    cursor.execute(query)

    data = cursor.fetchall()

    result = []

    for row in data:
        result.append({
            "city": row[0],
            "total": int(row[1])
        })

    return result



# CATEGORY-WISE API

@app.get("/category-wise")
def category_wise():

    query = """
    SELECT category, COUNT(*) as total
    FROM listing_master
    GROUP BY category
    """

    cursor.execute(query)

    data = cursor.fetchall()

    result = []

    for row in data:
        result.append({
            "category": row[0],
            "total": int(row[1])
        })

    return result



# SOURCE-WISE API

@app.get("/source-wise")
def source_wise():

    query = """
    SELECT source, COUNT(*) as total
    FROM listing_master
    GROUP BY source
    """

    cursor.execute(query)

    data = cursor.fetchall()

    result = []

    for row in data:
        result.append({
            "source": row[0],
            "total": int(row[1])
        })

    return result