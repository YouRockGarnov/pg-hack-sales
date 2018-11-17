import smtplib
import imaplib
import email
import json
from collections import namedtuple
from Components.InputComponent.EmailParser import EmailParser
from Components.InputComponent.EmailReceiver import EmailReceiver
from Components.OutputComponent.EmailSender import EmailSender

# LastSession = namedtuple('LastSession', ['last_read_email_id'])

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "pandgine" + ORG_EMAIL
FROM_PWD    = "dreamTeam13"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

class EmailBox:
    def __init__(self, mail_adress, pwd, server, port):
        self.mail_adress = mail_adress
        self.pwd = pwd
        self.server = server
        self.port = port

        self.__login()

        self._receiver = EmailReceiver(self.mail)
        # self._sender = EmailSender(self.mail) IT WILL BE

    def __login(self):
        self.mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        self.mail.login(FROM_EMAIL, FROM_PWD)
        self.mail.select('inbox')

    def close_session(self):
        last_session = dict(self.last_read_email_id)

        with open('InputComponent/last_session.json') as file:
            json.dumps(file, last_session)

    def read_email_from_gmail(self):
        return self._receiver.read_email_from_gmail()




# TRASH
# maintype = email_message_instance.get_content_maintype()
# if maintype == 'multipart':
#     for part in email_message_instance.get_payload():
#         if part.get_content_maintype() == 'text':
#             return part.get_payload()
# elif maintype == 'text':
#     print(email_message_instance.get_payload())
#
# email_subject = email_message_instance['subject']
# email_from = email_message_instance['from']
# print('From : ' + str(email_from) + '\n')
# # print('Subject : ' + str(email_subject) + '\n')