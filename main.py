from fastmcp import FastMCP

from crud import add_income, add_expense, list_incomes, list_expenses
from schemas import IncomeCreate, ExpenseCreate
from pydantic import ValidationError

mcp = FastMCP(name="BudgetApp")


# attach tools

@mcp.tool()
def add_income_tool(name: str, amount: float, month: str) -> dict:
    """Add income for a month with name, amount and for which month this income for in a natural language"""
    
    try:
        data = IncomeCreate(name=name, amount=amount, month=month)
        add_income(data.name, data.amount, data.month)
        return {"status": "Income added successfully", "data": data.model_dump()}

    except ValidationError as e:
        return {"status": "error", "message": e.errors()[0]['msg']}


@mcp.tool()
def add_expense_tool(name: str, amount: float, month: str) -> dict:
    """Add income for a month with name, amount and for which month this income for in a natural language"""
    
    try:
        data = ExpenseCreate(name=name, amount=amount, month=month)
        add_expense(data.name, data.amount, data.month)
        return {"status": "Expense added successfully", "data": data.model_dump()}

    except ValidationError as e:
        return {"status": "error", "message": e.errors()[0]['msg']}


# Get Summary Tool

@mcp.tool()
def get_summary(month: str) -> dict:
    """GET Monthly budget summary with income, expenses and balance"""
    incomes = list_incomes(month)
    expenses = list_expenses(month)
    
    total_income = sum(i['amount'] for i in incomes)
    total_expense = sum(i['amount'] for i in expenses)
    balance = total_income - total_expense
    
    return {
        "month": month,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "income_list": [dict(i) for i in incomes],
        "expense_list": [dict(i) for i in expenses]
    }
    

if __name__ == "__main__":
    import sys
    
    try:
        mcp.run()
    except Exception as e:
        sys.stderr.write(f"Server crushed: {e}\n")
        sys.exit(1)


# if __name__ == "__main__":
#     mcp.run(transport="http", host="127.0.0.1", port=8000)
                
    

# Request

# {
#   `name`: `salary`,
#   `month`: `December 2025`,
#   `amount`: 50000
# } 


# {"status":"Income added successfully","data":{"name":"salary","amount":50000.0,"month":"December 2025"}}   

# summary 

# {
#   `month`: `December 2025`
# }








# """
# FastMCP Budget Tracker Server
# ==============================

# Modern MCP server using FastMCP.
# Only defines tools and runs the server.
# Database logic lives in separate files.
# """

# import json
# from fastmcp import FastMCP

# # Import your existing CRUD functions
# from crud import add_income, add_expense, list_incomes, list_expenses

# # Create FastMCP instance
# mcp = FastMCP(name="BudgetTracker")

# # ---------------- Tools ---------------- #

# @mcp.tool()
# def add_income_tool(
#     name: str,
#     amount: float,
#     month: str
# ) -> dict:
#     """Add income for a month."""
#     add_income(name, amount, month)
#     return {"status": "Income added successfully"}

# @mcp.tool()
# def add_expense_tool(
#     name: str,
#     amount: float,
#     month: str
# ) -> dict:
#     """Add expense for a month."""
#     add_expense(name, amount, month)
#     return {"status": "Expense added successfully"}

# @mcp.tool()
# def get_summary(month: str) -> dict:
#     """Get monthly budget summary with income, expenses, and balance."""
#     incomes = list_incomes(month)
#     expenses = list_expenses(month)

#     total_income = sum(i["amount"] for i in incomes)
#     total_expense = sum(e["amount"] for e in expenses)

#     return {
#         "month": month,
#         "total_income": total_income,
#         "total_expense": total_expense,
#         "balance": total_income - total_expense,
#         "income_list": [dict(i) for i in incomes],
#         "expense_list": [dict(e) for e in expenses]
#     }

# # ---------------- Run Server ---------------- #

# if __name__ == "__main__":
#     import sys
#     # This ensures any errors go to the log file, not the main communication channel
#     try:
#         mcp.run()
#     except Exception as e:
#         sys.stderr.write(f"Server crashed: {e}\n")
#         sys.exit(1)

# # if __name__ == "__main__":
# #     mcp.run(transport="http", host="127.0.0.1", port=8000)



















# """
# MCP Budget Tracker Server - FIXED VERSION
# ==========================================
# This version fixes the bugs in your original code.
# """

# from mcp.server import Server
# from mcp.server.stdio import stdio_server
# from mcp.types import Tool, TextContent
# from models import create_tables
# from crud import add_income, add_expense, list_incomes, list_expenses
# import json

# # Initialize MCP server
# app = Server("budget-tracker")

# # Create database tables
# create_tables()

# # ---------------- MCP TOOLS ---------------- #

# @app.list_tools()
# async def list_tools() -> list[Tool]:
#     """List available tools"""
#     return [
#         Tool(
#             name="add_income",
#             description="Add income for a month",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "name": {
#                         "type": "string",
#                         "description": "Income source name"
#                     },
#                     "amount": {
#                         "type": "number",
#                         "description": "Income amount"
#                     },
#                     "month": {
#                         "type": "string",
#                         "description": "Month (e.g., 'January', '2024-01')"
#                     }
#                 },
#                 "required": ["name", "amount", "month"]
#             }
#         ),
#         Tool(
#             name="add_expense",
#             description="Add expense for a month",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "name": {
#                         "type": "string",
#                         "description": "Expense name"
#                     },
#                     "amount": {
#                         "type": "number",
#                         "description": "Expense amount"
#                     },
#                     "month": {
#                         "type": "string",
#                         "description": "Month (e.g., 'January', '2024-01')"
#                     }
#                 },
#                 "required": ["name", "cost", "month"]  # 🐛 FIX 1: Changed "amount" to "cost"
#             }
#         ),
#         Tool(
#             name="get_summary",
#             description="Get monthly budget summary with income, expenses, and balance",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "month": {
#                         "type": "string",
#                         "description": "Month (e.g., 'January', '2024-01')"
#                     }
#                 },
#                 "required": ["month"]
#             }
#         )
#     ]

