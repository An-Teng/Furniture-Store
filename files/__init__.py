from flask import Flask, render_template, request, redirect, url_for, session, flash
from Forms import CreateProductForm, CreateElectronicForm, PendingDeliveryForm, CreateDeliveryForm, CreateRewardForm, CreateSpecialForm, SetLimitForm
from FormsFurniture import CreateOrderForm, CreateProductFormJY, CreateSupplierForm, CreateSupplierPForm
from forms_web import CreateCustomerForm, CreateAdminForm, LoginForm
import shelve, Supplier, Order, Product, SupplierPhysical, ProductJY, Electronic, Pending, Delivery, Reward, Special, History1, admin_web, customer_web
# add in later tariq
from datetime import *

# stuff for file handling
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'any_random_string'

@app.route('/adminHome')
def home():
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    # session['id'] = 1
    return render_template('home.html', date_time=date_time, username=session['username'])

@app.route('/homeCustomer')
def homeCust():
    # for now
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('homeCustomer.html', date_time=date_time)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/inventory/inventory2')
def inventory2():
    try:
        products_dict = {}
        db = shelve.open('productJY.db', 'r')
        products_dict = db['Products']
        db.close()

        products_list = []
        for key in products_dict:
            product = products_dict.get(key)
            products_list.append(product)
    except:
        products_list = []
        print("Possibly no productJY.db.")

    return render_template('inventory2.html', count=len(products_list), products_list=products_list)

@app.route('/inventory/inventory3')
def inventory3():
    try:
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()

        orders_list = []
        for key in orders_dict:
            order = orders_dict.get(key)

            #  for specific filter
            # if order.get_supplier() == 'TTT':
            orders_list.append(order)
    except:
        orders_list = []
        print("Possibly no order.db.")

    return render_template('inventory3.html', count=len(orders_list), orders_list=orders_list)

@app.route('/inventory/inventory4', methods=['GET', 'POST'])
def inventory4():
    try:
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()

        suppliers_list = []
        for key in suppliers_dict:
            supplier = suppliers_dict.get(key)
            suppliers_list.append(supplier)
    except:
        suppliers_list = []
        print("Possibly no supplier.db.")

    return render_template('inventory4.html', count=len(suppliers_list), suppliers_list=suppliers_list)

@app.route('/inventory/inventory4P', methods=['GET', 'POST'])
def inventory4P():
    try:
        suppliersP_dict = {}
        db = shelve.open('supplierP.db', 'r')
        suppliersP_dict = db['SuppliersP']
        db.close()

        suppliersP_list = []
        for key in suppliersP_dict:
            supplierP = suppliersP_dict.get(key)
            suppliersP_list.append(supplierP)
    except:
        suppliersP_list = []
        print("Possibly no supplierP.db.")

    return render_template('inventory4P.html', count=len(suppliersP_list), suppliersP_list=suppliersP_list)

@app.route('/inventory/inventory5', methods=['GET', 'POST'])
def inventory5():
    try:
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()

        orders_list = []
        for key in orders_dict:
            order = orders_dict.get(key)

            #  for specific filter
            # if order.get_supplier() == 'TTT':
            orders_list.append(order)
    except:
        orders_list = []
        print("Possibly no order.db.")

    return render_template('inventory5.html', count=len(orders_list), orders_list=orders_list)

@app.route('/inventory/inventory2/createProduct2', methods=['GET', 'POST'])
def create_productJY():
    create_product_form = CreateProductFormJY(request.form)
    if request.method == 'POST' and create_product_form.validate():
        products_dict = {}
        db = shelve.open('productJY.db', 'c')

        try:
            productid = 1

            products_dict = db['Products']

            for key in products_dict:
                if key > productid:
                    productid = key
            productid = productid + 1
        except:
            print("Error in retrieving Users from productJY.db.")

        # email = 'test@email.com'
        ordered = 1
        product = ProductJY.ProductJY(productid,create_product_form.productname.data, create_product_form.producttype.data, create_product_form.availability.data, create_product_form.suppliers.data, create_product_form.quantity.data, create_product_form.cost.data, ordered)
        products_dict[product.get_productid()] = product
        db['Products'] = products_dict

        db.close()

        return redirect(url_for('inventory2'))
    return render_template('createProduct2.html', form=create_product_form)

@app.route('/inventory/inventory2/createOrder/<int:id>/', methods=['GET', 'POST'])
def create_order(id):
    create_order_form = CreateOrderForm(request.form)

    products_dict = {}
    db2 = shelve.open('productJY.db', 'r')
    products_dict = db2['Products']
    product = products_dict.get(id)
    # maybe
    for key in product.get_suppliers():
        create_order_form.supplier.choices.append(key)

    if request.method == 'POST' and create_order_form.validate():
        orders_dict = {}
        db = shelve.open('order.db', 'c')

        try:
            orderid = 1

            orders_dict = db['Orders']

            for key in orders_dict:
                if key > orderid:
                    orderid = key
            orderid = orderid + 1
        except:
            print("Error in retrieving Users from order.db.")

        # categories = [(c.get(id),c.get_suppliers()) for c in products_dict]
        # create_order_form.supplier.choices = [('test','TTT'), ('test2','TT3')]
        # look into jquery and sqlalchemy

        productid = product.get_productid()
        orderproduct = product.get_productname()
        ordercost = product.get_cost()
        orderdelivered = 0
        order = Order.Order(orderid, productid, orderproduct, create_order_form.orderamt.data, create_order_form.supplier.data, float(ordercost), create_order_form.remarks.data, orderdelivered)
        orders_dict[order.get_orderno()] = order
        db['Orders'] = orders_dict

        if order.get_delivered() == 0:
            product.set_ordered(0)

            db2['Products'] = products_dict
            db2.close()
        db.close()

        return redirect(url_for('inventory3'))
    return render_template('createOrder.html', form=create_order_form, product=product)

