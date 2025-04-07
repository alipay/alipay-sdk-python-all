#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinStatusNotifyOther(object):

    def __init__(self):
        self._approve_not_submit_code = None
        self._approve_not_submit_msg = None
        self._pay_method = None

    @property
    def approve_not_submit_code(self):
        return self._approve_not_submit_code

    @approve_not_submit_code.setter
    def approve_not_submit_code(self, value):
        self._approve_not_submit_code = value
    @property
    def approve_not_submit_msg(self):
        return self._approve_not_submit_msg

    @approve_not_submit_msg.setter
    def approve_not_submit_msg(self, value):
        self._approve_not_submit_msg = value
    @property
    def pay_method(self):
        return self._pay_method

    @pay_method.setter
    def pay_method(self, value):
        self._pay_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.approve_not_submit_code:
            if hasattr(self.approve_not_submit_code, 'to_alipay_dict'):
                params['approve_not_submit_code'] = self.approve_not_submit_code.to_alipay_dict()
            else:
                params['approve_not_submit_code'] = self.approve_not_submit_code
        if self.approve_not_submit_msg:
            if hasattr(self.approve_not_submit_msg, 'to_alipay_dict'):
                params['approve_not_submit_msg'] = self.approve_not_submit_msg.to_alipay_dict()
            else:
                params['approve_not_submit_msg'] = self.approve_not_submit_msg
        if self.pay_method:
            if hasattr(self.pay_method, 'to_alipay_dict'):
                params['pay_method'] = self.pay_method.to_alipay_dict()
            else:
                params['pay_method'] = self.pay_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinStatusNotifyOther()
        if 'approve_not_submit_code' in d:
            o.approve_not_submit_code = d['approve_not_submit_code']
        if 'approve_not_submit_msg' in d:
            o.approve_not_submit_msg = d['approve_not_submit_msg']
        if 'pay_method' in d:
            o.pay_method = d['pay_method']
        return o


