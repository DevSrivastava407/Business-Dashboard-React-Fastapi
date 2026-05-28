

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nothing@12",
    database="business_db"
)

cursor = db.cursor(dictionary=True)

# Home API
@app.get("/")
def home():
    return {"message": "Backend Running"}

# City-wise count API
@app.get("/city-wise")
def city_wise():

    query = """
    SELECT city, COUNT(*) as total
    FROM listing_master
    GROUP BY city
    """

    cursor.execute(query)

    result = cursor.fetchall()

    return result

# Category-wise count API
@app.get("/category-wise")
def category_wise():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nothing@12",
        database="business_db"
    )

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT category, COUNT(*) as total
    FROM listing_master
    GROUP BY category
    """

    cursor.execute(query)

    data = cursor.fetchall()

    return data

# Source-wise count API
@app.get("/source-wise")
def source_wise():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nothing@12",
        database="business_db"
    )

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT source, COUNT(*) as total
    FROM listing_master
    GROUP BY source
    """

    cursor.execute(query)

    data = cursor.fetchall()

    return data