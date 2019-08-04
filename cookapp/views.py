from django.shortcuts import render
from .models import Recipe, Post

def temp(request):
    post = Post.objects.all()
    ingr = Post.objects.values_list('name', flat=True)
    full_list = list(ingr)
    all = Recipe.objects
    choose = ["쌀밥", "고추장", "안심"]
    sub = set(full_list) - set(choose)
    recipe = all
    for r in sub:
        recipe = recipe.exclude(ingredients__name = r)
    # recipe = all.filter(ingredients__name = '쌀밥')
    return render(request, 'temp.html',{'post':post, 'all':all, 'recipe':recipe})