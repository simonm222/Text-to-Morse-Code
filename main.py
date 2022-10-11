letters_to_morse_code = {
    "a": "·-",
    "b": "-··",
    "c": "-·-·",
    "d": "-··",
    "e": "·",
    "f": "··-·",
    "g": "--·",
    "h": "····",
    "i": "··",
    "j": "·---",
    "k": "-·-",
    "l": "·-··",
    "m": "--",
    "n": "·-",
    "o": "---",
    "p": "·--·",
    "q": "--·-",
    "r": "·-·",
    "s": "···",
    "t": "-",
    "u": "··-",
    "v": "···-",
    "w": "·--",
    "x": "-··-",
    "y": "-·--",
    "z": "--··",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    "0": "-----"
}


def convert_to_morse_code():
    morse_code_list = []
    word = str(input("Type a sentence here:"))
    list_of_letters = [letter for letter in word]
    for letter in list_of_letters:
        for key in letters_to_morse_code.items():
            if key[0] == letter:
                morse_code_list.append(key[1])
    print(morse_code_list)


convert_to_morse_code()
