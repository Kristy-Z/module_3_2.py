def send_email(message, recipient, *, sender = 'university.help@gmail.com' ):

    tuple = ('.com', '.ru', '.net')
    r = recipient.endswith(tuple)
    s = sender.endswith(tuple)

    if '@' in recipient and '@' in sender:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif '@' not in recipient and '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} ')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return

send_email('Привет!', 'kristy38rus@mail.ru', sender = 'university.help@gmail.com')
send_email('Привет!', 'kristy38rus@mail.ru')
send_email('Привет!', 'com.kristy38rus', sender = 'university.help@gmail.com')
send_email('Привет!', 'university.help@gmail.com', sender = 'university.help@gmail.com')
