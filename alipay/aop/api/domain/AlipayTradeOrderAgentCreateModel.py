#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeOrderAgentCreateModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._order_create_content = None
        self._order_create_type = None

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
    def order_create_content(self):
        return self._order_create_content

    @order_create_content.setter
    def order_create_content(self, value):
        self._order_create_content = value
    @property
    def order_create_type(self):
        return self._order_create_type

    @order_create_type.setter
    def order_create_type(self, value):
        self._order_create_type = value


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
        if self.order_create_content:
            if hasattr(self.order_create_content, 'to_alipay_dict'):
                params['order_create_content'] = self.order_create_content.to_alipay_dict()
            else:
                params['order_create_content'] = self.order_create_content
        if self.order_create_type:
            if hasattr(self.order_create_type, 'to_alipay_dict'):
                params['order_create_type'] = self.order_create_type.to_alipay_dict()
            else:
                params['order_create_type'] = self.order_create_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeOrderAgentCreateModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'order_create_content' in d:
            o.order_create_content = d['order_create_content']
        if 'order_create_type' in d:
            o.order_create_type = d['order_create_type']
        return o


