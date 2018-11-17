from Components.EmailBox import EmailBox

class InOutComponent:
    eboxes = dict()

    def add_ebox(self, mail, pwd, server, port):
        self.eboxes[mail] = EmailBox(mail, pwd, server, port)