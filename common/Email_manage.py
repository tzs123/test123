# _*_ coding: utf-8 _*_
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pytest

from common.yanl_handler import yaml_data


class EmailManage:
    def send_email(self,report_name):
        smtpserver = 'smtp.163.com'
        username = yaml_data['email']['send_email']
        password = yaml_data['email']['pwd']
        receiver = yaml_data['email']['receiver']
        message = MIMEMultipart('related')
        subject = '某某项目自动化报告'
        fujian = MIMEText(open(report_name,'rb').read(),'html','utf-8')
        message['form'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
        smtp.sendmail(username,receiver,message.as_string())
        smtp.quit()


# if __name__ == '__main__':
#     EmailManage().send_email('../test_demo/test_report.txt')
