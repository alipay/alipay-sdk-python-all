#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeOrderRefundQueryModel(object):

    def __init__(self):
        self._order_no = None
        self._out_refund_no = None
        self._request_id = None
        self._shop_id = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_refund_no:
            if hasattr(self.out_refund_no, 'to_alipay_dict'):
                params['out_refund_no'] = self.out_refund_no.to_alipay_dict()
            else:
                params['out_refund_no'] = self.out_refund_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeOrderRefundQueryModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_refund_no' in d:
            o.out_refund_no = d['out_refund_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


