message = input()
recipient = input()
sender = 'university.help@gmail.com'

def send_email(message, recipient, * sender):
    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    if '@' not in message and recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} ')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email(message, recipient, sender)



