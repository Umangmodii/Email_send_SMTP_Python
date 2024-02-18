import smtplib

sender = input("Enter the email : ")
receiver = input("Receiver Email : ")

subject = input("Subjects : ")
message = input("Message : ")

text = f"subject : {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, "ykzgyuncjvoavrax")

server.sendmail(sender, receiver, text)

print("Email has been Sent! " + receiver)
