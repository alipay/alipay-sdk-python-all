#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderConfirmModel(object):

    def __init__(self):
        self._order_no = None
        self._transaction_id = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderConfirmModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


