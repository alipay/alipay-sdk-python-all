#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecifiedChannelParam(object):

    def __init__(self):
        self._asset_id = None
        self._asset_type_code = None
        self._bank_card_type = None
        self._inst_id = None
        self._pay_tool_type = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def bank_card_type(self):
        return self._bank_card_type

    @bank_card_type.setter
    def bank_card_type(self, value):
        self._bank_card_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.bank_card_type:
            if hasattr(self.bank_card_type, 'to_alipay_dict'):
                params['bank_card_type'] = self.bank_card_type.to_alipay_dict()
            else:
                params['bank_card_type'] = self.bank_card_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecifiedChannelParam()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'bank_card_type' in d:
            o.bank_card_type = d['bank_card_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'pay_tool_type' in d:
            o.pay_tool_type = d['pay_tool_type']
        return o


