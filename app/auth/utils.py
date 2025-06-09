from flask_mail import Message
from flask import current_app, url_for
from app.extensions import mail

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                 sender=current_app.config['MAIL_USERNAME'],
                 recipients=[user.email])
    msg.body = f'''To reset your password, visit:
{url_for('auth.reset_password', token=token, _external=True)}

If you didn't make this request, please ignore this email.
'''
    mail.send(msg)

def send_welcome_email(user):
    msg = Message('Welcome to Our Platform',
                 sender=current_app.config['MAIL_USERNAME'],
                 recipients=[user.email])
    msg.body = f'''Hi {user.username},

Welcome to our platform! Your account has been successfully created.

Best regards,
The Team
'''
    mail.send(msg)