import smtplib

email_address = "sharma.pratik2016@gmail.com"
password ="bulletganpr@tik$harma"
## this function send an email to myself 
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(email_address, password)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(email_address, "sharma.chetan1998@gmail.com", message)
        server.quit()
        print("success: Email sent")
    except:
        print("Email failed to sent.Please check you're code.")

subject = "Hello, brother"
msg = "hey there, i am sending this message through my python code. I have to disable my 2 step verification but it was worth it."

send_email(subject,msg)
