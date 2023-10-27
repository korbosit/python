import re

def check_password(password):
    # создаем паттерны
    # проверка длины пароля
    # можно использовать проверку len(password)
    # проверка что в строке минимум 8 сиволов, пр  этом пробелы знаки @  и переходы на новую строку не считаются об это говорит /S
    # length_regexp = r"\S{8,}"
    # length_pattern = re.compile(length_regexp)
    length_pattern = re.compile(r"\S{8,}")
    # далее моздаем паттерн для проверки что есть буквы в нижнем регистре
    lowercase_pattern = re.compile(r"[a-z]+")
    # паттерн для проверки что есть буквы в верхнем регистре
    uppercase_pattern = re.compile(r"[A-Z]+")
    # паттерн для проверки наличия хотябы 1 цифры
    number_pattern = re.compile(r"[0-9]+")
    # паттерн для проверки хотя бы одного символа в пароле
    special_symbol_pattern = re.compile(r"[@%#!&*^]+")
    no_whitespace_pattern = re.compile(r"^\S*$")

    # проверка паролей согласно паттернов
    if not re.fullmatch(no_whitespace_pattern, password):
         return (False, "No whitespaces allowed in the password")
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase latter")
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase latter")
    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")
    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbolr @%#!&*^")

    return (True, "Password is valid!")


# print(check_password('asdfASD 2342  !234'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('asdbADGAG'))
# print(check_password('3234sfASDF'))
# print(check_password('asdfASDF3242!&'))

while True:
    password = input("Please enter password: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])
