# Проект Django + Telegram-бот

## Описание
Этот проект включает Django API для хранения информации о телеграм-пользователях и Telegram-бота, который регистрирует пользователей и показывает их информацию.

## Установка и запуск

### Требования
- Python 3.8+
- Память и свободное место для установки зависимостей

### Шаги

1. Клонируйте или распакуйте архив.
2. Создайте виртуальное окружение:
```bash  
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  
Установите зависимости:
bash
pip install -r requirements.txt  
Выполните миграции и запустите сервер Django:
bash
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
Запустите Telegram-бот:
bash
python bot_main.py  
В Telegram найдите бота по вашему токену, используйте команды:
/start — зарегистрировать пользователя
/myinfo — получить информацию о себе
Важное
Убедитесь, что сервер Django работает на http://127.0.0.1:8000/.
API разрешает все домены (разрешение CORS для теста).
Внимание
Обязательно замените BOT_TOKEN в bot_main.py на свой реальный токен.

Готовый проект — что внутри
Django проект с настроенной API и CORS
Телеграм-бот с командами /start и /myinfo
