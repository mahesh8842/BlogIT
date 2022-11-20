from django.utils.text import slugify



import random
import string

def generate_random_string(n):
    result =''.join(random.choices(string.ascii_uppercase + string.digits,k=n))
    return result

def generate_slug(text):
    from .models import BlogModel
    new_slug = slugify(text)
    if BlogModel.objects.filter(slug=new_slug).count()>0:
        new_slug=generate_slug(text+generate_random_string(5))
    print(BlogModel.objects.filter(slug=new_slug).count(),'-----------------------------')
    return new_slug