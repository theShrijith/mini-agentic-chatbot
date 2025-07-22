def calculator_tool(expression: str) -> str:
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: {str(e)}" 