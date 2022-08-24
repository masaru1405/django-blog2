from .models import Category

def categories(request):
   categories = Category.objects.all()
   context = {'categories': categories}
   return context