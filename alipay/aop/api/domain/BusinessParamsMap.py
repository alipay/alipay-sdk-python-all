#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessParamsMap(object):

    def __init__(self):
        self._change_time = None
        self._new_amount = None
        self._ori_amount = None

    @property
    def change_time(self):
        return self._change_time

    @change_time.setter
    def change_time(self, value):
        self._change_time = value
    @property
    def new_amount(self):
        return self._new_amount

    @new_amount.setter
    def new_amount(self, value):
        self._new_amount = value
    @property
    def ori_amount(self):
        return self._ori_amount

    @ori_amount.setter
    def ori_amount(self, value):
        self._ori_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_time:
            if hasattr(self.change_time, 'to_alipay_dict'):
                params['change_time'] = self.change_time.to_alipay_dict()
            else:
                params['change_time'] = self.change_time
        if self.new_amount:
            if hasattr(self.new_amount, 'to_alipay_dict'):
                params['new_amount'] = self.new_amount.to_alipay_dict()
            else:
                params['new_amount'] = self.new_amount
        if self.ori_amount:
            if hasattr(self.ori_amount, 'to_alipay_dict'):
                params['ori_amount'] = self.ori_amount.to_alipay_dict()
            else:
                params['ori_amount'] = self.ori_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessParamsMap()
        if 'change_time' in d:
            o.change_time = d['change_time']
        if 'new_amount' in d:
            o.new_amount = d['new_amount']
        if 'ori_amount' in d:
            o.ori_amount = d['ori_amount']
        return o


