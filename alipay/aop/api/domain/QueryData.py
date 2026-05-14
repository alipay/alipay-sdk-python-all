#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryData(object):

    def __init__(self):
        self._fulfillment_id = None
        self._trade_order_id = None

    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, value):
        self._trade_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.trade_order_id:
            if hasattr(self.trade_order_id, 'to_alipay_dict'):
                params['trade_order_id'] = self.trade_order_id.to_alipay_dict()
            else:
                params['trade_order_id'] = self.trade_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryData()
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'trade_order_id' in d:
            o.trade_order_id = d['trade_order_id']
        return o


