#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo


class JourneyLocation(object):

    def __init__(self):
        self._aoi_id = None
        self._city = None
        self._ext_info = None
        self._location_id = None
        self._location_id_type = None
        self._merchant_division_id = None
        self._merchant_id = None
        self._merchant_poi = None
        self._name = None
        self._poi_id = None

    @property
    def aoi_id(self):
        return self._aoi_id

    @aoi_id.setter
    def aoi_id(self, value):
        self._aoi_id = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, value):
        self._location_id = value
    @property
    def location_id_type(self):
        return self._location_id_type

    @location_id_type.setter
    def location_id_type(self, value):
        self._location_id_type = value
    @property
    def merchant_division_id(self):
        return self._merchant_division_id

    @merchant_division_id.setter
    def merchant_division_id(self, value):
        self._merchant_division_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_poi(self):
        return self._merchant_poi

    @merchant_poi.setter
    def merchant_poi(self, value):
        self._merchant_poi = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aoi_id:
            if hasattr(self.aoi_id, 'to_alipay_dict'):
                params['aoi_id'] = self.aoi_id.to_alipay_dict()
            else:
                params['aoi_id'] = self.aoi_id
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.location_id:
            if hasattr(self.location_id, 'to_alipay_dict'):
                params['location_id'] = self.location_id.to_alipay_dict()
            else:
                params['location_id'] = self.location_id
        if self.location_id_type:
            if hasattr(self.location_id_type, 'to_alipay_dict'):
                params['location_id_type'] = self.location_id_type.to_alipay_dict()
            else:
                params['location_id_type'] = self.location_id_type
        if self.merchant_division_id:
            if hasattr(self.merchant_division_id, 'to_alipay_dict'):
                params['merchant_division_id'] = self.merchant_division_id.to_alipay_dict()
            else:
                params['merchant_division_id'] = self.merchant_division_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_poi:
            if hasattr(self.merchant_poi, 'to_alipay_dict'):
                params['merchant_poi'] = self.merchant_poi.to_alipay_dict()
            else:
                params['merchant_poi'] = self.merchant_poi
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JourneyLocation()
        if 'aoi_id' in d:
            o.aoi_id = d['aoi_id']
        if 'city' in d:
            o.city = d['city']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'location_id' in d:
            o.location_id = d['location_id']
        if 'location_id_type' in d:
            o.location_id_type = d['location_id_type']
        if 'merchant_division_id' in d:
            o.merchant_division_id = d['merchant_division_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_poi' in d:
            o.merchant_poi = d['merchant_poi']
        if 'name' in d:
            o.name = d['name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        return o


