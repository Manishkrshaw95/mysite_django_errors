from django.db import models

# Create your models here.
class Muser(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=24)
    ranking = models.FloatField()

    def upload_dir(self, filename) :
        path = 'employee/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_dir , null=True, blank = True)


    def upload_file(self, filename) :
        path = 'employee/file/{}'.format(filename)
        return path
    resume = models.ImageField(upload_to=upload_file , null=True, blank = True)

    def __str__(self) :
        return self.name