@app.route('/inventory/inventory4/createSupplier', methods=['GET', 'POST'])
def create_supplier():
    create_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and create_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'c')

        try:
            supplierid = 1

            suppliers_dict = db['Suppliers']

            for key in suppliers_dict:
                if key > supplierid:
                   supplierid = key
            supplierid = supplierid+1

        except:
            print("Error in retrieving Users from supplier.db.")

        assets_dir = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )

        # d = create_supplier_form.logo.data
        # filename = secure_filename(d.filename)
        # # Document and Profile photo save
        # d.save(os.path.join(assets_dir, filename))

        supplier = Supplier.Supplier(supplierid, create_supplier_form.name.data, create_supplier_form.abbreviation.data, create_supplier_form.products_offered.data, create_supplier_form.website.data, create_supplier_form.email.data, create_supplier_form.contactno.data, create_supplier_form.availability.data, create_supplier_form.logo.data)
        suppliers_dict[supplier.get_supplier_id()] = supplier
        db['Suppliers'] = suppliers_dict

        db.close()

        return redirect(url_for('inventory4'))
    return render_template('createSupplier.html', form=create_supplier_form)

@app.route('/inventory/inventory4P/createSupplierPhysical', methods=['GET', 'POST'])
def create_supplierP():
    create_supplier_form = CreateSupplierForm(request.form)
    create_supplierP_form = CreateSupplierPForm(request.form)
    if request.method == 'POST' and create_supplierP_form.validate() and create_supplier_form.validate():
        suppliersP_dict = {}
        db2 = shelve.open('supplierP.db', 'c')
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'c')

        try:
            supplierPid = 1

            suppliersP_dict = db2['SuppliersP']

            for key in suppliersP_dict:
                if key > supplierPid:
                    supplierPid = key
            supplierPid = supplierPid + 1

        except:
            print("Error in retrieving Users from supplierP.db.")

        try:
            supplierid = 1

            suppliers_dict = db['Suppliers']

            for key in suppliers_dict:
                if key > supplierid:
                    supplierid = key
            supplierid = supplierid + 1

        except:
            print("**Error in retrieving Users from supplier.db.")

        supplierP = SupplierPhysical.SupplierPhysical(supplierid, supplierPid, create_supplierP_form.name.data,
                                                      create_supplierP_form.abbreviation.data,
                                                      create_supplierP_form.products_offered.data,
                                                      create_supplierP_form.website.data,
                                                      create_supplierP_form.email.data,
                                                      create_supplierP_form.contactno.data, create_supplier_form.availability.data,
                                                      create_supplierP_form.logo.data,
                                                      create_supplierP_form.address.data)
        suppliersP_dict[supplierP.get_supplierphysical_id()] = supplierP
        db2['SuppliersP'] = suppliersP_dict

        supplier = Supplier.Supplier(supplierid, create_supplier_form.name.data, create_supplier_form.abbreviation.data,
                                     create_supplier_form.products_offered.data, create_supplier_form.website.data,
                                     create_supplier_form.email.data, create_supplier_form.contactno.data, create_supplier_form.availability.data,
                                     create_supplier_form.logo.data)
        suppliers_dict[supplier.get_supplier_id()] = supplier
        db['Suppliers'] = suppliers_dict

        db2.close()
        db.close()

        return redirect(url_for('inventory4P'))
    return render_template('createSupplierPhysical.html', form=create_supplierP_form)

# can try
@app.route('/inventory/inventory3/updateOrder/<int:id>/', methods=['GET', 'POST'])
def update_order(id):
    update_order_form = CreateOrderForm(request.form)
    #can delete
    # orders_dict = {}
    # db2 = shelve.open('order.db', 'r')
    # products_dict = db2['Orders']
    # db2.close()
    # order2 = orders_dict.get(id)

    if request.method == 'POST':
        orders_dict = {}
        db = shelve.open('order.db', 'w')
        orders_dict = db['Orders']

        order = orders_dict.get(id)
        order.set_product(order.get_product())
        order.set_orderamt(update_order_form.orderamt.data)
        order.set_cost(order.get_cost())

        order.set_remarks(update_order_form.remarks.data)
        order.set_delivered(update_order_form.delivered.data)

        db['Orders'] = orders_dict

        if order.get_delivered() == 1:
            products_dict = {}
            db2 = shelve.open('productJY.db', 'w')
            products_dict = db2['Products']

            product = products_dict.get(order.get_productid())
            product.set_quantity(int(order.get_orderamt() + product.get_quantity()))
            product.set_ordered(1)

            db2['Products'] = products_dict
            db2.close()

        db.close()

        return redirect(url_for('inventory3'))
    else:
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()

        order = orders_dict.get(id)
        update_order_form.product.data = order.get_product()
        update_order_form.orderamt.data = order.get_orderamt()
        update_order_form.cost.data = order.get_cost()

        update_order_form.remarks.data = order.get_remarks()
        update_order_form.delivered.data = order.get_delivered()

        return render_template('updateOrder.html', form=update_order_form, order=order)

@app.route('/inventory/inventory4/updateSupplier/<int:id>/', methods=['GET', 'POST'])
def update_supplier(id):
    update_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and update_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'w')
        suppliers_dict = db['Suppliers']

        supplier = suppliers_dict.get(id)
        supplier.set_name(update_supplier_form.name.data)
        supplier.set_abbreviation(update_supplier_form.abbreviation.data)
        supplier.set_products_offered(update_supplier_form.products_offered.data)
        supplier.set_availability(update_supplier_form.availability.data)
        supplier.set_website(update_supplier_form.website.data)
        supplier.set_email(update_supplier_form.email.data)
        supplier.set_contactno(update_supplier_form.contactno.data)
        supplier.set_logo(update_supplier_form.logo.data)

        try:
            db2 = shelve.open('supplierP.db', 'w')
            # print("success 1st")
            suppliersP_dict = db2['SuppliersP']
            # print("success 2nd")

            for key in suppliersP_dict:
                # print('real test %d' % key)
                if supplier.get_supplier_id() == suppliersP_dict.get(key).get_supplier_id():
                    supplierP1 = suppliersP_dict.get(key).get_supplierphysical_id()
                    # print("success 3rd")
                    print(supplierP1)
            supplierP = suppliersP_dict.get(supplierP1)
            supplierP.set_name(update_supplier_form.name.data)
            supplierP.set_abbreviation(update_supplier_form.abbreviation.data)
            supplierP.set_products_offered(update_supplier_form.products_offered.data)
            supplierP.set_availability(update_supplier_form.availability.data)
            supplierP.set_website(update_supplier_form.website.data)
            supplierP.set_email(update_supplier_form.email.data)
            supplierP.set_contactno(update_supplier_form.contactno.data)
            supplierP.set_logo(update_supplier_form.logo.data)
            print('successful test P')
            db2['SuppliersP'] = suppliersP_dict
            db2.close()
        except:

          print("Supplier %d has no Physical Address" %id)

        db['Suppliers'] = suppliers_dict
        print('test 1')
        db.close()

        return redirect(url_for('inventory4'))
    else:
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()

        supplier = suppliers_dict.get(id)
        update_supplier_form.name.data = supplier.get_name()
        update_supplier_form.abbreviation.data = supplier.get_abbreviation()
        update_supplier_form.products_offered.data = supplier.get_products_offered()
        update_supplier_form.availability.data = supplier.get_availability()
        update_supplier_form.website.data = supplier.get_website()
        update_supplier_form.email.data = supplier.get_email()
        update_supplier_form.contactno.data = supplier.get_contactno()
        update_supplier_form.logo.data = supplier.get_logo()
        print('test 2')

        return render_template('updateSupplier.html', form=update_supplier_form, suppliertest = supplier)

