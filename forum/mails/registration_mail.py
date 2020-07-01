from flask_mail import Message
from forum import mail
from forum.config import Config


class RegistrationMail():

    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
        message = self._get_message()

        mail.send(message)

    def _get_message(self):

        return Message("Dev forum - confirmation", 
            sender="devforum@example.com", 
            recipients=[self.recipient.email],
            body=self._get_body()
        )

    def _get_body(self):
        link = Config.APP_HOST + "/register/confirmation/" + self.recipient.confirmation_token 

        return """
            Hi M/Mrs.
            You registered to our forum, please confirm your email by clicking to the following link:
            {link}
        """.format(link=link)

    