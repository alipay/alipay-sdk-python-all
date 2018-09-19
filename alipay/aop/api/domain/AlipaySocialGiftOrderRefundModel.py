#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialGiftOrderRefundModel(object):

    def __init__(self):
        self._mid = None
        self._order_id = None
        self._refund_price = None
        self._refund_type = None

    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def refund_price(self):
        return self._refund_price

    @refund_price.setter
    def refund_price(self, value):
        self._refund_price = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.refund_price:
            if hasattr(self.refund_price, 'to_alipay_dict'):
                params['refund_price'] = self.refund_price.to_alipay_dict()
            else:
                params['refund_price'] = self.refund_price
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialGiftOrderRefundModel()
        if 'mid' in d:
            o.mid = d['mid']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'refund_price' in d:
            o.refund_price = d['refund_price']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        return o


