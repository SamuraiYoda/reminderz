import smtplib
import schedule
import time

video_links = [
  " Day One -- https://www.youtube.com/watch?v=SA9EtffBZsw&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=3&ab_channel=Pebbleslive",

  "Day TWO-- https://www.youtube.com/watch?v=lmkCsfy0U4U&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=3&ab_channel=Pebbleslive",

  "Day Three-- https://www.youtube.com/watch?v=kikhEwMzyjA&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=4&ab_channel=Pebbleslive",

  "Day Four-- https://www.youtube.com/watch?v=A0Fct6lfWLE&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=5&ab_channel=Pebbleslive",

  "Day Five-- https://www.youtube.com/watch?v=C3kxVOpxtps&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=6&ab_channel=Pebbleslive",

  "Day Six-- https://www.youtube.com/watch?v=U1u-uUcrnnA&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=7&ab_channel=Pebbleslive",

  "Day Seven-- https://www.youtube.com/watch?v=Q2_Mg88Tr6s&list=PLruU8BdoC0U9jTPfpAZTedFm3xVPJValg&index=8&ab_channel=Pebbleslive"

  # Add more video links as needed
]


def send_email():
  if video_links:
    subject = "Daily Personality Development Videos Links"
    body = "\n".join(video_links)

    sender_email = ""  # Replace with your email address
    receiver_email = ""  # Replace with the recipient's email address
    password = ""  # Replace with your email- app  password

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(
        "smtp.gmail.com",
        587) as server:  # Replace with your email server and port
      server.starttls()
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)

    print("Email sent successfully.")
  else:
    print("No more video links remaining.")


def schedule_email():
  schedule.every().day.at("07:30","17:30").do(send_email)


def run_scheduler():
  while True:
    schedule.run_pending()
    time.sleep(1)


schedule_email()
run_scheduler()
