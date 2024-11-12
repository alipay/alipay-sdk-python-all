#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditIsvcapitalFreezeModel(object):

    def __init__(self):
        self._enterprise_code = None
        self._enterprise_id = None
        self._freeze_amount = None
        self._out_freeze_no = None

    @property
    def enterprise_code(self):
        return self._enterprise_code

    @enterprise_code.setter
    def enterprise_code(self, value):
        self._enterprise_code = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def out_freeze_no(self):
        return self._out_freeze_no

    @out_freeze_no.setter
    def out_freeze_no(self, value):
        self._out_freeze_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_code:
            if hasattr(self.enterprise_code, 'to_alipay_dict'):
                params['enterprise_code'] = self.enterprise_code.to_alipay_dict()
            else:
                params['enterprise_code'] = self.enterprise_code
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.out_freeze_no:
            if hasattr(self.out_freeze_no, 'to_alipay_dict'):
                params['out_freeze_no'] = self.out_freeze_no.to_alipay_dict()
            else:
                params['out_freeze_no'] = self.out_freeze_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditIsvcapitalFreezeModel()
        if 'enterprise_code' in d:
            o.enterprise_code = d['enterprise_code']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'out_freeze_no' in d:
            o.out_freeze_no = d['out_freeze_no']
        return o


