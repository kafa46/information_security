from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email

class PersonalInfomationForm(FlaskForm):
    '''개인정보 변경에 사용할 form'''
    user_id = StringField('user_id', validators=[DataRequired()])
    passwd = PasswordField('passwd', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    university = StringField('university', validators=[DataRequired(), Email()])
    
    