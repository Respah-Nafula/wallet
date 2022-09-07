# from tkinter import N
from django.contrib import admin

# Register your models here.
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet,Currency
 

class CustomerAdmin(admin.ModelAdmin):
   list_display=("first_name","last_name","age","email", "address","gender","phone_number")
   search_fields=("first_name","last_name","age","email", "address","gender","phone_number")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
     list_display=("balance","customer","amount","date_created","status","history", "pin")
     search_fields=("balance","customer","amount","date_created","status","history", "pin")
admin.site.register(Wallet,WalletAdmin)


class AccountAdmin(admin.ModelAdmin):
      list_display=("account_name", "account_number", "account_type", "account_balance")
      search_fields=("account_name", "account_number", "account_type", "account_balance",)
admin.site.register(Account, AccountAdmin)
   


class TransactionAdmin(admin.ModelAdmin):
       list_display=("message", "wallet", "transaction_description", "transaction_amount","transaction_charge", "transaction_type", "origin_account","destination_account", "receipt")
       search_fields=("message", "wallet", "transaction_description", "transaction_amount","transaction_charge", "transaction_type", "origin_account","destination_account", "receipt")
admin.site.register(Transaction,TransactionAdmin)

       

class CardAdmin(admin.ModelAdmin):
    list_display=("card_number","card_type", "expiry_date","security_code","date_of_issue", "wallet","issuer")
    search_fields=("card_number","card_type", "expiry_date","security_code","date_of_issue", "wallet","issuer")
admin.site.register(Card,CardAdmin)
   
    
class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=("account", "transaction_amount","currency","date_of_issue","wallet","issuer")
    search_fields=("account", "transaction_amount","currency","date_of_issue","wallet","issuer")
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("message", "date","recipient","title")
    search_fields=("message", "date","recipient","title")
admin.site.register(Notification,NotificationAdmin)
       

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_types", "receipt_date","receipt_num", "receipt_file")
    search_fields=("receipt_types", "receipt_date","receipt_num", "receipt_file")
admin.site.register(Receipt,ReceiptAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_id","loan_type","loan_balance","amount","guaranter","issuer","wallet")
    search_fields=("loan_id","loan_type","loan_balance","amount","guaranter","issuer","wallet")
admin.site.register(Loan,LoanAdmin)

# class RewardAdmin(admin.ModelAdmin):
#     list_display=("transaction","recipient", "date_of_reward" "loyalty_points")
#     search_fields=("transaction","recipient", "date_of_reward" "loyalty_points")
# admin.site.register(Reward,ReceiptAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("country", "symbol","amount")
    search_fields=("country", "symbol","amount")
admin.site.register(Currency,CurrencyAdmin)













