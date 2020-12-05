import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email=os.environ.get('FROM_EMAIL'),
    to_emails=os.environ.get('TO_EMAIL'),
    subject='test email',
    html_content='<strong> beep boop </strong>'
)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

