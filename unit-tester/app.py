import streamlit as st
from utils.folder_utils import find_python_functions

st.title("Generate all unit-tests you need")

# Enter a directory path
target_directory = st.text_input(
    "Directory or github url", placeholder="/path/to/your/directory"
)
st.write(target_directory)


# Find all Python functions in the specified directory
python_functions = find_python_functions(target_directory)
st.write(python_functions)

# # Generate pytest tests for each function
# pytest_tests = generate_tests_for_functions(python_functions)

# # Run the generated tests
# for test_case in pytest_tests:
#     test_case()

# Display directory content

# Select a folder or a file

# Display files content

# Select a list of function

# Send function content to LLM

# Display LLM output

# Run the LLM output to test the test

# Edit the test

# Write the test into the directory into "tests directory"
