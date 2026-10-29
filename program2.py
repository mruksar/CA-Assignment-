# Q2: Rotate Operations on 8-bit Binary Numbers

def rotate_left_without_carry(binary, positions):
    print("\n--- Rotate Left Without Carry (ROL) ---")
    print("Original binary:", binary)

    result = binary

    for i in range(positions):
        msb = result[0]
        result = result[1:] + msb

        print("Step", i + 1, ":", result)

    print("Final 8-bit result:", result)


def rotate_left_with_carry(binary, positions, carry):
    print("\n--- Rotate Left With Carry (RCL) ---")
    print("Original binary:", binary)
    print("Initial carry flag:", carry)

    result = binary

    for i in range(positions):
        msb = result[0]

        # Shift left and insert the old carry at the right
        result = result[1:] + str(carry)

        # Old MSB becomes the new carry
        carry = int(msb)

        print("Step", i + 1, ":", result, "| Carry =", carry)

    print("Final 8-bit result:", result)
    print("Final carry flag:", carry)


# Given binary number
binary_number = "10110110"

# (a) ROL by 2 positions
rotate_left_without_carry(binary_number, 2)

# (b) RCL by 2 positions, assuming initial carry = 0
rotate_left_with_carry(binary_number, 2, 0)