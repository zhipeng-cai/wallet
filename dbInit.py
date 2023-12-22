
# TODO check the table schema design
def create_tables(conn):
    cursor = conn.cursor()
    # SQL statements to create tables
    # Create User table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY autoincrement,
        Name TEXT,
        SSN TEXT
    );
    ''')

    # Create Email table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Email (
        EmailID INTEGER PRIMARY KEY autoincrement,
        UserID INTEGER,
        Address TEXT,
        IsVerified INTEGER,
        FOREIGN KEY(UserID) REFERENCES User(UserID)
    );
    ''')

    # Create Phone table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Phone (
        PhoneID INTEGER PRIMARY KEY autoincrement, 
        UserID INTEGER,
        Number INTEGER,
        IsVerified INTEGER,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    );
    ''')

    # Create BankAccount table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BankAccount (
        AccountNumber INTEGER PRIMARY KEY,
        IsVerified INTEGER
    );
    ''')

    # Create UBRelation table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS UBRelation (
        UBRelationID INTEGER PRIMARY KEY autoincrement,
        UserID INTEGER,
        AccountNumber INTEGER,
        FOREIGN KEY (UserID) REFERENCES User(UserID),
        FOREIGN KEY (AccountNumber) REFERENCES BankAccount(AccountNumber)
    );
    ''')

    # Create Transaction table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY autoincrement,
        Typo TEXT,
        TotalAmount DOUBLE 
    );
    ''')

    # Create Payment table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Payment (
        PaymentID INTEGER PRIMARY KEY autoincrement,
        SenderUserID INTEGER,
        ReceiverUserID INTEGER,
        TransactionID INTEGER,
        Amount DOUBLE,
        Memo TEXT,
        BeginDate TEXT,
        EndDate TEXT,
        IsSuccessful INTEGER,
        FOREIGN KEY (SenderUserID) REFERENCES User(UserID),
        FOREIGN KEY (ReceiverUserID) REFERENCES User(UserID),
        FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID)
    );
    ''')

    # Commit the changes and close the connection
    conn.commit()



# TODO 插入初始数据
def insert_init_data(conn):
    cursor = conn.cursor()
    users_add = '''
    INSERT OR IGNORE INTO User 
    VALUES (1, 'bro', '1234')
    '''
    cursor.execute(users_add)
    conn.commit()