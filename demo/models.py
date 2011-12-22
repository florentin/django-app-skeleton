from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import F
from django.db.models import Count
from django.db.models import get_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, \
                                   MaxLengthValidator, MinLengthValidator
from .managers import MyManager()


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(u'%s is not an even number' % value)

class MyModel(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    f = models.IntegerField(validators=[validate_even])
    f = models.ImageField(upload_to="icons", null=True, blank=True)
    f = models.DateField(help_text="Date")
    f = models.IntegerField(default=0)
    f = models.PositiveIntegerField()
    f = models.FloatField()
    f = models.OneToOneField(User, unique=True, verbose_name='user', related_name='my_profile')
    f = models.ForeignKey(User, help_text="The guy")
    f = models.CharField(_('language'), max_length=5, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE[:2])
    f = models.ManyToManyField("User", related_name="u",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = MyManager()
    
    class Meta:
        db_table = 'boo'
        ordering = ['name', 'description']
        verbose_name = 'boo'
        verbose_name_plural = _('boos')
        permissions = (("can_view_boo", "Can view the boo"),
                       ("can_view_boo", "Can view the boo"))
        unique_together = (("f", "f"),)
        abstract = True
        
    def __unicode__(self):
        return self.name