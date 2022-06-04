from django.db import models


class Careers(models.Model):
    title = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    reserves = models.IntegerField()
    mined = models.IntegerField()
    residue = models.FloatField()


class Samples(models.Model):
    sample = models.TextField(max_length=20)
    career = models.TextField(max_length=100)
    stack = models.TextField(max_length=20)
    production_date = models.DateField(blank=True)
    production_tonnage = models.IntegerField()
    used_tonnage = models.IntegerField(blank=True)
    rest_tonnage = models.IntegerField(blank=True)
    al2o = models.FloatField()
    fe2o3 = models.FloatField()
    tio2 = models.FloatField()
    sio2 = models.FloatField()
    k2o = models.FloatField()
    cao = models.FloatField()
    mgo = models.FloatField(blank=True)
    na2o = models.FloatField(blank=True)
    loi = models.FloatField(blank=True)
    total = models.FloatField()
    carbon = models.FloatField(blank=True)
    rest_on_sieve = models.FloatField(blank=True)
    sulfur = models.FloatField(blank=True)
    plastic = models.FloatField(blank=True)
    fluidity = models.FloatField(blank=True)
    grade = models.TextField(max_length=20)


class Stacks(models.Model):
    stack = models.TextField(max_length=20)
    career = models.TextField(max_length=100)
    production_tonnage = models.IntegerField()
    used_tonnage = models.IntegerField(blank=True)
    rest_tonnage = models.IntegerField(blank=True)
    al2o = models.FloatField()
    fe2o3 = models.FloatField()
    tio2 = models.FloatField()
    sio2 = models.FloatField()
    k2o = models.FloatField()
    cao = models.FloatField()
    mgo = models.FloatField(blank=True)
    na2o = models.FloatField(blank=True)
    loi = models.FloatField(blank=True)
    total = models.FloatField()
    carbon = models.FloatField(blank=True)
    rest_on_sieve = models.FloatField(blank=True)
    sulfur = models.FloatField(blank=True)
    plastic = models.FloatField(blank=True)
    fluidity = models.FloatField(blank=True)
    grade = models.TextField(max_length=20)


class Stocks(models.Model):
    stack = models.TextField(max_length=20)
    career = models.TextField(max_length=100)
    date_of_transport = models.DateField()
    transported_tonnage = models.IntegerField()
    destination = models.TextField(max_length=200)
    grade = models.TextField(max_length=20)


class Shipped(models.Model):
    destination = models.TextField(max_length=200)
    date_of_shipped = models.DateField()
    stack = models.TextField(max_length=20)
    shipped_tonnage = models.IntegerField()
    rest_tonnage = models.IntegerField(blank=True)
    decommissioned = models.IntegerField(blank=True)
    grade = models.TextField(max_length=20)
