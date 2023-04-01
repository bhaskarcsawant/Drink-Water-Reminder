import threading
from notifypy import Notify


notification = Notify()

notification.title = "Water Reminder"
notification.message = "Take a sip of water bro!!"
notification.icon = "C:\img/favicon.ico"
notification.audio = "C:\img/ring.wav"
notification.application_name = "Water Reminder"


def clearAfter40():
    notification.send()
    t = threading.Timer(40*60, clearAfter40)
    t.start()


clearAfter40()
