from wtforms import Form, StringField, SelectField, validators, PasswordField
from wtforms.fields import EmailField, DateField
import datetime

class CreateAdminForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    phone_number = StringField('Phone Number', [validators.length(min=8, max=8), validators.DataRequired()])
    username = StringField('Username', [validators.length(min=5, max=12), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    status = SelectField('Status', [validators.DataRequired()], choices=[('Online'),('Offline')],default=('Online'))


class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    phone_number = StringField('Phone Number', [validators.length(min=8, max=8), validators.DataRequired()])
    date_of_birth = DateField('Date Of Birth', format='%Y-%m-%d', default=datetime.date.today())
    region = StringField('Region', [validators.length(min=1, max=150), validators.DataRequired()])
    street = StringField('Street', [validators.length(min=1, max=150), validators.DataRequired()])
    unit_number = StringField('Unit Number', [validators.length(min=1, max=150), validators.DataRequired()])
    block = StringField('Block', [validators.length(min=1, max=150), validators.DataRequired()])
    username = StringField('Username', [validators.length(min=5, max=12), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    status = SelectField('Status', [validators.DataRequired()], choices=[('Online'), ('Offline')],default=('Offline'))

class LoginForm(Form):
    username = StringField('Username', [validators.length(min=5, max=12), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


#/\+65(6|8|9)|d{7}
