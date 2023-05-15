from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def home_page(request):

    if request.method == "GET":
        all_categories = Category.objects.all()
        mens_products = Product.objects.filter(category='MN') # This helps the database to recognize and use the Instance category name and not its default ID
        womens_products = Product.objects.filter(category='WM')
        kids_products = Product.objects.filter(category='KD')
        social_images = Social.objects.all()

        context = {
            'all_categories': all_categories,
            'mens_product': mens_products,
            'womens_product': womens_products,
            'kids_product': kids_products,
            'social_images': social_images

        }
    # Bound instance
    else:
        #  NOTE The name and email we have in the bracket in quotes is pointing to the name and email in quote in the form
        new_subscribers_name = request.POST["name"] # OR request.POST.get("name")
        new_subscribers_email = request.POST("email") # OR request.POST.get["email"]
        Subscriber.objects.create(name=new_subscribers_name, email=new_subscribers_email)
        # return HttpResponse("You have subscribed sucessfully")
        return redirect("productslink")
    
    return render(request, "Web/index.html", context)




    

def about_page(request):
    return render(request, "Web/about.html")

def products_page(request):
    product = Product.objects.all()
    context = {
        "product": product
    }
    return render(request, "Web/products.html", context)

def singleproduct_page(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'oneproduct': product
    }
    return render(request, "Web/single-product.html", context)
