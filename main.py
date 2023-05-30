import keyboard
import random

key_is_pressed = False

def main():
  print("What is the ICAO code?")
  icao = input()
  print("What type of ATIS? (D for departure, A for arrival, C for combined)")
  atis_type = input()

  while True:
    while True:
      print("Press space to update, or Q to quit")
      key = keyboard.read_hotkey()
      if key == "q": 
        exit()
      elif key == "space":
        update_atis()
      else:
        break

def update_atis():
  letter = random.randint(1, 26)
  print(letter)
   
main()
