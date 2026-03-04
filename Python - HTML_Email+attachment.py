#HTML Email with attachment
import smtplib
from os.path import basename
from email import encoders
from email.mime.text import MIMEText
from email.mime.MIMEMultipart import MIMEMultipart
from email.mime.MIMEApplication import MIMEApplication
from email.mime.base import MIMEBase
from datetime import date

#get today's date, 2 formats
DATE = str(date.today())
dd = date.today().strftime('%y%m%d')

#edit subject
SUBJECT="some subj"+DATE

#edit email addr
TO=["email@gmail.com"] 

#from what server?
FROM="email server"

server="127.0.0.1"

html = """\
<html>
<body>
<p>Some Email Content</p>
</body>
</html>
"""

#file to attach, jpg as an example, print to verify
fileName= "name"+dd+".jpg"
#fileName= "image001.jpg"
print(fileName)

#assemble email content
message = MIMEMultipart()
message["From"] = FROM
message["To"] = ", ".join(TO)
message["Subject"] = SUBJECT
message.attach(MIMEText(html,"html"))

with open(fileName, "rb") as attachment :
	part = MIMEBase("application","octet-stream")
	part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header("Content-Disposition", 'attachment; filename="%s"' % basename(fileName))

message.attach(part)

smtpServer = smtplib.SMTP(server)
smtpServer.sendmail(FROM, TO, message.as_string())
smtpServer.quit()

print("Email sent with "+fileName+"!")



#end
