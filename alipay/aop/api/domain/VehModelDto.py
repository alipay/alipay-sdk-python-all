#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehModelDto(object):

    def __init__(self):
        self._acid = None
        self._body_type = None
        self._brand_id = None
        self._brand_logo_url = None
        self._brand_name = None
        self._car_type = None
        self._cylinder_arrangement = None
        self._cylinders_num = None
        self._displacement = None
        self._doors_num = None
        self._drive_mode = None
        self._emission_standard = None
        self._fuel_injection = None
        self._fuel_type = None
        self._horsepower = None
        self._intake = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._power_kw = None
        self._power_rpm = None
        self._price = None
        self._sale_name = None
        self._sale_years = None
        self._seat_num = None
        self._series_id = None
        self._series_image_url = None
        self._series_name = None
        self._show_name = None
        self._torque_nm = None
        self._torque_rpm = None
        self._transmission = None
        self._transmission_type = None
        self._vehicle_size = None
        self._vehicle_type = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, value):
        self._body_type = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_logo_url(self):
        return self._brand_logo_url

    @brand_logo_url.setter
    def brand_logo_url(self, value):
        self._brand_logo_url = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def cylinder_arrangement(self):
        return self._cylinder_arrangement

    @cylinder_arrangement.setter
    def cylinder_arrangement(self, value):
        self._cylinder_arrangement = value
    @property
    def cylinders_num(self):
        return self._cylinders_num

    @cylinders_num.setter
    def cylinders_num(self, value):
        self._cylinders_num = value
    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value
    @property
    def doors_num(self):
        return self._doors_num

    @doors_num.setter
    def doors_num(self, value):
        self._doors_num = value
    @property
    def drive_mode(self):
        return self._drive_mode

    @drive_mode.setter
    def drive_mode(self, value):
        self._drive_mode = value
    @property
    def emission_standard(self):
        return self._emission_standard

    @emission_standard.setter
    def emission_standard(self, value):
        self._emission_standard = value
    @property
    def fuel_injection(self):
        return self._fuel_injection

    @fuel_injection.setter
    def fuel_injection(self, value):
        self._fuel_injection = value
    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = value
    @property
    def horsepower(self):
        return self._horsepower

    @horsepower.setter
    def horsepower(self, value):
        self._horsepower = value
    @property
    def intake(self):
        return self._intake

    @intake.setter
    def intake(self, value):
        self._intake = value
    @property
    def manufacturer_id(self):
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, value):
        self._manufacturer_id = value
    @property
    def manufacturer_name(self):
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, value):
        self._manufacturer_name = value
    @property
    def power_kw(self):
        return self._power_kw

    @power_kw.setter
    def power_kw(self, value):
        self._power_kw = value
    @property
    def power_rpm(self):
        return self._power_rpm

    @power_rpm.setter
    def power_rpm(self, value):
        self._power_rpm = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sale_name(self):
        return self._sale_name

    @sale_name.setter
    def sale_name(self, value):
        self._sale_name = value
    @property
    def sale_years(self):
        return self._sale_years

    @sale_years.setter
    def sale_years(self, value):
        self._sale_years = value
    @property
    def seat_num(self):
        return self._seat_num

    @seat_num.setter
    def seat_num(self, value):
        self._seat_num = value
    @property
    def series_id(self):
        return self._series_id

    @series_id.setter
    def series_id(self, value):
        self._series_id = value
    @property
    def series_image_url(self):
        return self._series_image_url

    @series_image_url.setter
    def series_image_url(self, value):
        self._series_image_url = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
    @property
    def show_name(self):
        return self._show_name

    @show_name.setter
    def show_name(self, value):
        self._show_name = value
    @property
    def torque_nm(self):
        return self._torque_nm

    @torque_nm.setter
    def torque_nm(self, value):
        self._torque_nm = value
    @property
    def torque_rpm(self):
        return self._torque_rpm

    @torque_rpm.setter
    def torque_rpm(self, value):
        self._torque_rpm = value
    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, value):
        self._transmission = value
    @property
    def transmission_type(self):
        return self._transmission_type

    @transmission_type.setter
    def transmission_type(self, value):
        self._transmission_type = value
    @property
    def vehicle_size(self):
        return self._vehicle_size

    @vehicle_size.setter
    def vehicle_size(self, value):
        self._vehicle_size = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.acid:
            if hasattr(self.acid, 'to_alipay_dict'):
                params['acid'] = self.acid.to_alipay_dict()
            else:
                params['acid'] = self.acid
        if self.body_type:
            if hasattr(self.body_type, 'to_alipay_dict'):
                params['body_type'] = self.body_type.to_alipay_dict()
            else:
                params['body_type'] = self.body_type
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_logo_url:
            if hasattr(self.brand_logo_url, 'to_alipay_dict'):
                params['brand_logo_url'] = self.brand_logo_url.to_alipay_dict()
            else:
                params['brand_logo_url'] = self.brand_logo_url
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.cylinder_arrangement:
            if hasattr(self.cylinder_arrangement, 'to_alipay_dict'):
                params['cylinder_arrangement'] = self.cylinder_arrangement.to_alipay_dict()
            else:
                params['cylinder_arrangement'] = self.cylinder_arrangement
        if self.cylinders_num:
            if hasattr(self.cylinders_num, 'to_alipay_dict'):
                params['cylinders_num'] = self.cylinders_num.to_alipay_dict()
            else:
                params['cylinders_num'] = self.cylinders_num
        if self.displacement:
            if hasattr(self.displacement, 'to_alipay_dict'):
                params['displacement'] = self.displacement.to_alipay_dict()
            else:
                params['displacement'] = self.displacement
        if self.doors_num:
            if hasattr(self.doors_num, 'to_alipay_dict'):
                params['doors_num'] = self.doors_num.to_alipay_dict()
            else:
                params['doors_num'] = self.doors_num
        if self.drive_mode:
            if hasattr(self.drive_mode, 'to_alipay_dict'):
                params['drive_mode'] = self.drive_mode.to_alipay_dict()
            else:
                params['drive_mode'] = self.drive_mode
        if self.emission_standard:
            if hasattr(self.emission_standard, 'to_alipay_dict'):
                params['emission_standard'] = self.emission_standard.to_alipay_dict()
            else:
                params['emission_standard'] = self.emission_standard
        if self.fuel_injection:
            if hasattr(self.fuel_injection, 'to_alipay_dict'):
                params['fuel_injection'] = self.fuel_injection.to_alipay_dict()
            else:
                params['fuel_injection'] = self.fuel_injection
        if self.fuel_type:
            if hasattr(self.fuel_type, 'to_alipay_dict'):
                params['fuel_type'] = self.fuel_type.to_alipay_dict()
            else:
                params['fuel_type'] = self.fuel_type
        if self.horsepower:
            if hasattr(self.horsepower, 'to_alipay_dict'):
                params['horsepower'] = self.horsepower.to_alipay_dict()
            else:
                params['horsepower'] = self.horsepower
        if self.intake:
            if hasattr(self.intake, 'to_alipay_dict'):
                params['intake'] = self.intake.to_alipay_dict()
            else:
                params['intake'] = self.intake
        if self.manufacturer_id:
            if hasattr(self.manufacturer_id, 'to_alipay_dict'):
                params['manufacturer_id'] = self.manufacturer_id.to_alipay_dict()
            else:
                params['manufacturer_id'] = self.manufacturer_id
        if self.manufacturer_name:
            if hasattr(self.manufacturer_name, 'to_alipay_dict'):
                params['manufacturer_name'] = self.manufacturer_name.to_alipay_dict()
            else:
                params['manufacturer_name'] = self.manufacturer_name
        if self.power_kw:
            if hasattr(self.power_kw, 'to_alipay_dict'):
                params['power_kw'] = self.power_kw.to_alipay_dict()
            else:
                params['power_kw'] = self.power_kw
        if self.power_rpm:
            if hasattr(self.power_rpm, 'to_alipay_dict'):
                params['power_rpm'] = self.power_rpm.to_alipay_dict()
            else:
                params['power_rpm'] = self.power_rpm
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sale_name:
            if hasattr(self.sale_name, 'to_alipay_dict'):
                params['sale_name'] = self.sale_name.to_alipay_dict()
            else:
                params['sale_name'] = self.sale_name
        if self.sale_years:
            if hasattr(self.sale_years, 'to_alipay_dict'):
                params['sale_years'] = self.sale_years.to_alipay_dict()
            else:
                params['sale_years'] = self.sale_years
        if self.seat_num:
            if hasattr(self.seat_num, 'to_alipay_dict'):
                params['seat_num'] = self.seat_num.to_alipay_dict()
            else:
                params['seat_num'] = self.seat_num
        if self.series_id:
            if hasattr(self.series_id, 'to_alipay_dict'):
                params['series_id'] = self.series_id.to_alipay_dict()
            else:
                params['series_id'] = self.series_id
        if self.series_image_url:
            if hasattr(self.series_image_url, 'to_alipay_dict'):
                params['series_image_url'] = self.series_image_url.to_alipay_dict()
            else:
                params['series_image_url'] = self.series_image_url
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
        if self.show_name:
            if hasattr(self.show_name, 'to_alipay_dict'):
                params['show_name'] = self.show_name.to_alipay_dict()
            else:
                params['show_name'] = self.show_name
        if self.torque_nm:
            if hasattr(self.torque_nm, 'to_alipay_dict'):
                params['torque_nm'] = self.torque_nm.to_alipay_dict()
            else:
                params['torque_nm'] = self.torque_nm
        if self.torque_rpm:
            if hasattr(self.torque_rpm, 'to_alipay_dict'):
                params['torque_rpm'] = self.torque_rpm.to_alipay_dict()
            else:
                params['torque_rpm'] = self.torque_rpm
        if self.transmission:
            if hasattr(self.transmission, 'to_alipay_dict'):
                params['transmission'] = self.transmission.to_alipay_dict()
            else:
                params['transmission'] = self.transmission
        if self.transmission_type:
            if hasattr(self.transmission_type, 'to_alipay_dict'):
                params['transmission_type'] = self.transmission_type.to_alipay_dict()
            else:
                params['transmission_type'] = self.transmission_type
        if self.vehicle_size:
            if hasattr(self.vehicle_size, 'to_alipay_dict'):
                params['vehicle_size'] = self.vehicle_size.to_alipay_dict()
            else:
                params['vehicle_size'] = self.vehicle_size
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehModelDto()
        if 'acid' in d:
            o.acid = d['acid']
        if 'body_type' in d:
            o.body_type = d['body_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_logo_url' in d:
            o.brand_logo_url = d['brand_logo_url']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'cylinder_arrangement' in d:
            o.cylinder_arrangement = d['cylinder_arrangement']
        if 'cylinders_num' in d:
            o.cylinders_num = d['cylinders_num']
        if 'displacement' in d:
            o.displacement = d['displacement']
        if 'doors_num' in d:
            o.doors_num = d['doors_num']
        if 'drive_mode' in d:
            o.drive_mode = d['drive_mode']
        if 'emission_standard' in d:
            o.emission_standard = d['emission_standard']
        if 'fuel_injection' in d:
            o.fuel_injection = d['fuel_injection']
        if 'fuel_type' in d:
            o.fuel_type = d['fuel_type']
        if 'horsepower' in d:
            o.horsepower = d['horsepower']
        if 'intake' in d:
            o.intake = d['intake']
        if 'manufacturer_id' in d:
            o.manufacturer_id = d['manufacturer_id']
        if 'manufacturer_name' in d:
            o.manufacturer_name = d['manufacturer_name']
        if 'power_kw' in d:
            o.power_kw = d['power_kw']
        if 'power_rpm' in d:
            o.power_rpm = d['power_rpm']
        if 'price' in d:
            o.price = d['price']
        if 'sale_name' in d:
            o.sale_name = d['sale_name']
        if 'sale_years' in d:
            o.sale_years = d['sale_years']
        if 'seat_num' in d:
            o.seat_num = d['seat_num']
        if 'series_id' in d:
            o.series_id = d['series_id']
        if 'series_image_url' in d:
            o.series_image_url = d['series_image_url']
        if 'series_name' in d:
            o.series_name = d['series_name']
        if 'show_name' in d:
            o.show_name = d['show_name']
        if 'torque_nm' in d:
            o.torque_nm = d['torque_nm']
        if 'torque_rpm' in d:
            o.torque_rpm = d['torque_rpm']
        if 'transmission' in d:
            o.transmission = d['transmission']
        if 'transmission_type' in d:
            o.transmission_type = d['transmission_type']
        if 'vehicle_size' in d:
            o.vehicle_size = d['vehicle_size']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        return o


