
from datetime import datetime

from twilio.rest import Client

account_sid = "ADD ACCOUNT SID"
auth_token = "ADD AUTH TOKEN"
client = Client(account_sid, auth_token)


day_of_week = datetime.today().strftime("%A")
list_of_messages = [
    "Hello, have a wonderful week.",
    "Happy Tuesday",
    "Good luck today.",
    "You are holding on too good.",
    "Weekend is coming.",
    "Ha! Weekend is here!",
    "Take a good rest.",
]


if day_of_week == "Monday":
    MESSAGE_SENT = list_of_messages[0]
elif day_of_week == "Tuesday":
    MESSAGE_SENT = list_of_messages[1]
elif day_of_week == "Wednesday":
    MESSAGE_SENT = list_of_messages[2]
elif day_of_week == "Thursday":
    MESSAGE_SENT = list_of_messages[3]
elif day_of_week == "Friday":
    MESSAGE_SENT = list_of_messages[4]
elif day_of_week == "Saturday":
    MESSAGE_SENT = list_of_messages[5]
else:
    MESSAGE_SENT = list_of_messages[6]


message = client.messages.create(
    body=MESSAGE_SENT, from_="ADD SOURCE NUMBER", to="ADD TARGET NUMBER"
)


print(message.sid)
