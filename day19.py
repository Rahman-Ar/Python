#Automation with Python
import os

def rename_files(directory, prefix):
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                new_name = prefix + filename
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Files in '{directory}' have been renamed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
directory_path = "/path/to/your/directory"
prefix_to_add = "prefix_"
rename_files(directory_path, prefix_to_add)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_email, to_email, subject, body, smtp_server, smtp_port, login, password):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        
        # Attach the body to the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        
        # Send the email
        server.send_message(message)
        server.quit()

        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
from_email = "your_email@example.com"
to_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email."
smtp_server = "smtp.example.com"
smtp_port = 587
login = "your_email@example.com"
password = "your_email_password"

send_email(from_email, to_email, subject, body, smtp_server, smtp_port, login, password)
