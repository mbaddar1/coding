"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=238827593802550&c=282010630480533&ppid=454615229006519&practice_plan=1
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678

"""


def rotationalCipher(input, rotation_factor):
    # Write your code here
    out = ""
    a_code = ord('a')
    A_code = ord('A')
    z_code = ord('z')
    Z_code = ord('Z')
    zero_code = ord('0')
    nine_code = ord('9')
    for c in input:
        c_order = ord(c)
        chr_diff = Z_code - A_code + 1
        num_diff = nine_code - zero_code + 1
        if c.isalpha():
            max_order = Z_code if c.isupper() else z_code
            start_order = A_code if c.isupper() else a_code
            if c_order + rotation_factor < max_order:
                new_order = c_order + rotation_factor
            else:
                shift_ = (c_order + rotation_factor - max_order - 1) % chr_diff
                new_order = start_order + shift_
            new_char = chr(new_order)
        elif c.isnumeric():

            if c_order + rotation_factor < nine_code:
                new_order = c_order + rotation_factor
            else:
                shift_ = (c_order + rotation_factor - nine_code - 1) % num_diff
                new_order = zero_code + shift_
            new_char = chr(new_order)
        else:
            new_char = c  # just pass it
        out += new_char

    return out


if __name__ == "__main__":
    # input_1 = "All-convoYs-9-be:Alert1."
    # rotation_factor_1 = 4
    # expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    # output_1 = rotationalCipher(input_1, rotation_factor_1)
    # print(expected_1, output_1)
    # input_2 = "abcdZXYzxy-999.@"
    # rotation_factor_2 = 200
    # expected_2 = "stuvRPQrpq-999.@"
    # output_2 = rotationalCipher(input_2, rotation_factor_2)
    # print(expected_2, output_2)
    cases = [("All-convoYs-9-be:Alert1.", 4, "Epp-gsrzsCw-3-fi:Epivx5."),
             ("abcdZXYzxy-999.@", 200, "stuvRPQrpq-999.@"),
             ("Zebra-493?", 3, "Cheud-726?"),
             ("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39, "nopqrstuvwxyzABCDEFGHIJKLM9012345678")]
    for c in cases:
        out = rotationalCipher(c[0], c[1])
        assert out == c[2]
    print(f'Success! for {len(cases)} cases')
