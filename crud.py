from database import get_db


# Add Income function 

def add_income(name, amount, month):
    conn = get_db()
    conn.execute(
        "INSERT INTO income (name, amount, month) VALUES (?, ?, ?)",
        (name, amount, month)
    )
    conn.commit()
    conn.close()


# Add Expense
def add_expense(name, amount, month):
    conn = get_db()
    conn.execute(
        "INSERT INTO expense (name, amount, month) VALUES (?, ?, ?)",
        (name, amount, month)
    )
    conn.commit()
    conn.close()


# list of incomes 

def list_incomes(month):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM income WHERE month = ?", (month,)
    ).fetchall()
    conn.close()
    return rows



# Fetch List of Expenses 
def list_expenses(month):
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM expense WHERE month = ?", (month,)
    ).fetchall()
    conn.close()
    return rows