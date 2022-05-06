#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeBusinessOperateQueryModel(object):

    def __init__(self):
        self._order_no = None
        self._request_no = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeBusinessOperateQueryModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