@app.route('/inventory/inventory4P/updateSupplierPhysical/<int:id>/', methods=['GET', 'POST'])
def update_supplierP(id):
    update_supplierP_form = CreateSupplierPForm(request.form)
    update_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and update_supplierP_form.validate():
        suppliersP_dict = {}
        db = shelve.open('supplierP.db', 'w')
        suppliersP_dict = db['SuppliersP']

        suppliers_dict = {}
        db2 = shelve.open('supplier.db', 'w')
        suppliers_dict = db2['Suppliers']

        supplierP = suppliersP_dict.get(id)
        supplierP.set_name(update_supplierP_form.name.data)
        supplierP.set_abbreviation(update_supplierP_form.abbreviation.data)
        supplierP.set_products_offered(update_supplierP_form.products_offered.data)
        supplierP.set_availability(update_supplierP_form.availability.data)
        supplierP.set_website(update_supplierP_form.website.data)
        supplierP.set_email(update_supplierP_form.email.data)
        supplierP.set_contactno(update_supplierP_form.contactno.data)
        supplierP.set_address(update_supplierP_form.address.data)
        supplierP.set_logo(update_supplierP_form.logo.data)

        for key in suppliers_dict:
            if supplierP.get_supplier_id() == suppliers_dict.get(key).get_supplier_id():
                supplier1 = suppliers_dict.get(key).get_supplier_id()
                print(supplier1)
        supplier = suppliers_dict.get(supplier1)
        supplier.set_name(update_supplierP_form.name.data)
        supplier.set_abbreviation(update_supplierP_form.abbreviation.data)
        supplier.set_products_offered(update_supplierP_form.products_offered.data)
        supplier.set_availability(update_supplierP_form.availability.data)
        supplier.set_website(update_supplierP_form.website.data)
        supplier.set_email(update_supplierP_form.email.data)
        supplier.set_contactno(update_supplierP_form.contactno.data)
        supplier.set_logo(update_supplierP_form.logo.data)

        db['SuppliersP'] = suppliersP_dict
        db2['Suppliers'] = suppliers_dict
        db.close()
        db2.close()

        return redirect(url_for('inventory4P'))
    else:
        suppliersP_dict = {}
        db = shelve.open('supplierP.db', 'r')
        suppliersP_dict = db['SuppliersP']
        db.close()

        supplierP = suppliersP_dict.get(id)
        update_supplierP_form.name.data = supplierP.get_name()
        update_supplierP_form.abbreviation.data = supplierP.get_abbreviation()
        update_supplierP_form.products_offered.data = supplierP.get_products_offered()
        update_supplierP_form.availability.data = supplierP.get_availability()
        update_supplierP_form.website.data = supplierP.get_website()
        update_supplierP_form.email.data = supplierP.get_email()
        update_supplierP_form.contactno.data = supplierP.get_contactno()
        update_supplierP_form.address.data = supplierP.get_address()
        update_supplierP_form.logo.data = supplierP.get_logo()

        return render_template('updateSupplierPhysical.html', form=update_supplierP_form,suppliertest = supplierP)

@app.route('/updateAvailabilityProduct/<int:id>', methods=['POST'])
def update_availability_product(id):
    update_availability_form = CreateProductFormJY(request.form)
    if request.method == 'POST':
        products_dict = {}
        db = shelve.open('productJY.db', 'w')
        products_dict = db['Products']

        product = products_dict.get(id)
        if product.get_availability() == 1:
            product.set_availability(0)
        else:
            product.set_availability(1)

        db['Products'] = products_dict
        db.close()

        return redirect(url_for('inventory2'))

@app.route('/updateDeliveredOrder/<int:id>', methods=['POST'])
def update_delivered_order(id):
    if request.method == 'POST':
        orders_dict = {}
        db = shelve.open('order.db', 'w')
        orders_dict = db['Orders']

        order = orders_dict.get(id)
        if order.get_delivered() == 0:
            order.set_delivered(1)
            if order.get_delivered() == 1:
                products_dict = {}
                db2 = shelve.open('productJY.db', 'w')
                products_dict = db2['Products']

                product = products_dict.get(order.get_productid())
                product.set_quantity(int(order.get_orderamt() + product.get_quantity()))
                product.set_ordered(1)

                db2['Products'] = products_dict
                db2.close()

        db['Orders'] = orders_dict
        db.close()

        return redirect(url_for('inventory3'))

@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    orders_dict = {}
    db = shelve.open('order.db', 'w')
    orders_dict = db['Orders']

    products_dict = {}
    db2 = shelve.open('productJY.db', 'w')
    products_dict = db2['Products']

    order = orders_dict.get(id)
    product = products_dict.get(order.get_productid())
    product.set_ordered(1)
    db2['Products'] = products_dict
    db2.close()

    orders_dict.pop(id)

    db['Orders'] = orders_dict
    db.close()

    return redirect(url_for('inventory3'))

# Tariq Part ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@app.route('/')
def pg1():
    # if session['username'] == None:
    #
    return render_template('Pg1.html', username=session['username'])

@app.route('/Pg2')
def pg2():
    return render_template('Pg2.html')

@app.route('/single')
def single():
    return render_template('single.html')



@app.route('/createProduct', methods=['GET', 'POST'])
def create_product():
    create_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and create_product_form.validate():


        products_dict = {}
        db = shelve.open('product.db', 'c')

        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving Products from product.db.")

        product = Product.Product(create_product_form.name.data, create_product_form.description.data, create_product_form.features.data, create_product_form.colours.data, create_product_form.category.data, create_product_form.status.data, create_product_form.price.data)
        products_dict[product.get_product_id()] = product
        db['Products'] = products_dict



        db.close()

        return redirect(url_for('retrieve_products'))
    return render_template('createProduct.html', form=create_product_form)

