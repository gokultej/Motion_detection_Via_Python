import smtplib
from email.message import EmailMessage
import imghdr
password="hjhttfnpieqgsqjv"
Email_sent_to ="gokulteja960@gmail.com"
receiver="gokulteja960@gmail.com"

def send_email(image_path):
    print("email sent successfully")
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer Showed up"
    email_message.set_content("Hey,We just saw A new customer")

    with open(image_path,'rb') as file:
        content = file.read()
    email_message.add_attachment(content,maintype="image",subtype=imghdr.what(None,content))

    gmail =smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(Email_sent_to,password)
    gmail.sendmail(Email_sent_to,receiver,email_message.as_string())
    gmail.quit()


if __name__ == "__main_-":
    send_email(image_path="images/33.png")
