import sqlite3


def test_database_connection():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('../db/data.db')
        print("Database connected successfully")

        # Check if the tables exist
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("Tables exist:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found.")

    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()


if __name__ == '__main__':
    test_database_connection()
