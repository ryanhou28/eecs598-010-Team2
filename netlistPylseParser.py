import ply.lex as lex
import ply.yacc as yacc
import random

# ------------------------ LEXER ------------------------

# Dictionary of reserved words
reserved = {
    'module' : 'MODULE',
    'input'  : 'INPUT',
    'output' : 'OUTPUT',
    'wire'   : 'WIRE',
    'buf'    : 'BUF',
    'not'    : 'NOT',
    'and'    : 'AND',
    'or'     : 'OR',
    'endmodule' : 'ENDMODULE',
}

# Define tokens
tokens = [
    'ID',
    # 'NUMBER',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMI',
    # 'COLON',
]

tokens += list(reserved.values())

# Define a dictionary of tokens
# t_NUMBER  = r'\d+'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','
t_SEMI    = r';'
# t_COLON   = r':'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Token rule with some action code, checking for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

# Define a rule to ignore whitespace
t_ignore = ' \t'

# Define error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# ------------------------ END LEXER ------------------------

# ------------------------ PARSER ------------------------

# Define the grammar

# Module declaration
def p_module(p):
    'module_decl : MODULE ID ports SEMI module_items ENDMODULE'
    p[0] = ('module_decl', p[2], p[3], p[5])

def p_ports(p):
    '''ports : LPAREN port_list RPAREN
             | LPAREN RPAREN'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_port_list(p):
    '''port_list : port_list COMMA port
                 | port'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_port(p):
    '''port : INPUT ID
            | OUTPUT ID
            | WIRE ID
            | ID'''
    if len(p) == 3:
        # For cases where there are two elements: INPUT/OUTPUT/WIRE and ID
        p[0] = ('port', p[1], p[2])
    elif len(p) == 2:
        # For the case where there's only an ID
        p[0] = ('port', 'ID', p[1])


# def p_range(p):
#     'range : LPAREN NUMBER COLON NUMBER RPAREN'
#     p[0] = (p[2], p[4])  # Return a tuple representing the 

def p_module_items(p):
    '''module_items : module_items module_item
                    | module_item'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Rule for handling gate primitives instantiation
def p_gate_instantiation(p):
    '''gate_instantiation : buf_instantiation
                          | not_instantiation
                          | or_instantiation
                          | and_instantiation'''
    p[0] = p[1]

def p_buf_instantiation(p):
    'buf_instantiation : BUF LPAREN output_terminal COMMA input_terminal RPAREN SEMI'
    p[0] = ('buf', p[3], p[5])

def p_not_instantiation(p):
    'not_instantiation : NOT LPAREN output_terminal COMMA input_terminal RPAREN SEMI'
    p[0] = ('not', p[3], p[5])

def p_or_instantiation(p):
    'or_instantiation : OR LPAREN output_terminal COMMA input_list RPAREN SEMI'
    p[0] = ('or', p[3], p[5])

def p_and_instantiation(p):
    'and_instantiation : AND LPAREN output_terminal COMMA input_list RPAREN SEMI'
    p[0] = ('and', p[3], p[5])

# Define rules for output_terminal and input_terminal which are basically identifiers (IDs)
def p_output_terminal(p):
    'output_terminal : ID'
    p[0] = p[1]

def p_input_terminal(p):
    'input_terminal : ID'
    p[0] = p[1]

# Input list for gates like OR and AND that can have multiple inputs
def p_input_list(p):
    '''input_list : input_list COMMA input_terminal
                  | input_terminal'''
    if len(p) == 4:  # Multiple inputs
        p[0] = p[1] + [p[3]]
    else:  # Single input
        p[0] = [p[1]]

def p_input_decl(p):
    '''input_decl : INPUT ID SEMI'''
    p[0] = ('input', p[2])

def p_output_decl(p):
    '''output_decl : OUTPUT ID SEMI'''
    p[0] = ('output', p[2])

def p_wire_decl(p):
    'wire_decl : WIRE ID SEMI'
    p[0] = ('wires', p[2])

def p_module_item(p):
    '''module_item : wire_decl
                   | gate_instantiation
                   | input_decl
                   | output_decl'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# ------------------------ END PARSER ------------------------

