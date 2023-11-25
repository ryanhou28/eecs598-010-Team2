import re
import argparse

def delete_comments(code):
    # Regular expression to match the comment pattern with syntax /* ... */ or //
    pattern = r"(/\*.*?\*/)|(//.*?$)"

    # Delete all occurrences of the pattern in the provided code
    code = re.sub(pattern, "", code)

    return code

def delete_par(code):
    # Regular expression to find patterns that start with (* and ends with *)
    pattern = r"\(\*.*?\*\)"

    # Delete all occurrences of the pattern in the provided code
    code = re.sub(pattern, "", code)

    return code


def reformat_gates(code):
    # Regular expression to find the NAND structure
    nand_pattern = r"NAND\s+\w+\s*\(\s*\.A\(([^)]+)\),\s*\.B\(([^)]+)\),\s*\.Y\(([^)]+)\)\s*\);"

    def replace_pattern(match):
        # Extract the variables from the match
        var1, var2, var3 = match.group(1), match.group(2), match.group(3)
        # Return the reformatted string
        return f"nand ({var3}, {var1}, {var2});"

    code = re.sub(nand_pattern, replace_pattern, code)

    return code


def replace_zero_inputs(code):
    # Define the pattern to match the nand statements
    pattern = r"nand\s*\([^)]*\)"

    # Find all matches of nand statements
    matches = re.findall(pattern, code)

    # Iterate over the matches
    for match in matches:
        # Replace occurrences of 1'h0 with "wire_zeros" inside each nand statement
        replaced_match = re.sub(r"1'h0", "wire_zeros", match)
        code = code.replace(match, replaced_match)

    # Now define the wire_zeros wire in the module
    # Find the first wire declaration
    pattern = r"wire\s+\w+\s*;"
    match = re.search(pattern, code)

    zero_wire_declaration = f'wire wire_zeros;\n  assign wire_zeros = 1\'b0;\n  '
    code = code.replace(match.group(0), zero_wire_declaration + match.group(0))

    return code

def expand_arrays(code):
    # Define the pattern to match the array declarations
    pattern = r"(input|wire|output|reg)\s+\[\s*(\d+)\s*:\s*(\d+)\s*\]\s+(\w+)\s*;"

    # Find all matches in the code
    matches = re.findall(pattern, code)

    # Iterate over the matches
    for match in matches:
        declaration_type, number1, number2, wirename = match
        number1 = int(number1)
        number2 = int(number2)

        # Expand the array declaration into multiple single wire declarations
        single_declarations = []
        for i in range(number2, number1 + 1):
            single_declaration = f"{declaration_type} {wirename}_{i}_;"
            single_declarations.append(single_declaration)

        # Replace the array declaration with the single declarations
        array_declaration = f"{declaration_type} [{number1}:{number2}] {wirename};"
        code = code.replace(array_declaration, "\n  ".join(single_declarations))

        # Replace the input declaration in the module with multiple single wires
        if declaration_type == "input" or declaration_type == "output":
            # Find the module declaration code
            pattern = r"module\s+\w+\s*\([^)]*\)\s*;"

            # Find the module declaration
            match = re.search(pattern, code)

            # Extract the module declaration
            module_declaration = match.group(0)

            # Find the input ports in the module declaration, which are words in the brackets separated by commas
            pattern = r"\([^)]*\)"
            match = re.search(pattern, module_declaration)
            ports = match.group(0)[1:-1].split(",")
            ports = [port.strip() for port in ports]

            # Find a match from this list of ports as the variable wirename
            for port in ports:
                if port == wirename:
                    # Generate the sinlge wire declarations
                    single_declarations = []
                    for i in range(number2, number1 + 1):
                        single_declaration = f"{wirename}_{i}_"
                        single_declarations.append(single_declaration)
                    break
            
            # Replace the declaration with the single declarations
            # Search for the port in the module declaration
            pattern = rf"\b{wirename}\b"
            match = re.search(pattern, module_declaration)
            # Replace the port with the single declarations
            new_module_declaration = module_declaration.replace(match.group(0), ", ".join(single_declarations))
            # Replace the module declaration in the code
            code = code.replace(module_declaration, new_module_declaration)


    return code

def move_in_out_reg_up(code):
    # The scripts require that the input, output and reg declarations are at the top of the module
    # Find all input, output, and register declarations
    pattern = r"(input|output|reg)\s+(\w+)\s*;"
    matches = re.findall(pattern, code)

    # Record the name of each declaration
    var_dict = {}

    # For every match, record the name of the declaration and replace it with an empty string
    for match in matches:
        declaration_type, name = match
        if declaration_type == "input":
            var_dict[name] = "input"
        elif declaration_type == "output":
            var_dict[name] = "output"
        elif declaration_type == "reg":
            var_dict[name] = "reg"
    
    # Delete the found matches from the code
    code = re.sub(pattern, "", code)
    
    # Add the declarations back to the top of the module
    # Find the module declaration
    pattern = r"module\s+\w+\s*\([^)]*\)\s*;"
    match = re.search(pattern, code)
    module_declaration = match.group(0)

    # Add the declarations back to the top of the module
    input_declaration_code = ""
    output_declaration_code = ""
    reg_declaration_code = ""

    for name in var_dict:
        if var_dict[name] == "input":
            input_declaration_code += var_dict[name] + " " + name + ";\n  "
        elif var_dict[name] == "output":
            output_declaration_code += var_dict[name] + " " + name + ";\n  "
        elif var_dict[name] == "reg":
            reg_declaration_code += var_dict[name] + " " + name + ";\n  "

    code = code.replace(match.group(0), match.group(0) + input_declaration_code + output_declaration_code + reg_declaration_code)

    return code
    
def replace_square_brackets(code):
    # Regular expression to find square brackets
    pattern = r"\[([^\]]+)\]"
    # Replace the square brackets with underscores
    code = re.sub(pattern, r"_\1_", code)

    return code

def replace_slash(code):
    # Regular expression to find \
    pattern = r"\\"
    # Replace the square brackets with underscores
    code = re.sub(pattern, r"_", code)

    return code

if __name__ == "__main__":
    # Parse the input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the file to be converted")
    parser.add_argument("-o", "--output", help="Path to the output file")
    args = parser.parse_args()

    # Get the file path
    file_path = args.file_path

    # Set the output file path
    if args.output:
        output_file_path = args.output
    else:
        # Default: file_name_structural.v
        output_file_path = file_path.split(".")[0] + "_structural.v"

    # Open the file
    with open(file_path, "r") as f:
        code = f.read()

    # Reformat
    code = delete_comments(code)
    code = delete_par(code)
    code = reformat_gates(code)
    code = replace_zero_inputs(code)
    code = expand_arrays(code)
    code = replace_square_brackets(code)
    code = replace_slash(code)
    code = move_in_out_reg_up(code)

    # Write the reformatted code to the output file
    with open(output_file_path, "w") as f:
        f.write(code)

    print(f"Reformatted structural Verilog written to {output_file_path}")