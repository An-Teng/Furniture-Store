from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DecimalField, IntegerField, SelectMultipleField, BooleanField, widgets, \
    ValidationError
from wtforms.fields import EmailField, DateField, FileField

# from wtforms.fields.html5 import EmailField, DataField

class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

def checkbox_length_check(form, field):
    if len(field.data) < 1:
        raise ValidationError('1 Checkbox must be selected!')

class CreateOrderForm(Form):
    product = StringField('Enter Product Name')
    orderamt = IntegerField('Enter Order Amount', [validators.NumberRange(min=1, max=200), validators.DataRequired()])
    cost = DecimalField('Enter Cost', places=2, rounding=None, use_locale=False, number_format=None)
    # cost = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    supplier = RadioField('Select Supplier', [validators.DataRequired()], choices=[], default='CKS')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    delivered = BooleanField('Delivered?')

class CreateSupplierForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    abbreviation = StringField('Abbreviation (Shortforms)', [validators.Length(min=1, max=150), validators.DataRequired()])
    products_offered = MultiCheckboxField('Select Products Offered', [checkbox_length_check], choices=[('Chairs'), ('Tables'), ('Cabinet')], default='')
    # products_offered = SelectMultipleField('Select Products Offered', [validators.DataRequired()], choices=[('Chairs'), ('Tables')], default='')
    availability = BooleanField('Available?')
    website = StringField('Website', [validators.Optional()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    logo = SelectField('Select Logo', [validators.DataRequired()], choices=[('CKS','Korean Cabinet Supplier'),('CBS','Comfy Bed Supplier'),('ATS','Authentic Tables Supplier')], default='CKS')
    contactno = IntegerField('Contact No.', [validators.DataRequired(message='ERROR'), validators.NumberRange(min=10000000,max=99999999)])

class CreateSupplierPForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    abbreviation = StringField('Abbreviation (Shortforms)', [validators.Length(min=1, max=150), validators.DataRequired()])
    products_offered = MultiCheckboxField('Select Products Offered', [checkbox_length_check], choices=[('Chairs'), ('Tables'), ('Cabinet')], default='')
    availability = BooleanField('Available?')
    website = StringField('Website', [validators.Optional()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    logo = SelectField('Select Logo', [validators.DataRequired()], choices=[('CKS','Korean Cabinet Supplier'),('CBS','Comfy Bed Supplier'),('ATS','Authentic Tables Supplier')], default='CKS')
    contactno = IntegerField('Contact No.', [validators.NumberRange(min=10000000,max=99999999), validators.DataRequired()])
    address = StringField('Address (can insert image tba)', [validators.Length(min=1, max=200), validators.DataRequired()])

# for now
class CreateProductFormJY(Form):
    productname = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    producttype = SelectField('Product type', [validators.DataRequired()], choices=[('', 'Select'), ('Ch', 'Chair'), ('Tb', 'Table'), ('Cb', 'Cabinet'), ('Bd', 'Bed')], default='')
    availability = BooleanField('Available?')
    quantity = IntegerField('Enter Amount', [validators.NumberRange(min=1, max=200), validators.DataRequired()])
    suppliers = MultiCheckboxField('Select Suppliers', [checkbox_length_check], choices=[('CKS', 'South Korea Furniture Chair'), ('TTT', 'Taiwan Tables')], default='')
    cost = DecimalField('Enter Cost', [validators.NumberRange(min=0.1), validators.DataRequired()])