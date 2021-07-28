#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BeikeAccountResponse(object):

    def __init__(self):
        self._change_amount = None
        self._current_amount = None
        self._outer_biz_no = None

    @property
    def change_amount(self):
        return self._change_amount

    @change_amount.setter
    def change_amount(self, value):
        self._change_amount = value
    @property
    def current_amount(self):
        return self._current_amount

    @current_amount.setter
    def current_amount(self, value):
        self._current_amount = value
    @property
    def outer_biz_no(self):
        return self._outer_biz_no

    @outer_biz_no.setter
    def outer_biz_no(self, value):
        self._outer_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_amount:
            if hasattr(self.change_amount, 'to_alipay_dict'):
                params['change_amount'] = self.change_amount.to_alipay_dict()
            else:
                params['change_amount'] = self.change_amount
        if self.current_amount:
            if hasattr(self.current_amount, 'to_alipay_dict'):
                params['current_amount'] = self.current_amount.to_alipay_dict()
            else:
                params['current_amount'] = self.current_amount
        if self.outer_biz_no:
            if hasattr(self.outer_biz_no, 'to_alipay_dict'):
                params['outer_biz_no'] = self.outer_biz_no.to_alipay_dict()
            else:
                params['outer_biz_no'] = self.outer_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BeikeAccountResponse()
        if 'change_amount' in d:
            o.change_amount = d['change_amount']
        if 'current_amount' in d:
            o.current_amount = d['current_amount']
        if 'outer_biz_no' in d:
            o.outer_biz_no = d['outer_biz_no']
        return o


