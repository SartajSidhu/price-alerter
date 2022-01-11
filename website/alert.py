from email.message import EmailMessage
import smtplib, ssl

def alert(name,desire,url,email):
    port = 465  # For SSL

    msg = EmailMessage()
    msg.set_content("Hi there,\n\nThe %s has reached %.2f or lower.\n\nHere is the link to the product:\n%s" % (name,desire,url))

    msg['Subject'] = "Sartaj's Price Alert!"
    msg['From'] = "sartajpricealerts@gmail.com"
    msg['To'] = email

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sartajpricealerts@gmail.com", "pricealert123")
        server.send_message(msg)