from esp.interface import ESP
from esp.models import Email


class ESP(ESP):
    def add_email(self, email):
        Email.objects.create(email=email)
        return Email.objects.filter(email=email)

    def add_emails_list(self, emails_list):
        for email in emails_list:
            if not Email.objects.filter(email=email).exists():
                Email.objects.create(email=email)
            else:
                print(email + 'уже есть в базе')

    def check_email(self, email):
        return Email.objects.filter(email=email).exists()

    def delete_email(self, email):
        Email.objects.filter(email=email).delete()
        if not Email.objects.filter(email=email).exists():
            print(email + "удален успешно")
        else:
            print(email + "не удается удалить")

    def delete_emails_list(self, emails_list):
        for email in emails_list:
            Email.objects.filter(email=email).delete()
            if not Email.objects.filter(email=email).exists():
                print(email + "удален успешно")
            else:
                print(email + "не удается удалить")

    def sendmail(self, message):
        pass