@app.route('/retrieveProducts')
def retrieve_products():
    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)



    return render_template(('retrieveProducts.html'), count=len(products_list), products_list=products_list)

@app.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        products_dict = {}
        db = shelve.open('product.db', 'w')
        products_dict = db['Products']

        product = products_dict.get(id)
        product.set_name(update_product_form.name.data)
        product.set_description(update_product_form.description.data)
        product.set_features(update_product_form.features.data)
        product.set_colours(update_product_form.colours.data)
        product.set_category(update_product_form.category.data)
        product.set_status(update_product_form.status.data)
        product.set_price(update_product_form.price.data)

        db['Products'] = products_dict
        db.close()



        return redirect(url_for('retrieve_products'))
    else:
        products_dict = {}
        db = shelve.open('product.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        update_product_form.name.data = product.get_name()
        update_product_form.description.data = product.get_description()
        update_product_form.features.data = product.get_features()
        update_product_form.colours.data = product.get_colours()
        update_product_form.category.data = product.get_category()
        update_product_form.status.data = product.get_status()
        update_product_form.price.data = product.get_price()

        return render_template('updateProduct.html', form=update_product_form)

@app.route('/retrieveProductsCustomer')
def retrieve_products_customer():

    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()


    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)



    return render_template(('Pg2.html'), count=len(products_list), products_list=products_list)

@app.route('/viewProductsCustomer')
def view_products_customer():

    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()


    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)



    return render_template(('single.html'), count=len(products_list), products_list=products_list)

@app.route('/viewProductsCustomer2')
def view_products_customer2():

    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()


    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)



    return render_template(('single2.html'), count=len(products_list), products_list=products_list)

@app.route('/viewProductsCustomer3')
def view_products_customer3():

    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()


    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)



    return render_template(('single3.html'), count=len(products_list), products_list=products_list)

@app.route('/createElectronic', methods=['GET', 'POST'])
def create_electronic():
    create_electronic_form = CreateElectronicForm(request.form)
    if request.method == 'POST' and create_electronic_form.validate():
        electronics_dict = {}
        db = shelve.open('electronic.db', 'c')

        try:
            electronics_dict = db['Electronics']
        except:
            print("Error in retrieving Electronics from electronic.db.")

        electronic = Electronic.Electronic(create_electronic_form.name.data, create_electronic_form.description.data, create_electronic_form.features.data, create_electronic_form.colours.data, create_electronic_form.category.data, create_electronic_form.status.data, create_electronic_form.price.data, create_electronic_form.assembly.data )
        electronics_dict[electronic.get_electronic_id()] = electronic
        db['Electronics'] = electronics_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createElectronic.html', form=create_electronic_form)

@app.route('/retrieveElectronics')
def retrieve_electronics():
    electronics_dict = {}
    db = shelve.open('electronic.db', 'r')
    electronics_dict = db['Electronics']
    db.close()

    electronics_list = []
    for key in electronics_dict:
        electronic = electronics_dict.get(key)
        electronics_list.append(electronic)

    return render_template('retrieveElectronics.html', count=len(electronics_list), electronics_list=electronics_list)

# Tariq END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alfi START @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @app.route('/home2')
# def home2():
#     return render_template('home2.html')


@app.route('/createDelivery', methods=['GET', 'POST'])
def create_delivery():
    create_delivery_form = CreateDeliveryForm(request.form)
    if request.method == 'POST' and create_delivery_form.validate():
        deliveries_dict = {}
        db = shelve.open('delivery.db', 'c')

        try:
            deliveries_dict = db['Deliveries']

        except:
            print("Error in retrieving Deliveries from deliveries.db.")

        delivery = Delivery.Delivery(create_delivery_form.date_delivery.data, create_delivery_form.time_delivery.data,
                                     create_delivery_form.delivery_address.data, create_delivery_form.receiver_name.data,
                                     create_delivery_form.pricing.data)
        deliveries_dict[delivery.get_delivery_id()] = delivery
        db['Deliveries'] = deliveries_dict

        db.close()

        return redirect(url_for('review_delivery'))
    return render_template('createDelivery.html', form=create_delivery_form)

@app.route('/reviewDelivery')
def review_delivery():
    deliveries_dict = {}
    db = shelve.open('delivery.db', 'r')
    deliveries_dict = db['Deliveries']
    db.close()

    deliveries_list = []
    for key in deliveries_dict:
        delivery = deliveries_dict.get(key)
        deliveries_list.append(delivery)

    return render_template('reviewDelivery.html', count=len(deliveries_list), deliveries_list=deliveries_list)

# @app.route('/Pg1')
# def Pg1():
#     deliveries_dict = {}
#     db = shelve.open('delivery.db', 'r')
#     deliveries_dict = db['Deliveries']
#     db.close()
#
#     deliveries_list = []
#     for key in deliveries_dict:
#         delivery = deliveries_dict.get(key)
#         deliveries_list.append(delivery)
#
#     return render_template('Pg1.html', count=len(deliveries_list), deliveries_list=deliveries_list)

@app.route('/updateDelivery/<int:id>/', methods=['GET', 'POST'])
def update_delivery(id):
    update_delivery_form = CreateDeliveryForm(request.form)
    if request.method == 'POST' and update_delivery_form.validate():
        deliveries_dict = {}
        db = shelve.open('delivery.db', 'w')
        deliveries_dict = db['Deliveries']

        delivery = deliveries_dict.get(id)
        delivery.set_receiver_name(update_delivery_form.receiver_name.data)
        delivery.set_delivery_address(update_delivery_form.delivery_address.data)
        delivery.set_date_delivery(update_delivery_form.date_delivery.data)
        delivery.set_time_delivery(update_delivery_form.time_delivery.data)
        delivery.set_pricing(update_delivery_form.pricing.data)

        db['Deliveries'] = deliveries_dict
        db.close()

        return redirect(url_for('review_delivery'))
    else:
        deliveries_dict = {}
        db = shelve.open('delivery.db', 'r')
        deliveries_dict = db['Deliveries']
        db.close()

        delivery = deliveries_dict.get(id)
        update_delivery_form.receiver_name.data = delivery.get_receiver_name()
        update_delivery_form.delivery_address.data = delivery.get_delivery_address()
        update_delivery_form.date_delivery.data = delivery.get_date_delivery()
        update_delivery_form.time_delivery.data = delivery.get_time_delivery()
        update_delivery_form.pricing.data = delivery.get_pricing()

        return render_template('updateDelivery.html', form=update_delivery_form)
