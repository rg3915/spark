from django.contrib.auth.models import User

email = 'admin@admin.com'
password = 'demodemo'
user = User.objects.create_user('admin', email=email, password=password)
user.is_superuser = True
user.is_staff = True
user.save()
