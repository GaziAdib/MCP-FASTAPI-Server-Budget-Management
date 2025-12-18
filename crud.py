import sqlite3
from database import get_db

# ---------------- Database Initialization ---------------- #

def init_db():
    """Ensures the tables exist before any tools are called."""
    conn = get_db()
    # Create the income table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            month TEXT NOT NULL
        )
    ''')
    # Create the expense table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS expense (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            month TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Run initialization immediately on import
init_db()

# ---------------- Helper Functions ---------------- #

def rows_to_dicts(rows):
    return [dict(row) for row in rows]

# ---------------- CRUD Functions ---------------- #

def add_income(name, amount, month):
    conn = get_db()
    conn.execute(
        "INSERT INTO income (name, amount, month) VALUES (?, ?, ?)",
        (name, amount, month)
    )
    conn.commit()
    conn.close()

def add_expense(name, amount, month):
    conn = get_db()
    conn.execute(
        "INSERT INTO expense (name, amount, month) VALUES (?, ?, ?)",
        (name, amount, month)
    )
    conn.commit()
    conn.close()

def list_incomes(month):
    conn = get_db()
    # Ensure we use the Row factory to return data Claude can read
    conn.row_factory = sqlite3.Row 
    rows = conn.execute(
        "SELECT * FROM income WHERE month = ?", (month,)
    ).fetchall()
    conn.close()
    return rows_to_dicts(rows)

def list_expenses(month):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT * FROM expense WHERE month = ?", (month,)
    ).fetchall()
    conn.close()
    return rows_to_dicts(rows)


# from database import get_db


# def rows_to_dicts(rows):
#     return [dict(row) for row in rows]

# # Add Income function 

# def add_income(name, amount, month):
#     conn = get_db()
#     conn.execute(
#         "INSERT INTO income (name, amount, month) VALUES (?, ?, ?)",
#         (name, amount, month)
#     )
#     conn.commit()
#     conn.close()


# # Add Expense
# def add_expense(name, amount, month):
#     conn = get_db()
#     conn.execute(
#         "INSERT INTO expense (name, amount, month) VALUES (?, ?, ?)",
#         (name, amount, month)
#     )
#     conn.commit()
#     conn.close()


# # list of incomes 

# def list_incomes(month):
#     conn = get_db()
#     rows = conn.execute(
#         "SELECT * FROM income WHERE month = ?", (month,)
#     ).fetchall()
#     conn.close()
#     return rows_to_dicts(rows)



# # Fetch List of Expenses 
# def list_expenses(month):
#     conn = get_db()
#     rows = conn.execute(
#         "SELECT * FROM expense WHERE month = ?", (month,)
#     ).fetchall()
#     conn.close()
#     return rows_to_dicts(rows)











# shape 

# [
#     (1, "Salary", 50000, "January"),
#     (2, "Freelancing", 12000, "January")
# ]

# [
#   {
#     "id": 1,
#     "name": "Salary",
#     "amount": 50000,
#     "month": "January"
#   },
#   {
#     "id": 2,
#     "name": "Freelancing",
#     "amount": 12000,
#     "month": "January"
#   }
# ]