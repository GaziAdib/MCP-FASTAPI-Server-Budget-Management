from pydantic import BaseModel

# Income Schema 

class IncomeCreate(BaseModel):
    name: str
    amount: float
    month: str


# Expense Schema 
class ExpenseCreate(BaseModel):
    name: str
    amount: float
    month: str