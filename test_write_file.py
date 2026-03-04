import os
from functions.write_files import write_file

def test_write_file():
    print("Result for current file:")
    print(f'  {write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')
    print("Result for current file:")
    print(f'  {write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
    print("Result for current file:")
    print(f'  {write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')         
 







if __name__ == "__main__":
    test_write_file()