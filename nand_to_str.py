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

    # Write the reformatted code to the output file
    with open(output_file_path, "w") as f:
        f.write(code)

    print(f"Reformatted structural Verilog written to {output_file_path}")