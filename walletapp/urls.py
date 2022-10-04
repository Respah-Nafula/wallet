# from ast import pattern
# from unicodedata import name
from django.urls import path
from .views import register_accounts, register_cards, register_currencys, register_customers,register_receipts, register_loans, register_notifications, register_rewards, register_thirdPartys, register_wallets
from .views import register_currency
from .views import register_customer
from .views import register_account
from .views import register_wallet
from .views import register_transaction
from .views import register_card
from .views import register_thirdParty
from .views import register_notification
from .views import register_reward
from .views import register_loan
from .views import register_receipt


urlpatterns = [
    path("register/",register_customer,name="register"),
    path("currency/",register_currency,name="currency"),
    path("wallet/",register_wallet,name="wallet"),
    path("account/",register_account,name="account"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdParty/",register_thirdParty,name="thirdParty"),
    path("notification/",register_notification,name="notification"),
    path("reward/",register_reward,name="reward"),
    path("loan/",register_loan, name="loan"),
    path("receipt/",register_receipt, name="receipt"),


    path("customers/",register_customers,name="customers"),
    path("currencys/",register_currencys,name="currencys"),
    path("wallets/",register_wallets, name="wallets"),
    path("accounts/",register_accounts, name="loans"),
    path("transactions/",register_transaction, name="transactions"),
    path("cards/",register_cards, name="cards"),
    path("thirdPartys/", register_thirdPartys, name="thirdPartys"),
    path("notifications/",register_notifications,name="notifications"),
    path("rewards/",register_rewards,name="rewards"),
    path("loans/",register_loans,name="loans"),
    path("receipt/",register_receipt, name="receipts"),

    # path("customers/<int:id", customer_profile,name ="customer_profile"),
    # path("customers/edit/<int:id", edit_profile, name="edit_profile"),

]
    
  
   
    