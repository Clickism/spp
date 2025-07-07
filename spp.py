# Written by: Yagiz Aktas

# MIT License
#
# Copyright (c) 2025 Yagiz Aktas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys

def parse_spp_file(input_file: str) -> list[str]:
    file = open(input_file, 'r')
    lines = file.readlines()
    constants = []
    output_lines = []
    for line in lines:
        if line.startswith('.equ'):
            parts = line.split()
            if len(parts) == 4:
                name = parts[1]
                value = parts[3]
                for (constant_name, constant_value) in constants:
                    if constant_name == name:
                        print(f"Error: Constant {name} already defined as {constant_value}")
                        sys.exit(1)
                    else:
                        value = value.replace(constant_name, constant_value)
                constants.append((name, value))
                print(f"Added constant: {name} = {value}")
            else:
                print(f"Error: Invalid .equ constant declaration: {line.strip()}")
                sys.exit(1)
        else:
            if '#' in line:
                code, comment = line.split('#', 1)
                for (name, value) in constants:
                    code = code.replace(name, value)
                line = code + '#' + comment
            else:
                for (name, value) in constants:
                    line = line.replace(name, value)
            output_lines.append(line)

    return output_lines

def main():
    if len(sys.argv) < 2:
        print("Usage: python spp.py <input_file> [output_file]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.rstrip('.sp') + '.s'
    output_lines = parse_spp_file(input_file)
    with open(output_file, 'w') as out_file:
        for line in output_lines:
            out_file.write(line)
    print(f"Output written to {output_file}")
    pass

version = "0.1"

if __name__ == "__main__":
    print("-----------------")
    print(f"SPP Compiler {version}")
    print("-----------------")
    main()