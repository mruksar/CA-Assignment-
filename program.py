# Q1: Signed Binary Arithmetic using 8-bit 2's Complement

def to_8bit_binary(num):
    return format(num & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def subtract(a, b):
    # Represent operands in 8-bit 2's complement
    bin_a = to_8bit_binary(a)
    bin_b = to_8bit_binary(b)

    # 2's complement of B
    complement_b = to_8bit_binary(~b + 1)

    # Perform subtraction using A + 2's complement of B
    result_unsigned = int(bin_a, 2) + int(complement_b, 2)

    # Keep only the lower 8 bits
    result_binary = format(result_unsigned & 0xFF, '08b')
    result_decimal = signed_value(result_binary)

    # Overflow detection for subtraction
    overflow = ((a < 0) != (b < 0)) and ((result_decimal < 0) != (a < 0))

    print("\n--------------------------------")
    print("Expression:", a, "-", "(" + str(b) + ")")
    print("--------------------------------")
    print("First operand (8-bit):       ", bin_a)
    print("Second operand (8-bit):      ", bin_b)
    print("2's complement of second:    ", complement_b)
    print("Binary addition result:      ", bin(result_unsigned)[2:])
    print("Final 8-bit binary result:    ", result_binary)
    print("Final decimal result:         ", result_decimal)
    print("Arithmetic overflow:          ", "Yes" if overflow else "No")


# (a) 45 - (+19)
subtract(45, 19)

# (b) (-35) - (-12)
subtract(-35, -12)