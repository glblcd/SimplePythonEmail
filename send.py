import smtplib

recipient = "DESTINATION-EMAIL@gmail.com"

# Read the username and password and strip extra whitespace
# Make sure to .gitignore username.txt and password.txt!
with open("username.txt", 'r') as u_file:
    username = u_file.read().strip()
with open("password.txt", 'r') as p_file:
    password = p_file.read().strip()

if username and password:
    # Connect to the server and send an emails
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)

    msg = "This is a test!"
    server.sendmail(username, recipient, msg)