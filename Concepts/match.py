
letter = input("Ingresa una letra: ")

match letter:
  case('A' | 'a'):
    print("Esto es una vocal")
  case('E' | 'e'):
    print("Esto es una vocal")
  case('I' | 'i'):
    print("Esto es una vocal")
  case('O' | 'o'):
    print("Esto es una vocal")
  case('U' | 'u'):
    print("Esto es una vocal")
  case _:
    print('NO ES VOCAL 😠')