from faker import Faker
from person.models import Person
from accounts.models import BankAccount
import time
from django.db.models import Model
import random
import string
from django.db.models.functions import Cast
from django.db.models import CharField
from django.db.models import Q
from django.db.models.functions import Cast
from django.db import connection


fake = Faker()


def generate_random_data_account(count=20000):
    data = []
    for _ in range(count):
        person = Person.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            national_code=''.join(random.choices(string.digits, k=10))
        )
        account = BankAccount(
            person=person,
            account_id=''.join(random.choices(string.digits, k=20)),
            balance=random.uniform(100, 100000)
        )
        data.append(account)

    BankAccount.objects.bulk_create(data)


if __name__ == "__main__":
    generate_random_data_account()
  

def get_info():
    accounts = BankAccount.objects.all()[:100000]#صرفا برای کوتاه شدن خروجی
    for account in accounts:
        print(f"account: {account.person.first_name}    {account.person.last_name}  balance: {account.balance}")
       

def richest():
    richest_account = BankAccount.objects.order_by('-balance').first()
    print(richest_account)
    




def less_amount():
    less_amount= BankAccount.objects.order_by('balance')[:5]
    for account in less_amount:
        print(account)

def transfer_money(from_account_id, to_account_id, amount):
    from_account = BankAccount.objects.get(id=from_account_id)
    to_account = BankAccount.objects.get(id=to_account_id)
    print("before transfer: ")
    print(f"balance: {from_account.balance}  the account: {from_account.account_id}")
    print(f"balance: {to_account.balance}  the account: {to_account.account_id}")
    from_account.balance -= amount
    to_account.balance += amount
    print("after transfer: ")
    print(f"balance: {from_account.balance}  the account: {from_account.account_id}")
    print(f"balance: {to_account.balance}  the account: {to_account.account_id}")
    from_account.balance -= amount
    from_account.save()
    to_account.save()


def acoount_grter():
       
    accounts = BankAccount.objects.filter(account_id__gt=Cast('balance', output_field=CharField()))
    print(accounts) 




def generate_random_data_person(count=10000000):
    data_P = []
    data_A=[]
    for _ in range(count):
        person = Person.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            national_code=''.join(random.choices(string.digits, k=10))
        )
        data_P.append(person)
        account = BankAccount(
            person=person,
            account_id=''.join(random.choices(string.digits, k=20)),
            balance=random.uniform(100, 100000)
        )
        data_A.append(account)

    Person.objects.bulk_create(data_P)
    BankAccount.objects.bulk_create(data_A)

#متاسفانه وقت نشد بقیه را بنویسم

    