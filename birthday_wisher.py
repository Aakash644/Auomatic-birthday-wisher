import datetime as dt
import smtplib  
import pandas  
time=dt.datetime 
now=time.now() 

mnth=now.month
dy=now.day

today=(mnth,dy)
#using pandas library to read csv
data=pandas.read_csv(r"C:\Users\Acer\Downloads\birthdays.csv")
dict={(data_row.month,data_row.day):data_row for(index,data_row) in data.iterrows() } 
if today in dict:
    email="your_email" 
    password="your_password"  
    birthday_person=dict[today]
    with open(r"C:\Users\Acer\Downloads\letter_templates\letter_1.txt","r") as letter:
        info=letter.read() 
     
        updated_letter=info.replace("[NAME]",birthday_person["name"]) 
   
    connection=smtplib.SMTP("smtp.gmail.com") 
    connection.starttls()  
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs=birthday_person.email,msg=f"Subject:Happy birthday!\n\n{updated_letter}")      
    connection.close()

        


