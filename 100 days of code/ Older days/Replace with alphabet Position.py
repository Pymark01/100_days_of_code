alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Input = ").lower()
def alphabet_position(input_text):
    output = ""
    for char in input_text:
        if char in alphabet:
            position = str(alphabet.index(char) + 1)
            output += position + " "
        else:
            output += ""
    print(f'Output = "{output} "')

alphabet_position(input_text=text)
