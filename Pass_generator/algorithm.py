import random

def generate_password(long):
  capital_letters = ('A',  'B',  'C',  'D',  'E',  'F',  'G',  'H',  'I',  'J',  'K',  'L',  'M', 'N','Ñ','O','P','Q','R','S','T','U','V','X','Y','Z')
  lower_case = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
  numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
  symbols = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"', " ")

  just_one_tuple = capital_letters + lower_case + numbers + symbols

  one_list = []
  for x in range(long):
    char = random.choice(just_one_tuple)
    one_list.append(char)

  return "".join(one_list)
