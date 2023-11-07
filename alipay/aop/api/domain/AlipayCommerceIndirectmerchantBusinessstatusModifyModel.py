#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIndirectmerchantBusinessstatusModifyModel(object):

    def __init__(self):
        self._business_status = None
        self._merchant_pid = None

    @property
    def business_status(self):
        return self._business_status

    @business_status.setter
    def business_status(self, value):
        self._business_status = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_status:
            if hasattr(self.business_status, 'to_alipay_dict'):
                params['business_status'] = self.business_status.to_alipay_dict()
            else:
                params['business_status'] = self.business_status
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
        o = AlipayCommerceIndirectmerchantBusinessstatusModifyModel()
        if 'business_status' in d:
            o.business_status = d['business_status']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        return o


