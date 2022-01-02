import bcrypt
import jwt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from datetime import datetime
from configs.env import getEnv

JWT_SECRET = getEnv().JWT_SECRET
SENDGRID_API_KEY = getEnv().SENDGRID_API_KEY

class EmailService:

    @classmethod
    def sendEmail(cls, toEmail, name, validated_link):
        url_youtube = "www.youtube.com"
        message = Mail(
            from_email='tiendat101001@gmail.com',
            to_emails=toEmail,
            subject="Forget Password",
            html_content="""
                Xin chào {},<br>
                Hãy nhấp vào 
                <a href={}>khôi phục mật khẩu</a> 
                để đặt lại mật khẩu mới.<br>
                Cảm ơn đã sử dụng dịch vụ của chúng tôi,<br>
                Me0Me0
                """.format(name,validated_link)
        )
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            return [response.status_code, "email has been sent"]

        except Exception as e:
            return [e,"failed to send email!"]

        
        
