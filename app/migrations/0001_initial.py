# Generated by Django 3.2.4 on 2021-06-10 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Account',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Authuser',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=255, null=True)),
                ('role', models.CharField(blank=True, db_column='Role', max_length=255, null=True)),
                ('accountid', models.ForeignKey(db_column='AccountID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.account')),
                ('adminid', models.ForeignKey(db_column='AdminID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.admin')),
            ],
            options={
                'db_table': 'AuthUser',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Bank',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('detail', models.CharField(blank=True, db_column='Detail', max_length=255, null=True)),
                ('authuserid', models.ForeignKey(db_column='AuthUserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.authuser')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Discountcode',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'DiscountCode',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('cityid', models.ForeignKey(db_column='CityID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.city')),
            ],
            options={
                'db_table': 'District',
            },
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True)),
                ('midname', models.CharField(blank=True, db_column='Midname', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Fullname',
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Nation',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('orderdate', models.DateField(blank=True, db_column='OrderDate', null=True)),
                ('code', models.IntegerField(blank=True, db_column='Code', null=True)),
                ('cartid', models.ForeignKey(db_column='CartID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.cart')),
                ('discountcodeid', models.ForeignKey(db_column='DiscountCodeID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.discountcode')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Paymenttype',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'PaymentType',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('image', models.CharField(blank=True, db_column='Image', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('brandid', models.ForeignKey(db_column='BrandID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.brand')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Productcategory',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ProductCategory',
            },
        ),
        migrations.CreateModel(
            name='Shipperunit',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ShipperUnit',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('dateofbirth', models.DateField(blank=True, db_column='DateOfBirth', null=True)),
                ('fullnameid', models.ForeignKey(db_column='FullnameID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.fullname')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Usertype',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
            ],
            options={
                'db_table': 'UserType',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('districtid', models.ForeignKey(db_column='DistrictID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.district')),
            ],
            options={
                'db_table': 'Ward',
            },
        ),
        migrations.CreateModel(
            name='Viewedproduct',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user')),
            ],
            options={
                'db_table': 'ViewedProduct',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='usertypeid',
            field=models.ForeignKey(db_column='UserTypeID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.usertype'),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('authuserid', models.ForeignKey(db_column='AuthUserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.authuser')),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('shipmentdate', models.IntegerField(blank=True, db_column='ShipmentDate', null=True)),
                ('fee', models.TextField(db_column='Fee')),
                ('orderid', models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.order')),
                ('shipperunitid', models.ForeignKey(db_column='ShipperUnitID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.shipperunit')),
            ],
            options={
                'db_table': 'Shipment',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('star', models.TextField(db_column='Star')),
                ('commentid', models.ForeignKey(db_column='CommentID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.comment')),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user')),
            ],
            options={
                'db_table': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='Productsubcategory',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('productcategoryid', models.ForeignKey(db_column='ProductCategoryID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.productcategory')),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
            ],
            options={
                'db_table': 'ProductSubCategory',
            },
        ),
        migrations.CreateModel(
            name='Productofsupplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('price', models.TextField(db_column='Price')),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
                ('supplierid', models.ForeignKey(db_column='SupplierID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.supplier')),
            ],
            options={
                'db_table': 'ProductOfSupplier',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productsubcategoryid',
            field=models.ForeignKey(db_column='ProductSubCategoryID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.productsubcategory'),
        ),
        migrations.CreateModel(
            name='Personalsupplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('supplierid', models.ForeignKey(db_column='SupplierID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.supplier')),
            ],
            options={
                'db_table': 'PersonalSupplier',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('paymentdate', models.DateField(blank=True, db_column='PaymentDate', null=True)),
                ('orderid', models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.order')),
                ('paymenttypeid', models.ForeignKey(db_column='PaymentTypeID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.paymenttype')),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Organizedsupplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('companyid', models.ForeignKey(db_column='CompanyID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.company')),
                ('supplierid', models.ForeignKey(db_column='SupplierID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.supplier')),
            ],
            options={
                'db_table': 'OrganizedSupplier',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='userid',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user'),
        ),
        migrations.CreateModel(
            name='Officialsupplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('organizedsupplierid', models.ForeignKey(db_column='OrganizedSupplierID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.organizedsupplier')),
            ],
            options={
                'db_table': 'OfficialSupplier',
            },
        ),
        migrations.CreateModel(
            name='Normalorganizedsupplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('organizedsupplierid', models.ForeignKey(db_column='OrganizedSupplierID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.organizedsupplier')),
            ],
            options={
                'db_table': 'NormalOrganizedSupplier',
            },
        ),
        migrations.CreateModel(
            name='Creditcard',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('number', models.CharField(blank=True, db_column='Number', max_length=255, null=True)),
                ('cvc', models.CharField(blank=True, db_column='Cvc', max_length=255, null=True)),
                ('expire', models.CharField(blank=True, db_column='Expire', max_length=255, null=True)),
                ('bankid', models.ForeignKey(db_column='BankID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.bank')),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user')),
            ],
            options={
                'db_table': 'CreditCard',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='nationid',
            field=models.ForeignKey(db_column='NationID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.nation'),
        ),
        migrations.CreateModel(
            name='Cartproduct',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('cartid', models.ForeignKey(db_column='CartID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.cart')),
                ('orderid', models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.order')),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
            ],
            options={
                'db_table': 'CartProduct',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='userid',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('detail', models.CharField(blank=True, db_column='Detail', max_length=255, null=True)),
                ('companyid', models.ForeignKey(db_column='CompanyID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.company')),
                ('supplierid', models.ForeignKey(db_column='SupplierID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.supplier')),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.user')),
                ('wardid', models.ForeignKey(db_column='WardID', on_delete=django.db.models.deletion.DO_NOTHING, to='app.ward')),
            ],
            options={
                'db_table': 'Address',
            },
        ),
    ]
