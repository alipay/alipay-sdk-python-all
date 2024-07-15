#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallOrderConfirmModel(object):

    def __init__(self):
        self._order_id = None
        self._purchase_order_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, value):
        self._purchase_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.purchase_order_id:
            if hasattr(self.purchase_order_id, 'to_alipay_dict'):
                params['purchase_order_id'] = self.purchase_order_id.to_alipay_dict()
            else:
                params['purchase_order_id'] = self.purchase_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallOrderConfirmModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'purchase_order_id' in d:
            o.purchase_order_id = d['purchase_order_id']
        return o


