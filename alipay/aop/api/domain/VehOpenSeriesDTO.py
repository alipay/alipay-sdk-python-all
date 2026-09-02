#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehOpenSeriesDTO(object):

    def __init__(self):
        self._body_type = None
        self._brand_id = None
        self._brand_name = None
        self._fuel_type = None
        self._guide_price_max = None
        self._guide_price_min = None
        self._launch_date = None
        self._manufacturer = None
        self._manufacturer_type = None
        self._sale_status = None
        self._seat_num = None
        self._series_id = None
        self._series_img = None
        self._series_name = None
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
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = value
    @property
    def guide_price_max(self):
        return self._guide_price_max

    @guide_price_max.setter
    def guide_price_max(self, value):
        self._guide_price_max = value
    @property
    def guide_price_min(self):
        return self._guide_price_min

    @guide_price_min.setter
    def guide_price_min(self, value):
        self._guide_price_min = value
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
    def manufacturer_type(self):
        return self._manufacturer_type

    @manufacturer_type.setter
    def manufacturer_type(self, value):
        self._manufacturer_type = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
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
    def series_img(self):
        return self._series_img

    @series_img.setter
    def series_img(self, value):
        self._series_img = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
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
        if self.fuel_type:
            if hasattr(self.fuel_type, 'to_alipay_dict'):
                params['fuel_type'] = self.fuel_type.to_alipay_dict()
            else:
                params['fuel_type'] = self.fuel_type
        if self.guide_price_max:
            if hasattr(self.guide_price_max, 'to_alipay_dict'):
                params['guide_price_max'] = self.guide_price_max.to_alipay_dict()
            else:
                params['guide_price_max'] = self.guide_price_max
        if self.guide_price_min:
            if hasattr(self.guide_price_min, 'to_alipay_dict'):
                params['guide_price_min'] = self.guide_price_min.to_alipay_dict()
            else:
                params['guide_price_min'] = self.guide_price_min
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
        if self.manufacturer_type:
            if hasattr(self.manufacturer_type, 'to_alipay_dict'):
                params['manufacturer_type'] = self.manufacturer_type.to_alipay_dict()
            else:
                params['manufacturer_type'] = self.manufacturer_type
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
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
        if self.series_img:
            if hasattr(self.series_img, 'to_alipay_dict'):
                params['series_img'] = self.series_img.to_alipay_dict()
            else:
                params['series_img'] = self.series_img
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
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
        o = VehOpenSeriesDTO()
        if 'body_type' in d:
            o.body_type = d['body_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'fuel_type' in d:
            o.fuel_type = d['fuel_type']
        if 'guide_price_max' in d:
            o.guide_price_max = d['guide_price_max']
        if 'guide_price_min' in d:
            o.guide_price_min = d['guide_price_min']
        if 'launch_date' in d:
            o.launch_date = d['launch_date']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'manufacturer_type' in d:
            o.manufacturer_type = d['manufacturer_type']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'seat_num' in d:
            o.seat_num = d['seat_num']
        if 'series_id' in d:
            o.series_id = d['series_id']
        if 'series_img' in d:
            o.series_img = d['series_img']
        if 'series_name' in d:
            o.series_name = d['series_name']
        if 'vehicle_size' in d:
            o.vehicle_size = d['vehicle_size']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        return o


