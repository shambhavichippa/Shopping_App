from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from webapp.models import *
# Create your views here.
def home_page(request):
    obj = category.objects.all()
    return render(request, 'home_page.html', {'cats': obj})


def products(request):
    cat_id = request.POST['cat_id']
    obj = list(product.objects.filter(category_id=cat_id))
    return render(request, 'product_page.html', {'products':obj})


class add_to_cart(APIView):
    def post(self, request):
        user_id = request.user.id
        try:
            old_obj = cart.objects.get(user_id=user_id,
                         product_id=request.POST['id'])
            if old_obj:
                old_obj.quantity=request.POST['buy_quant']
                old_obj.save()
        except cart.DoesNotExist:
            obj = cart.objects.create(user_id=user_id,
                         product_id=request.POST['id'],
                        quantity=request.POST['buy_quant'])
            obj.save()
        return HttpResponse(status=200)

def view_cart(request):
    user_id = request.user.id
    cost = 0
    obj=cart.objects.filter(user_id=user_id).values('product_id__name','product_id__price','product_id__quantity','quantity')
    for i in obj:
        i['cost']=(i['quantity'] * i['product_id__price'])
        cost += i['cost']
    return render(request,'view_cart.html',{'data':obj, 'cost':cost })

def checkout(request):
    user_id = request.user.id
    obj=address_book.objects.filter(user_id=user_id).values()
    return render(request, 'checkout_page.html', {'address':obj})

def add_address(request):
    user_id = request.user.id
    obj = address_book.objects.create(user_id=user_id,
                                      address=request.POST['address'],
                                      default=True)
    obj.save()
    obj = address_book.objects.filter(user_id=user_id).values()
    return render(request, 'checkout_page.html', {'address': obj})


def proceed_to_payment(request):
    user_id = request.user.id
    address_id = request.POST['id']
    cost = 0
    obj=cart.objects.filter(user_id=user_id).values('product_id__price','product_id__quantity','quantity')
    for i in obj:
        i['cost']=(i['quantity'] * i['product_id__price'])
        cost += i['cost']
    return render(request, 'payment_page.html', {'address_id': address_id, 'cost':cost})


def payment(request):
    user_id = request.user.id
    address_id = request.POST['id']
    order_obj = order.objects.create(user_id=user_id,
                                     address_id=address_id)
    order_obj.save()
    obj=cart.objects.filter(user_id=user_id).values('id', 'product_id', 'product_id__price','product_id__quantity','quantity')
    for i in obj:
        i['cost']=(i['quantity'] * i['product_id__price'])
        order_pro_obj = order_product.objects.create(order_id=order_obj.id,
                                     product_id=i['product_id'],
                                     quantity=i['quantity'],
                                     price=i['cost'],
                                     )
        order_pro_obj.save()
        product_obj = product.objects.get(id = i['product_id'])
        product_obj.quantity = product_obj.quantity - i['quantity']
        product_obj.save()
        cart_obj = cart.objects.get(id=i['id'])
        cart_obj.delete()
    return render(request, 'success_page.html', {'order_id': order_obj.id})


def my_order(request):
    user_id = request.user.id
    obj=order.objects.filter(user_id=user_id).values('id', 'address_id__address')
    return render(request, 'my_orders.html', {'order_list': obj })