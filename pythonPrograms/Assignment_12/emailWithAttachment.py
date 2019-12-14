import os
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


def mailSender(eid, pwd, to, filename):
    try:
        msg = MIMEMultipart()
        msg['from'] = eid
        msg['to'] = to
        body = """Hello,
        Please find the attached file of running process information
        """

        msg['sub'] = "Assignment12_4 : process log file"
        msg.attach(MIMEText(body, 'plain'))

        attchmnt = open(filename, 'rb')
        p = MIMEBase("application", 'octet-stream')
        p.set_payload((attchmnt).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment;filename =  %s " %  os.path.basename(filename))
        msg.attach(p)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.starttls()

        server.login(eid, pwd)
        text = msg.as_string()

        server.sendmail(eid, to, text)
        server.close()
        print("Email sent successfully...")
    except Exception as e:
        print("Unable to send email", e)


