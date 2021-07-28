#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CateringMerchantInfo(object):

    def __init__(self):
        self._brand_name = None
        self._merchant_logo = None
        self._pid = None
        self._smid = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateringMerchantInfo()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'pid' in d:
            o.pid = d['pid']
        if 'smid' in d:
            o.smid = d['smid']
        return o


