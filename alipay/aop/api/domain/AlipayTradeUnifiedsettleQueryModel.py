#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeUnifiedsettleQueryModel(object):

    def __init__(self):
        self._order_id = None
        self._order_sync_id = None
        self._out_request_no = None
        self._out_trade_no = None
        self._product_code = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_sync_id(self):
        return self._order_sync_id

    @order_sync_id.setter
    def order_sync_id(self, value):
        self._order_sync_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_sync_id:
            if hasattr(self.order_sync_id, 'to_alipay_dict'):
                params['order_sync_id'] = self.order_sync_id.to_alipay_dict()
            else:
                params['order_sync_id'] = self.order_sync_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeUnifiedsettleQueryModel()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_sync_id' in d:
            o.order_sync_id = d['order_sync_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


