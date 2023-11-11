import re
import numpy as np

with open('iol.txt') as file:
    [icnt, ocnt, lcnt] = [int(match.group(1)) for line in file
                          if (match := re.search(r'\((.*?)\)', line))]

# Read the binary data from the file into a list
with open('bin.txt', 'r') as file:
    binary_data = [list(line.strip()) for line in file]

binary_data = [[int(y) for y in x] for x in binary_data]

# Convert the binary data list to a NumPy array
binary_array = np.array(binary_data, dtype=bool)

from_in = binary_array[:, :icnt]
frstl = np.any(from_in, axis=1)
rest_of = binary_array[:, icnt:]
lvlist = [frstl]
reached = frstl
while (not bool(np.all(reached))):
    nu = rest_of @ lvlist[-1][ocnt:]
    lvlist.append(nu)
    reached = np.logical_or(reached, nu)
lvls = np.vstack(lvlist)
lvli = np.argmax(lvls, axis=0)
chks = np.sum(lvls, axis=0)
cch = bool(np.all(chks == 1))
assert cch

print(list(lvli))
