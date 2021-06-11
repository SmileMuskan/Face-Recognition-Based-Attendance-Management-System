import smtplib
from email.message import EmailMessage


SENDER_EMAIL="kankariya26mahima@gmail.com"
APP_PASSWORD="ssfzgqnosvtvnmee"

msg = EmailMessage()
msg['Subject'] = "Attendance"
msg['From'] = SENDER_EMAIL
print("To whom you want to send mail..?")
print("1 for Ruchika Sinhal Ma'am \n2 for Gajanan Tikhe Sir \n3 for Priti Bhagat Ma'am \n4 for Vikas Palekar Sir \n5 for Shimpli Dhale Ma'am \n6 for Mahima Kankariya")
choice = int(input("To whom you want to send the mail ..?"))
if choice == 1:
    msg['To'] = "ruchikasinhal@dmietr.edu.in"
    with open("Attendance.csv", 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="csv", filename="Attendance")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
elif choice == 2:
    msg['To'] = "gajanan_tikhe@yahoo.com"
    with open("Attendance.csv", 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="csv", filename="Attendance")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
elif choice == 3:
    msg['To'] = "bhagat.preetee@gmail.com"
    with open("Attendance.csv", 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="csv", filename="Attendance")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
elif choice == 4:
    msg['To'] = "kankariya26mahima@gmail.com"
    with open("Attendance.csv", 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="csv", filename="Attendance")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
elif choice == 5:
    msg['To'] = "dhaleshimpli@gmail.com"
    with open("Attendance.csv", 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="csv", filename="Attendance")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
elif choice == 6:
    msg['To'] = "mahimakankariya@dmietr.edu.in"
    with open("Attendance.csv", 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="csv", filename="Attendance")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
else:
    print("Wrong Choice")
