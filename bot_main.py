import telebot
import requests

API_URL = "http://127.0.0.1:8000/api"
BOT_TOKEN = "BOT_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }
    response = requests.post(f"{API_URL}/register", json=data)
    if response.status_code == 200:
        bot.send_message(message.chat.id, f"Вы успешно зарегистрированы! Ваш ID: {response.json().get('id')}")

    elif response.status_code in [400, 409]:
    # Предположим, что это означает, что пользователь уже зарегистрирован
        bot.send_message(message.chat.id, "Вы уже зарегистрированы.")
    else:
        bot.send_message(message.chat.id, "Произошла ошибка при регистрации!")

@bot.message_handler(commands=['myinfo'])
def user_info(message):
    user_id = message.from_user.id
    response = requests.get(f"{API_URL}/user/{user_id}")
    if response.status_code == 200:
        user_data = response.json()
        info_text = (
            f"ID: {user_data.get('user_id')}\n"
            f"Username: {user_data.get('username')}\n"
            f"Зарегистрирован: {user_data.get('created_at')}"
        )
        bot.reply_to(message, info_text)

    elif response.status_code == 404:
        bot.send_message(message.chat.id, "Вы не зарегистрированы! Используйте /start для регистрации.")
    else:
        bot.send_message(message.chat.id, "Ошибка получения информации.")

if __name__ == "__main__":
    bot.polling(none_stop=True)

