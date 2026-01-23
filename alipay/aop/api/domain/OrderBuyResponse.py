#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayInfoResponse import PayInfoResponse


class OrderBuyResponse(object):

    def __init__(self):
        self._order_id = None
        self._out_order_id = None
        self._pay_info_response = None

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
    def pay_info_response(self):
        return self._pay_info_response

    @pay_info_response.setter
    def pay_info_response(self, value):
        if isinstance(value, PayInfoResponse):
            self._pay_info_response = value
        else:
            self._pay_info_response = PayInfoResponse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        if self.pay_info_response:
            if hasattr(self.pay_info_response, 'to_alipay_dict'):
                params['pay_info_response'] = self.pay_info_response.to_alipay_dict()
            else:
                params['pay_info_response'] = self.pay_info_response
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderBuyResponse()
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'pay_info_response' in d:
            o.pay_info_response = d['pay_info_response']
        return o


