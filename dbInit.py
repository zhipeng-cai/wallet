
# TODO check the table schema design
def create_tables(conn):
    cursor = conn.cursor()
    # SQL statements to create tables
    users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255)
        -- Add other columns as needed
        -- For example: first_name VARCHAR(255), last_name VARCHAR(255), etc.
    );
    '''

    account_table = '''
    CREATE TABLE IF NOT EXISTS account (
        username VARCHAR(255) PRIMARY KEY,
        ssn VARCHAR(20),
        email VARCHAR(255),
        phone_number VARCHAR(20),
        bank VARCHAR(255)
        -- Add other columns as needed
        -- For example: balance DECIMAL(10, 2), last_login TIMESTAMP, etc.
    );
    '''

    transactions_table = '''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY,
        sender_username VARCHAR(255),
        receiver_username VARCHAR(255),
        date DATE,
        time TIME,
        transaction_type VARCHAR(20),
        money_amount DECIMAL(10, 2)
        -- Add other columns as needed
        -- For example: description VARCHAR(255), status VARCHAR(20), etc.
    );
    '''

    # Execute SQL statements
    cursor.execute(users_table)
    cursor.execute(account_table)
    cursor.execute(transactions_table)

    # Commit the changes and close the connection
    conn.commit()



# TODO 插入初始数据
def insert_init_data(conn):
    pass

