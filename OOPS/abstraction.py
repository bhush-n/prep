from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send_notification(self):
        pass

class Email(Notification):
    def send_notification(self):
        print("Email sent")


# n = Notification()

e = Email()
e.send_notification()