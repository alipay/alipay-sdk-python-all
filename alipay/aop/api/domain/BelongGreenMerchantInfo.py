#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BelongGreenMerchantInfo(object):

    def __init__(self):
        self._business_type = None
        self._merchant_pid = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BelongGreenMerchantInfo()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        return o


