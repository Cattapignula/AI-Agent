import os
from functions.get_file_content import get_file_content

def test_get_file_content():
    print("Result for current file:")
    print(f'  {get_file_content("calculator", "lorem.txt")}')
    print("Result for current file:")
    print(f'  {get_file_content("calculator", "main.py")}')
    print("Result for current file:")
    print(f'  {get_file_content("calculator", "pkg/calculator.py")}')         
    print("Result for '/bin/cat' file:")
    print(f'   {get_file_content("calculator", "/bin/cat")}')
    print(f'   {get_file_content("calculator", "pkg/does_not_exist.py")}')








if __name__ == "__main__":
    test_get_file_content()