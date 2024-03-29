from django.db import models

# added code to send data
class Code(models.Model):
    lines=models.DecimalField(max_digits=9, decimal_places=2,null=False,blank=False)
    code=models.TextField()
    output=models.TextField()
    def __str__(self):
        return self.code
