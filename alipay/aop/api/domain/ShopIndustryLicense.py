#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopIndustryLicense(object):

    def __init__(self):
        self._license_pic = None
        self._license_type = None

    @property
    def license_pic(self):
        return self._license_pic

    @license_pic.setter
    def license_pic(self, value):
        self._license_pic = value
    @property
    def license_type(self):
        return self._license_type

    @license_type.setter
    def license_type(self, value):
        self._license_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_pic:
            if hasattr(self.license_pic, 'to_alipay_dict'):
                params['license_pic'] = self.license_pic.to_alipay_dict()
            else:
                params['license_pic'] = self.license_pic
        if self.license_type:
            if hasattr(self.license_type, 'to_alipay_dict'):
                params['license_type'] = self.license_type.to_alipay_dict()
            else:
                params['license_type'] = self.license_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopIndustryLicense()
        if 'license_pic' in d:
            o.license_pic = d['license_pic']
        if 'license_type' in d:
            o.license_type = d['license_type']
        return o


