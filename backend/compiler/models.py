from django.db import models

# added code for fetch data
class Code(models.Model):
    lines=models.DecimalField(max_digits=9, decimal_places=2,null=False,blank=False)
    code=models.TextField()
    # image=models.ImageField(upload_to='uploade/images',null=False,blank=False)
    # name=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.code
