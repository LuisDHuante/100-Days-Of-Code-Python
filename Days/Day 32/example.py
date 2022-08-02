import smtplib
#SMTP's Information

#Gmail: smtp.gmail.com
#Gmail: smtp.live.com
#Gmail: smtp.mail.yahoo.com


my_email = "deutoronomy35@gmail.com"
my_password = "kngkhtabjuzxsuwt"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="luisdhuante@gmail.com", msg="YOU CAN´T HIDE")
connection.close()