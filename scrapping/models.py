from django.db import models


class Passing(models.Model):
    year = models.DecimalField(max_digits=10, decimal_places=5)
    name = models.CharField(max_length=30)
    pass_yds = models.DecimalField(max_digits=10, decimal_places=5)
    yds_att = models.DecimalField(max_digits=10, decimal_places=5)
    att = models.DecimalField(max_digits=10, decimal_places=5)
    cmp = models.DecimalField(max_digits=10, decimal_places=5)
    cmp_percent = models.DecimalField(max_digits=10, decimal_places=5)
    td = models.DecimalField(max_digits=10, decimal_places=5)
    int = models.DecimalField(max_digits=10, decimal_places=5)
    rate = models.DecimalField(max_digits=10, decimal_places=5)
    one_st = models.DecimalField(max_digits=10, decimal_places=5)
    one_st_percent = models.DecimalField(max_digits=10, decimal_places=5)
    twentyplus = models.DecimalField(max_digits=10, decimal_places=5)
    fourtyplus = models.DecimalField(max_digits=10, decimal_places=5)
    lng = models.DecimalField(max_digits=10, decimal_places=5)
    sck = models.DecimalField(max_digits=10, decimal_places=5)
    scky = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name


class Rushing(models.Model):
    year = models.DecimalField(max_digits=10, decimal_places=5)
    name = models.CharField(max_length=30)
    rush_yds = models.DecimalField(max_digits=10, decimal_places=5)
    att = models.DecimalField(max_digits=10, decimal_places=5)
    td = models.DecimalField(max_digits=10, decimal_places=5)
    twentyplus = models.DecimalField(max_digits=10, decimal_places=5)
    fourtyplus = models.DecimalField(max_digits=10, decimal_places=5)
    rush_one_st = models.DecimalField(max_digits=10, decimal_places=5)
    rush_one_st_percent = models.DecimalField(max_digits=10, decimal_places=5)
    rush_fum = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name


class Receiving(models.Model):
    year = models.DecimalField(max_digits=10, decimal_places=5)
    name = models.CharField(max_length=30)
    rec = models.DecimalField(max_digits=10, decimal_places=5)
    yds = models.DecimalField(max_digits=10, decimal_places=5)
    td = models.DecimalField(max_digits=10, decimal_places=5)
    twentyplus = models.DecimalField(max_digits=10, decimal_places=5)
    fourtyplus = models.DecimalField(max_digits=10, decimal_places=5)
    lng = models.DecimalField(max_digits=10, decimal_places=5)
    rec_1st = models.DecimalField(max_digits=10, decimal_places=5)
    one_st_percent = models.DecimalField(max_digits=10, decimal_places=5)
    rec_fum = models.DecimalField(max_digits=10, decimal_places=5)
    one_st_percent = models.DecimalField(max_digits=10, decimal_places=5)
    rec_fum = models.DecimalField(max_digits=10, decimal_places=5)
    rec_yac_r = models.DecimalField(max_digits=10, decimal_places=5)
    tgts = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name


class Fumbles(models.Model):
    year = models.DecimalField(max_digits=10, decimal_places=5)
    name = models.CharField(max_length=30)
    ff = models.DecimalField(max_digits=10, decimal_places=5)
    fr = models.DecimalField(max_digits=10, decimal_places=5)
    fr_td = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name


class Tackles(models.Model):
    year = models.DecimalField(max_digits=10, decimal_places=5)
    name = models.CharField(max_length=30)
    comb = models.DecimalField(max_digits=10, decimal_places=5)
    asst = models.DecimalField(max_digits=10, decimal_places=5)
    solo = models.DecimalField(max_digits=10, decimal_places=5)
    sck = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name