#
@app.route('/createPending', methods=['GET', 'POST'])
def pending_delivery():
    pending_delivery_form = PendingDeliveryForm(request.form)
    if request.method == 'POST' and pending_delivery_form.validate():
        pending_dict = {}
        db = shelve.open('pending.db', 'c')

        try:
            pending_dict = db['Pendings']
        except:
            print("Error in retrieving Pendings from pending.db")

        pending = Pending.Pending(pending_delivery_form.delivery_address.data, pending_delivery_form.receiver_name.data,
                                  pending_delivery_form.email.data, pending_delivery_form.confirmation.data,
                                  pending_delivery_form.remarks.data, pending_delivery_form.date_delivery.data,
                                  pending_delivery_form.time_delivery.data, pending_delivery_form.pricing.data)
        pending_dict[pending.get_pending_id()] = pending
        db['Pendings'] = pending_dict

        db.close()

        return redirect(url_for('retrieve_pending'))
    return render_template('createPending.html', form=pending_delivery_form)

@app.route('/retrievePending')
def retrieve_pending():
    pending_dict = {}
    db = shelve.open('pending.db', 'r')
    pending_dict = db['Pendings']
    db.close()

    pending_list = []
    for key in pending_dict:
        pending = pending_dict.get(key)
        pending_list.append(pending)


    return render_template('retrievePending.html', count=len(pending_list), pending_list=pending_list)

@app.route('/updatePending/<int:id>/', methods=['GET', 'POST'])
def update_pending(id):
    update_pending_form = PendingDeliveryForm(request.form)
    if request.method == 'POST' and update_pending_form.validate():
        pending_dict = {}
        db = shelve.open('pending.db', 'w')
        pending_dict = db['Pendings']

        pending = pending_dict.get(id)
        pending.set_receiver_name(update_pending_form.time_delivery.data)
        pending.set_delivery_address(update_pending_form.date_delivery.data)
        pending.set_email(update_pending_form.email.data)
        pending.set_confirmation(update_pending_form.confirmation.data)
        pending.set_remarks(update_pending_form.remarks.data)
        pending.set_date_delivery(update_pending_form.delivery_address.data)
        pending.set_time_delivery(update_pending_form.receiver_name.data)
        pending.set_pricing(update_pending_form.pricing.data)


        db['Pendings'] = pending_dict
        db.close()

        return redirect(url_for('retrieve_pending'))
    else:
        pending_dict = {}
        db = shelve.open('pending.db', 'r')
        pending_dict = db['Pendings']
        db.close()

        pending = pending_dict.get(id)
        update_pending_form.receiver_name.data = pending.get_time_delivery()
        update_pending_form.delivery_address.data = pending.get_date_delivery()
        update_pending_form.email.data = pending.get_email()
        update_pending_form.confirmation.data = pending.get_confirmation()
        update_pending_form.remarks.data = pending.get_remarks()
        update_pending_form.date_delivery.data = pending.get_delivery_address()
        update_pending_form.time_delivery.data = pending.get_receiver_name()
        update_pending_form.pricing.data = pending.get_pricing()


        return render_template('updatePending.html', form=update_pending_form)

# Alfi END @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# An Teng $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

@app.route('/CreateReward', methods=['GET', 'POST'])
def Create_Reward():
    Create_Reward_form = CreateRewardForm(request.form)
    if request.method == 'POST' and Create_Reward_form.validate():
        Rewards_dict = {}
        db = shelve.open('Reward.db', 'c')

        try:
            Reward_ID=1
            Rewards_dict = db['Rewards']
            for key in Rewards_dict:
                if key>Reward_ID:
                    Reward_ID=key
                Reward_ID+=1
        except:
            print("Error in retrieving Rewards from Reward.db.")
        reward = Reward.Reward(Reward_ID,Create_Reward_form.Name.data,Create_Reward_form.Description.data,Create_Reward_form.Price.data,Create_Reward_form.Validity.data)
        Rewards_dict[reward.get_Reward_ID()] = reward
        db['Rewards'] = Rewards_dict

        db.close()

        return redirect(url_for('RewardList'))
    return render_template('CreateReward.html', form=Create_Reward_form)

@app.route('/CreateSpecial', methods=['GET', 'POST'])
def Create_Special():
    Create_Special_Form = CreateSpecialForm(request.form)
    if request.method == 'POST' and Create_Special_Form.validate():
        Special_dict = {}
        db = shelve.open('Special.db', 'c')

        try:
            Special_ID=1
            Special_dict = db['Special']
            for key in Special_dict:
                if key>Special_ID:
                    Special_ID=key
                Special_ID+=1
        except:
            print("Error in retrieving Special Reward from Special.db.")
        special = Special.Special(Special_ID,Create_Special_Form.Name.data,Create_Special_Form.Description.data,Create_Special_Form.Price.data,Create_Special_Form.Validity.data,Create_Special_Form.Usability.data)
        Special_dict[special.get_Special_ID()] = special
        db['Special'] = Special_dict

        db.close()

        return redirect(url_for('SpecialList'))
    return render_template('CreateSpecial.html', form=Create_Special_Form)

@app.route('/RewardList')
def RewardList():
    Rewards_dict = {}
    db = shelve.open('Reward.db', 'r')
    Rewards_dict = db['Rewards']
    db.close()
    rewards_list = []
    for key in Rewards_dict:
        reward = Rewards_dict.get(key)
        rewards_list.append(reward)

    return render_template('RewardList.html',count=len(rewards_list), rewards_list=rewards_list)

@app.route('/SpecialList')
def SpecialList():
    Special_dict = {}
    db = shelve.open('Special.db', 'r')
    Special_dict = db['Special']
    db.close()
    special_list = []
    for key in Special_dict:
        special = Special_dict.get(key)
        special_list.append(special)

    return render_template('SpecialList.html',count=len(special_list), special_list=special_list)

