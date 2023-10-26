import ssl
import smtplib
from urllib.request import urlopen

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()  # turn sequence of bytes into a string
        if line.startswith('datetime'):
            print(line.rstrip())  # remove trailing newline

from urllib.request import urlopen
import json

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.json') as response:
    body = json.loads(response.read())
    print(body['datetime'])

# Code copied from https://docs.python.org/3/tutorial/stdlib.html#internet-access

# TODO: remove after you create a function that actually works


def doesnt_work():
    import smtplib

    server = smtplib.SMTP('localhost')
    server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                    """To: jcaesar@example.org
    From: soothsayer@example.org
    
    Beware the Ides of March.
    """)
    server.quit()

# Adapted with code from https://realpython.com/python-send-email/


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as server:
    # login fails with user password, @see https://devanswers.co/outlook-and-gmail-problem-application-specific-password-required/
    # password as created here: https://myaccount.google.com/apppasswords
    server.login('antony.mistretta@gmail.com', 'zgjohvcfjjwhuarh')
    server.sendmail(
        'antony.mistretta@gmail.com',
        'antony.mistretta@gmail.com',
        """Subject: Hello

    Hello from Python!
    """
    )

# For extra email features @see https://docs.python.org/3/library/email.html
