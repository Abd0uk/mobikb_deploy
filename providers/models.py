from django.db import models
from django_countries.fields import CountryField


class Operator(models.Model):
    operator_name = models.CharField(max_length=64)
    
    contact_list = models.TextField(max_length=500, default='n/a')
    contact_notes = models.CharField(max_length=1000, default='n/a')
    
    phone_no = models.CharField(max_length=255, default='n/a')
    call_min = models.CharField(max_length=500, default='n/a')
    topup_eligibility = models.CharField(max_length=500) # link to topup
    
    provider_name = models.CharField(max_length=124)
    apn = models.CharField(max_length=64)
    iccid = models.CharField(max_length=100)

    check_usage = models.CharField(max_length=200, default='n/a')
    esim_status = models.CharField(max_length=255, default='n/a')
    ip_breakout = models.CharField(max_length=100, default='n/a') # needs to be added
    

    activation = models.CharField(max_length=1000, default='n/a')
    pkg_change = models.CharField(max_length=1000, default='n/a')
    esim_replacement = models.CharField(max_length=1000, default='n/a')
    
    cancellation = models.CharField(max_length=1000, default='n/a')
    cancel_if_activated = models.CharField(max_length=1000, default='n/a')
    admin_refund_method = models.CharField(max_length=1000, default='n/a')
    second_tier_notes = models.CharField(max_length=1000, default='n/a')


    def __str__(self):
        return f"{self.operator_name}"


class Network(models.Model):
    network_name = models.CharField(max_length=24)
    
    def __str__(self):
        return self.network_name


class CountryData(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    country = CountryField()
    # change the kyc_policy to country restrictions
    kyc_policy = models.CharField(max_length=1000)
    networks = models.ManyToManyField(Network) 
    
    def __str__(self):
        return f"{self.operator} in {self.country}"