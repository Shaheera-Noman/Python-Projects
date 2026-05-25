import smtplib

my_email = "shaheeranoman889@gmail.com"
password = "hnbwpdtrmixjnhhk"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=my_email, 
        msg="Subject:Hello\n\nThis is the body of my email."
        )
# connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1996, month=5, day=20, hour=12)
# print(date_of_birth)