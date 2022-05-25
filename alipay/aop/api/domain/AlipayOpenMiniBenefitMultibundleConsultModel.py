#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniBenefitMultibundleConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._category_code = None
        self._device_id = None
        self._latitude = None
        self._login_mobile_id = None
        self._longitude = None
        self._product_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def login_mobile_id(self):
        return self._login_mobile_id

    @login_mobile_id.setter
    def login_mobile_id(self, value):
        self._login_mobile_id = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.login_mobile_id:
            if hasattr(self.login_mobile_id, 'to_alipay_dict'):
                params['login_mobile_id'] = self.login_mobile_id.to_alipay_dict()
            else:
                params['login_mobile_id'] = self.login_mobile_id
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniBenefitMultibundleConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'login_mobile_id' in d:
            o.login_mobile_id = d['login_mobile_id']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'product_id' in d:
            o.product_id = d['product_id']
        return o


