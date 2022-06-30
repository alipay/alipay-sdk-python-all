#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayerPaymentDTO(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._inst_name = None
        self._pay_tool_type = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def pay_tool_type(self):
        return self._pay_tool_type

    @pay_tool_type.setter
    def pay_tool_type(self, value):
        self._pay_tool_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.pay_tool_type:
            if hasattr(self.pay_tool_type, 'to_alipay_dict'):
                params['pay_tool_type'] = self.pay_tool_type.to_alipay_dict()
            else:
                params['pay_tool_type'] = self.pay_tool_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayerPaymentDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'pay_tool_type' in d:
            o.pay_tool_type = d['pay_tool_type']
        return o


