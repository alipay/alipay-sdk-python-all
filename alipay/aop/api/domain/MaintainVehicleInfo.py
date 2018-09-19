#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaintainVehicleInfo(object):

    def __init__(self):
        self._bg_url = None
        self._engine_no = None
        self._engine_type = None
        self._manufacturer = None
        self._model_id = None
        self._production_year = None
        self._swept_volume = None
        self._vi_brand_logo = None
        self._vi_brand_name = None
        self._vi_city_id = None
        self._vi_city_name = None
        self._vi_logo_url = None
        self._vi_mileage = None
        self._vi_model_name = None
        self._vi_number = None
        self._vi_series_name = None
        self._vi_start_time = None
        self._vi_style_name = None
        self._vi_vin = None
        self._vl_start_time = None

    @property
    def bg_url(self):
        return self._bg_url

    @bg_url.setter
    def bg_url(self, value):
        self._bg_url = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value
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
    def production_year(self):
        return self._production_year

    @production_year.setter
    def production_year(self, value):
        self._production_year = value
    @property
    def swept_volume(self):
        return self._swept_volume

    @swept_volume.setter
    def swept_volume(self, value):
        if isinstance(value, list):
            self._swept_volume = list()
            for i in value:
                self._swept_volume.append(i)
    @property
    def vi_brand_logo(self):
        return self._vi_brand_logo

    @vi_brand_logo.setter
    def vi_brand_logo(self, value):
        self._vi_brand_logo = value
    @property
    def vi_brand_name(self):
        return self._vi_brand_name

    @vi_brand_name.setter
    def vi_brand_name(self, value):
        self._vi_brand_name = value
    @property
    def vi_city_id(self):
        return self._vi_city_id

    @vi_city_id.setter
    def vi_city_id(self, value):
        self._vi_city_id = value
    @property
    def vi_city_name(self):
        return self._vi_city_name

    @vi_city_name.setter
    def vi_city_name(self, value):
        self._vi_city_name = value
    @property
    def vi_logo_url(self):
        return self._vi_logo_url

    @vi_logo_url.setter
    def vi_logo_url(self, value):
        self._vi_logo_url = value
    @property
    def vi_mileage(self):
        return self._vi_mileage

    @vi_mileage.setter
    def vi_mileage(self, value):
        self._vi_mileage = value
    @property
    def vi_model_name(self):
        return self._vi_model_name

    @vi_model_name.setter
    def vi_model_name(self, value):
        self._vi_model_name = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value
    @property
    def vi_series_name(self):
        return self._vi_series_name

    @vi_series_name.setter
    def vi_series_name(self, value):
        self._vi_series_name = value
    @property
    def vi_start_time(self):
        return self._vi_start_time

    @vi_start_time.setter
    def vi_start_time(self, value):
        self._vi_start_time = value
    @property
    def vi_style_name(self):
        return self._vi_style_name

    @vi_style_name.setter
    def vi_style_name(self, value):
        self._vi_style_name = value
    @property
    def vi_vin(self):
        return self._vi_vin

    @vi_vin.setter
    def vi_vin(self, value):
        if isinstance(value, list):
            self._vi_vin = list()
            for i in value:
                self._vi_vin.append(i)
    @property
    def vl_start_time(self):
        return self._vl_start_time

    @vl_start_time.setter
    def vl_start_time(self, value):
        self._vl_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bg_url:
            if hasattr(self.bg_url, 'to_alipay_dict'):
                params['bg_url'] = self.bg_url.to_alipay_dict()
            else:
                params['bg_url'] = self.bg_url
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.engine_type:
            if hasattr(self.engine_type, 'to_alipay_dict'):
                params['engine_type'] = self.engine_type.to_alipay_dict()
            else:
                params['engine_type'] = self.engine_type
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
        if self.production_year:
            if hasattr(self.production_year, 'to_alipay_dict'):
                params['production_year'] = self.production_year.to_alipay_dict()
            else:
                params['production_year'] = self.production_year
        if self.swept_volume:
            if isinstance(self.swept_volume, list):
                for i in range(0, len(self.swept_volume)):
                    element = self.swept_volume[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.swept_volume[i] = element.to_alipay_dict()
            if hasattr(self.swept_volume, 'to_alipay_dict'):
                params['swept_volume'] = self.swept_volume.to_alipay_dict()
            else:
                params['swept_volume'] = self.swept_volume
        if self.vi_brand_logo:
            if hasattr(self.vi_brand_logo, 'to_alipay_dict'):
                params['vi_brand_logo'] = self.vi_brand_logo.to_alipay_dict()
            else:
                params['vi_brand_logo'] = self.vi_brand_logo
        if self.vi_brand_name:
            if hasattr(self.vi_brand_name, 'to_alipay_dict'):
                params['vi_brand_name'] = self.vi_brand_name.to_alipay_dict()
            else:
                params['vi_brand_name'] = self.vi_brand_name
        if self.vi_city_id:
            if hasattr(self.vi_city_id, 'to_alipay_dict'):
                params['vi_city_id'] = self.vi_city_id.to_alipay_dict()
            else:
                params['vi_city_id'] = self.vi_city_id
        if self.vi_city_name:
            if hasattr(self.vi_city_name, 'to_alipay_dict'):
                params['vi_city_name'] = self.vi_city_name.to_alipay_dict()
            else:
                params['vi_city_name'] = self.vi_city_name
        if self.vi_logo_url:
            if hasattr(self.vi_logo_url, 'to_alipay_dict'):
                params['vi_logo_url'] = self.vi_logo_url.to_alipay_dict()
            else:
                params['vi_logo_url'] = self.vi_logo_url
        if self.vi_mileage:
            if hasattr(self.vi_mileage, 'to_alipay_dict'):
                params['vi_mileage'] = self.vi_mileage.to_alipay_dict()
            else:
                params['vi_mileage'] = self.vi_mileage
        if self.vi_model_name:
            if hasattr(self.vi_model_name, 'to_alipay_dict'):
                params['vi_model_name'] = self.vi_model_name.to_alipay_dict()
            else:
                params['vi_model_name'] = self.vi_model_name
        if self.vi_number:
            if hasattr(self.vi_number, 'to_alipay_dict'):
                params['vi_number'] = self.vi_number.to_alipay_dict()
            else:
                params['vi_number'] = self.vi_number
        if self.vi_series_name:
            if hasattr(self.vi_series_name, 'to_alipay_dict'):
                params['vi_series_name'] = self.vi_series_name.to_alipay_dict()
            else:
                params['vi_series_name'] = self.vi_series_name
        if self.vi_start_time:
            if hasattr(self.vi_start_time, 'to_alipay_dict'):
                params['vi_start_time'] = self.vi_start_time.to_alipay_dict()
            else:
                params['vi_start_time'] = self.vi_start_time
        if self.vi_style_name:
            if hasattr(self.vi_style_name, 'to_alipay_dict'):
                params['vi_style_name'] = self.vi_style_name.to_alipay_dict()
            else:
                params['vi_style_name'] = self.vi_style_name
        if self.vi_vin:
            if isinstance(self.vi_vin, list):
                for i in range(0, len(self.vi_vin)):
                    element = self.vi_vin[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vi_vin[i] = element.to_alipay_dict()
            if hasattr(self.vi_vin, 'to_alipay_dict'):
                params['vi_vin'] = self.vi_vin.to_alipay_dict()
            else:
                params['vi_vin'] = self.vi_vin
        if self.vl_start_time:
            if hasattr(self.vl_start_time, 'to_alipay_dict'):
                params['vl_start_time'] = self.vl_start_time.to_alipay_dict()
            else:
                params['vl_start_time'] = self.vl_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaintainVehicleInfo()
        if 'bg_url' in d:
            o.bg_url = d['bg_url']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'engine_type' in d:
            o.engine_type = d['engine_type']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'production_year' in d:
            o.production_year = d['production_year']
        if 'swept_volume' in d:
            o.swept_volume = d['swept_volume']
        if 'vi_brand_logo' in d:
            o.vi_brand_logo = d['vi_brand_logo']
        if 'vi_brand_name' in d:
            o.vi_brand_name = d['vi_brand_name']
        if 'vi_city_id' in d:
            o.vi_city_id = d['vi_city_id']
        if 'vi_city_name' in d:
            o.vi_city_name = d['vi_city_name']
        if 'vi_logo_url' in d:
            o.vi_logo_url = d['vi_logo_url']
        if 'vi_mileage' in d:
            o.vi_mileage = d['vi_mileage']
        if 'vi_model_name' in d:
            o.vi_model_name = d['vi_model_name']
        if 'vi_number' in d:
            o.vi_number = d['vi_number']
        if 'vi_series_name' in d:
            o.vi_series_name = d['vi_series_name']
        if 'vi_start_time' in d:
            o.vi_start_time = d['vi_start_time']
        if 'vi_style_name' in d:
            o.vi_style_name = d['vi_style_name']
        if 'vi_vin' in d:
            o.vi_vin = d['vi_vin']
        if 'vl_start_time' in d:
            o.vl_start_time = d['vl_start_time']
        return o


