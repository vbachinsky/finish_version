from django.core.management.base import BaseCommand, CommandError
from sales.models import *
import csv
from datetime import datetime

f_obj = "50000 Sales Records.csv"

class Command(BaseCommand):
    help = 'Parser for CSV files'

    def handle(self, *args, **options):
        total_cost = 0
        units_sold = 0
        unit_cost = 0
        num_line = 0
        Sales.objects.all().delete()
        objects = []

        with open(f_obj, 'r', newline="") as file:
            reader = csv.DictReader(file, delimiter=',')
            for line in reader:
                if len(line) == 14:
                    sales_channel = True if line['Sales Channel'] == 'Online' else False

                    if line['Order Date'] == '':
                        order_date = datetime.strptime('01/01/1970', '%m/%d/%Y')
                    else:
                        try:
                            order_date = datetime.strptime(line['Order Date'], '%m/%d/%Y')
                        except ValueError:
                            try:
                                order_date = datetime.strptime(line['Order Date'], '%m/%d/%y')
                            except ValueError:
                                try:
                                    order_date = datetime.strptime(line['Order Date'], '%b-%d-%Y')
                                except ValueError:
                                    order_date = line['Order Date']
                                    order_date = order_date.split('/')
                                    for order_date_temp in order_date:
                                        order_date_temp += order_date_temp
                                    if order_date_temp.isalpha():
                                        order_date = datetime.strptime('01/01/1970', '%m/%d/%Y')

                    if line['Ship Date'] == '':
                        ship_date = datetime.strptime('01/01/1970', '%m/%d/%Y')
                    else:                        
                        try:
                            ship_date = datetime.strptime(line['Ship Date'], '%m/%d/%Y')
                        except ValueError:
                            try:
                                ship_date = datetime.strptime(line['Ship Date'], '%m/%d/%y')
                            except ValueError:
                                try:
                                    ship_date = datetime.strptime(line['Ship Date'], '%b-%d-%Y')
                                except ValueError:
                                    ship_date = line['Ship Date']
                                    ship_date = ship_date.split('/')
                                    for ship_date_temp in ship_date:
                                        ship_date_temp += ship_date_temp
                                    if ship_date_temp.isalpha():
                                        ship_date = datetime.strptime('01/01/1970', '%m/%d/%Y')

                    if line['Order ID'].isdigit():
                        order_id = line['Order ID']
                    else:
                        order_id = None

                    if line['Units Sold'].isdigit():
                        units_sold = line['Units Sold']
                    else:
                        units_sold = None

                    if line['Unit Price'].isdigit():
                        unit_price = lineline['Unit Price']
                    else:
                        unit_price = None

                    if line['Unit Cost'].isdigit():
                        unit_cost = line['Unit Cost']
                    else:
                        unit_cost = None

                    if line['Total Revenue'].isdigit():
                        total_revenue = line['Total Revenue']
                    else:
                        total_revenue = None

                    if line['Total Cost'].isdigit():
                        total_cost = line['Total Cost']
                    else:
                        total_cost = None

                    if line['Total Profit'].isdigit():
                        total_profit = line['Total Profit']
                    else:
                        total_profit = None

                else:
                    print("This strings is not parsing: ", line)

                entry = Sales(region=line['Region'], 
                    country=line['Country'], 
                    item_type=line['Item Type'],
                    sales_channel=sales_channel, 
                    order_priority=line['Order Priority'],
                    order_date=order_date, 
                    order_id=order_id, 
                    ship_date=ship_date,
                    units_sold=units_sold, 
                    unit_price=unit_price,
                    unit_cost=unit_cost, 
                    total_revenue=total_revenue,
                    total_cost=total_cost, 
                    total_profit=total_profit)

                objects.append(entry)

        Sales.objects.bulk_create(objects, 70)
        print('Complited. All enties: ', Sales.objects.all().count())