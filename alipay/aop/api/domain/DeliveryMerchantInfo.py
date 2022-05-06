#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryMerchantInfo(object):

    def __init__(self):
        self._merchant_id = None
        self._merchant_id_type = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_id_type(self):
        return self._merchant_id_type

    @merchant_id_type.setter
    def merchant_id_type(self, value):
        self._merchant_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_id_type:
            if hasattr(self.merchant_id_type, 'to_alipay_dict'):
                params['merchant_id_type'] = self.merchant_id_type.to_alipay_dict()
            else:
                params['merchant_id_type'] = self.merchant_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryMerchantInfo()
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_id_type' in d:
            o.merchant_id_type = d['merchant_id_type']
        return o


