def generate_budget_summary(income, expenses):
    total_expense = sum(expenses.values())
    savings = income - total_expense
    return f"Your total savings this month: ₹{savings}"
from transformers import pipeline

# Load a conversational model
chatbot = pipeline("text-generation", model="gpt2")

def get_finance_response(prompt):
    full_prompt = f"You are a personal finance assistant. {prompt}"
    response = chatbot(full_prompt, max_length=100, do_sample=True)
    return response[0]['generated_text']
