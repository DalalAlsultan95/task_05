from django.shortcuts import render
from restaurants.models import Restaurant

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	restaurant = Restaurant.objects.all()
	context = {
		"restaurants": restaurant
	}
	return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
	restaurant = Restaurant.objects.get(id = restaurant_id)
	context = {
		"restaurant": restaurant
	}
	return render(request, 'detail.html', context)
