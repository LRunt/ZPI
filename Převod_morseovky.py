from m5stack import *
from m5stack_ui import *
from uiflow import *
from m5stack import touch

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)

MORSE_CODE_DICT = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')', '':''}

morseovka = ""

def buttonA_wasPressed():
  # global params
  global morseovka
  lcd.fill(0x000000)
  lcd.print('A short "."', 0, 0, 0xffffff)
  morseovka = morseovka + "."
  lcd.print(morseovka, 0, 10, 0xffffff)
  translate()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  global morseovka
  lcd.fill(0x000000)
  lcd.print('B short "/"', 0, 0, 0xffffff)
  morseovka = morseovka + "/"
  lcd.print(morseovka, 0, 10, 0xffffff)
  translate()
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  # global params
  global morseovka
  lcd.fill(0x000000)
  lcd.print('C short "Delete"', 0, 0, 0xffffff)
  morseovka = morseovka[:-1]
  lcd.print(morseovka, 0, 10, 0xffffff)
  translate()
  pass
btnC.wasPressed(buttonC_wasPressed)

def buttonA_pressFor():
  # global params
  global morseovka
  lcd.fill(0x000000)
  lcd.print('A long "-"', 0, 0, 0xffffff)
  morseovka = morseovka[:-1]
  morseovka = morseovka + "-";
  lcd.print(morseovka, 0, 10, 0xffffff)
  translate()
  pass
btnA.pressFor(0.5, buttonA_pressFor)

def translate():
  global morseovka
  morseovka_words = morseovka.split('//')
  morseovka_translated = ""
  for word in morseovka_words:
    morseovka_letter = word.split('/')
    for letter in morseovka_letter:
      if letter in MORSE_CODE_DICT:
        morseovka_translated = morseovka_translated + MORSE_CODE_DICT[letter]
      else:
        morseovka_translated = "SYNTAX ERROR"
    morseovka_translated = morseovka_translated + " "
  lcd.print(morseovka_translated, 0, 20, 0xffffff)