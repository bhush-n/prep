class Notification:
    def send_notification(self):
        print("Notification sent")
    

class Email(Notification):
    def send_notification(self):
        print("Email sent")

class Push(Notification):
    def send_notification(self):
        print("Push sent")


myNotifications = [
    Notification(),
    Email(),
    Push()
]

for n in myNotifications:
    n.send_notification()