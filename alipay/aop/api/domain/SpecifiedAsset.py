#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecifiedAsset(object):

    def __init__(self):
        self._bank_card_no = None
        self._inst_id = None
        self._pay_tool_type = None
        self._specified_reason_code = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def pay_tool_type(self):
        return self._pay_tool_type

    @pay_tool_type.setter
    def pay_tool_type(self, value):
        self._pay_tool_type = value
    @property
    def specified_reason_code(self):
        return self._specified_reason_code

    @specified_reason_code.setter
    def specified_reason_code(self, value):
        self._specified_reason_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.pay_tool_type:
            if hasattr(self.pay_tool_type, 'to_alipay_dict'):
                params['pay_tool_type'] = self.pay_tool_type.to_alipay_dict()
            else:
                params['pay_tool_type'] = self.pay_tool_type
        if self.specified_reason_code:
            if hasattr(self.specified_reason_code, 'to_alipay_dict'):
                params['specified_reason_code'] = self.specified_reason_code.to_alipay_dict()
            else:
                params['specified_reason_code'] = self.specified_reason_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecifiedAsset()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'pay_tool_type' in d:
            o.pay_tool_type = d['pay_tool_type']
        if 'specified_reason_code' in d:
            o.specified_reason_code = d['specified_reason_code']
        return o


