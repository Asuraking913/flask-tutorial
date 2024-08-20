import logging
from logging.handlers import SMTPHandler

SMTPHandler = SMTPHandler(
    mailhost=("localhost", "1025"), 
    fromaddr="test@example.com",
    toaddrs="israelshedrack913@gmail.com",
    subject='Error log entries', 
    credentials=None, 
    secure=None
)

logger = logging.getLogger()
#error level
logger.setLevel(logging.ERROR)
logger.addHandler(SMTPHandler)
while True:
    logger.error('Hey I hope this is working.... An error basically occured')