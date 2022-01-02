from email.message import EmailMessage
import smtplib, ssl

def alert(name,desire,url):
    port = 465  # For SSL
    password = ("Type your password and press enter: ")

    #hey
    msg = EmailMessage()
    msg.set_content("Hi there,\n\nThe %s has reached %.2f or lower.\n\nHere is the link to the product:\n%s" % (name,desire,url))
    

    msg['Subject'] = "Sartaj's Price Alert!"
    msg['From'] = "sartajsidhu16@gmail.com"
    msg['To'] = "22sartajsidhu@gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = "sartajsidhu16@gmail.com"
    receiver_email = ""
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sartajsidhu16@gmail.com", "S@rt@j1234")
        server.send_message(msg)