from Components.EmailBase import EmailBase

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
import smtplib

class EmailSender(EmailBase):
    def __init__(self):
        pass
        # self.mail = mail HERE MUST BE EMAIL OBJECT

    def send_mes(self, path_to_file, whom):
        outer = MIMEMultipart()
        outer['Subject'] = 'Test Message'

        COMMASPACE = ', '
        outer['To'] = COMMASPACE.join(whom)
        outer['From'] = 'pandgine@gmail.com'

        ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        msg = EmailMessage()
        with open(path_to_file, 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=path_to_file)

        outer.attach(msg)

        composed = outer.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('pandgine@gmail.com', "dreamTeam13")

        server.sendmail('pandgine@gmail.com', whom, composed)
        server.quit()