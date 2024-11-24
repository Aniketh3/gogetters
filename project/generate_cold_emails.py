import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Generate a cold email
def generate_cold_email(combined_content):
    # Email Template
    email_template = f"""
    Hi {{recipient_name}},

    I hope this email finds you well! We noticed you're interested in the latest trends in Golang, and we have some exciting insights to share.

    Here's what's trending:
    {combined_content}

    At GoFr, we specialize in providing top-notch resources and tools for developers to excel in Golang. We'd love to hear your thoughts or collaborate further.

    Best regards,  
    The GoFr Team  
    """

    return email_template

# Send cold email
def send_email(to_email, subject, body):
    # Sender email and credentials
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Email setup
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Add body
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to the Gmail server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login
            server.sendmail(sender_email, to_email, msg.as_string())  # Send email
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
