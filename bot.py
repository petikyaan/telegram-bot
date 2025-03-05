import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Используйте ваш токен, полученный от @BotFather
TOKEN = '7491473794:AAGfwaIIobwx6189JvIj3-mbTh0XzUWBgDU'
bot = telebot.TeleBot(TOKEN)

def main_menu():
    """Функция для создания главного меню"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Посмотреть ассортимент"))
    markup.add(KeyboardButton("Сделать заказ"))
    markup.add(KeyboardButton("Связь с администратором"))
    return markup

def back_button():
    """Функция для кнопки 'Назад'"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Назад"))
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Отправка приветственного сообщения с основными командами"""
    welcome_text = "Выберите команду ниже:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "Посмотреть ассортимент")
def show_assortment(message):
    """Отправка ссылки на ассортимент"""
    link = "https://telegra.ph/privet-03-02-78"
    bot.send_message(message.chat.id, f"Для ознакомления с ассортиментом перейдите по ссылке ниже:\n{link}", reply_markup=back_button())

@bot.message_handler(func=lambda message: message.text == "Сделать заказ")
def make_order(message):
    """Вывод инструкции по оформлению заказа"""
    order_text = "Для оформления заказа напишите нашему администратору по ссылке ниже:\n"
    order_text += "https://t.me/ggjoud"
    bot.send_message(message.chat.id, order_text, reply_markup=back_button())

@bot.message_handler(func=lambda message: message.text == "Связь с администратором")
def contact_admin(message):
    """Отправка ссылки на профиль администратора"""
    admin_link = "Вы можете связаться с администратором, перейдя по ссылке ниже:\n"
    admin_link += "https://t.me/ggjoud"
    bot.send_message(message.chat.id, admin_link, reply_markup=back_button())

@bot.message_handler(func=lambda message: message.text == "Назад")
def go_back(message):
    """Возврат в главное меню"""
    bot.send_message(message.chat.id, "Вы вернулись в главное меню.", reply_markup=main_menu())

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
