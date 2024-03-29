import os
import importlib.util
import inspect
from data_model.function_model import FunctionInfos
from loguru import logger
from utils.text_cleaning import clean_llm_output


def find_python_functions(directory, sub_directory=None):
    functions = []
    if sub_directory:
        directory += sub_directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                logger.info(file)
                module_name = os.path.splitext(file)[0]
                module_path = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                    for name, obj in inspect.getmembers(module):
                        if inspect.isfunction(obj):
                            function_ = FunctionInfos(
                                module_name=module_name,
                                module_path=module_path,
                                function=obj,
                            )
                            functions.append(function_)
                except:
                    logger.exception(f"{file} contains uninstalled dependencies")

    return functions


def extract_text_from_function(function: FunctionInfos) -> str:
    return inspect.getsource(function.function)


def create_test_file(path: str, script_content: str, mode: str = "w") -> None:
    with open(path, mode) as f:
        f.write(script_content)


def create_directory_and_subdirectory_if_not_exists_with_init(
    root_path: str, path: str
) -> None:
    list_sub = path.split(root_path)[1].split("/")[1:-1]
    path_tests = create_tests_folder_path(root_path)
    create_directory_if_not_exists_with_init(path_tests)
    path_sub = path_tests
    for sub in list_sub:
        path_sub += sub + "/"
        create_directory_if_not_exists_with_init(path_sub)


def create_tests_folder_path(root_path: str) -> str:
    return root_path + "/tests/"


def create_directory_if_not_exists_with_init(path: str) -> None:
    create_directory_if_not_exists(path)
    add_init_file(path)


def create_directory_if_not_exists(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def add_init_file(path: str) -> None:
    with open(path + "__init__.py", "a"):
        os.utime(path, None)


def create_test_file_path(
    root_path: str, module_path: str, test_module_path: str
) -> None:
    return (
        create_tests_folder_path(root_path)
        + "/".join(module_path.split(root_path)[1].split("/")[1:-1])
        + "/"
        + test_module_path
    )


def append_or_create_test_file(path_test_module, text_clean_content_test):
    mode = "w"
    if os.path.exists(path_test_module):
        mode = "a"
    create_test_file(path_test_module, text_clean_content_test, mode=mode)


def read_clean_close(path_test_module: str) -> None:
    with open(path_test_module, "r") as f:
        data = f.read()

    data_cleaned = clean_llm_output(data)

    with open(path_test_module, "w") as f:
        f.write(data_cleaned)