# @app.call_tool()
# async def call_tool(name: str, arguments: dict) -> list[TextContent]:
#     """Handle tool calls"""
    
#     if name == "add_income":
#         add_income(
#             arguments["name"],
#             arguments["amount"],
#             arguments["month"]
#         )
#         return [TextContent(
#             type="text",
#             text=json.dumps({"status": "Income added successfully"})
#         )]
    
#     elif name == "add_expense":
#         add_expense(
#             arguments["name"],
#             arguments["amount"],  # 🐛 FIX 2: Changed from "amount" to "cost"
#             arguments["month"]
#         )
#         return [TextContent(
#             type="text",
#             text=json.dumps({"status": "Expense added successfully"})
#         )]
    
#     elif name == "get_summary":
#         month = arguments["month"]
#         incomes = list_incomes(month)
#         expenses = list_expenses(month)
        
#         total_income = sum(i["amount"] for i in incomes)
#         total_expense = sum(e["amount"] for e in expenses)  # 🐛 FIX 3: Changed from "amount" to "cost"
        
#         summary = {
#             "month": month,
#             "total_income": total_income,
#             "total_expense": total_expense,
#             "balance": total_income - total_expense,
#             "income_list": [dict(i) for i in incomes],
#             "expense_list": [dict(e) for e in expenses]
#         }
        
#         return [TextContent(
#             type="text",
#             text=json.dumps(summary, indent=2)
#         )]
    
#     else:
#         raise ValueError(f"Unknown tool: {name}")

# async def main():
#     """Run the MCP server"""
#     async with stdio_server() as (read_stream, write_stream):
#         await app.run(
#             read_stream,
#             write_stream,
#             app.create_initialization_options()
#         )

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())














# from mcp.server import Server
# from mcp.server.stdio import stdio_server
# from mcp.types import Tool, TextContent
# from models import create_tables
# from crud import add_income, add_expense, list_incomes, list_expenses
# import json

# # Initialize MCP server
# app = Server("budget-tracker")

# # Create database tables
# create_tables()

# # ---------------- MCP TOOLS ---------------- #

# @app.list_tools()
# async def list_tools() -> list[Tool]:
#     """List available tools"""
#     return [
#         Tool(
#             name="add_income",
#             description="Add income for a month",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "name": {
#                         "type": "string",
#                         "description": "Income source name"
#                     },
#                     "amount": {
#                         "type": "number",
#                         "description": "Income amount"
#                     },
#                     "month": {
#                         "type": "string",
#                         "description": "Month (e.g., 'January', '2024-01')"
#                     }
#                 },
#                 "required": ["name", "amount", "month"]
#             }
#         ),
#         Tool(
#             name="add_expense",
#             description="Add expense for a month",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "name": {
#                         "type": "string",
#                         "description": "Expense name"
#                     },
#                     "cost": {
#                         "type": "number",
#                         "description": "Expense cost"
#                     },
#                     "month": {
#                         "type": "string",
#                         "description": "Month (e.g., 'January', '2024-01')"
#                     }
#                 },
#                 "required": ["name", "amount", "month"]
#             }
#         ),
#         Tool(
#             name="get_summary",
#             description="Get monthly budget summary with income, expenses, and balance",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "month": {
#                         "type": "string",
#                         "description": "Month (e.g., 'January', '2024-01')"
#                     }
#                 },
#                 "required": ["month"]
#             }
#         )
#     ]

# @app.call_tool()
# async def call_tool(name: str, arguments: dict) -> list[TextContent]:
#     """Handle tool calls"""
    
#     if name == "add_income":
#         add_income(
#             arguments["name"],
#             arguments["amount"],
#             arguments["month"]
#         )
#         return [TextContent(
#             type="text",
#             text=json.dumps({"status": "Income added successfully"})
#         )]
    
#     elif name == "add_expense":
#         add_expense(
#             arguments["name"],
#             arguments["amount"],
#             arguments["month"]
#         )
#         return [TextContent(
#             type="text",
#             text=json.dumps({"status": "Expense added successfully"})
#         )]
    
#     elif name == "get_summary":
#         month = arguments["month"]
#         incomes = list_incomes(month)
#         expenses = list_expenses(month)
        
#         total_income = sum(i["amount"] for i in incomes)
#         total_expense = sum(e["amount"] for e in expenses)
        
#         summary = {
#             "month": month,
#             "total_income": total_income,
#             "total_expense": total_expense,
#             "balance": total_income - total_expense,
#             "income_list": [dict(i) for i in incomes],
#             "expense_list": [dict(e) for e in expenses]
#         }
        
#         return [TextContent(
#             type="text",
#             text=json.dumps(summary, indent=2)
#         )]
    
#     else:
#         raise ValueError(f"Unknown tool: {name}")

# async def main():
#     """Run the MCP server"""
#     async with stdio_server() as (read_stream, write_stream):
#         await app.run(
#             read_stream,
#             write_stream,
#             app.create_initialization_options()
#         )

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())