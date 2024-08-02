from django.db import models

class CashFlowSection(models.Model):
    SECTION_CHOICES = [
        ('Operations', 'Cash Flow from Operations'),
        ('Investing', 'Cash Flow from Investing'),
        ('Financing', 'Cash Flow from Financing'),
    ]
    name = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    section = models.ForeignKey(CashFlowSection, on_delete=models.CASCADE, related_name='transactions')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.description}: {self.amount}'

class CashFlowStatement(models.Model):
    transactions = models.ManyToManyField(Transaction, related_name='statements')
    change_in_cash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beginning_balance = models.DecimalField(max_digits=10, decimal_places=2)
    ending_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calculate_change_in_cash(self):
       if not self.pk:
           # Ensure the instance is saved before calculations
           return
       total_change = sum(transaction.amount for transaction in self.transactions.all())
       self.change_in_cash = total_change
       self.ending_balance = self.beginning_balance + self.change_in_cash
       self.save()
