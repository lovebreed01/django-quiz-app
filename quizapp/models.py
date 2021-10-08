from django.db import models
from django.contrib.auth.models import User,AnonymousUser




class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
        

class Question(models.Model):
    taker = models.ForeignKey(User, on_delete=models.CASCADE,default=AnonymousUser)
    question_text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question_text} ?'

    def save(self, *args,**kwargs):
        self.question_text = self.question_text.lower()
        return super().save()
    def to_dict(self):
        data  = {}
        



class Choice(models.Model):
    data = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, null=True)
    is_correct = models.BooleanField(default= False)

    def save(self, *args,**kwargs):
        self.data = self.data.lower()
        print(self.data.islower())
        return super().save()


    def __str__(self) -> str:
        return f'{self.data}'
class HighScore(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount= models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} in {self.category}"
