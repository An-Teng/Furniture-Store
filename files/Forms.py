from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators,IntegerField
from wtforms.fields import EmailField, DateField, FileField, TimeField
from datetime import *
from wtforms_validators import Alpha, Integer,ValidationError
# TARIQ CODE

class CreateProductForm(Form):
    name = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = StringField('Product Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    features = StringField('Key Features', [validators.Length(min=1, max=150), validators.DataRequired()])
    colours = SelectField('Colours Available', [validators.DataRequired()], choices=[('', 'Select'), ('R', 'Red'), ('G', 'Green'), ('B', 'Blue')], default='')
    category = RadioField('Category', choices=[('S', 'Sofa'), ('B', 'Bed'), ('T', 'Table')], default='F')
    status = RadioField('Status', choices=[('A', 'Available'), ('N', 'Not Available')], default='F')
    price = IntegerField('Product Price', [validators.Optional(), validators.NumberRange(min=1)])
    image = FileField('Image')

class CreateElectronicForm(Form):
    name = StringField('Electronic Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = StringField('Electronic Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    features = StringField('Key Features', [validators.Length(min=1, max=150), validators.DataRequired()])
    colours = SelectField('Colours Available', [validators.DataRequired()], choices=[('', 'Select'), ('R', 'Red'), ('G', 'Green'), ('B', 'Blue')], default='')
    category = RadioField('Category', choices=[('S', 'Sofa'), ('B', 'Bed'), ('T', 'Table')], default='S')
    status = RadioField('Status', choices=[('A', 'Available'), ('N', 'Not Available')], default='A')
    price = IntegerField('Product Price', [validators.Optional()])
    assembly = SelectField('Do you want assembly +$30', [validators.DataRequired()], choices=[('', 'Select'), ('Y', 'Yes'), ('N', 'No')], default='')

# ALFI FORMS

class CreateDeliveryForm(Form):
    date_delivery = DateField('Available Date For Delivery', format='%Y-%m-%d')
    time_delivery = TimeField('Available Time For Delivery', format='%H:%M')
    delivery_address = TextAreaField('Delivery Address', [validators.length(max=200), validators.DataRequired()])
    receiver_name = StringField('Receiver Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    pricing = StringField('Pricing', [validators.Length(min=1, max=150), validators.DataRequired()])

class PendingDeliveryForm(Form):
    receiver_name = StringField('Receiver Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    delivery_address = TextAreaField('Delivery Address', [validators.length(max=200), validators.DataRequired()])
    pricing = StringField('Pricing', [validators.Length(min=1, max=150), validators.DataRequired()])
    confirmation = RadioField('Have you received your Delivery?', choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    remarks = TextAreaField('Remarks on Delivery', [validators.Optional()])
    date_delivery = DateField('Available Date For Delivery', format='%Y-%m-%d')
    time_delivery = TimeField('Available Time For Delivery', format='%H:%M')

# AN TENG FORMS

def validate_date(form, field):
    if field.data < date.today():
        raise ValidationError("The date cannot be in the past!")


class CreateRewardForm(Form):
    Name = StringField('Reward Name:', [validators.Length(min=1, max=30), validators.DataRequired(),
                                        Alpha(message="Name should only contain Alphabets")])
    Description = TextAreaField('Description:', [validators.Optional()])
    Price = StringField('Price:', [validators.DataRequired(), Integer(message="Price should only contain numbers")])
    Validity = StringField('Validity (days):',
                           [validators.DataRequired(), Integer(message="Validity should only contain numbers")])
    Image = FileField('Select Reward Image:')


class CreateSpecialForm(Form):
    Name = StringField('Reward Name:', [validators.Length(min=1, max=30), validators.DataRequired(),
                                        Alpha(message="Name should only contain Alphabets")])
    Description = TextAreaField('Description:', [validators.Optional()])
    Price = StringField('Price:', [validators.DataRequired(), Integer(message="Price should only contain numbers")])
    Validity = StringField('Validity (days):',
                           [validators.DataRequired(), Integer(message="Validity should only contain numbers")])
    Usability = DateField('Set Usability:', [validate_date, validators.DataRequired()])
    Image = FileField('Select Reward Image:')


class SetLimitForm(Form):
    Limit = StringField('Set Limit:', [validators.length(min=1, max=30), validators.DataRequired(),
                                       Integer(message="Limit should only contain numbers")])