import shlex

commands = ["ls", "cd", "exit"]
while True:
    command_line = input("VFS> ")
    try:
        user_input = shlex.split(command_line)
    except ValueError as err:
        print(f"Ошибка парсинга: {err}")
        continue
    if not user_input:
        continue
    cmd = user_input[0]
    args = user_input[1:]
    if cmd not in commands:
        print(f"Неизвестная команда: {cmd}")
        continue
    if cmd == "ls":
        print()
    elif cmd == "cd":
        print()
    elif cmd == "exit":
        print("Выход из эмулятора.")
        break