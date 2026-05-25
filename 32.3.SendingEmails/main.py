import smtplib
import datetime as dt
import random

MY_EMAIL = "shaheeranoman889@gmail.com"
MY_PASSWORD = "hnbw pdtr mixj nhhk"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("32.3.SendingEmails\\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="zahidkhan2410@gmail.com", 
            msg=f"Subject:Tuesday Motivation\n\n{quote}"
            )