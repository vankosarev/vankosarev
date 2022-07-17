import smtplib
import pprint


def send_email(message):
    sender = "ivankosarev07@gmail.com"
    pasword = "310970qq"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, pasword)
        server.sendmail(sender,sender,message)

        return "отправлено"
    except Exception as _ex:
        return f"{_ex}\жопа" 
    

def main():
    message = str(input("сообщениe: "))
    print(send_email(message = message))

if __name__ == "__main__":
    main()

