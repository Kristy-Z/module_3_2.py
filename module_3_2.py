def send_email(message, recipient, *, sender = 'university.help@gmail.com' ):

    r = recipient.endswith('.com')  or recipient.endswith('.ru') or recipient.endswith('.net')
    s = sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')

    if '@' not in recipient and sender and r and s is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} ')
    elif '@' in recipient and sender and r and s is True:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return

send_email('Привет!', 'kristy38rus@mail.ru', sender = 'university.help@gmail.com')
send_email('Привет!', 'kristy38rus')
send_email('Привет!', 'com.kristy38rus', sender = 'university.help@gmail.com')
send_email('Привет!', 'university.help@gmail.com', sender = 'university.help@gmail.com')
