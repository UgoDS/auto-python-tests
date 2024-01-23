def generate_pytest_code(text_input: str):
    return [
        {
            "role": "system",
            "content": f"""Write a python using pytest and parametrize for this function:
            {text_input}
            Start the code at @pytest.mark.parametrize skip the import part""",
        },
        {
            "role": "user",
            "content": text_input,
        },
    ]