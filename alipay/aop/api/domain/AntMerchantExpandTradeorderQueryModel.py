#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandTradeorderQueryModel(object):

    def __init__(self):
        self._contain_item_order = None
        self._order_id = None

    @property
    def contain_item_order(self):
        return self._contain_item_order

    @contain_item_order.setter
    def contain_item_order(self, value):
        self._contain_item_order = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contain_item_order:
            if hasattr(self.contain_item_order, 'to_alipay_dict'):
                params['contain_item_order'] = self.contain_item_order.to_alipay_dict()
            else:
                params['contain_item_order'] = self.contain_item_order
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandTradeorderQueryModel()
        if 'contain_item_order' in d:
            o.contain_item_order = d['contain_item_order']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