@app.route('/deleteReward/<int:id>', methods=['POST'])
def delete_reward(id):
    reward_dict = {}
    db = shelve.open('reward.db', 'w')
    Rewards_dict = db['Rewards']

    Rewards_dict.pop(id)

    db['Rewards'] = Rewards_dict
    db.close()

    return redirect(url_for('RewardList'))

@app.route('/deleteSpecial/<int:id>', methods=['POST'])
def delete_special(id):
    special_dict = {}
    db = shelve.open('Special.db', 'w')
    Special_dict = db['Special']

    Special_dict.pop(id)

    db['Special'] = Special_dict
    db.close()

    return redirect(url_for('SpecialList'))

@app.route('/currentspecial/<int:id>')
def current_special(id):
    Special_dict={}
    current_dict={}
    db = shelve.open('Special.db', 'r')
    Special_dict = db['Special']
    db2 = shelve.open('Current.db', 'c')
    try:
        current_dict=db2['Current']
    except:
        print("Error in opening Current.db")
    current_dict[id]=Special_dict[id]
    c=Special_dict.get(id)
    c.set_check(1)
    db['Special']=Special_dict
    db2['Current']=current_dict
    db.close()
    db2.close()
    return redirect(url_for('CurrentSpecialList'))

@app.route('/currentreward/<int:id>')
def current_reward(id):
    Reward_dict={}
    current_dict={}
    db = shelve.open('Reward.db', 'r')
    Reward_dict = db['Rewards']
    db2 = shelve.open('CurrentReward.db', 'c')
    try:
        current_dict=db2['Current']
    except:
        print("Error in opening CurrentReward.db")
    current_dict[id]=Reward_dict[id]
    c=Reward_dict.get(id)
    c.set_check(1)
    db['Rewards']=Reward_dict
    db2['Current']=current_dict
    db.close()
    db2.close()
    return redirect(url_for('CurrentList'))

@app.route('/CurrentSpecial')
def CurrentSpecialList():
    try:
        Current_dict = {}
        db = shelve.open('Current.db', 'r')
        Current_dict = db['Current']
        db.close()
        current_list = []
        for key in Current_dict:
            current = Current_dict.get(key)
            current_list.append(current)
    except:
        current_list=[]
    return render_template('CurrentSpecial.html',count=len(current_list), current_list=current_list)

@app.route('/Current')
def CurrentList():
    try:
        Current_dict = {}
        db = shelve.open('CurrentReward.db', 'r')
        Current_dict = db['Current']
        db.close()
        current_list = []
        for key in Current_dict:
            current = Current_dict.get(key)
            current_list.append(current)
    except:
        current_list=[]
    return render_template('Current.html',count=len(current_list), current_list=current_list)

@app.route('/SetLimit/<int:id>/', methods=['GET', 'POST'])
def SetLimit(id):
    Set_Limit=SetLimitForm(request.form)
    if request.method=='POST' and Set_Limit.validate():
        Current_dict = {}
        db = shelve.open('Current.db', 'w')
        Current_dict=db['Current']
        Set=Current_dict.get(id)
        Set.set_Limit(Set_Limit.Limit.data)
        Set.set_Redeemed(0)
        db['Current']=Current_dict
        db.close()
        return redirect(url_for('CurrentSpecialList'))
    return render_template('SetLimit.html', form=Set_Limit)

@app.route('/SetLimitReward/<int:id>/', methods=['GET', 'POST'])
def SetLimitReward(id):
    Set_Limit=SetLimitForm(request.form)
    if request.method=='POST' and Set_Limit.validate():
        Current_dict = {}
        db = shelve.open('CurrentReward.db', 'w')
        Current_dict=db['Current']
        Set=Current_dict.get(id)
        Set.set_Limit(Set_Limit.Limit.data)
        Set.set_Redeemed(0)
        db['Current']=Current_dict
        db.close()
        return redirect(url_for('CurrentList'))
    return render_template('SetLimit.html', form=Set_Limit)

@app.route('/removespecial/<int:id>', methods=['POST'])
def removespecial(id):
    Current_dict = {}
    Special_dict={}
    db = shelve.open('Current.db', 'w')
    Current_dict = db['Current']
    Current_dict.pop(id)
    db2 = shelve.open('Special.db', 'r')
    Special_dict = db2['Special']
    c=Special_dict.get(id)
    c.set_check(0)
    db['Current'] = Current_dict
    db2['Special']=Special_dict
    db.close()
    db2.close()
    return redirect(url_for('CurrentSpecialList'))

@app.route('/removereward/<int:id>', methods=['POST'])
def removereward(id):
    Current_dict = {}
    Reward_dict={}
    db = shelve.open('CurrentReward.db', 'w')
    Current_dict = db['Current']
    Current_dict.pop(id)
    db2 = shelve.open('Reward.db', 'r')
    Reward_dict = db2['Rewards']
    c=Reward_dict.get(id)
    c.set_check(0)
    db['Current'] = Current_dict
    db2['Rewards']=Reward_dict
    db.close()
    db2.close()
    return redirect(url_for('CurrentList'))

@app.route('/Store')
def Store():
    try:
        Current_dict = {}
        db = shelve.open('CurrentReward.db', 'r')
        Current_dict = db['Current']
        db.close()
        current_list = []
        for key in Current_dict:
            current = Current_dict.get(key)
            current_list.append(current)
    except:
        current_list=[]
    return render_template('Store.html',count=len(current_list), current_list=current_list)

@app.route('/SpecialStore')
def SpecialStore():
    try:
        today=date.today()
        Current_dict = {}
        db = shelve.open('Current.db', 'r')
        Current_dict = db['Current']
        db.close()
        current_list = []
        for key in Current_dict:
            current = Current_dict.get(key)
            current_list.append(current)
    except:
        current_list=[]
    return render_template('SpecialStore.html',count=len(current_list), current_list=current_list, today=today)

