from flask_mail import Message
from forum import mail
from forum.config import Config


class RegistrationMail:

    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
        message = self._get_message()

        mail.send(message)

    def _get_message(self):
        return Message("Dev Forum Registration - Email confirmation.",
                       sender="devforum@example.com",
                       recipients=[self.recipient.email],
                       html=self._get_html(),
                       body=self._get_body()
                       )

    def _get_body(self):
        return """
            Dev Forum
            
            Hi M/Mrs.
            You have been registered to our forum, please confirm your email by 
            clicking to the following link: {link}
            
            You are not the owner of the registration, please forget this email.
        """.format(link=self._get_confirmation_link())

    def _get_html(self):
        return """
            <h2>Dev Forum.</h2>
            <p>
                Hi M/Mrs.
                You have been registered to our forum, please confirm your email by 
                clicking to the following link: <a href="{link}">confirmation link</a>.
            </p>
            <p>
                You are not the owner of the registration, please forget this email.
            </p>
        """.format(link=self._get_confirmation_link())

    def _get_confirmation_link(self):
        return Config.APP_HOST + "/register/confirmation/" + self.recipient.confirmation_token


def send_validation_email(recipient_email):
    registration_mail = RegistrationMail(recipient_email)
    registration_mail.send()