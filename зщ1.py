import shlex

command = input("VFS> ").strip().lower()

def parse_with_shlex(input_string):
    try:
        return shlex.split(input_string)
    except ValueError as e:
        return f"Ошибка парсинга: {e}"

test_cases = [
    'echo "Hello World"',
    'copy "C:\\Program Files\\file.txt" backup',
    'command "arg with spaces" regular "another quoted"',
    'text with "nested \\"quotes\\"" inside',
    'empty "" quotes',
    'mixed "quoted" and unquoted']
for test in test_cases:
    result = parse_with_shlex(test)
    print(result)