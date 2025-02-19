#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationIotnspoperationDeliveryQueryModel(object):

    def __init__(self):
        self._merchant_access_mode = None
        self._n_delivery_id = None

    @property
    def merchant_access_mode(self):
        return self._merchant_access_mode

    @merchant_access_mode.setter
    def merchant_access_mode(self, value):
        self._merchant_access_mode = value
    @property
    def n_delivery_id(self):
        return self._n_delivery_id

    @n_delivery_id.setter
    def n_delivery_id(self, value):
        self._n_delivery_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_access_mode:
            if hasattr(self.merchant_access_mode, 'to_alipay_dict'):
                params['merchant_access_mode'] = self.merchant_access_mode.to_alipay_dict()
            else:
                params['merchant_access_mode'] = self.merchant_access_mode
        if self.n_delivery_id:
            if hasattr(self.n_delivery_id, 'to_alipay_dict'):
                params['n_delivery_id'] = self.n_delivery_id.to_alipay_dict()
            else:
                params['n_delivery_id'] = self.n_delivery_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationIotnspoperationDeliveryQueryModel()
        if 'merchant_access_mode' in d:
            o.merchant_access_mode = d['merchant_access_mode']
        if 'n_delivery_id' in d:
            o.n_delivery_id = d['n_delivery_id']
        return o


