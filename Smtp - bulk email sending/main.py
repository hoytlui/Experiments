import datetime as dt
import pandas as pd
import random
import smtplib


# create today tuple
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# constants
MY_EMAIL = 'somename@gmail.com'
MY_PASSWORD = 'somepassword'
EMAIL_HOST = 'smtp.gmail.com'

# create df
df = pd.read_csv('followup_date.csv', header=0)
# check all rows
for i in range(len(df)):
    # select random letter for each row
    letter_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(letter_path) as letter_file:
        content = letter_file.read()

        # if today matches followup date, replace name in letter and send email
        if (df['month'][i], df['day'][i]) == today_tuple:
            firstname = df['firstname'][i]
            recipient_email = df['email'][i]
            content = content.replace('[NAME]', firstname)

            with smtplib.SMTP(EMAIL_HOST) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=recipient_email,
                    msg=f"Subject:Follow-Up\n\n{content}"
                )
