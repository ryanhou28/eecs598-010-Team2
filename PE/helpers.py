# Helper functions


def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def twos_to_dec(binary_array):
    # Convert a binary array of bits of the 8-bit twos complement to a decimal number
    if not binary_array:
        return 0

    # Check if the number is negative (MSB is 1)
    is_negative = binary_array[-1] == 1

    if is_negative:
        # Invert the bits
        inverted_array = [1 - bit for bit in binary_array]

        # Add 1 to the inverted array
        carry = 1
        for i in range(len(inverted_array)):
            inverted_array[i] += carry
            if inverted_array[i] == 2:
                inverted_array[i] = 0
                carry = 1
            else:
                carry = 0

        # Convert to number and negate
        number = -sum(bit * (2 ** i) for i, bit in enumerate(inverted_array))
    else:
        # Convert to number directly
        number = sum(bit * (2 ** i) for i, bit in enumerate(binary_array))

    return number

def twos_complement_bin(num):
    # Generate a binary array of bits of the 8-bit twos complement of the number
    # Saturate the bit array if the number is out of range
    if num < -128:
        num = -128
    elif num > 127:
        num = 127

    if num < 0:
        num = 256 + num

    bin_str = bin(num)[2:].zfill(8)

    binarr = [int(x) for x in bin_str]

    # Flip the binarr so that the LSB is at the beginning
    binarr.reverse()

    return binarr