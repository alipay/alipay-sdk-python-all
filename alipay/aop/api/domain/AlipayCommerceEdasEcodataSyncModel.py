#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LocationData import LocationData


class AlipayCommerceEdasEcodataSyncModel(object):

    def __init__(self):
        self._data_scene_code = None
        self._industry_id = None
        self._inst_id = None
        self._location_data = None
        self._merchant_id = None

    @property
    def data_scene_code(self):
        return self._data_scene_code

    @data_scene_code.setter
    def data_scene_code(self, value):
        self._data_scene_code = value
    @property
    def industry_id(self):
        return self._industry_id

    @industry_id.setter
    def industry_id(self, value):
        self._industry_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def location_data(self):
        return self._location_data

    @location_data.setter
    def location_data(self, value):
        if isinstance(value, LocationData):
            self._location_data = value
        else:
            self._location_data = LocationData.from_alipay_dict(value)
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_scene_code:
            if hasattr(self.data_scene_code, 'to_alipay_dict'):
                params['data_scene_code'] = self.data_scene_code.to_alipay_dict()
            else:
                params['data_scene_code'] = self.data_scene_code
        if self.industry_id:
            if hasattr(self.industry_id, 'to_alipay_dict'):
                params['industry_id'] = self.industry_id.to_alipay_dict()
            else:
                params['industry_id'] = self.industry_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.location_data:
            if hasattr(self.location_data, 'to_alipay_dict'):
                params['location_data'] = self.location_data.to_alipay_dict()
            else:
                params['location_data'] = self.location_data
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEdasEcodataSyncModel()
        if 'data_scene_code' in d:
            o.data_scene_code = d['data_scene_code']
        if 'industry_id' in d:
            o.industry_id = d['industry_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'location_data' in d:
            o.location_data = d['location_data']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


