
  
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `  ` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class Account(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Account'


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #companyid = models.ForeignKey('Company', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    #supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    wardid = models.ForeignKey('Ward', models.DO_NOTHING, db_column='WardID')  # Field name made lowercase.
    #userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    detail = models.CharField(db_column='Detail', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Address'


class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Admin'


class Authuser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='AdminID')  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='AccountID')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'AuthUser'


class Bank(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Bank'


class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Brand'


class Cart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'Cart'


class Cartproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Order', models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
          
        db_table = 'CartProduct'


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nationid = models.ForeignKey('Nation', models.DO_NOTHING, db_column='NationID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'City'


class Comment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    authuser = models.ForeignKey(User, models.DO_NOTHING, db_column='AuthUserID')  # Field name made lowercase.
    detail = models.CharField(db_column='Detail',max_length=2550, blank=True, null=True)  # Field name made lowercase.
    rate = models.IntegerField(default=1)
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')
    create_at=models.DateTimeField(db_column='create_at',auto_now_add=True)
    update_at=models.DateTimeField(db_column='update_at',auto_now=True)
    subject = models.CharField(max_length=255,blank=True)
    label = models.IntegerField(db_column='Label')
    def __str__(self):
        return self.subject
    class Meta:
          
        db_table = 'Comment'


class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Company'


class Creditcard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bankid = models.ForeignKey(Bank, models.DO_NOTHING, db_column='BankID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvc = models.CharField(db_column='Cvc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    expire = models.CharField(db_column='Expire', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'CreditCard'


class Discountcode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'DiscountCode'


class District(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CityID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'District'


class Fullname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    midname = models.CharField(db_column='Midname', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Fullname'


class Nation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Nation'


class Normalorganizedsupplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organizedsupplierid = models.ForeignKey('Organizedsupplier', models.DO_NOTHING, db_column='OrganizedSupplierID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'NormalOrganizedSupplier'


class Officialsupplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organizedsupplierid = models.ForeignKey('Organizedsupplier', models.DO_NOTHING, db_column='OrganizedSupplierID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'OfficialSupplier'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    discountcodeid = models.ForeignKey(Discountcode, models.DO_NOTHING, db_column='DiscountCodeID')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Order'


class Organizedsupplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'OrganizedSupplier'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paymenttypeid = models.ForeignKey('Paymenttype', models.DO_NOTHING, db_column='PaymentTypeID')  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Payment'


class Paymenttype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'PaymentType'


class Personalsupplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'PersonalSupplier'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BrandID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2550, blank=True, null=True)  # Field name made lowercase.
    productsubcategoryid = models.ForeignKey('Productsubcategory', models.DO_NOTHING, db_column='ProductSubCategoryID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'Product'


class Productcategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'ProductCategory'


class Productofsupplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    price = models.TextField(db_column='Price')  # Field name made lowercase. This field type is a guess.

    class Meta:
          
        db_table = 'ProductOfSupplier'


class Productsubcategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productcategoryid = models.ForeignKey(Productcategory, models.DO_NOTHING, db_column='ProductCategoryID')  # Field name made lowercase.
   
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'ProductSubCategory'


class Rating(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    commentid = models.ForeignKey(Comment, models.DO_NOTHING, db_column='CommentID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    star = models.TextField(db_column='Star')  # Field name made lowercase. This field type is a guess.

    class Meta:
          
        db_table = 'Rating'


class Shipment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shipperunitid = models.ForeignKey('Shipperunit', models.DO_NOTHING, db_column='ShipperUnitID')  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    shipmentdate = models.IntegerField(db_column='ShipmentDate', blank=True, null=True)  # Field name made lowercase.
    fee = models.TextField(db_column='Fee')  # Field name made lowercase. This field type is a guess.

    class Meta:
          
        db_table = 'Shipment'


class Shipperunit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'ShipperUnit'


class Supplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    authuserid = models.ForeignKey(Authuser, models.DO_NOTHING, db_column='AuthUserID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Supplier'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usertypeid = models.ForeignKey('Usertype', models.DO_NOTHING, db_column='UserTypeID')  # Field name made lowercase.
    fullnameid = models.ForeignKey(Fullname, models.DO_NOTHING, db_column='FullnameID')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'User'


class Usertype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'UserType'



class Viewedproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.        
    #productid2 = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID2')  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
          
        db_table = 'ViewedProduct'


class Ward(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    districtid = models.ForeignKey(District, models.DO_NOTHING, db_column='DistrictID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
          
        db_table = 'Ward'

