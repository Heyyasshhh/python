from datetime import datetime
class Message:
    def greetings():
        if datetime.now().hour < 12:
            return "Good morning"
        elif datetime.now().hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
        
m = Message
print(m.greetings())