#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderCreditModifyModel(object):

    def __init__(self):
        self._out_order_no = None
        self._overdue_time = None
        self._zm_order_no = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def overdue_time(self):
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, value):
        self._overdue_time = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.overdue_time:
            if hasattr(self.overdue_time, 'to_alipay_dict'):
                params['overdue_time'] = self.overdue_time.to_alipay_dict()
            else:
                params['overdue_time'] = self.overdue_time
        if self.zm_order_no:
            if hasattr(self.zm_order_no, 'to_alipay_dict'):
                params['zm_order_no'] = self.zm_order_no.to_alipay_dict()
            else:
                params['zm_order_no'] = self.zm_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderCreditModifyModel()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'overdue_time' in d:
            o.overdue_time = d['overdue_time']
        if 'zm_order_no' in d:
            o.zm_order_no = d['zm_order_no']
        return o


