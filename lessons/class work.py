class SavingAccount:...
class ChekingAccount:...
class Stock:...
class Bond:...
class RealEstate:...
class BankAccount(SavingAccount,ChekingAccount):...
class Security(Stock,Bond):...
class InterestBearingItem(BankAccount,Security):...
class InsurableItem(BankAccount,RealEstate):...
class Asset(BankAccount,Security,RealEstate):...

print(Security.mro())
print(InsurableItem.mro())
print(InterestBearingItem.mro())
print(Asset.mro())
print(BankAccount.mro())