@app.route('/Purchase/<int:id>')
def Purchase(id):
    Current_dict = {}
    History_dict ={}
    Inventory_dict={}
    db = shelve.open('CurrentReward.db', 'w')
    Current_dict = db['Current']
    c=Current_dict.get(id)
    Redeemed=c.get_Redeemed()
    Redeemed+=1
    c.set_Redeemed(Redeemed)
    db['Current'] = Current_dict
    try:
        db2 = shelve.open('History.db', 'c')
        History_dict=db2['History']
    except:
        print("Error in opening History.db")
    history=History1.History('Redeemed',c.get_Name(),date.today())
    History_dict[c.get_Name()]=history
    db2['History']=History_dict
    try:
        db3 = shelve.open('Inventory.db', 'c')
        Inventory_dict=db3['Inventory']
    except:
        print("Error in opening Inventory.db")
    Inventory_dict[id]=Current_dict[id]
    Inv=Inventory_dict.get(id)
    expiary=date.today() + timedelta(days=int(c.get_Validity()))
    Inv.set_expiary(expiary)
    db3['Inventory']=Inventory_dict
    db.close()
    db2.close()
    db3.close()
    return redirect(url_for('Inventory'))

@app.route('/PurchaseSpecial/<int:id>')
def PurchaseSpecial(id):
    Current_dict = {}
    db = shelve.open('Current.db', 'w')
    Current_dict = db['Current']
    c=Current_dict.get(id)
    Redeemed=c.get_Redeemed()
    Redeemed+=1
    c.set_Redeemed(Redeemed)
    db['Current'] = Current_dict
    db.close()
    return redirect(url_for('Inventory'))

@app.route('/History')
def History():
    try:
        History_dict = {}
        db = shelve.open('History.db', 'r')
        History_dict = db['History']
        db.close()
        history_list = []
        for key in History_dict:
            history = History_dict.get(key)
            history_list.append(history)
    except:
        history_list=[]
    return render_template('History.html',count=len(history_list), history_list=history_list)

@app.route('/Inventory')
def Inventory():
    try:
        Inventory_dict = {}
        db = shelve.open('Inventory.db', 'w')
        Inventory_dict = db['Inventory']
        inventory_list = []
        for key in Inventory_dict:
            inventory = Inventory_dict.get(key)
            inventory_list.append(inventory)
    except:
        inventory_list=[]
    return render_template('RewardInventory.html',count=len(inventory_list), inventory_list=inventory_list)

# An Teng END $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Heng Feng ********************************************************************

@app.route('/login_web', methods=['GET', 'POST'])
def login_customer_web(error=None):

    login_customer_web_form = LoginForm(request.form)
    if request.method == 'POST' and login_customer_web_form.validate():

        db = shelve.open('customer_web.db', 'r')
        customers_web_dict = db['Customers_web']

        for key in customers_web_dict:
            if login_customer_web_form.username.data == customers_web_dict.get(key).get_username():
                if login_customer_web_form.password.data == customers_web_dict.get(key).get_password():
                    session['username'] = request.form.get('username')
                    error = None
                    return redirect(url_for('pg1'))
                else:
                    error = 'wrongpassword'
                    break
            else:
                flash("Account not created")
    return render_template('login_web.html', form=login_customer_web_form, error=error, username= login_customer_web_form.username.object_data)

@app.route('/login_admin_web', methods=['GET', 'POST'])
def login_admin_web(error=None):

    login_admin_web_form = LoginForm(request.form)
    if request.method == 'POST' and login_admin_web_form.validate():

        db = shelve.open('admin_web.db', 'r')
        admins_web_dict = db['Admins_web']

        for key in admins_web_dict:
            if login_admin_web_form.username.data == admins_web_dict.get(key).get_username():
                if login_admin_web_form.password.data == admins_web_dict.get(key).get_password():
                    session['username'] = request.form.get('username')
                    error = None
                    return redirect(url_for('home'))
                else:
                    error = 'wrongpassword'
                    break
            else:
                flash("Account not created. Returning to Customer Login Page.")
                break
    return render_template('login_web.html', form=login_admin_web_form, error=error)

@app.route('/register_customer', methods=['GET', 'POST'])
def register_customer():
    create_customer_web_form = CreateCustomerForm(request.form)

    if request.method == 'POST' and create_customer_web_form.validate():
        customers_web_dict = {}
        db = shelve.open('customer_web.db', 'c')

        try:
            customers_web_dict = db['Customers_web']
        except:
            print("Error in retrieving Customers from customer_web.db.")

        customer = customer_web.customer_web(create_customer_web_form.first_name.data,
                                             create_customer_web_form.last_name.data,
                                             create_customer_web_form.gender.data,
                                             create_customer_web_form.email.data,
                                             create_customer_web_form.phone_number.data,
                                             create_customer_web_form.date_of_birth.data,
                                             create_customer_web_form.region.data,
                                             create_customer_web_form.street.data,
                                             create_customer_web_form.unit_number.data,
                                             create_customer_web_form.block.data,
                                             create_customer_web_form.username.data,
                                             create_customer_web_form.password.data,
                                             create_customer_web_form.confirm_password.data,
                                             create_customer_web_form.status.data)

        customers_web_dict[customer.get_customer_id()] = customer
        db['Customers_web'] = customers_web_dict

        db.close()
        session['username'] = customer.get_username()

        return redirect(url_for('customer_account_created'))
    return render_template('register_customer_web.html', form=create_customer_web_form)

@app.route('/customer_account_created')
def customer_account_created():
    return render_template("customer_account_created_web.html")

@app.route('/customer_retrieve_account')
def customer_retrieve_account():
    customers_web_dict = {}
    db = shelve.open('customer_web.db', 'r')
    customers_web_dict = db['Customers_web']
    db.close()

    customers_list = []
    current_customer = session['username']
    for key in customers_web_dict:
        customer = customers_web_dict.get(key)
        if customer.get_username() == current_customer:
            customers_list.append(customer)

    return render_template('customer_retrieve_account.html', count=len(customers_list), customers_list=customers_list)

@app.route('/admin_retrieve_account')
def admin_retrieve_account():
    customers_web_dict = {}
    db = shelve.open('customer_web.db', 'r')
    customers_web_dict = db['Customers_web']
    db.close()

    customers_list = []
    for key in customers_web_dict:
        customer = customers_web_dict.get(key)
        customers_list.append(customer)

    return render_template('admin_retrieve_account.html', count=len(customers_list), customers_list=customers_list)

