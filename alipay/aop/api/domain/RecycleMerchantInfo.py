#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleMerchantInfo(object):

    def __init__(self):
        self._merchant_logo_url = None
        self._merchant_name = None

    @property
    def merchant_logo_url(self):
        return self._merchant_logo_url

    @merchant_logo_url.setter
    def merchant_logo_url(self, value):
        self._merchant_logo_url = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_logo_url:
            if hasattr(self.merchant_logo_url, 'to_alipay_dict'):
                params['merchant_logo_url'] = self.merchant_logo_url.to_alipay_dict()
            else:
                params['merchant_logo_url'] = self.merchant_logo_url
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleMerchantInfo()
        if 'merchant_logo_url' in d:
            o.merchant_logo_url = d['merchant_logo_url']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        return o


