import csv
import smtplib
from pytube import YouTube
#Importing csv file 
with open('Mailid.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row[2])
        print(type(row[2]))
        if row[2].strip() !="urls":
            youtube_link=row[2]
            #downloading youtube vedio 
            YouTube(youtube_link).streams.first().download()
            #Sending mail notification message after downloading 
            msg= EmailMessage()
            msg['Subject']="Vedio Download result"
            msg['From']="####@gmail.com"
            msg['To']=row[1]
            msg.sent_content("Vedio downloaded succesfully")
            mail_id=r"####@gmail.com"
            Password=r"####"
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
                server.login(mail_id,Password)
                server.sendmessage(msg)
                
