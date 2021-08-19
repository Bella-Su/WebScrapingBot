import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    ## Varibles
    from_add = 'send@email.com' ## add the sending email
    to_add = 'receving@email.com' ## add the receving email
    subject = "Your subject" ## the subject of the sending email


    ##------------------------------------ header----------------------------------##
    msg = MIMEMultipart() ## kind of a list of standard format for email
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject
    ##----------------------------------------------------------------------------##


    ##------------------------------------ body-----------------------------------##
    body = "<b>Hey XXX, today's finance report attached! Please review! </b>"
    msg.attach(MIMEText(body, 'html')) ## 'plain' -> just plain text
    ##----------------------------------------------------------------------------##


    ##------------------------------------- file----------------------------------##
    my_file = open(filename, 'rb') ## 'rb' -> the method that I use, which is binary mode

    part = MIMEBase('application', 'octet-stream') ## create an object
    part.set_payload((my_file).read()) ## use set_palyload() to attach my file
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)
    ##---------------------------------------------------------------------------##


    message = msg.as_string() ## everything converted into string

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() ## object for securety
    server.login(from_add, 'password') ## login the email for sending email with password


    server.sendmail(from_add, to_add, message)

    server.quit()

