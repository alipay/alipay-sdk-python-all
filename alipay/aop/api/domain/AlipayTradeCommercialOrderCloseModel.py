#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCommercialOrderCloseModel(object):

    def __init__(self):
        self._close_reason = None
        self._order_no = None

    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCommercialOrderCloseModel()
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


