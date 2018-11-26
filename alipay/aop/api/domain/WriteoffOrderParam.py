#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WriteoffOrderParam(object):

    def __init__(self):
        self._is_clearance = None
        self._order_num = None
        self._sub_order_num = None

    @property
    def is_clearance(self):
        return self._is_clearance

    @is_clearance.setter
    def is_clearance(self, value):
        self._is_clearance = value
    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, value):
        self._order_num = value
    @property
    def sub_order_num(self):
        return self._sub_order_num

    @sub_order_num.setter
    def sub_order_num(self, value):
        self._sub_order_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_clearance:
            if hasattr(self.is_clearance, 'to_alipay_dict'):
                params['is_clearance'] = self.is_clearance.to_alipay_dict()
            else:
                params['is_clearance'] = self.is_clearance
        if self.order_num:
            if hasattr(self.order_num, 'to_alipay_dict'):
                params['order_num'] = self.order_num.to_alipay_dict()
            else:
                params['order_num'] = self.order_num
        if self.sub_order_num:
            if hasattr(self.sub_order_num, 'to_alipay_dict'):
                params['sub_order_num'] = self.sub_order_num.to_alipay_dict()
            else:
                params['sub_order_num'] = self.sub_order_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WriteoffOrderParam()
        if 'is_clearance' in d:
            o.is_clearance = d['is_clearance']
        if 'order_num' in d:
            o.order_num = d['order_num']
        if 'sub_order_num' in d:
            o.sub_order_num = d['sub_order_num']
        return o


