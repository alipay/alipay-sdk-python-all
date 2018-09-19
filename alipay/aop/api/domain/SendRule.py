#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SendRule(object):

    def __init__(self):
        self._allow_repeat_send = None
        self._min_cost = None
        self._send_budget = None
        self._send_num = None

    @property
    def allow_repeat_send(self):
        return self._allow_repeat_send

    @allow_repeat_send.setter
    def allow_repeat_send(self, value):
        self._allow_repeat_send = value
    @property
    def min_cost(self):
        return self._min_cost

    @min_cost.setter
    def min_cost(self, value):
        self._min_cost = value
    @property
    def send_budget(self):
        return self._send_budget

    @send_budget.setter
    def send_budget(self, value):
        self._send_budget = value
    @property
    def send_num(self):
        return self._send_num

    @send_num.setter
    def send_num(self, value):
        self._send_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_repeat_send:
            if hasattr(self.allow_repeat_send, 'to_alipay_dict'):
                params['allow_repeat_send'] = self.allow_repeat_send.to_alipay_dict()
            else:
                params['allow_repeat_send'] = self.allow_repeat_send
        if self.min_cost:
            if hasattr(self.min_cost, 'to_alipay_dict'):
                params['min_cost'] = self.min_cost.to_alipay_dict()
            else:
                params['min_cost'] = self.min_cost
        if self.send_budget:
            if hasattr(self.send_budget, 'to_alipay_dict'):
                params['send_budget'] = self.send_budget.to_alipay_dict()
            else:
                params['send_budget'] = self.send_budget
        if self.send_num:
            if hasattr(self.send_num, 'to_alipay_dict'):
                params['send_num'] = self.send_num.to_alipay_dict()
            else:
                params['send_num'] = self.send_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SendRule()
        if 'allow_repeat_send' in d:
            o.allow_repeat_send = d['allow_repeat_send']
        if 'min_cost' in d:
            o.min_cost = d['min_cost']
        if 'send_budget' in d:
            o.send_budget = d['send_budget']
        if 'send_num' in d:
            o.send_num = d['send_num']
        return o


