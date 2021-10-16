from django.db import models

class Faculty(models.Model):
    f_no = models.IntegerField()
    f_name = models.CharField(max_length=30)
    f_sal = models.FloatField()
    f_city = models.CharField(max_length=40)

    class Meta:
        db_table = "faculty"

    def __str__(self):
        return self.f_name