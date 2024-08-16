from django.db import models


class BankAccount(models.Model):
    person = models.ForeignKey(to='person.Person', on_delete=models.CASCADE,default="000000000000",null=True)
    account_id = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)