# Print the AST
def print_ast(ast, level=0):
    indent = "  " * level
    if isinstance(ast, tuple):
        print(f"{indent}{ast[0]}")
        for item in ast[1:]:
            print_ast(item, level + 1)
    elif isinstance(ast, list):
        for item in ast:
            print_ast(item, level)
    elif isinstance(ast, dict):
        for key, value in ast.items():
            print(f"{indent}{key}")
            print_ast(value, level + 1)
    else:  # for leaves of the AST
        print(f"{indent}{ast}")


# ------------------------ GENERATE CODE ------------------------

# Generate the PyLSE code
def generate_code(node):
    node_type = node[0]
    if node_type == 'module_decl':
        return generate_module(node)
    elif node_type == 'ports':
        return generate_ports(node)
    elif node_type == 'port_list':
        return generate_port_list(node)
    elif node_type == 'port':
        return generate_port(node)
    elif node_type == 'module_items':
        return generate_module_items(node)
    elif node_type == 'gate_instantiation':
        return generate_gate_instantiation(node)
    elif node_type == 'buf':
        return generate_buf(node)
    elif node_type == 'not':
        return generate_not(node)
    elif node_type == 'or':
        return generate_or(node)
    elif node_type == 'and':
        return generate_and(node)
    elif node_type == 'output_terminal':
        return generate_output_terminal(node)
    elif node_type == 'input_terminal':
        return generate_input_terminal(node)
    elif node_type == 'input':
        return generate_input(node)
    elif node_type == 'output':
        return generate_output(node)
    elif node_type == 'wires':
        return generate_wires(node)
    elif node_type == 'module_item':
        return generate_module_item(node)
    else:
        print("*** ERROR ***")
        print("Unknown node type:", node_type)
        print(node)
        raise Exception(f"Unknown node type: {node_type}")


# Some global variables to keep track of important info about the module
module_name = []
module_ports = []
input_ports = []
output_ports = []
# Dictionary of the variable names of the splitted wires, value is the number of splitted wires
# Used for counting how many times a wire needs to be split
splitter_dict = {} 

def generate_module(node):
    # node is a tuple like ('module_decl', module_name, ports, items)
    print("Generating code for module")
    name = node[1]
    ports = node[2]
    items = node[3]
    # Generate helper codee that defines the xSFQ gates
    helper_code = f'''
    # Define helpers to ensure same delay numbers (currently the same as PyLSE example)
    def jtl(*args):
        return pylse.jtl(*args, firing_delay=5.7)

    def fa(x, y):
        """ First-arrival cell based on an inverted C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c_inv(jtl(x), jtl(y), firing_delay=9.0)

    def la(x, y):
        """ Last-arrival cell based on a C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c(jtl(x), jtl(y), firing_delay=8.0)

    def s(x):
        return pylse.s(x, firing_delay=4.3)

    def dro(*args):
        return pylse.dro(*args, firing_delay=5.1)\n'''

    module_name.append(name)
    
    # ports_code = ', '.join(generate_code(port) for port in ports)

    items_code = ''
    for item in items:
        item_code = generate_code(item)
        if item_code != '':
            items_code += f'    {item_code}\n'

    # items_code = '\n    '.join(generate_code(item) for item in items)

    # Remove double newlines for better formatting
    items_code = items_code.replace('\n    \n', '')

    input_ports_code = ', '.join(f'{input_port}_p, {input_port}_n' for input_port in input_ports)
    output_ports_code = ', '.join(f'{output_port}' for output_port in output_ports)

    # Add the splitter code
    # Go through every wire in the splitter dictionary
    input_splitter_code = ''
    for wire_name, num_splitters in splitter_dict.items():
        # Two cases:
        #   1. The wire is an input to the module, instantiate the splitter before the items code
        #   2. The wire is instantiated in the middle of the items code, instantiate the splitter after the wire definition

        # Case 1: Wire is an input to the module
        # Check whether this wire is an input to the module
        if wire_name[:-2] in input_ports:
            # This wire is an input to the module
            # Instantiate the splitter before the items code
            input_splitter_code += f'    {wire_name}_spl_ = pylse.split({wire_name}, n={num_splitters}, firing_delay=4.3)\n'
        else:
            # Case 2: wire instantiated in the items code
            # Find where the wire_name is defined in the items_code and insert the splitter code after that
            def insert_splitter_code(items_code, wire_name):
                # Split the code into lines
                lines = items_code.split('\n')
                
                # Find the index of the line with the wire definition
                for i, line in enumerate(lines):
                    if line.strip().startswith(wire_name + ' ='):
                        # Insert the new line after the wire definition
                        new_line = f'''    {wire_name}_spl_ = pylse.split({wire_name}, n={num_splitters}, firing_delay=4.3)'''
                        lines.insert(i + 1, new_line)
                        break  # Assuming only one occurrence, we can break the loop here
                
                # Join the lines back into a single string
                return '\n'.join(lines)
        
            items_code = insert_splitter_code(items_code, wire_name)

    return f'def {name}({input_ports_code}):\n{helper_code}\n{input_splitter_code}\n{items_code}\n\n    return {output_ports_code}\n'

