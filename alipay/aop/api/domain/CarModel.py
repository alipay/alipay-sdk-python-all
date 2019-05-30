#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarModel(object):

    def __init__(self):
        self._brand_name = None
        self._config_name = None
        self._engine_desc = None
        self._family_short_name = None
        self._gear_box_type = None
        self._purchase_price = None
        self._seat = None
        self._seat_max = None
        self._seat_min = None
        self._vehicle_class_code = None
        self._vehicle_code = None
        self._vehicle_name = None
        self._year_pattern = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def config_name(self):
        return self._config_name

    @config_name.setter
    def config_name(self, value):
        self._config_name = value
    @property
    def engine_desc(self):
        return self._engine_desc

    @engine_desc.setter
    def engine_desc(self, value):
        self._engine_desc = value
    @property
    def family_short_name(self):
        return self._family_short_name

    @family_short_name.setter
    def family_short_name(self, value):
        self._family_short_name = value
    @property
    def gear_box_type(self):
        return self._gear_box_type

    @gear_box_type.setter
    def gear_box_type(self, value):
        self._gear_box_type = value
    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, value):
        self._purchase_price = value
    @property
    def seat(self):
        return self._seat

    @seat.setter
    def seat(self, value):
        self._seat = value
    @property
    def seat_max(self):
        return self._seat_max

    @seat_max.setter
    def seat_max(self, value):
        self._seat_max = value
    @property
    def seat_min(self):
        return self._seat_min

    @seat_min.setter
    def seat_min(self, value):
        self._seat_min = value
    @property
    def vehicle_class_code(self):
        return self._vehicle_class_code

    @vehicle_class_code.setter
    def vehicle_class_code(self, value):
        self._vehicle_class_code = value
    @property
    def vehicle_code(self):
        return self._vehicle_code

    @vehicle_code.setter
    def vehicle_code(self, value):
        self._vehicle_code = value
    @property
    def vehicle_name(self):
        return self._vehicle_name

    @vehicle_name.setter
    def vehicle_name(self, value):
        self._vehicle_name = value
    @property
    def year_pattern(self):
        return self._year_pattern

    @year_pattern.setter
    def year_pattern(self, value):
        self._year_pattern = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.config_name:
            if hasattr(self.config_name, 'to_alipay_dict'):
                params['config_name'] = self.config_name.to_alipay_dict()
            else:
                params['config_name'] = self.config_name
        if self.engine_desc:
            if hasattr(self.engine_desc, 'to_alipay_dict'):
                params['engine_desc'] = self.engine_desc.to_alipay_dict()
            else:
                params['engine_desc'] = self.engine_desc
        if self.family_short_name:
            if hasattr(self.family_short_name, 'to_alipay_dict'):
                params['family_short_name'] = self.family_short_name.to_alipay_dict()
            else:
                params['family_short_name'] = self.family_short_name
        if self.gear_box_type:
            if hasattr(self.gear_box_type, 'to_alipay_dict'):
                params['gear_box_type'] = self.gear_box_type.to_alipay_dict()
            else:
                params['gear_box_type'] = self.gear_box_type
        if self.purchase_price:
            if hasattr(self.purchase_price, 'to_alipay_dict'):
                params['purchase_price'] = self.purchase_price.to_alipay_dict()
            else:
                params['purchase_price'] = self.purchase_price
        if self.seat:
            if hasattr(self.seat, 'to_alipay_dict'):
                params['seat'] = self.seat.to_alipay_dict()
            else:
                params['seat'] = self.seat
        if self.seat_max:
            if hasattr(self.seat_max, 'to_alipay_dict'):
                params['seat_max'] = self.seat_max.to_alipay_dict()
            else:
                params['seat_max'] = self.seat_max
        if self.seat_min:
            if hasattr(self.seat_min, 'to_alipay_dict'):
                params['seat_min'] = self.seat_min.to_alipay_dict()
            else:
                params['seat_min'] = self.seat_min
        if self.vehicle_class_code:
            if hasattr(self.vehicle_class_code, 'to_alipay_dict'):
                params['vehicle_class_code'] = self.vehicle_class_code.to_alipay_dict()
            else:
                params['vehicle_class_code'] = self.vehicle_class_code
        if self.vehicle_code:
            if hasattr(self.vehicle_code, 'to_alipay_dict'):
                params['vehicle_code'] = self.vehicle_code.to_alipay_dict()
            else:
                params['vehicle_code'] = self.vehicle_code
        if self.vehicle_name:
            if hasattr(self.vehicle_name, 'to_alipay_dict'):
                params['vehicle_name'] = self.vehicle_name.to_alipay_dict()
            else:
                params['vehicle_name'] = self.vehicle_name
        if self.year_pattern:
            if hasattr(self.year_pattern, 'to_alipay_dict'):
                params['year_pattern'] = self.year_pattern.to_alipay_dict()
            else:
                params['year_pattern'] = self.year_pattern
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarModel()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'config_name' in d:
            o.config_name = d['config_name']
        if 'engine_desc' in d:
            o.engine_desc = d['engine_desc']
        if 'family_short_name' in d:
            o.family_short_name = d['family_short_name']
        if 'gear_box_type' in d:
            o.gear_box_type = d['gear_box_type']
        if 'purchase_price' in d:
            o.purchase_price = d['purchase_price']
        if 'seat' in d:
            o.seat = d['seat']
        if 'seat_max' in d:
            o.seat_max = d['seat_max']
        if 'seat_min' in d:
            o.seat_min = d['seat_min']
        if 'vehicle_class_code' in d:
            o.vehicle_class_code = d['vehicle_class_code']
        if 'vehicle_code' in d:
            o.vehicle_code = d['vehicle_code']
        if 'vehicle_name' in d:
            o.vehicle_name = d['vehicle_name']
        if 'year_pattern' in d:
            o.year_pattern = d['year_pattern']
        return o


