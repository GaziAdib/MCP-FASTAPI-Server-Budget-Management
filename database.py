import sqlite3

import sqlite3

# DB_NAME = "budget.db"

# Define the absolute path to ensure Claude finds the same file every time
DB_NAME = r"G:\Python_AI_Projects\GenAi_Projects\MCP_Projects\MCP_Expense_Tracker_Backend\budget.db"


# get db
def get_db():
    conn = sqlite3.connect(
        DB_NAME,
        check_same_thread=False  # ✅ REQUIRED
    )
    conn.row_factory = sqlite3.Row
    return conn

