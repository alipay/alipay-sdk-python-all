#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentOrderQueryModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._order_id = None
        self._out_order_id = None
        self._query_options = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def query_options(self):
        return self._query_options

    @query_options.setter
    def query_options(self, value):
        if isinstance(value, list):
            self._query_options = list()
            for i in value:
                self._query_options.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.query_options:
            if isinstance(self.query_options, list):
                for i in range(0, len(self.query_options)):
                    element = self.query_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_options[i] = element.to_alipay_dict()
            if hasattr(self.query_options, 'to_alipay_dict'):
                params['query_options'] = self.query_options.to_alipay_dict()
            else:
                params['query_options'] = self.query_options
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderQueryModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'query_options' in d:
            o.query_options = d['query_options']
        return o


