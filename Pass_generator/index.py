from algorithm import generate_password, generate_password2

def run():
  print("Program is running 🏃")
  long = int(input("Type how many characters you want your password: ?"))
  password = generate_password2(long)
  print(password)

if __name__ == "__main__":
  run()