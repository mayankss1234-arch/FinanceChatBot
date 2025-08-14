def tailor_response(response, user_type):
    if user_type == "Student":
        return f"Hey there! Here's a simple tip: {response}"
    else:
        return f"As a professional, consider this strategy: {response}"
