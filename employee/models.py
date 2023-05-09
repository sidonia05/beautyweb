from django.db import models



class Employee(models.Model):

    gender_options = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=20) # pt CharFiedl -> max_lenght va fi maxim 255 chars
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=300) # pt TextField -> max_lenght poate fi mai mare de 255 chars
    active = models.BooleanField(default=True) # in interfata campul active va arata ca un checkbox



    created_at = models.DateTimeField(auto_now_add=True) # in momentul in care voi adauga un nou student, voi stoca data si ora respectiva. Acest camp nu va fi vizibil in interfata
    updated_at = models.DateTimeField(auto_now=True) # in momentul in care voi face modificari pe un anumit student , voi stoca data si ora respectiva. Acest camp nu va fi vizibil in interfata.

    def __str__(self):
        return  f'{self.first_name} {self.last_name}'