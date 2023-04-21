# === GMAIL SMTP ===
import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('mealhouse3377@gmail.com', 'dueqlswsrdjmwzis')

msg = MIMEText("contents : hellow GMAIL")
msg['Subject'] = "Hello there it's title"

smtp.sendmail("mealhouse3377@gmail.com", "mealhouse3377@gmail.com", msg.as_string())
smtp.quit()

# === NAVER SMTP ===
# HOST = 'smtp.gmail.com:587'
# USER = 'mealhouse3377@gmail.com'
# PASS = 'dueqlswsrdjmwzis'
# 
# TO = 'mealhouse3377@gmail.com'
# msg = MIMEText('Hello Google Email')
# msg['Subject'] = 'Rpi email Text'
# msg['From'] = 'mealhouse3377@gmail.com'
# msg['To'] = 'Gmail smtp'
# 
# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.starttls()
# print('stst')
# 
# smtp.login(USER, PASS)
# smtp.sendmail(USER, TO, msg.as_string())
# print('Send email.')
# smtp.quit()