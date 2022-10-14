from django.db import models

class Band(models.Model): 
    bname = models.CharField(max_length = 255, null = True ,blank = True)
    bgenre = models.CharField(max_length = 255, null = True ,blank = True)
    binstrument = models.CharField(max_length = 255, null = True ,blank = True)
    bnationality = models.CharField(max_length = 255, null = True ,blank = True)
    bemail = models.EmailField(max_length = 255, null = True , blank = True)
    def __str__(self):
        return self.bname
    

class Musician(models.Model):
    mname = models.CharField(max_length = 255, null = True ,blank = True)
    mgenre = models.CharField(max_length = 255, null = True ,blank = True)
    minstrument = models.CharField(max_length = 255, null = True ,blank = True)
    mnationality = models.CharField(max_length = 255, null = True ,blank = True)
    memail = models.EmailField(max_length = 255, null = True , blank = True)
    def __str__(self):
        return self.mname
    