def generate_ports(node):
    # node is a tuple like ('ports', port_list)
    print("Generating code for ports")
    port_list = node[1]
    return ', '.join(generate_code(port) for port in port_list)

def generate_port_list(node):
    # node is a tuple like ('port_list', port_list)
    print("Generating code for port list")
    port_list = node[1]
    return ', '.join(generate_code(port) for port in port_list)

def generate_port(node):
    # node is a tuple like ('port', port_type, port_name)
    print("Generating code for port")
    port_type = node[1]
    port_name = node[2]
    # Create dual-railed ports
    port_p = f'{port_name}_p'
    port_n = f'{port_name}_n'
    # Add the port to the list of ports to the module
    module_ports.append(port_name)

    return f'{port_p}, {port_n}'

def generate_module_items(node):
    # node is a tuple like ('module_items', module_items)
    print("Generating code for module items")
    module_items = node[1]
    
    return '\n    '.join(generate_code(item) for item in module_items)

def generate_gate_instantiation(node):
    # node is a tuple like ('gate_instantiation', gate_instantiation)
    print("Generating code for gate instantiation")
    gate_instantiation = node[1]
    return generate_code(gate_instantiation)

def generate_buf(node):
    # node is a tuple like ('buf', output_terminal, input_terminal)
    print("Generating code for buf")
    output_terminal = node[1]
    input_terminal = node[2]
    if input_terminal in input_ports:
        #   Since we already have dual-railed input we don't need this BUF gate
        return f''
    elif output_terminal in output_ports:
        # If the output terminal is one of the module's outputs, connect the input_terminal to the output
        # return f'{output_terminal} = {input_terminal}'
        return f'{output_terminal} = ' + generate_input_terminal(input_terminal)
    elif 'spl' in output_terminal:
        # This is a splitter
        # Skip splitting and deal with it with the whole module
        # return f'{output_terminal}1, {output_terminal}2 = s({input_terminal})'
        return f''
    else:
        # Raise exception
        raise Exception(f"Unhandled use of buffers.")
        return f''

def generate_not(node):
    # node is a tuple like ('not', output_terminal, input_terminal)
    print("Generating code for not")
    output_terminal = node[1]
    input_terminal = node[2]
    # Check that the input terminal is not one of the inputs to the module
    #   Since we already have dual-railed inputs, we don't need this NOT gate
    if input_terminal in input_ports:
        # If the input terminal is one of the inputs to the module, we don't need this NOT gate
        #   since we already have dual-railed inputs
        return f''
    elif output_terminal in output_ports:
        # If the output terminal is one of the outputs to the module, we don't need this NOT gate
        #   The true output is just the input to the NOT gate
        # return f'{output_terminal} = {input_terminal}'
        return f'{output_terminal} = ' + generate_input_terminal(input_terminal)
    else:
        # Not gate in xSFQ is just connecting the dual-railed terminals
        if input_terminal.endswith('_p'):
            input_terminal_compliment = input_terminal[:-2] + '_n'
        elif input_terminal.endswith('_n'):
            input_terminal_compliment = input_terminal[:-2] + '_p'
        else:
            # Raise exception
            raise Exception(f"Input terminal {input_terminal} is not dual-railed")

        return f'{output_terminal} = {input_terminal_compliment}'

