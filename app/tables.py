import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="postgres",
    user="postgres",
    password="password"
)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    is_waiter BOOL NULL DEFAULT FALSE
);
""")

conn.commit()
