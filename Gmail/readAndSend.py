import ezgmail

# print(ezgmail.EMAIL_ADDRESS)

# ezgmail.send('example1@gmail.com', 'Test line', 'Test Body of the email')

unreadmessages = ezgmail.unread()
# print(ezgmail.summary(unreadmessages))
# print(len(unreadmessages))
print(unreadmessages[0])