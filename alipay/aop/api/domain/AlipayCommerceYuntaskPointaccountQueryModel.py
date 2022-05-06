#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskPointaccountQueryModel(object):

    def __init__(self):
        self._hunter_id = None
        self._merchant_pid = None

    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
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
        o = AlipayCommerceYuntaskPointaccountQueryModel()
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        return o


