def rot13_decode(input_string):
    result = ""

    for char in input_string:
        ascii_val = ord(char)

        if ascii_val >= ord('a') and ascii_val <= ord('z'):
            result += chr((ascii_val - ord('a') + 13) % 26 + ord('a'))
        elif ascii_val >= ord('A') and ascii_val <= ord('Z'):
            result += chr((ascii_val - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char

    return result

input_string = input("Enter the ROT13 encoded string: ")
print("Decoded string: ", rot13_decode(input_string))