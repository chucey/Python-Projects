import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials

def create_image_attachment(path: str) -> MIMEImage:
    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header("Content-Disposition",
                              f'attachment; filename={path}')
        return mime_image

def send_email(to_email: str,  subject: str,
               body: str,  image: str | None = None):
    host: str = 'smpt-mail-outlook.com'
    port: int = 587
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print('logging in...')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.email, credentials.password)

        # prepare email
        print('Attempting to send the email...')
        message = MIMEMultipart()
        message['From'] = credentials.email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)
        server.sendmail(from_addr=credentials.email, to_addrs=to_email,
                        msg=message.as_string())
        print('Message Sent')


if __name__ == '__main__':
    send_email(to_email='destination email',
               subject='Greetings',
               body='Whats up bud?. I sent you an image',
               image='your_image_here')


