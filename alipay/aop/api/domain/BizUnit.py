#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizUnit(object):

    def __init__(self):
        self._amap_id = None
        self._biz_address = None
        self._biz_city_code = None
        self._biz_city_name = None
        self._biz_latitude = None
        self._biz_longitude = None
        self._biz_province_code = None
        self._biz_province_name = None
        self._biz_region_code = None
        self._biz_region_name = None
        self._biz_unit_id = None
        self._biz_unit_name = None

    @property
    def amap_id(self):
        return self._amap_id

    @amap_id.setter
    def amap_id(self, value):
        self._amap_id = value
    @property
    def biz_address(self):
        return self._biz_address

    @biz_address.setter
    def biz_address(self, value):
        self._biz_address = value
    @property
    def biz_city_code(self):
        return self._biz_city_code

    @biz_city_code.setter
    def biz_city_code(self, value):
        self._biz_city_code = value
    @property
    def biz_city_name(self):
        return self._biz_city_name

    @biz_city_name.setter
    def biz_city_name(self, value):
        self._biz_city_name = value
    @property
    def biz_latitude(self):
        return self._biz_latitude

    @biz_latitude.setter
    def biz_latitude(self, value):
        self._biz_latitude = value
    @property
    def biz_longitude(self):
        return self._biz_longitude

    @biz_longitude.setter
    def biz_longitude(self, value):
        self._biz_longitude = value
    @property
    def biz_province_code(self):
        return self._biz_province_code

    @biz_province_code.setter
    def biz_province_code(self, value):
        self._biz_province_code = value
    @property
    def biz_province_name(self):
        return self._biz_province_name

    @biz_province_name.setter
    def biz_province_name(self, value):
        self._biz_province_name = value
    @property
    def biz_region_code(self):
        return self._biz_region_code

    @biz_region_code.setter
    def biz_region_code(self, value):
        self._biz_region_code = value
    @property
    def biz_region_name(self):
        return self._biz_region_name

    @biz_region_name.setter
    def biz_region_name(self, value):
        self._biz_region_name = value
    @property
    def biz_unit_id(self):
        return self._biz_unit_id

    @biz_unit_id.setter
    def biz_unit_id(self, value):
        self._biz_unit_id = value
    @property
    def biz_unit_name(self):
        return self._biz_unit_name

    @biz_unit_name.setter
    def biz_unit_name(self, value):
        self._biz_unit_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amap_id:
            if hasattr(self.amap_id, 'to_alipay_dict'):
                params['amap_id'] = self.amap_id.to_alipay_dict()
            else:
                params['amap_id'] = self.amap_id
        if self.biz_address:
            if hasattr(self.biz_address, 'to_alipay_dict'):
                params['biz_address'] = self.biz_address.to_alipay_dict()
            else:
                params['biz_address'] = self.biz_address
        if self.biz_city_code:
            if hasattr(self.biz_city_code, 'to_alipay_dict'):
                params['biz_city_code'] = self.biz_city_code.to_alipay_dict()
            else:
                params['biz_city_code'] = self.biz_city_code
        if self.biz_city_name:
            if hasattr(self.biz_city_name, 'to_alipay_dict'):
                params['biz_city_name'] = self.biz_city_name.to_alipay_dict()
            else:
                params['biz_city_name'] = self.biz_city_name
        if self.biz_latitude:
            if hasattr(self.biz_latitude, 'to_alipay_dict'):
                params['biz_latitude'] = self.biz_latitude.to_alipay_dict()
            else:
                params['biz_latitude'] = self.biz_latitude
        if self.biz_longitude:
            if hasattr(self.biz_longitude, 'to_alipay_dict'):
                params['biz_longitude'] = self.biz_longitude.to_alipay_dict()
            else:
                params['biz_longitude'] = self.biz_longitude
        if self.biz_province_code:
            if hasattr(self.biz_province_code, 'to_alipay_dict'):
                params['biz_province_code'] = self.biz_province_code.to_alipay_dict()
            else:
                params['biz_province_code'] = self.biz_province_code
        if self.biz_province_name:
            if hasattr(self.biz_province_name, 'to_alipay_dict'):
                params['biz_province_name'] = self.biz_province_name.to_alipay_dict()
            else:
                params['biz_province_name'] = self.biz_province_name
        if self.biz_region_code:
            if hasattr(self.biz_region_code, 'to_alipay_dict'):
                params['biz_region_code'] = self.biz_region_code.to_alipay_dict()
            else:
                params['biz_region_code'] = self.biz_region_code
        if self.biz_region_name:
            if hasattr(self.biz_region_name, 'to_alipay_dict'):
                params['biz_region_name'] = self.biz_region_name.to_alipay_dict()
            else:
                params['biz_region_name'] = self.biz_region_name
        if self.biz_unit_id:
            if hasattr(self.biz_unit_id, 'to_alipay_dict'):
                params['biz_unit_id'] = self.biz_unit_id.to_alipay_dict()
            else:
                params['biz_unit_id'] = self.biz_unit_id
        if self.biz_unit_name:
            if hasattr(self.biz_unit_name, 'to_alipay_dict'):
                params['biz_unit_name'] = self.biz_unit_name.to_alipay_dict()
            else:
                params['biz_unit_name'] = self.biz_unit_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizUnit()
        if 'amap_id' in d:
            o.amap_id = d['amap_id']
        if 'biz_address' in d:
            o.biz_address = d['biz_address']
        if 'biz_city_code' in d:
            o.biz_city_code = d['biz_city_code']
        if 'biz_city_name' in d:
            o.biz_city_name = d['biz_city_name']
        if 'biz_latitude' in d:
            o.biz_latitude = d['biz_latitude']
        if 'biz_longitude' in d:
            o.biz_longitude = d['biz_longitude']
        if 'biz_province_code' in d:
            o.biz_province_code = d['biz_province_code']
        if 'biz_province_name' in d:
            o.biz_province_name = d['biz_province_name']
        if 'biz_region_code' in d:
            o.biz_region_code = d['biz_region_code']
        if 'biz_region_name' in d:
            o.biz_region_name = d['biz_region_name']
        if 'biz_unit_id' in d:
            o.biz_unit_id = d['biz_unit_id']
        if 'biz_unit_name' in d:
            o.biz_unit_name = d['biz_unit_name']
        return o


