import smtplib

sender = "example2@gmail.com"
res_email = "example1@gmail.com"
password = input(str("Please enter your password: "))
message = "hello , this message sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("login successs")
server.sendmail(sender,res_email,message)
print("email has been sent to ", res_email)
server.quit()
