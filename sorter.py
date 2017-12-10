import re

x = open('e-mail_base_1.txt', 'r')

y = open('sorted_emailes/email_mail_base_1.txt', 'w')

for line in x:
    if line.find('@mail.') != -1:
        y.write(line)
x.close()
y.close()
