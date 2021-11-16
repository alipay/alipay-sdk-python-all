#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasSecondmerchantMaintainQuerystatusModel(object):

    def __init__(self):
        self._payment_method = None
        self._secondary_merchant_id = None
        self._store_id = None

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def secondary_merchant_id(self):
        return self._secondary_merchant_id

    @secondary_merchant_id.setter
    def secondary_merchant_id(self, value):
        self._secondary_merchant_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.secondary_merchant_id:
            if hasattr(self.secondary_merchant_id, 'to_alipay_dict'):
                params['secondary_merchant_id'] = self.secondary_merchant_id.to_alipay_dict()
            else:
                params['secondary_merchant_id'] = self.secondary_merchant_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasSecondmerchantMaintainQuerystatusModel()
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'secondary_merchant_id' in d:
            o.secondary_merchant_id = d['secondary_merchant_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


