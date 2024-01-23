import streamlit as st
from utils.folder import (
    create_directory_and_subdirectory_if_not_exists_with_init,
    create_test_file,
    create_test_file_path,
    find_python_functions,
    extract_text_from_function,
)
from utils.llm import generate_test, add_imports
from utils.text_cleaning import clean_llm_output

st.title("Generate all unit-tests you need")

# Enter a directory path
target_directory = st.text_input(
    "Directory or github url", placeholder="/path/to/your/directory"
)
st.write(target_directory)


# Find all Python functions in the specified directory
list_functions = find_python_functions(target_directory)
st.write(list_functions)

# # Generate pytest tests for each function
for funct in list_functions:
    module_path = funct.module_path
    function_name = funct.function.__name__
    # Directory manipulation
    create_directory_and_subdirectory_if_not_exists_with_init(
        target_directory, module_path
    )
    name_test_module = f"test_{funct.module_name}.py"
    path_test_module = create_test_file_path(
        target_directory, funct.module_path, name_test_module
    )

    lines_function = extract_text_from_function(funct)
    raw_txt_test_generated = generate_test(lines_function)
    text_content_test = add_imports(
        raw_txt_test_generated, target_directory, module_path, function_name
    )
    text_clean_content_test = clean_llm_output(text_content_test)

    create_test_file(path_test_module, text_clean_content_test)

