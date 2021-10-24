import abc


class ESP(abc.ABC):

    @abc.abstractmethod
    def add_email(self, email):
        pass

    @abc.abstractmethod
    def add_emails_list(self, emails_list):
        pass

    @abc.abstractmethod
    def check_email(self, email):
        pass

    @abc.abstractmethod
    def delete_email(self, email):
        pass

    @abc.abstractmethod
    def delete_emails_list(self, emails_list):
        pass

    @abc.abstractmethod
    def sendmail(self, message):
        pass
