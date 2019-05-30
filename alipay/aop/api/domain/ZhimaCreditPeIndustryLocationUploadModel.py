#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeIndustryLocationUploadModel(object):

    def __init__(self):
        self._biz_scene = None
        self._can_use = None
        self._ext_info = None
        self._latitude = None
        self._location_address = None
        self._location_code = None
        self._location_name = None
        self._longitude = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def can_use(self):
        return self._can_use

    @can_use.setter
    def can_use(self, value):
        self._can_use = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def location_address(self):
        return self._location_address

    @location_address.setter
    def location_address(self, value):
        self._location_address = value
    @property
    def location_code(self):
        return self._location_code

    @location_code.setter
    def location_code(self, value):
        self._location_code = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.can_use:
            if hasattr(self.can_use, 'to_alipay_dict'):
                params['can_use'] = self.can_use.to_alipay_dict()
            else:
                params['can_use'] = self.can_use
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.location_address:
            if hasattr(self.location_address, 'to_alipay_dict'):
                params['location_address'] = self.location_address.to_alipay_dict()
            else:
                params['location_address'] = self.location_address
        if self.location_code:
            if hasattr(self.location_code, 'to_alipay_dict'):
                params['location_code'] = self.location_code.to_alipay_dict()
            else:
                params['location_code'] = self.location_code
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeIndustryLocationUploadModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'can_use' in d:
            o.can_use = d['can_use']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'location_address' in d:
            o.location_address = d['location_address']
        if 'location_code' in d:
            o.location_code = d['location_code']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


