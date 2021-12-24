import bcrypt
import jwt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from datetime import datetime
from configs.constant import JWT_SECRET


class EmailService:

    @classmethod
    def sendEmail(cls, toEmail, name, validated_link):
        message = Mail(
            from_email='tiendat101001@gmail.com',
            to_emails=toEmail,
            subject="Forget Password",
            html_content="""
                Xin chào {}<br>
                Hãy nhấp vào đường link bên dưới để khôi phục mật khẩu.<br>
                {}
                """.format(name,validated_link)
        )
        try:
            sg = SendGridAPIClient("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")
            response = sg.send(message)
            return [response.status_code, "email has been sent"]

        except Exception as e:
            return [e,"failed to send mail!"]

        
        
