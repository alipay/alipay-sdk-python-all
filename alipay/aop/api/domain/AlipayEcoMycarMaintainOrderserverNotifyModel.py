#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMaintainOrderserverNotifyModel(object):

    def __init__(self):
        self._change_cost = None
        self._change_desc = None
        self._order_no = None

    @property
    def change_cost(self):
        return self._change_cost

    @change_cost.setter
    def change_cost(self, value):
        self._change_cost = value
    @property
    def change_desc(self):
        return self._change_desc

    @change_desc.setter
    def change_desc(self, value):
        self._change_desc = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_cost:
            if hasattr(self.change_cost, 'to_alipay_dict'):
                params['change_cost'] = self.change_cost.to_alipay_dict()
            else:
                params['change_cost'] = self.change_cost
        if self.change_desc:
            if hasattr(self.change_desc, 'to_alipay_dict'):
                params['change_desc'] = self.change_desc.to_alipay_dict()
            else:
                params['change_desc'] = self.change_desc
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
        o = AlipayEcoMycarMaintainOrderserverNotifyModel()
        if 'change_cost' in d:
            o.change_cost = d['change_cost']
        if 'change_desc' in d:
            o.change_desc = d['change_desc']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