def generate_or(node):
    # node is a tuple like ('or', output_terminal, input_list)
    print("Generating code for or")
    output_terminal = node[1]
    input_list = node[2]
    # input_list_code = ', '.join((input_terminal) for input_terminal in input_list)
    input_list_code = ', '.join(generate_input_terminal(input_terminal) for input_terminal in input_list)
    # input_list_code = ', '.join(generate_input_list(input_list))
    # OR gate in xSFQ is a first-arrival cell
    return f'{output_terminal} = fa({input_list_code})'

def generate_and(node):
    # node is a tuple like ('and', output_terminal, input_list)
    print("Generating code for and")
    output_terminal = node[1]
    input_list = node[2]
    input_list_code = ', '.join(generate_input_terminal(input_terminal) for input_terminal in input_list)
    # input_list_code = ', '.join((input_terminal) for input_terminal in input_list)
    # input_list_code = ', '.join(generate_input_list(input_list))
    # AND gate in xSFQ is a last-arrival cell
    return f'{output_terminal} = la({input_list_code})'

def generate_output_terminal(node):
    # node is a single output terminal
    # NOT USED CURRENTLY
    print("Generating code for output terminal")
    output_terminal = node
    return output_terminal

def generate_input_terminal(node):
    # node is a single input terminal
    print("Generating code for input terminal")
    input_terminal = node
    # Check if the input terminal is a splitter
    if 'spl' in input_terminal:
        # This is a splitter
        # Find the name of the input terminal, ie the name before '_spl_'
        input_name_split = input_terminal.split('_spl')
        var_name = input_name_split[0]
        # If the variable name is not in the splitter count dictionary, add it
        if var_name not in splitter_dict:
            splitter_dict[var_name] = 1
            return f'{var_name}_spl_[0]'
        else:
            splitter_dict[var_name] += 1
            return f'{var_name}_spl_[{splitter_dict[var_name] - 1}]'
    return input_terminal

def generate_input(node):
    # node is a tuple like ('input', input_name)
    print("Generating code for input")
    input_name = node[1]
    # Add the input to the list of inputs to the module
    input_ports.append(input_name)
    # Add the input to the list of ports to the module
    module_ports.append(input_name)
    # return f'{input_name} = Input()'
    return f''

def generate_output(node):
    # node is a tuple like ('output', output_name)
    print("Generating code for output")
    output_name = node[1]
    # Add the output to the list of outputs to the module
    output_ports.append(output_name)
    # Add the output to the list of ports to the module
    module_ports.append(output_name)
    # return f'{output_name} = Output()'
    return f''

def generate_wires(node):
    # node is a tuple like ('wires', wire_name)
    print("Generating code for wires")
    wire_name = node[1]
    # return f'{wire_name} = Wire()'
    return f''

def generate_module_item(node):
    # node is a tuple like ('module_item', module_item)
    print("Generating code for module item")
    module_item = node[1]
    return generate_code(module_item)

def generate_pylse(result):
    # result is the AST
    print("Generating Python code")
    
    # First generate the imports needed
    code = f'import pylse\n\n'

    code += generate_code(result)

    # Generate simulation code
    code += generate_pylse_sim()

    return code