@app.route('/update_customer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_web_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_web_form.validate():
        customers_web_dict = {}
        db = shelve.open('customer_web.db', 'w')
        customers_web_dict = db['Customers_web']

        customer = customers_web_dict.get(id)
        customer.set_first_name(update_customer_web_form.first_name.data)
        customer.set_last_name(update_customer_web_form.last_name.data)
        customer.set_username(update_customer_web_form.username.data)
        customer.set_gender(update_customer_web_form.gender.data)
        customer.set_email(update_customer_web_form.email.data)
        customer.set_phone_number(update_customer_web_form.phone_number.data)
        customer.set_date_of_birth(update_customer_web_form.date_of_birth.data)
        customer.set_region(update_customer_web_form.region.data)
        customer.set_street(update_customer_web_form.street.data)
        customer.set_unit_number(update_customer_web_form.unit_number.data)
        customer.set_block(update_customer_web_form.block.data)
        customer.set_password(update_customer_web_form.password.data)
        customer.set_confirm_password(update_customer_web_form.confirm_password.data)
        customer.set_status(update_customer_web_form.status.data)
        db['Customers_web'] = customers_web_dict
        db.close()
        session['customer_updated'] = customer.get_first_name() + ' ' + customer.get_last_name()

        return redirect(url_for('customer_retrieve_account'))
    else:
        customers_web_dict = {}
        db = shelve.open('customer_web.db', 'r')
        customers_web_dict = db['Customers_web']
        db.close()

        customer = customers_web_dict.get(id)
        update_customer_web_form.first_name.data = customer.get_first_name()
        update_customer_web_form.last_name.data = customer.get_last_name()
        update_customer_web_form.username.data = customer.get_username()
        update_customer_web_form.gender.data = customer.get_gender()
        update_customer_web_form.email.data = customer.get_email()
        update_customer_web_form.phone_number.data = customer.get_phone_number()
        update_customer_web_form.date_of_birth.data = customer.get_date_of_birth()
        update_customer_web_form.region.data = customer.get_region()
        update_customer_web_form.street.data = customer.get_street()
        update_customer_web_form.unit_number.data = customer.get_unit_number()
        update_customer_web_form.block.data = customer.get_block()
        update_customer_web_form.password.data = customer.get_password()
        update_customer_web_form.confirm_password.data = customer.get_confirm_password()
        update_customer_web_form.status.data = customer.get_status()
        return render_template('update_customer_web.html', form=update_customer_web_form)
#
# @app.route('/home_admin')
# def homepage_admin():
#     return render_template("home_admin_web.html")
#
@app.route('/register_admin', methods=['GET', 'POST'])
def register_admin():
    create_admin_web_form = CreateAdminForm(request.form)

    if request.method == 'POST' and create_admin_web_form.validate():
        admins_web_dict = {}
        db = shelve.open('admin_web.db', 'c')

        try:
            admins_web_dict = db['Admins_web']
        except:
            print("Error in retrieving Admins from admin_web.db.")

        admin = admin_web.admin_web(create_admin_web_form.first_name.data,
                                    create_admin_web_form.last_name.data,
                                    create_admin_web_form.username.data,
                                    create_admin_web_form.password.data,
                                    create_admin_web_form.confirm_password.data,
                                    create_admin_web_form.gender.data,
                                    create_admin_web_form.email.data,
                                    create_admin_web_form.phone_number.data,
                                    create_admin_web_form.status.data)
        admins_web_dict[admin.get_admin_id()] = admin
        db['Admins_web'] = admins_web_dict

        db.close()
        session['admin_created'] = admin.get_first_name() + ' ' + admin.get_last_name()
        return redirect(url_for('customer_account_created'))
    return render_template('register_admin_web.html', form=create_admin_web_form)

# for the update
# session['username'] = 'hflow'

@app.route('/retrieve_admin_account')
def retrieve_admin_account():
    admins_web_dict = {}
    db = shelve.open('admin_web.db', 'r')
    admins_web_dict = db['Admins_web']
    db.close()

    admins_list = []
    current_admin = session['username']
    for key in admins_web_dict:
        admin = admins_web_dict.get(key)
        if admin.get_username() == current_admin:
            admins_list.append(admin)

    return render_template('retrieve_admin_account.html', count=len(admins_list), admins_list=admins_list)

# not for the update (for viewing)
@app.route('/retrieve_admin')
def retrieve_admin():
    admins_web_dict = {}
    db = shelve.open('admin_web.db', 'r')
    admins_web_dict = db['Admins_web']
    db.close()

    admins_list = []
    for key in admins_web_dict:
        admin = admins_web_dict.get(key)
        admins_list.append(admin)

    return render_template('retrieve_admin.html', count=len(admins_list), admins_list=admins_list)

@app.route('/update_admin/<int:id>/', methods=['GET', 'POST'])
def update_admin(id):
    update_admin_web_form = CreateAdminForm(request.form)
    if request.method == 'POST' and update_admin_web_form.validate():
        admins_web_dict = {}
        db = shelve.open('admin_web.db', 'w')
        admins_web_dict = db['Admins_web']

        admin = admins_web_dict.get(id)
        admin.set_first_name(update_admin_web_form.first_name.data)
        admin.set_last_name(update_admin_web_form.last_name.data)
        admin.set_username(update_admin_web_form.username.data)
        admin.set_gender(update_admin_web_form.gender.data)
        admin.set_email(update_admin_web_form.email.data)
        admin.set_phone_number(update_admin_web_form.phone_number.data)
        admin.set_password(update_admin_web_form.password.data)
        admin.set_confirm_password(update_admin_web_form.confirm_password.data)
        admin.set_status(update_admin_web_form.status.data)

        db['Admins_web'] = admins_web_dict
        db.close()
        session['admin_updated'] = admin.get_first_name() + ' ' + admin.get_last_name()

        return redirect(url_for('retrieve_admin_account'))
    else:
        admins_web_dict = {}
        db = shelve.open('admin_web.db', 'r')
        admins_web_dict = db['Admins_web']
        db.close()

        admin = admins_web_dict.get(id)
        update_admin_web_form.first_name.data = admin.get_first_name()
        update_admin_web_form.last_name.data = admin.get_last_name()
        update_admin_web_form.username.data = admin.get_username()
        update_admin_web_form.gender.data = admin.get_gender()
        update_admin_web_form.email.data = admin.get_email()
        update_admin_web_form.phone_number.data = admin.get_phone_number()
        update_admin_web_form.password.data = admin.get_password()
        update_admin_web_form.confirm_password.data = admin.get_confirm_password()
        update_admin_web_form.status.data = admin.get_status()

        return render_template('update_admin_web.html', form=update_admin_web_form)

@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('pg1'))

# Heng Feng END **************************************************************************

if __name__ == '__main__':
    app.run(debug=True)
