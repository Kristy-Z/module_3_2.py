def send_email(message, recipient, *, sender = 'university.help@gmail.com' ):

    tuple = ('.com', '.ru', '.net')
    r = recipient.endswith(tuple)
    s = sender.endswith(tuple)

    if '@' not in recipient or '@' not in sender or r is False or s is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} ')
        return

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')



