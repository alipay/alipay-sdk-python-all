#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BelongMerchantInfoDTO(object):

    def __init__(self):
        self._business_type = None
        self._merchant_id = None
        self._merchant_open_id = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_open_id(self):
        return self._merchant_open_id

    @merchant_open_id.setter
    def merchant_open_id(self, value):
        self._merchant_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_open_id:
            if hasattr(self.merchant_open_id, 'to_alipay_dict'):
                params['merchant_open_id'] = self.merchant_open_id.to_alipay_dict()
            else:
                params['merchant_open_id'] = self.merchant_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BelongMerchantInfoDTO()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_open_id' in d:
            o.merchant_open_id = d['merchant_open_id']
        return o


