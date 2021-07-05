import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from app import mail

# Create a Random Hex for Image File Name
def change_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # Scale down the Image File that User uploads to the server.
    output_size = (200, 200)
    x = Image.open(form_picture)
    x.thumbnail(output_size)
    x.save(picture_path)
    return picture_fn

# Email Reset
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f"""To Reset the password, click on the link: {url_for('users.reset_token', token = token, _external=True)}

    If this is not you, please ignore.
    """
    mail.send(msg)
