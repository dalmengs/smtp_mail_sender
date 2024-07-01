import smtplib
from email.mime.text import MIMEText

from Util.EnvironmentVariable import env
from Util.Util import get_random_verification_code

class EmailSender:
    def __init__(self):
        self.__smtp_server = env("SMTP_SERVER")
        self.__smtp_port = int(env("SMTP_PORT"))
        self.__email = env("SENDER_EMAIL")
        self.__password = env("SENDER_PASSWORD")
        self.__title = "[Naly] Verify Your Email"
        f = open("./email_template.html", "r")
        self.__content = f.read()
        f.close()

    def send_email(self, recv_email):
        verification_code = get_random_verification_code()
        msg = MIMEText(self.__content.replace(
            "verification_code", verification_code
        ), "html")
        msg['From'] = self.__email
        msg['To'] = recv_email
        msg['Subject'] = self.__title

        with smtplib.SMTP(self.__smtp_server, self.__smtp_port) as server:
            server.starttls()
            server.login(self.__email, self.__password)
            server.sendmail(self.__email, recv_email, msg.as_string())

if __name__ == "__main__":
    email_sender = EmailSender()
    email_sender.send_email(
        recv_email="dalmenglee@gmail.com"
    )
