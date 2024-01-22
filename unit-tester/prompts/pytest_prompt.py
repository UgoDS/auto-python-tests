def generate_pytest_code(text_input: str):
    return [
        {
            "role": "system",
            "content": f"""Write a python using pytest and parametrize for this function:
            {text_input}""",
        },
        {
            "role": "user",
            "content": text_input,
        },
    ]
