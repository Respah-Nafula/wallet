from django.shortcuts import render

from walletapp.models import ThirdParty
from .forms import CurrencyRegistrationForm,CustomerRegistrationForm,  WalletRegistrationForm,AccountRegistrationForm,CardRegistrationForm,ThirdPartyRegistrationForm,NotificationRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm


# Create your views here.

def register_customer(request):
    form = CustomerRegistrationForm()
    return render (request,'wallet/register_customer.html', {'form':form})


def register_wallet(request):
    form = WalletRegistrationForm()
    return render (request,'wallet/register_wallet.html', {'form':form})

def register_account(request):
    form = AccountRegistrationForm()
    return render (request,'wallet/register_account.html', {'form':form})

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render (request,'wallet/register_currency.html', {'form':form})

def register_thirdParty(request):
    form = ThirdPartyRegistrationForm()
    return render (request,'wallet/register_thirdParty.html', {'form':form})

def register_card(request):
    form =CardRegistrationForm()
    return render (request,'wallet/register_card.html', {'form':form})

def register_notification(request):
    form = ThirdPartyRegistrationForm()
    return render (request,'wallet/register_notification.html', {'form':form})

def register_reward(request):
    form = NotificationRegistrationForm()
    return render (request,'wallet/register_reward.html', {'form':form})
def register_transaction(request):
    form = RewardRegistrationForm()
    return render (request,'wallet/register_transaction.html', {'form':form})

def register_loan(request):
    form = LoanRegistrationForm()
    return render (request,'wallet/register_loan.html', {'form':form})
