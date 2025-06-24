import pywhatkit
import random 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


validation = 0

while validation != 3:
    username = input('Enter your username: ')
    req_check = False
    req_check2 = False
    req_check3 = False

    # Length check
    if 4 <= len(username) <= 15:
        req_check = True
    else:
        print('❌ Username must be between 4 and 15 characters.')

    # Special character check
    if not any(char in "@#$%^&*()~`" for char in username):
        req_check2 = True
    else:
        print('❌ Username must not contain special characters.')

    # Space check
    if not any(char == " " for char in username):
        req_check3 = True
    else:
        print('❌ Username must not contain spaces.')

    # Final decision
    if req_check and req_check2 and req_check3:
        validation = 3
        print("✅ Username is valid!")
    else:
        validation = 0


validation2 = 0
while validation2 != 2:
    passw = input('Enter password: ')
    req_check4 = False
    req_check5 = False
    #len
    if len(passw) >= 8:
        req_check4 = True
    else:
        print('❌ password must be atleast 8 characters long.')
    #strong
    if any(char in "~!@#$%^&*" for char in passw):
        req_check5 = True
    else:
        print('❌ password must contain atleast one special character (~!@#$%^&*)')
    if req_check4 and req_check5:
        validation2  = 2
        print("✅ password is valid!")
    else:
        validation2 = 0



validation3 = 0

while validation3 != 2:
    email = input('Enter your email: ')
    req_check6 = False
    req_check7 = False

    # Check for @ and . in correct places
    if "@" in email and "." in email and email.index("@") < email.rindex(".")  and email.index('@') > 0  and email.index('.') > 0 :
        req_check6 = True
    else:
        print("❌ Email must contain '@' and '.' in a valid format (e.g., name@example.com)")

    # Check for spaces
    if " " not in email:
        req_check7 = True
    else:
        print("❌ Email must not contain spaces.")

    # Final decision
    if req_check6 and req_check7:
        validation3 = 2
        print("✅ Email is valid!")
    else:
        validation3 = 0



code = str(random.randint(100000, 999999))  # 6-digit code
sender_email = "kteachbook@gmail.com"
receiver_email = email
password = "xtmz cahk tqpr ksna"  


message = MIMEMultipart("alternative")
message["Subject"] = "Your Verification Code"
message["From"] = sender_email
message["To"] = receiver_email

text = f"Hello {username}! Your verification code is : {code}"
message.attach(MIMEText(text, "plain"))


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())



entered_code = input("Enter the verification code sent to your email: ")
if entered_code == code:
    print("Email verified successfully!")
else:
    print("Incorrect code!")




      
    