def generate_pylse_sim():
    # Generate the simulation code for the module in PyLSE
    code = f'''
def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1\n\n'''

    # Generate test_single_input function
    code += f'def test_single_input('
    # Generate the input ports
    for input_port in input_ports:
        code += f'{input_port}, '
    # Remove the last comma and space
    code = code[:-2]
    code += f'):\n'
    code += f'    print("Inputs:")\n'
    # print the name of the input ports
    code += f'    print("' + ' '.join(f'{input_port}' for input_port in input_ports) + f'")\n'
    code += f'    print(' + ', '.join(f'{input_port}' for input_port in input_ports) + f')\n'
    for input_port in input_ports:
        code += f'    {input_port}_p_t = inv({input_port})\n'
        code += f'    {input_port}_n_t = {input_port}\n'
    code += f'\n'
    for input_port in input_ports:
        code += f'    {input_port}_p = pylse.inp_at({input_port}_p_t*T, name=\'{input_port}_p\')\n'
        code += f'    {input_port}_n = pylse.inp_at({input_port}_n_t*T, name=\'{input_port}_n\')\n'
    code += f'\n'

    code += f'    return '
    for input_port in input_ports:
        code += f'{input_port}_p, {input_port}_n, '
    # Remove the last comma and space
    code = code[:-2]
    code += f'\n\n'

    # Generate check_events function
    code += f'def check_events(events, T):\n'
    code += f'    print("Output Events:")\n'
    code += f'    print("' + ' '.join(f'{output_port}' for output_port in output_ports) + f'")\n'
    code += f'    print('
    for output_port in output_ports:
        code += f'int(events[\'{output_port}\'][0] < T), '
    # Remove the last comma and space
    code = code[:-2]
    code += f')\n\n'

    # Generate the main function
    code += f'if __name__ == "__main__":\n'
    code += f'    # Create clock signal\n'
    time_period = 100
    code += f'    T = {time_period}  # duration of a phase\n'
    code += "    clk = pylse.inp(start=T/2, period=T, n=4, name='clk')\n"

    # Generate the test inputs
    code += f'    '
    for input_port in input_ports:
        code += f'{input_port}_p, {input_port}_n, '

    # Remove the last comma and space
    code = code[:-2]
    code += f'= test_single_input('
    # Generate random inputs from 0 or 1 for each input
    for input_port in input_ports:
        code += f'{random.randint(0, 1)}, '
    # Remove the last comma and space
    code = code[:-2]
    code += f')\n\n'

    # Instantiate the module
    code += f'    # Instantiate the module\n'
    
    # For each output port, instantiate the output port
    code += f'    '
    for output_port in output_ports:
        code += f'{output_port}, '
    # Remove the last comma and space
    code = code[:-2]

    code += f'= {module_name[0]}('
    # For each input port, instantiate the input port
    for input_port in input_ports:
        code += f'{input_port}_p, {input_port}_n, '
    # Remove the last comma and space
    code = code[:-2]
    code += f')\n\n'

    # Probe outputs
    code += f'    # Probe outputs\n'
    for output_port in output_ports:
        code += f'    pylse.inspect({output_port}, \'{output_port}\')\n'

    # Run the simulation
    code += f'''
    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()


    # Print out the events
    check_events(events, T)
'''

    return code

# ------------------------ END GENERATE CODE ------------------------

# ------------------------ MAIN ------------------------

# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()

# Parse the input Verilog file...
verilog_file = "synth_scripts/comb85/c17_N.v"
# verilog_file = "synth_scripts/comb85/c432_N.v"
verilog_file = "synth_scripts/comb85/c499_N.v"
verilog_file = "synth_scripts/comb85/c880_N.v"
verilog_file = "synth_scripts/comb85/c1355_N.v"
verilog_file = "synth_scripts/comb85/c1908_N.v"
verilog_file = "synth_scripts/comb85/c2670_N.v"
verilog_file = "synth_scripts/comb85/c3540_N.v"
verilog_file = "synth_scripts/comb85/c5315_N.v"
verilog_file = "synth_scripts/comb85/c6288_N.v"

with open(verilog_file, 'r') as file:
    verilog_code = file.read()

# Parse the input Verilog code
result = parser.parse(verilog_code, lexer=lexer)

# Now result contains the AST, we can print it
print_ast(result)

# Assume `ast` is the root of your AST
python_code = generate_pylse(result)

# Write the generated Python code to the file of the same name as the input but to the current directory
# outfile_name = verilog_file.split('.')[0] + '_PyLSE.py' # This saves to the same directory as the input file
outfile_name = verilog_file.split('/')[-1].split('.')[0] + '_PyLSE.py'
with open(outfile_name, 'w') as f:
    f.write(python_code)

print("----------------------------------")
print(python_code)
print("----------------------------------")
print("Saved generated Python code to", outfile_name)


# ------------------------ END MAIN ------------------------