import smtplib
import time
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# set up email variables
sender_email = 'ABC@gmail.com'
# Add a list of HR e-mails here
recipient_list = ['DEF@gmail.com']
# If you need help inserting your Google app password, please check out this guide: "https://support.google.com/accounts/answer/185833?hl=en"
password = 'XXX'
subject = "קורות חיים למשרת סטודנט"
file_path = 'C:/Users/User/OneDrive - Holon Institute of Technology/מסמכים/Visual Studio 2022/Netanel Zohar-CV.docx'
message =  " שלום! קוראים לי נתנאל זהר ,בן 24 , סטודנט במהלך השנה השניה , לומד מדעי המחשב במכון הטכנולוגי חולון,אני מחפש מקום שאוכל להשתקע, ללמוד ולתרום בו באופן האופטימלי ביותר"
message2="מצורף בזאת קורות החיים שלי,בתוכם ניתן למצוא קישור לגיט וללינקדין שלי"
message3="!תודה רבה על ההזדמנות"
finalmessage=message+" "+"\n"+"."+message2+"\n"+message3

# create email message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject
msg.attach(MIMEText(finalmessage, 'plain'))

# create email server object
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password) 

for receiver_email in recipient_list:
    # create email message object and attach file
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg.add_header('To', receiver_email) # use add_header method instead
    msg['Subject'] = subject
    msg.attach(MIMEText(finalmessage, 'plain'))
    with open(file_path, "rb") as attachment:
        attachment_file = MIMEApplication(attachment.read(), _subtype='txt')
        attachment_file.add_header('Content-Disposition', 'attachment', filename=basename(file_path))
        msg.attach(attachment_file)

    # send email
    server.send_message(msg)
    time.sleep(4)  # add a delay to avoid being flagged as spam

# close server connection
server.quit()