#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoParam(object):

    def __init__(self):
        self._actual_order_time = None

    @property
    def actual_order_time(self):
        return self._actual_order_time

    @actual_order_time.setter
    def actual_order_time(self, value):
        self._actual_order_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_order_time:
            if hasattr(self.actual_order_time, 'to_alipay_dict'):
                params['actual_order_time'] = self.actual_order_time.to_alipay_dict()
            else:
                params['actual_order_time'] = self.actual_order_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoParam()
        if 'actual_order_time' in d:
            o.actual_order_time = d['actual_order_time']
        return o


