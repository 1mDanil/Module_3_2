a = ['.com', '.ru', '.net']

def send_email(message, recepient, sender = 'university.help@gmail.com'):
    if '@' in sender == False or sender.endswith(('.com', '.ru', '.net')) == False :
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recepient}')
    elif '@' in recepient == False or recepient.endswith(('.com', '.ru', '.net')) == False :
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recepient}')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса  {sender} на адрес  {recepient}')
    elif sender == recepient:
        print('Нельзя отправить письмо самому себе')
    else:
        print('Нестандартный отправитель! Письмо отправлено с адреса ', sender, 'на адрес ', recepient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

