import isort
from black import format_str, FileMode


def clean_llm_output(llm_output: str) -> str:
    return isort_llm_output(black_llm_output(llm_output))


def isort_llm_output(llm_output: str) -> str:
    return isort.code(llm_output)


def black_llm_output(llm_output: str) -> str:
    return format_str(llm_output, mode=FileMode())
