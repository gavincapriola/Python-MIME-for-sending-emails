import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(fromaddr, to_addrs, cc_addrs, bcc_addres, subject, body, attachment, password):
    """The function sends an email with the given arguments.

    The arguments are:
        - fromaddr   : the email address of the sender
        - to_addrs   : the email address of the recipient
        - cc_addrs   : the email address of the cc recipient
        - bcc_addres : the email address of the bcc recipient
        - subject    : the subject of the email
        - body       : the body of the email
        - attachment : the path of the attachment
        - password   : the password of the email account
    """
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ', '.join(to_addrs)
    msg['Cc'] = ', '.join(cc_addrs)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    with open(attachment, 'rb') as f:
        attach = MIMEBase('application', 'octet-stream')
        attach.set_payload(f.read()) 
        encoders.encode_base64(attach) 
        attach.add_header('Content-Disposition',
                          'attachment; filename="{}"'.format(attachment))
        msg.attach(attach)
        
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)

    message = msg.as_string()
    server.sendmail(fromaddr, to_addrs + cc_addrs + bcc_addres, message)
    server.quit()


if __name__ == '__main__':
    fromaddr = ''
    to_addrs = []
    cc_addrs = []
    bcc_addres = []
    subject = ''
    body = ''
    attachment = ''
    password = ''
    
    send_email(fromaddr, to_addrs, cc_addrs, bcc_addres, 
               subject, body, attachment, password)
