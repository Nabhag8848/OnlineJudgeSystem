from django.db import models
from django.db import OperationalError

class Example(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    input = models.CharField(max_length=200,null=False)
    output = models.CharField(max_length=200,null=False)
    def __str__(self):
        return str(self.id)


class CQuestions(models.Model):
    heading = models.CharField(max_length=300 , null=False )
    difficulty = models.CharField(max_length=300 , null=False)
    description = models.CharField(max_length=300 , null=False)
    long_description = models.CharField(max_length=700 , null = False,default="no heading")
    accuracy = models.FloatField(null=False,default="90.9")
    example_1 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example1",default="no heading")
    example_2 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example2",default="no heading")

    def __str__(self):
         return self.heading

class CPPQuestions(models.Model):
    heading = models.CharField(max_length=300 , null=False )
    difficulty = models.CharField(max_length=300 , null=False)
    description = models.CharField(max_length=300 , null=False)
    long_description = models.CharField(max_length=700 , null = False,default="no heading")
    accuracy = models.FloatField(null=False,default="90.9")
    example_1 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example13",default="no heading")
    example_2 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example23",default="no heading")

    def __str__(self):
         return self.heading


class JAVAQuestions(models.Model):
    heading = models.CharField(max_length=300 , null=False )
    difficulty = models.CharField(max_length=300 , null=False)
    description = models.CharField(max_length=300 , null=False)
    long_description = models.CharField(max_length=700 , null = False,default="no heading")
    accuracy = models.FloatField(null=False,default="90.9")
    example_1 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example12",default="no heading")
    example_2 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example22",default="no heading")

    def __str__(self):
         return self.heading

class PYTHONQuestions(models.Model):
    heading = models.CharField(max_length=300 , null=False )
    difficulty = models.CharField(max_length=300 , null=False)
    description = models.CharField(max_length=300 , null=False)
    long_description = models.CharField(max_length=700 , null = False,default="no heading")
    accuracy = models.FloatField(null=False,default="90.9")
    example_1 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example14",default="no heading")
    example_2 = models.OneToOneField(Example,on_delete=models.CASCADE , related_name="example24",default="no heading")

    def __str__(self):
         return self.heading