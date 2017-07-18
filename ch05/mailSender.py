import smtplib
from email.mime.text import MIMEText

msg = MIMEText("안녕!!!!! 파이썬으로 보낼거야 이거!!!")

msg["Subject"] = "Email From Python Study"
msg["From"] = "phewphewsimsim@naver.com"
msg["To"] = "fairesy@gmail.com"
s = smtplib.SMTP("smtp.naver.com", 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login("phewphewsimsim", "password")
s.send_message(msg)
s.quit()
