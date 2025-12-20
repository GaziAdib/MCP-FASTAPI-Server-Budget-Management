from pydantic import BaseModel, Field
from typing import Optional


# income schema

class IncomeCreate(BaseModel):
    name: str
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    month: str
    


# Expense schema 
class ExpenseCreate(BaseModel):
    name: str
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    month: str    