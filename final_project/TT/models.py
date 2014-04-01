from django.db import models
from django import forms
from django.contrib.auth.models import User



class Buyer(models.Model):
	user = models.ForeignKey(User)
	orders = models.ManyToManyField("Order",related_name="order-buy")


	def _unicode_(self):
		return 'Buyer:'+self.user.email

class Seller(models.Model):
	user = models.ForeignKey(User)
	orders = models.ManyToManyField("Order",related_name="order-sell")


	def _unicode_(self):
		return 'Seller:'+self.user.email

class Wallet(models.Model):
	user = models.ForeignKey(User)
	balance = models.IntegerField()

	def _unicode_(self):
		return 'Wallet:'+self.user.email

class Item(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length = 200)
	tag = models.IntegerField()
	description = models.CharField(max_length = 2000)
	images = models.ManyToManyField("ImageDesc")

	def _unicode_(self):
		return 



class Document(models.Model):
	user = models.ForeignKey(User)



	def addDocumentValue():

		return

	def removeDocumentValue():

		return

	def updateDocumentValue():

		return

	def _unicode_(self):
		return 'Document:'+self.user.email

class DocumentValue(models.Model):
	doc = models.ForeignKey(Document)
	tag = models.IntegerField()
	orderNum = models.IntegerField()
	totalPrice = models.IntegerField()

	def _unicode_(self):
		return self.orderNum+" :"+self.totalPrice

class ImageDesc(models.Model):
	pic = models.ImageField(upload_to="TT-pics", blank=True)
	description = models.CharField(max_length=200)

	def _unicode_(self):
		return self.description


class UserToken(models.Model):
	user = models.ForeignKey(User)
	token = models.CharField(max_length=200)
	def __unicode__(self):
		return self.token 

class Order(models.Model):
	buyer = models.ForeignKey(Buyer,related_name="order-buy")
	seller = models.ForeignKey(Seller,related_name="order-sell")
	items = models.ManyToManyField(Item)

	def _unicode_(self):
		return ""
