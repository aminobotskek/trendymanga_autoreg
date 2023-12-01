import trendymanga , temp_mail
# https://github.com/aminobotskek/trendymanga/blob/main/trendymanga.py
# https://github.com/aminobotskek/temp_mail/blob/main/temp_mail.py
from nickname_generator import generate
password=input("password»")
while True:
	try:
		client=trendymanga.Client()
		email=temp_mail.Client().new_email()['email']
		id=client.register(email=email,password=password,username=generate("en"))['id']
		print(f"account {email} register . id »{id}")
		accounts= open("accounts.txt", "a+")
		accounts.write(f"{email}:{password}\n")
		accounts.close()
	except Exception as e:
		print(e)