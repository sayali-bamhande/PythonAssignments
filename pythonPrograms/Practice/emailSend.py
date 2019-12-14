import smtplib
from urllib import request
from urllib.request import urlopen


def isConnected():
    try:
        urlopen('http://216.58.192.142', timeout=10)
        return True
    except request.URLError as err:
        print(err)
        return False


def mailSender(eid, pwd, to, text):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(eid, pwd)
        server.sendmail(eid, to, text)
        server.close()
        print("Email sent successfully...")
    except Exception as e:
        print("Unable to send email", e)


def main():
    try:
        emailId = "sayali.bamhande@gmail.com"
        pwd = "****"
        connected = isConnected()
        t = "hello"
        if connected:
            SUBJECT = "Love u Dabbi maau"
            TEXT = "Ikde bagh dabbi maaaau <eom>"
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            to = "patilmeet007@gmail.com"
            mailSender(emailId, pwd, to, message)
        else:
            print("No internet....")
    except Exception as e:
        print("Invalid argument ", e)


if __name__ == "__main__":
    main()
