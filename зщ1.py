import shlex

commands = ["ls", "cd", "exit"] #коммандыы

while True:
    command_line = input("VFS> ")
    try:
        tokens = shlex.split(command_line)  #считка
    except ValueError as err:
        print(f"Ошибка парсинга: {err}")
        continue
    if not tokens:
        continue

    #проверка ввода
    cmd = tokens[0]
    args = tokens[1:]

    if cmd not in commands:
        print(f"Неизвестная команда: {cmd}")
        continue

    if cmd == "ls":
        print()
    elif cmd == "cd":
        print()

    #вывод
    elif cmd == "exit":
        print("Выход из эмулятора.")
        break