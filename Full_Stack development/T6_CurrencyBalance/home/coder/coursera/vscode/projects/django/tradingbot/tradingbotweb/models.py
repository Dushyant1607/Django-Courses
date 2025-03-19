from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import requests, json, decimal 

# Create your models here.
class Currency(models.Model):
    symbol                     = models.CharField(max_length=10, primary_key=True)
    usd_value                  = models.DecimalField(max_digits=10,decimal_places=2, default=1.0)

class Transaction(models.Model):
    origin_currency            = models.ForeignKey('Currency',on_delete=models.CASCADE, related_name='origin_currency')
    destination_currency       = models.ForeignKey('Currency', on_delete=models.CASCADE,related_name='destination_currency')
    original_currency_value    = models.DecimalField(max_digits=10, decimal_places=2)
    destination_currency_value = models.DecimalField(max_digits=10, decimal_places=2)
    commission                 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    exchange_date              = models.DateTimeField(auto_now_add=True)

class CurrencyHistory(models.Model):
    symbol = models.ForeignKey('Currency', on_delete=models.CASCADE)
    usd_value = models.DecimalField(max_digits=10, decimal_places=6, default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # add your logic
        self.usd_value = self.get_value()
        super(CurrencyHistory, self).save(*args, **kwargs)

    def get_value(self):
        api_url = f'https://economia.awesomeapi.com.br/last/{self.symbol}-USD'
        response = requests.get(api_url).content
        json_data = json.loads(response)
        usd_ask_value = json_data[f'{self.symbol}USD']['ask']
        print(f"usd ask value: (usd ask value)")
        decimal_value = decimal.Decimal(usd_ask_value)
        return decimal_value
    
class CurrencyBalance(models.Model):
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    share_portfolio = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
