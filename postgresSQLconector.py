import psycopg2

# connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="real_estate_crm",
    user="username",
    password="password"
)

# create a cursor to execute queries
cur = conn.cursor()

# create a table for properties
cur.execute("""
CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    address TEXT NOT NULL,
    bedrooms INTEGER,
    bathrooms INTEGER,
    sqft INTEGER,
    price DECIMAL(10, 2)
)
""")

# insert some data
cur.execute("""
INSERT INTO properties (address, bedrooms, bathrooms, sqft, price)
VALUES
    ('123 Main St', 2, 1, 1000, 200000),
    ('456 Elm St', 3, 2, 1500, 300000),
    ('789 Oak St', 4, 3, 2000, 400000)
""")

# commit the changes to the database
conn.commit()

# select all properties
cur.execute("SELECT * FROM properties")
properties = cur.fetchall()

# print the results
for property in properties:
    print(property)

# close the cursor and the database connection
cur.close()
conn.close()
