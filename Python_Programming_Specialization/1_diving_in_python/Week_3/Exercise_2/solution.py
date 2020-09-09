'''

https://www.coursera.org/learn/diving-in-python/programming/bd6aI/klassy-i-nasliedovaniie

Classes and inheritances

'''


import os
import csv



TYPE_OF_CAR = {'Car': 'car', 'Truck': 'truck', 'SpecMachine': 'spec_machine'}
PHOTO_EXTENSION = ('.jpg', '.jpeg', '.png', '.gif')




class CarBase:
    """Base class with common methods and attributes"""
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]




class Car(CarBase):
    """Class of a passenger car"""
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = TYPE_OF_CAR['Car']
        self.passenger_seats_count = int(passenger_seats_count)




class Truck(CarBase):
    """Class truck"""
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = TYPE_OF_CAR['Truck']
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0
        self.body_volume = 0.0

        if body_whl:
            self.set_truck_body(body_whl)

    def set_truck_body(self, body_whl):
        try:
            l, w, h = map(float, body_whl.split('x'))
        except ValueError:
            l, w, h = 0.0, 0.0, 0.0

        self.body_width = w
        self.body_height = h
        self.body_length = l
        self.body_volume = w * h * l

    def get_body_volume(self):
        return self.body_volume




class SpecMachine(CarBase):
    """Class of special equipment"""
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = TYPE_OF_CAR['SpecMachine']
        self.extra = extra




def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_f:
        reader = csv.reader(csv_f, delimiter=';')
        next(reader)  # skip csv-header
        for row in reader:
            car = get_car_from_csv_row(row)
            if car:
                car_list.append(car)
        return car_list




def get_car_from_csv_row(row):
    if len(row) != 7 or row[0] not in TYPE_OF_CAR.values():
        return None

    car_type, brand, passenger_sc, photo_fn, body_whl, carrying, extra = row

    if car_type not in TYPE_OF_CAR.values():
        return None

    if not (brand and photo_fn and carrying):
        return None

    if os.path.splitext(photo_fn)[1] not in PHOTO_EXTENSION:
        return None

    try:
        carrying = float(carrying)
    except ValueError:
        return None

    if car_type == TYPE_OF_CAR['Car']:
        try:
            passenger_sc = int(passenger_sc)
        except ValueError:
            return None
        return Car(brand, photo_fn, carrying, passenger_sc)

    if car_type == TYPE_OF_CAR['Truck']:
        return Truck(brand, photo_fn, carrying, body_whl)

    if car_type == TYPE_OF_CAR['SpecMachine']:
        if not extra:
            return None
        return SpecMachine(brand, photo_fn, carrying, extra)
