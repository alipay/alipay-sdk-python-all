#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayRepayVO(object):

    def __init__(self):
        self._first_merge_day = None
        self._repay_day = None
        self._repay_desc = None
        self._repay_mode = None

    @property
    def first_merge_day(self):
        return self._first_merge_day

    @first_merge_day.setter
    def first_merge_day(self, value):
        self._first_merge_day = value
    @property
    def repay_day(self):
        return self._repay_day

    @repay_day.setter
    def repay_day(self, value):
        self._repay_day = value
    @property
    def repay_desc(self):
        return self._repay_desc

    @repay_desc.setter
    def repay_desc(self, value):
        self._repay_desc = value
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.first_merge_day:
            if hasattr(self.first_merge_day, 'to_alipay_dict'):
                params['first_merge_day'] = self.first_merge_day.to_alipay_dict()
            else:
                params['first_merge_day'] = self.first_merge_day
        if self.repay_day:
            if hasattr(self.repay_day, 'to_alipay_dict'):
                params['repay_day'] = self.repay_day.to_alipay_dict()
            else:
                params['repay_day'] = self.repay_day
        if self.repay_desc:
            if hasattr(self.repay_desc, 'to_alipay_dict'):
                params['repay_desc'] = self.repay_desc.to_alipay_dict()
            else:
                params['repay_desc'] = self.repay_desc
        if self.repay_mode:
            if hasattr(self.repay_mode, 'to_alipay_dict'):
                params['repay_mode'] = self.repay_mode.to_alipay_dict()
            else:
                params['repay_mode'] = self.repay_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayRepayVO()
        if 'first_merge_day' in d:
            o.first_merge_day = d['first_merge_day']
        if 'repay_day' in d:
            o.repay_day = d['repay_day']
        if 'repay_desc' in d:
            o.repay_desc = d['repay_desc']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        return o


