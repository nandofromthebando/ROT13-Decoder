# ROT13 Decoder

This Python script decodes a string that has been encoded using the ROT13 encoding method.

## Usage

1. Run the script: `python ROT13Decoder.py`
2. When prompted, enter the ROT13 encoded string.
3. The script will print the decoded string.

## Function

The script contains a single function, `rot13_decode(input_string)`, which takes a string as input and returns the decoded string.

The function works by iterating over each character in the input string. If the character is a lowercase or uppercase alphabetic character, it is shifted 13 places in the alphabet. Non-alphabetic characters are left unchanged.

## Example

Input: `nqzva`
Output: `admin`
