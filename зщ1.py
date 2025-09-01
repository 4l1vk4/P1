import shlex

commands = ['cd','ls']
while True:
    command = input("VFS> ").strip().lower()

    def parse_with_shlex(a):
        try:
            return shlex.split(a)
        except ValueError as e:
            return f"Ошибка парсинга: {e}"
