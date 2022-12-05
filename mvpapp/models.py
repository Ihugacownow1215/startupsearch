from django.db import models


class Person(models.Model):
    person_id=models.CharField(max_length=255)
    name=models.CharField("Name of Person", max_length=255, null=True) 

    def __str__(self):
        return self.name


class Job(models.Model):
    person_id=models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    company_li_name=models.CharField(max_length=255, null=True) 
    last_title=models.CharField(max_length=255) 
    start_date=models.DateTimeField(null=True) 
    end_date=models.DateTimeField(null=True) 

    def __str__(self):
        return self.last_title


class Company(models.Model):
    name=models.CharField("Company Name", max_length=255)
    company_linkedin_names=models.JSONField("Array of company linkedin names", default=None, blank=True, null=True) 
    headcount=models.IntegerField("Number of people in company", default=None, blank=True, null=True)
    known_total_funding=models.IntegerField("Public valuation", default=None, blank=True, null=True) 
    investors=models.JSONField("Investor List", default=None, blank=True, null=True)

    def __str__(self):
        return self.name


