import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
        msg = MIMEMultipart()
        msg['from']=eid
        msg['to']=to
        mau = "Dabbi maau"
        body = """Hello %s
        Zopu nako...study kar...
        Assignment complete kar %s""" %(mau,mau)

        msg['sub']="uth %s"%mau
        msg.attach(MIMEText(body,'plain'))
        fileName = "Log.txt"
        attchmnt = open(fileName,'rb')
        p = MIMEBase("application",'octet-stream')
        p.set_payload((attchmnt).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment;filename =  %s "%fileName)
        msg.attach(p)
        # print("\nmsg :",msg)
        # file = open(fileName,'r')
        # cont = file.read()
        # print("\nprint file : ",cont)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #server.starttls()

        server.login(eid, pwd)
        text =msg.as_string()

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
            to = "sayali.bamhande@gmail.com"
            mailSender(emailId, pwd, to, message)
        else:
            print("No internet....")
    except Exception as e:
        print("Invalid argument ", e)


if __name__ == "__main__":
    main()
