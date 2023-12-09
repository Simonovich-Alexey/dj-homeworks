from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorted_type = request.GET.get('sort', 'id')

    match sorted_type:
        case 'name':
            sorted_type = 'name'
        case 'min_price':
            sorted_type = 'price'
        case 'max_price':
            sorted_type = '-price'

    phone_objects = Phone.objects.order_by(sorted_type)
    phones_list = [{"name": phone.name,
                    "price": phone.price,
                    "image": phone.image,
                    "release_date": phone.release_date,
                    "lte_exists": phone.lte_exists,
                    "slug": phone.slug} for phone in phone_objects]

    context = {"phones": phones_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    phone = [{"name": p.name,
             "price": p.price,
             "image": p.image,
             "release_date": p.release_date,
             "lte_exists": p.lte_exists} for p in phone_object]

    context = {"phone": phone[0]}
    return render(request, template, context)
