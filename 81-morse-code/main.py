ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def convert_to_morse(message):
    morse = []  # Will contain Morse versions of letters
    for char in message:
        if char in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[char])
    return " ".join(morse)

#Creating a while loop that continues to execute the program if the user types 'yes'. 
should_continue = True
while should_continue:
  message = input("Type your message:\n").upper()
  morse = convert_to_morse(message)
  print("### Morse Code ###")
  print(morse)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if result == 'no':
    should_continue = False
    print("Goodbye")