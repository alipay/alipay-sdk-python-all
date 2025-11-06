#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPayEntryDTO(object):

    def __init__(self):
        self._fee = None
        self._in_account_no = None
        self._in_account_type = None
        self._out_account_no = None
        self._out_account_type = None
        self._pay_flow_id = None
        self._pay_time = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def in_account_no(self):
        return self._in_account_no

    @in_account_no.setter
    def in_account_no(self, value):
        self._in_account_no = value
    @property
    def in_account_type(self):
        return self._in_account_type

    @in_account_type.setter
    def in_account_type(self, value):
        self._in_account_type = value
    @property
    def out_account_no(self):
        return self._out_account_no

    @out_account_no.setter
    def out_account_no(self, value):
        self._out_account_no = value
    @property
    def out_account_type(self):
        return self._out_account_type

    @out_account_type.setter
    def out_account_type(self, value):
        self._out_account_type = value
    @property
    def pay_flow_id(self):
        return self._pay_flow_id

    @pay_flow_id.setter
    def pay_flow_id(self, value):
        self._pay_flow_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.in_account_no:
            if hasattr(self.in_account_no, 'to_alipay_dict'):
                params['in_account_no'] = self.in_account_no.to_alipay_dict()
            else:
                params['in_account_no'] = self.in_account_no
        if self.in_account_type:
            if hasattr(self.in_account_type, 'to_alipay_dict'):
                params['in_account_type'] = self.in_account_type.to_alipay_dict()
            else:
                params['in_account_type'] = self.in_account_type
        if self.out_account_no:
            if hasattr(self.out_account_no, 'to_alipay_dict'):
                params['out_account_no'] = self.out_account_no.to_alipay_dict()
            else:
                params['out_account_no'] = self.out_account_no
        if self.out_account_type:
            if hasattr(self.out_account_type, 'to_alipay_dict'):
                params['out_account_type'] = self.out_account_type.to_alipay_dict()
            else:
                params['out_account_type'] = self.out_account_type
        if self.pay_flow_id:
            if hasattr(self.pay_flow_id, 'to_alipay_dict'):
                params['pay_flow_id'] = self.pay_flow_id.to_alipay_dict()
            else:
                params['pay_flow_id'] = self.pay_flow_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPayEntryDTO()
        if 'fee' in d:
            o.fee = d['fee']
        if 'in_account_no' in d:
            o.in_account_no = d['in_account_no']
        if 'in_account_type' in d:
            o.in_account_type = d['in_account_type']
        if 'out_account_no' in d:
            o.out_account_no = d['out_account_no']
        if 'out_account_type' in d:
            o.out_account_type = d['out_account_type']
        if 'pay_flow_id' in d:
            o.pay_flow_id = d['pay_flow_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        return o


