#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MobileDeviceInfo(object):

    def __init__(self):
        self._imei = None
        self._mobile_brand = None
        self._mobile_type = None

    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def mobile_brand(self):
        return self._mobile_brand

    @mobile_brand.setter
    def mobile_brand(self, value):
        self._mobile_brand = value
    @property
    def mobile_type(self):
        return self._mobile_type

    @mobile_type.setter
    def mobile_type(self, value):
        self._mobile_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.mobile_brand:
            if hasattr(self.mobile_brand, 'to_alipay_dict'):
                params['mobile_brand'] = self.mobile_brand.to_alipay_dict()
            else:
                params['mobile_brand'] = self.mobile_brand
        if self.mobile_type:
            if hasattr(self.mobile_type, 'to_alipay_dict'):
                params['mobile_type'] = self.mobile_type.to_alipay_dict()
            else:
                params['mobile_type'] = self.mobile_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MobileDeviceInfo()
        if 'imei' in d:
            o.imei = d['imei']
        if 'mobile_brand' in d:
            o.mobile_brand = d['mobile_brand']
        if 'mobile_type' in d:
            o.mobile_type = d['mobile_type']
        return o


