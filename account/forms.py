
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AccountFrom(UserCreationForm):

    class Meta:
        model = User
        fields = ('email' , 'username')