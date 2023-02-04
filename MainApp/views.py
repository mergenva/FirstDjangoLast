from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item

# Create your views here.
user = {
    "name": "Дарсен",
    "middle": "Мергенович",
    "surname": "Васькаев",
}

# items = [
#     {"id": 1, "name": "Кроссовки адидас", "quantity": 10},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 0},
#     {"id": 3, "name": "Кока-кода 1л", "quantity": 8},
#     {"id": 4, "name": "Картофель фри", "quantity": 90},
#     {"id": 5, "name": "Кепка", "quantity": 100},
# ]


def main(request):
    return render(request, 'index.html')


def about(request):
    text = f"""
    Имя: {user['name']}<br>
    Отчество: {user['middle']}<br>
    Фамилия: {user['surname']}<br>   
    """
    return HttpResponse(text)


def show_item(request, id):
    try:
        current_item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    context = {
        "item": current_item,
    }
    return render(request, 'item.html', context)


def show_items(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, 'items.html', context)
