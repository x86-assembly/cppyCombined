"""
This is a program to combine python and c++ code into one file.

for more information see README.MD
"""


import json

def get_file_contents(path):
  with open(path, 'r') as file:
    return file.read()

def encode_python(file_path):
  return json.dumps(get_file_contents(file_path))[1:-1]
def clean_cpp(file_path):
  return get_file_contents(file_path).replace("\n", "")

# Usage:
python = 'python.py'
cplusplus = 'cplusplus.cpp'
escaped_python = encode_python(python)
escaped_cplusplus = clean_cpp(cplusplus)
cplusplus_includes = get_file_contents("cplusplusincludes.cpp")
cplusplus_includes += "\n#define __debug__ int cool(){\n#define license }\n#define copyright return 0"

program = f"{cplusplus_includes}\n#define exec(r) r\n__debug__\nexec(\"{escaped_python}\");\ncopyright;\nlicense\n#define False {escaped_cplusplus}\nFalse;"

with open("your_final_program.cppy", "w") as f:
  f.write(program)
