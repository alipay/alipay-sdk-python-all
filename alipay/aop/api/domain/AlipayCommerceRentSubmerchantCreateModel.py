#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentSubmerchantCreateModel(object):

    def __init__(self):
        self._merchant_name = None
        self._merchant_uscc = None
        self._sub_merchant_id = None

    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_uscc(self):
        return self._merchant_uscc

    @merchant_uscc.setter
    def merchant_uscc(self, value):
        self._merchant_uscc = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_uscc:
            if hasattr(self.merchant_uscc, 'to_alipay_dict'):
                params['merchant_uscc'] = self.merchant_uscc.to_alipay_dict()
            else:
                params['merchant_uscc'] = self.merchant_uscc
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentSubmerchantCreateModel()
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_uscc' in d:
            o.merchant_uscc = d['merchant_uscc']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        return o


