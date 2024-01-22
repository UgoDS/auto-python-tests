import openai
from icecream import ic

from utils.authent import get_openai_key
from prompts.pytest_prompt import generate_pytest_code


get_openai_key()


def generate_test(function_text: str) -> str:
    prompt = generate_pytest_code(function_text)
    raw_output = get_chatgpt_parsing(prompt)
    ic(raw_output)
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
