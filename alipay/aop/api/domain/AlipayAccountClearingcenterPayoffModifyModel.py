#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountClearingcenterPayoffModifyModel(object):

    def __init__(self):
        self._is_high_priority = None
        self._pay_off_no = None

    @property
    def is_high_priority(self):
        return self._is_high_priority

    @is_high_priority.setter
    def is_high_priority(self, value):
        self._is_high_priority = value
    @property
    def pay_off_no(self):
        return self._pay_off_no

    @pay_off_no.setter
    def pay_off_no(self, value):
        self._pay_off_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_high_priority:
            if hasattr(self.is_high_priority, 'to_alipay_dict'):
                params['is_high_priority'] = self.is_high_priority.to_alipay_dict()
            else:
                params['is_high_priority'] = self.is_high_priority
        if self.pay_off_no:
            if hasattr(self.pay_off_no, 'to_alipay_dict'):
                params['pay_off_no'] = self.pay_off_no.to_alipay_dict()
            else:
                params['pay_off_no'] = self.pay_off_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountClearingcenterPayoffModifyModel()
        if 'is_high_priority' in d:
            o.is_high_priority = d['is_high_priority']
        if 'pay_off_no' in d:
            o.pay_off_no = d['pay_off_no']
        return o


