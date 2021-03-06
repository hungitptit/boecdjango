from django.db import models


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    authuserid = models.ForeignKey('Authuser', models.DO_NOTHING, db_column='AuthUserID')  # Field name made lowercase.
    wardid = models.ForeignKey('Ward', models.DO_NOTHING, db_column='WardID')  # Field name made 
lowercase.
    detail = models.CharField(db_column='Detail', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Authuser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made 
lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuthUser'


class Bank(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bank'


class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Brand'


class Cart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made 
lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'


class Cartproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    orderid = models.ForeignKey('Order', models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    productofsupplierid = models.ForeignKey('Productofsupplier', models.DO_NOTHING, db_column='ProductOfSupplierID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CartProduct'


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    nationid = models.ForeignKey('Nation', models.DO_NOTHING, db_column='NationID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'


class Comment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    authuserid = models.ForeignKey(Authuser, models.DO_NOTHING, db_column='AuthUserID')  # Field 
name made lowercase.
    detail = models.CharField(db_column='Detail', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'


class Creditcard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    bankid = models.ForeignKey(Bank, models.DO_NOTHING, db_column='BankID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made 
lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvc = models.CharField(db_column='Cvc', max_length=255, blank=True, null=True)  # Field name 
made lowercase.
    expire = models.CharField(db_column='Expire', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditCard'


class Discountcode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    code = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DiscountCode'


class District(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CityID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'District'


class Fullname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    midname = models.CharField(db_column='Midname', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fullname'


class Nation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nation'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartID')  # Field name made lowercase.
    discountcodeid = models.ForeignKey(Discountcode, models.DO_NOTHING, db_column='DiscountCodeID')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    paymentid = models.ForeignKey('Payment', models.DO_NOTHING, db_column='PaymentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    paymenttypeid = models.ForeignKey('Paymenttype', models.DO_NOTHING, db_column='PaymentTypeID')  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate', blank=True, null=True)  # Field name 
made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'


class Paymenttype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentType'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BrandID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productsubcategoryid = models.ForeignKey('Productsubcategory', models.DO_NOTHING, db_column='ProductSubCategoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Productcategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductCategory'


class Productofsupplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    price = models.TextField(db_column='Price')  # Field name made lowercase. This field type is 
a guess.

    class Meta:
        managed = False
        db_table = 'ProductOfSupplier'


class Productsubcategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    productcategoryid = models.ForeignKey(Productcategory, models.DO_NOTHING, db_column='ProductCategoryID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductSubCategory'


class Rating(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    productofsupplierid = models.ForeignKey(Productofsupplier, models.DO_NOTHING, db_column='ProductOfSupplierID')  # Field name made lowercase.
    commentid = models.ForeignKey(Comment, models.DO_NOTHING, db_column='CommentID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made 
lowercase.
    star = models.TextField(db_column='Star')  # Field name made lowercase. This field type is a 
guess.

    class Meta:
        managed = False
        db_table = 'Rating'


class Shipment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    shipperunitid = models.ForeignKey('Shipperunit', models.DO_NOTHING, db_column='ShipperUnitID')  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    shipmentdate = models.IntegerField(db_column='ShipmentDate', blank=True, null=True)  # Field 
name made lowercase.
    fee = models.TextField(db_column='Fee')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Shipment'


class Shipperunit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShipperUnit'


class Supplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    authuserid = models.ForeignKey(Authuser, models.DO_NOTHING, db_column='AuthUserID')  # Field 
name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    fullnameid = models.ForeignKey(Fullname, models.DO_NOTHING, db_column='FullnameID')  # Field 
name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name 
made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Viewedproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    productid2 = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID2')  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ViewedProduct'


class Ward(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    districtid = models.ForeignKey(District, models.DO_NOTHING, db_column='DistrictID')  # Field 
name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ward'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'