# from tkinter import N
from django import views
from django.shortcuts import render

from walletapp.models import Customer,ThirdParty, Account, Card, Currency, Transaction, Notification,Loan,Wallet,Receipt,Reward

from .forms import CurrencyRegistrationForm, CustomerRegistrationForm, TransactionRegistrationForm,  WalletRegistrationForm, AccountRegistrationForm, CardRegistrationForm,ThirdPartyRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm,LoanRegistrationForm, RewardRegistrationForm


# Create your views here.

# def register_customer(request):
#     form = CustomerRegistrationForm()
#     return render (request,'wallet/register_customer.html', {'form':form})

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})


def register_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers": customers})


def register_wallet(request):
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form": form})


def register_wallets(request):
    wallets = Wallet.objects.all()
    return render (request,'wallet/register_wallet.html', {"wallets":wallets})


def register_loan(request):
    if request.method == 'POST':
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form": form})


def register_loans(request):
    loans = Loan.objects.all()
    return render (request,'wallet/register_loan.html', {'loans':loans})


def register_account(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"account/register_account.html",{"form": form})

def register_accounts(request):
    accounts = Account.objects.all()
    return render (request,'account/register_account.html', {'accounts':accounts})


def register_currency(request):
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form": form})

def register_currencys(request):
    currencys = Currency.objects.all()
    return render (request,'wallet/register_currency.html', {'currenys':currencys})


def register_thirdParty(request):
    if request.method == 'POST':
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_thirdParty.html",{"form": form})


def register_thirdPartys(request):
    thirdPartys = ThirdParty.objects.all()
    return render (request,'wallet/register_thirdParty.html', {'thirdPartys':thirdPartys})

def register_card(request):
    if request.method == 'POST':
        form =CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form": form})

def register_cards(request):
    cards=Card.objects.all()
    return render (request,'card/register_card.html', {'cards':cards})

    
def register_notification(request):
    if request.method == 'POST':
        form =NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm()
    return render(request,'notification/register_notification.html',{"form": form})


def register_notifications(request):
    notifications=Notification.objects.all()
    return render (request,'notification/register_notification.html', {'notifications':notifications})


def register_reward(request):
    if request.method == 'POST':
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form": form})


def register_rewards(request):
    rewards = Reward.objects.all()
    return render (request,'reward/register_reward.html', {'rewards':rewards})


def register_transaction(request):
    if request.method == 'POST':
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()
    return render(request,"transaction/register_transaction.html",{"form": form})


def register_transactions(request):
    transactions = Transaction.objects.all()
    return render (request,"transaction/register_transaction.html", {"transactions":transactions})

def register_receipt(request):
    if request.method == 'POST':
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm()
    return render(request,"receipt/register_receipt.html",{"form": form})

def register_receipts(request):
    receipts=Receipt.objects.all()
    return render(request,"receipt/receipt_list.html",{"receipts": receipts})

    
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})

def register_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers": customers})


# def customer_profile(request,id):
#     customer=Customer.objects.get(id=id)
#     return render(request,"wallet/customer_profile.html",
#     {"customer".customer})


    # def edit_profile(request,id):
    #     customer=Customer.objects.get(id=id)
    #     # if request.method=="POST"
    #     form=CustomerRegistrationForm(request.POST,
    #     instance=Customer)
    #     if form.isvalid():
    #         form.save()
    #         return redirect ("customer_profile",id=customer)
    #     else:
    #         form=CardRegistrationForm(instance=customer)
    #         return render(request, "wallet/edit_profile.html",
    #         {"form": form})
















