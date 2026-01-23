#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecialLicenseInfo(object):

    def __init__(self):
        self._special_license_pic = None
        self._special_license_type = None

    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        self._special_license_pic = value
    @property
    def special_license_type(self):
        return self._special_license_type

    @special_license_type.setter
    def special_license_type(self, value):
        self._special_license_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.special_license_pic:
            if hasattr(self.special_license_pic, 'to_alipay_dict'):
                params['special_license_pic'] = self.special_license_pic.to_alipay_dict()
            else:
                params['special_license_pic'] = self.special_license_pic
        if self.special_license_type:
            if hasattr(self.special_license_type, 'to_alipay_dict'):
                params['special_license_type'] = self.special_license_type.to_alipay_dict()
            else:
                params['special_license_type'] = self.special_license_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecialLicenseInfo()
        if 'special_license_pic' in d:
            o.special_license_pic = d['special_license_pic']
        if 'special_license_type' in d:
            o.special_license_type = d['special_license_type']
        return o


