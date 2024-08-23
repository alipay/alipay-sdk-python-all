#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantApplyItemInfo(object):

    def __init__(self):
        self._apply_order_id = None
        self._id = None
        self._merchant_id = None
        self._result = None
        self._type = None

    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantApplyItemInfo()
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'id' in d:
            o.id = d['id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'result' in d:
            o.result = d['result']
        if 'type' in d:
            o.type = d['type']
        return o


