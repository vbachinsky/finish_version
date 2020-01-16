from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import Pizza, Order
from bs4 import BeautifulSoup
import requests
import json
import os
from django.conf import settings

URL = 'https://oliopizza.com.ua/product-category/pitstsa/'

logger = get_task_logger(__name__)


@task(name="add_pizza_to_basket")
def add_pizza(count, pizza_id, user_id):
    pizza = Pizza.objects.get(id=pizza_id)
    instance_pizza = pizza.make_order(count)
    order, created = Order.objects.get_or_create(user__id=user_id)
    order.pizzas.add(instance_pizza)
    order.update_price()
    logger.info("Pizza added to basket")


@periodic_task(
	run_every=(crontab(minute='*/2')), 
	name="pizza_parser", ignore_result=True
)
def parser():
    response = requests.get(URL)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    arr_1 = soup.find_all("div", {"class": "product-card"})
    full_dict = []
    for row in arr_1:
        temp_dict = {}
        name = row.find("span", {"class": "name"})
        price= row.find("span", {"class": "woocommerce-Price-amount amount"})
        text = row.find("span", {"class": "description"})
        if row.img:
            image_url = row.img['src']
        temp_dict["name"] = str(name.contents[0]).strip()
        temp_dict["price"] = str(price.contents[0])[:-1]
        temp_dict["text"] = str(text.contents[0]).strip()
        temp_dict["image_url"] = str(image_url)
        full_dict.append(temp_dict)
    print(full_dict, type(full_dict))
    with open(os.path.join(settings.MEDIA_ROOT, 'pizzas.json'), 'w') as f_obj:
        json.dump(full_dict, f_obj)
    logger.info("Parser finished work")
