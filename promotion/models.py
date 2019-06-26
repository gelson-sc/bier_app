from django.db import models

class UserApp(models.Model):
    cd_user = models.AutoField(primary_key=True)
    email = models.CharField(max_length=55, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=85, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_app'

    def __str__(self):
        return self.name + ' ' + self.last_name


class Promotion(models.Model):
    cd_promotion = models.AutoField(primary_key=True)
    cd_user_app = models.ForeignKey('UserApp', UserApp, db_column='cd_user_app')
    category = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    long = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotion'

    def __str__(self):
        return self.category + ' ' + self.description

