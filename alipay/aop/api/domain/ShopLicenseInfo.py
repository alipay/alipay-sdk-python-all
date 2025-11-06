#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopLicenseInfo(object):

    def __init__(self):
        self._expire_time = None
        self._license_name = None
        self._license_no = None
        self._license_pic = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def license_name(self):
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        self._license_name = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def license_pic(self):
        return self._license_pic

    @license_pic.setter
    def license_pic(self, value):
        self._license_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.license_name:
            if hasattr(self.license_name, 'to_alipay_dict'):
                params['license_name'] = self.license_name.to_alipay_dict()
            else:
                params['license_name'] = self.license_name
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.license_pic:
            if hasattr(self.license_pic, 'to_alipay_dict'):
                params['license_pic'] = self.license_pic.to_alipay_dict()
            else:
                params['license_pic'] = self.license_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopLicenseInfo()
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'license_name' in d:
            o.license_name = d['license_name']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'license_pic' in d:
            o.license_pic = d['license_pic']
        return o


