#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehOpenModelDTO(object):

    def __init__(self):
        self._body_type = None
        self._brand_id = None
        self._brand_name = None
        self._cylinder_arrangement = None
        self._cylinders = None
        self._displacement = None
        self._doors = None
        self._drive_mode = None
        self._emission_standard = None
        self._fuel_injection = None
        self._fuel_type = None
        self._guide_price = None
        self._horsepower = None
        self._intake = None
        self._launch_date = None
        self._manufacturer = None
        self._model_id = None
        self._model_img = None
        self._model_name = None
        self._power_kw = None
        self._power_rpm = None
        self._sale_status = None
        self._sale_years = None
        self._seat_num = None
        self._series_id = None
        self._series_name = None
        self._torque_nm = None
        self._torque_rpm = None
        self._transmission = None
        self._transmission_type = None
        self._vehicle_size = None
        self._vehicle_type = None

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
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def cylinder_arrangement(self):
        return self._cylinder_arrangement

    @cylinder_arrangement.setter
    def cylinder_arrangement(self, value):
        self._cylinder_arrangement = value
    @property
    def cylinders(self):
        return self._cylinders

    @cylinders.setter
    def cylinders(self, value):
        self._cylinders = value
    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value
    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        self._doors = value
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
    def guide_price(self):
        return self._guide_price

    @guide_price.setter
    def guide_price(self, value):
        self._guide_price = value
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
    def launch_date(self):
        return self._launch_date

    @launch_date.setter
    def launch_date(self, value):
        self._launch_date = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_img(self):
        return self._model_img

    @model_img.setter
    def model_img(self, value):
        self._model_img = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
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
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
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
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
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
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.cylinder_arrangement:
            if hasattr(self.cylinder_arrangement, 'to_alipay_dict'):
                params['cylinder_arrangement'] = self.cylinder_arrangement.to_alipay_dict()
            else:
                params['cylinder_arrangement'] = self.cylinder_arrangement
        if self.cylinders:
            if hasattr(self.cylinders, 'to_alipay_dict'):
                params['cylinders'] = self.cylinders.to_alipay_dict()
            else:
                params['cylinders'] = self.cylinders
        if self.displacement:
            if hasattr(self.displacement, 'to_alipay_dict'):
                params['displacement'] = self.displacement.to_alipay_dict()
            else:
                params['displacement'] = self.displacement
        if self.doors:
            if hasattr(self.doors, 'to_alipay_dict'):
                params['doors'] = self.doors.to_alipay_dict()
            else:
                params['doors'] = self.doors
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
        if self.guide_price:
            if hasattr(self.guide_price, 'to_alipay_dict'):
                params['guide_price'] = self.guide_price.to_alipay_dict()
            else:
                params['guide_price'] = self.guide_price
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
        if self.launch_date:
            if hasattr(self.launch_date, 'to_alipay_dict'):
                params['launch_date'] = self.launch_date.to_alipay_dict()
            else:
                params['launch_date'] = self.launch_date
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.model_img:
            if hasattr(self.model_img, 'to_alipay_dict'):
                params['model_img'] = self.model_img.to_alipay_dict()
            else:
                params['model_img'] = self.model_img
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
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
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
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
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
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
        o = VehOpenModelDTO()
        if 'body_type' in d:
            o.body_type = d['body_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'cylinder_arrangement' in d:
            o.cylinder_arrangement = d['cylinder_arrangement']
        if 'cylinders' in d:
            o.cylinders = d['cylinders']
        if 'displacement' in d:
            o.displacement = d['displacement']
        if 'doors' in d:
            o.doors = d['doors']
        if 'drive_mode' in d:
            o.drive_mode = d['drive_mode']
        if 'emission_standard' in d:
            o.emission_standard = d['emission_standard']
        if 'fuel_injection' in d:
            o.fuel_injection = d['fuel_injection']
        if 'fuel_type' in d:
            o.fuel_type = d['fuel_type']
        if 'guide_price' in d:
            o.guide_price = d['guide_price']
        if 'horsepower' in d:
            o.horsepower = d['horsepower']
        if 'intake' in d:
            o.intake = d['intake']
        if 'launch_date' in d:
            o.launch_date = d['launch_date']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'model_img' in d:
            o.model_img = d['model_img']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'power_kw' in d:
            o.power_kw = d['power_kw']
        if 'power_rpm' in d:
            o.power_rpm = d['power_rpm']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'sale_years' in d:
            o.sale_years = d['sale_years']
        if 'seat_num' in d:
            o.seat_num = d['seat_num']
        if 'series_id' in d:
            o.series_id = d['series_id']
        if 'series_name' in d:
            o.series_name = d['series_name']
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


