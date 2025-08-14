def spending_insights(expenses):
    if not expenses:
        return "No expense data provided."
    high_spend = max(expenses, key=expenses.get)
    return f"You spend the most on {high_spend}. Consider reducing this to save more."
