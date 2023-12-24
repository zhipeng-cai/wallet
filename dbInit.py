from datetime import datetime


# TODO check the table schema design
def create_tables(conn):
    cursor = conn.cursor()
    # SQL statements to create tables
    # Create User table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY autoincrement,
        UserName TEXT NOT NULL,
        SSN TEXT,
        PassWord TEXT NOT NULL
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
    # 银行账户应该还有余额和优先级属性（即先使用哪个银行账户优先支付，优先级指数大的先使用）
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BankAccount (
        AccountNumber INTEGER PRIMARY KEY,
        Balance INTEGER,
        Priority INTEGER,
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
    # 这个transation里原本的typo是type的意思？然后还加了一个发起人的属性InitiatorUserID
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        InitiatorUserID INTEGER,
        Type TEXT,
        TotalAmount DOUBLE,
        FOREIGN KEY (InitiatorUserID) REFERENCES User(UserID)
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
        PayTime DATETIME,
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

    # Inserting 5 users
    users_data = [
        (1, 'bro', '1234', '1234'),
        (2, 'user1', '5678', '5678'),
        (3, 'user2', '91011', '91011'),
        (4, 'user3', '121314', '121314'),
        (5, 'user4', '151617', '151617')
    ]
    cursor.executemany("INSERT OR IGNORE INTO User (UserID, UserName, SSN, PassWord) VALUES (?, ?, ?, ?)", users_data)

    # Inserting email data
    email_data = [
        (1, 1, 'bro@example.com', 1),  # User 'bro' has a verified email
        (2, 2, 'user1@example.com', 1),  # User 'user1' has a verified email
        (3, 3, 'user2@example.com', 0),  # User 'user2' has an unverified email
        (4, 4, 'user3@example.com', 1),  # User 'user3' has a verified email
        (5, 5, 'user4@example.com', 1)  # User 'user4' has a verified email
    ]
    cursor.executemany("INSERT INTO Email (EmailID, UserID, Address, IsVerified) VALUES (?, ?, ?, ?)", email_data)

    # Inserting phone number data
    phone_data = [
        (1, 1, '1234567890', 1),  # User 'bro' has a verified phone number
        (2, 2, '9876543210', 1),  # User 'user1' has a verified phone number
        (3, 3, '5555555555', 0),  # User 'user2' has an unverified phone number
        (4, 4, '3333333333', 1),  # User 'user3' has a verified phone number
        (5, 5, '9999999999', 1)  # User 'user4' has a verified phone number
    ]
    cursor.executemany("INSERT INTO Phone (PhoneID, UserID, Number, IsVerified) VALUES (?, ?, ?, ?)", phone_data)

    # Inserting bank account data (each user with their own bank account)
    bank_data = [
        (123456, 1000, 1, 1),  # Bank account for user 'bro', balance 1000, priority 1, and verified
        (234567, 500, 2, 1),  # Bank account for user 'user1', balance 500, priority 2, and verified
        (345678, 800, 3, 0),  # Bank account for user 'user2', balance 800, priority 3, and unverified
        (456789, 700, 4, 1),  # Bank account for user 'user3', balance 700, priority 4, and verified
        (567890, 900, 5, 1)  # Bank account for user 'user4', balance 900, priority 5, and verified
    ]
    cursor.executemany("INSERT INTO BankAccount (AccountNumber, Balance, Priority, IsVerified) VALUES (?, ?, ?, ?)",
                       bank_data)

    # Inserting UBRelation data
    ub_relation_data = [
        (1, 1, 123456),  # User 'bro' is associated with their bank account
        (2, 2, 234567),  # User 'user1' is associated with their bank account
        (3, 3, 345678),  # User 'user2' is associated with their bank account
        (4, 4, 456789),  # User 'user3' is associated with their bank account
        (5, 5, 567890)  # User 'user4' is associated with their bank account
    ]
    cursor.executemany("INSERT INTO UBRelation (UBRelationID, UserID, AccountNumber) VALUES (?, ?, ?)",
                       ub_relation_data)

    # Inserting transaction data
    transactions_data = [
        (1, 1, 'Send', 50.0),  # User 'bro' initiates a payment of 100.0
        (2, 2, 'Send', 25.0),  # User 'user1' initiates a payment of 50.0
        (3, 3, 'Send', 40.0),  # User 'user2' initiates a payment of 75.0
        (4, 4, 'Send', 60.0),  # User 'user3' initiates a payment of 120.0
        (5, 5, 'Send', 45.0,),  # User 'user4' initiates a payment of 90.0
        (6, 2, 'Request', 30.0),  # User 'user1' requests a payment of 30.0
        (7, 3, 'Request', 20.0),  # User 'user2' requests a payment of 20.0
        (8, 4, 'Request', 35.0),  # User 'user3' requests a payment of 35.0
        (9, 5, 'Request', 25.0),  # User 'user4' requests a payment of 25.0
        (10, 1, 'Send', 70.0),  # User 'bro' initiates a payment of 70.0
        (11, 2, 'Send', 40.0),  # User 'user1' initiates a payment of 40.0
        (12, 3, 'Send', 55.0),  # User 'user2' initiates a payment of 55.0
        (13, 4, 'Send', 80.0),  # User 'user3' initiates a payment of 80.0
        (14, 5, 'Send', 65.0)  # User 'user4' initiates a payment of 65.0
    ]
    cursor.executemany(
        "INSERT INTO Transactions (TransactionID, InitiatorUserID, Type, TotalAmount) VALUES (?, ?, ?, ?)",
        transactions_data)

    # Inserting payment data
    payment_data = [
        (1, 1, 2, 1, 50.0, 'Payment from bro to user1', datetime.now(), 1),  # Payment from 'bro' to 'user1'
        (2, 2, 3, 2, 25.0, 'Payment from user1 to user2', datetime.now(), 1),  # Payment from 'user1' to 'user2'
        (3, 3, 4, 3, 40.0, 'Payment from user2 to user3', datetime.now(), 1),  # Payment from 'user2' to 'user3'
        (4, 4, 5, 4, 60.0, 'Payment from user3 to user4', datetime.now(), 1),  # Payment from 'user3' to 'user4'
        (5, 5, 1, 5, 45.0, 'Payment from user4 to bro', datetime.now(), 1),  # Payment from 'user4' to 'bro'
        (6, 2, 1, 6, 30.0, 'Request payment from user1', datetime.now(), 1),  # Request payment from 'user1' by 'user2'
        (7, 3, 2, 7, 20.0, 'Request payment from user2', datetime.now(), 1),  # Request payment from 'user2' by 'user3'
        (8, 4, 3, 8, 35.0, 'Request payment from user3', datetime.now(), 1),  # Request payment from 'user3' by 'user4'
        (9, 5, 4, 9, 25.0, 'Request payment from user4', datetime.now(), 1),  # Request payment from 'user4' by 'bro'
        (10, 1, 2, 10, 70.0, 'Payment from bro to user1', datetime.now(), 1),  # Payment from 'bro' to 'user1'
        (11, 2, 3, 11, 40.0, 'Payment from user1 to user2', datetime.now(), 1),  # Payment from 'user1' to 'user2'
        (12, 3, 4, 12, 55.0, 'Payment from user2 to user3', datetime.now(), 1),  # Payment from 'user2' to 'user3'
        (13, 4, 5, 13, 80.0, 'Payment from user3 to user4', datetime.now(), 1),  # Payment from 'user3' to 'user4'
        (14, 5, 1, 14, 65.0, 'Payment from user4 to bro', datetime.now(), 1)  # Payment from 'user4' to 'bro'
    ]
    cursor.executemany(
        "INSERT INTO Payment (PaymentID, SenderUserID, ReceiverUserID, TransactionID, Amount, Memo, PayTime, IsSuccessful) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        payment_data)

    # Commit the changes
    conn.commit()