import smtplib
sender_gmail="parveenkmm1987@gmail.com"
rec_gmail="cdrs2014@gmail.com"
password=input(str("PLEASE ENTER YOUR GMAIL PASSWORD:"))
message=input(str("WHAT DO YOU WANT TO SEND:"))
server=smtplib.SMTP('smtp.gmail.com',965)
server.starttls()
server.login(sender_gmail, password)
print("LOGIN SUCCESS")
server.sendmail(sender_gmail,rec_gmail)
