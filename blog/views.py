from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib import messages

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(name__icontains=q)
        context = {'query': q, 'products': products}
    else:
        context = {}
    return render(request, 'blog/result.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if request.user.is_authenticated:
        print("YES")
        if request.user.profile.club == "None" or request.user.profile.batch == 'None':
            print("YEAH")
            messages.success(request, f'Please update your profile for better experience.')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'blog/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'blog/details.html', context)
