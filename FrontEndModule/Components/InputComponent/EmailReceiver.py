from Components.InputComponent.EmailParser import EmailParser
from Components.EmailBase import EmailBase
from pathlib import Path

class EmailReceiver(EmailBase):
    _last_session_path = 'last_session.json'

    def __init__(self, mail):
        self.mail = mail

        self.last_session = self.__load_last_session()

        if self.__check_adequacy_of_file(EmailReceiver._last_session_path):
            self.last_read_email_id = self.last_session['last_read_email_id']
        else:
            self.last_session = dict()
            self.last_session['last_read_email_id'] = 0
            self.last_read_email_id = 0

    def __load_last_session(self):
        if self.__check_adequacy_of_file(EmailReceiver._last_session_path):
            with open(EmailReceiver._last_session_path) as file:
                la = json.load(file)
                return la

    def __check_adequacy_of_file(self, file_path):
        last_session = Path(file_path)
        if not last_session.exists():
            file = open('last_session.json', 'w')
            file.close()
            return False

        with open('last_session.json') as file:
            return file.read() != ''

    def __update_inbox(self):
        type, data = self.mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        self.latest_email_id = int(id_list[-1])

    def read_email_from_gmail(self):
        self.__update_inbox()

        for i in range(self.latest_email_id,self.last_read_email_id, -1):
            typ, data = self.mail.fetch(str(i), '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                    # email_message_instance = email.message_from_string(str(response_part[1]))
                ep = EmailParser()
                return ep.parse_email(str(response_part[1]))