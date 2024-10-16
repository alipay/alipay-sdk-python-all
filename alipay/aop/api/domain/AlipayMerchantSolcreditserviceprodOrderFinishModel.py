#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolcreditserviceprodOrderFinishModel(object):

    def __init__(self):
        self._end_mode = None
        self._order_no = None

    @property
    def end_mode(self):
        return self._end_mode

    @end_mode.setter
    def end_mode(self, value):
        self._end_mode = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_mode:
            if hasattr(self.end_mode, 'to_alipay_dict'):
                params['end_mode'] = self.end_mode.to_alipay_dict()
            else:
                params['end_mode'] = self.end_mode
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
        o = AlipayMerchantSolcreditserviceprodOrderFinishModel()
        if 'end_mode' in d:
            o.end_mode = d['end_mode']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


