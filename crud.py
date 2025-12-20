from database import get_db
import sqlite3

# add sqlite models tables first (load them)
from models import create_tables

# add the income and expense table immediately
create_tables()


# helper function 

def rows_to_dict(rows):
    return [dict(row) for row in rows]


# CRUD FUNCTIONS


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
        


# lists of incomes and expenses

# Example without row_factory
#row = ('Salary', 3000, 'April')
#row[0]  # 'Salary'
#row[1]  # 3000
#row[2]  # 'April'

# row = rows[0]
# row['name']   # 'Salary'
# row['amount'] # 3000
# row['month']  # 'April'


# list of incomes 
def list_incomes(month):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    
    rows = conn.execute(
        "SELECT * FROM income WHERE month = ?", (month,)
    ).fetchall()
    
    conn.close()
    return rows_to_dict(rows)
    


# list of expenses 
def list_expenses(month):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    
    rows = conn.execute(
        "SELECT * FROM expense WHERE month = ?", (month,)
    ).fetchall()
    conn.close()
    return rows_to_dict(rows)


