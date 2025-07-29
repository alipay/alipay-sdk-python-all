#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleStdOrderMerchantInfoVO(object):

    def __init__(self):
        self._merchant_logo = None
        self._merchant_name = None
        self._merchant_phone = None

    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_phone(self):
        return self._merchant_phone

    @merchant_phone.setter
    def merchant_phone(self, value):
        self._merchant_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_phone:
            if hasattr(self.merchant_phone, 'to_alipay_dict'):
                params['merchant_phone'] = self.merchant_phone.to_alipay_dict()
            else:
                params['merchant_phone'] = self.merchant_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleStdOrderMerchantInfoVO()
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_phone' in d:
            o.merchant_phone = d['merchant_phone']
        return o


