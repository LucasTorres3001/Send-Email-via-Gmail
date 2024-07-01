import smtplib
import email.message

def send_email():
    body = """
    <p>Olá, Lucas! ...</p>
    <p>Segue o email abaixo.</p>
    """
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['From'] = 'l.torres3001.lt@gmail.com'
    msg['To'] = 'lukas.torres30.lt@gmail.com'
    password = 'gtoqivbhmwmcdzfs'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(user=msg['From'], password=password)
    s.sendmail(from_addr=msg['From'], to_addrs=msg['To'], msg=msg.as_string().encode('utf-8'))
    print('Email invalid')
    
send_email()