import openai
from utils.authent import get_openai_key
from prompts.pytest_prompt import generate_pytest_code


get_openai_key()


def generate_test(function_text: str) -> str:
    prompt = generate_pytest_code(function_text)
    raw_output = get_chatgpt_parsing(prompt)
    return extract_output_message(raw_output)


def get_chatgpt_parsing(messages: list):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )


def extract_output_message(raw_gpt_output: dict):
    return raw_gpt_output["choices"][0]["message"]["content"]


def parse_test_output(test_output: str) -> str:
    return "@" + test_output.split("@")[1]


def add_imports(
    test_output: str, root_path: str, module_path: str, function_name: str
) -> str:
    from_txt = (
        "/".join(module_path.split(root_path)[1].split("/"))
        .replace(".py", "")
        .replace("/", ".")[1:]
    )
    return f"""
import pytest
from {from_txt} import {function_name}

{test_output}
            """
