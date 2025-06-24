#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CounterpartyInfo(object):

    def __init__(self):
        self._counter_amount_range = None
        self._counter_count_range = None
        self._counter_org_name = None
        self._counter_reg_no = None
        self._counter_uscc = None
        self._transfer_direction = None

    @property
    def counter_amount_range(self):
        return self._counter_amount_range

    @counter_amount_range.setter
    def counter_amount_range(self, value):
        self._counter_amount_range = value
    @property
    def counter_count_range(self):
        return self._counter_count_range

    @counter_count_range.setter
    def counter_count_range(self, value):
        self._counter_count_range = value
    @property
    def counter_org_name(self):
        return self._counter_org_name

    @counter_org_name.setter
    def counter_org_name(self, value):
        self._counter_org_name = value
    @property
    def counter_reg_no(self):
        return self._counter_reg_no

    @counter_reg_no.setter
    def counter_reg_no(self, value):
        self._counter_reg_no = value
    @property
    def counter_uscc(self):
        return self._counter_uscc

    @counter_uscc.setter
    def counter_uscc(self, value):
        self._counter_uscc = value
    @property
    def transfer_direction(self):
        return self._transfer_direction

    @transfer_direction.setter
    def transfer_direction(self, value):
        self._transfer_direction = value


    def to_alipay_dict(self):
        params = dict()
        if self.counter_amount_range:
            if hasattr(self.counter_amount_range, 'to_alipay_dict'):
                params['counter_amount_range'] = self.counter_amount_range.to_alipay_dict()
            else:
                params['counter_amount_range'] = self.counter_amount_range
        if self.counter_count_range:
            if hasattr(self.counter_count_range, 'to_alipay_dict'):
                params['counter_count_range'] = self.counter_count_range.to_alipay_dict()
            else:
                params['counter_count_range'] = self.counter_count_range
        if self.counter_org_name:
            if hasattr(self.counter_org_name, 'to_alipay_dict'):
                params['counter_org_name'] = self.counter_org_name.to_alipay_dict()
            else:
                params['counter_org_name'] = self.counter_org_name
        if self.counter_reg_no:
            if hasattr(self.counter_reg_no, 'to_alipay_dict'):
                params['counter_reg_no'] = self.counter_reg_no.to_alipay_dict()
            else:
                params['counter_reg_no'] = self.counter_reg_no
        if self.counter_uscc:
            if hasattr(self.counter_uscc, 'to_alipay_dict'):
                params['counter_uscc'] = self.counter_uscc.to_alipay_dict()
            else:
                params['counter_uscc'] = self.counter_uscc
        if self.transfer_direction:
            if hasattr(self.transfer_direction, 'to_alipay_dict'):
                params['transfer_direction'] = self.transfer_direction.to_alipay_dict()
            else:
                params['transfer_direction'] = self.transfer_direction
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CounterpartyInfo()
        if 'counter_amount_range' in d:
            o.counter_amount_range = d['counter_amount_range']
        if 'counter_count_range' in d:
            o.counter_count_range = d['counter_count_range']
        if 'counter_org_name' in d:
            o.counter_org_name = d['counter_org_name']
        if 'counter_reg_no' in d:
            o.counter_reg_no = d['counter_reg_no']
        if 'counter_uscc' in d:
            o.counter_uscc = d['counter_uscc']
        if 'transfer_direction' in d:
            o.transfer_direction = d['transfer_direction']
        return o


