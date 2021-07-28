#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity


class AlipayBusinessPaymenthubQueryModel(object):

    def __init__(self):
        self._instruction_id = None
        self._instruction_type = None
        self._merchant_order_no = None
        self._out_request_no = None
        self._pay_request_no = None
        self._payer = None

    @property
    def instruction_id(self):
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, value):
        self._instruction_id = value
    @property
    def instruction_type(self):
        return self._instruction_type

    @instruction_type.setter
    def instruction_type(self, value):
        self._instruction_type = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_request_no(self):
        return self._pay_request_no

    @pay_request_no.setter
    def pay_request_no(self, value):
        self._pay_request_no = value
    @property
    def payer(self):
        return self._payer

    @payer.setter
    def payer(self, value):
        if isinstance(value, UserIdentity):
            self._payer = value
        else:
            self._payer = UserIdentity.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.instruction_id:
            if hasattr(self.instruction_id, 'to_alipay_dict'):
                params['instruction_id'] = self.instruction_id.to_alipay_dict()
            else:
                params['instruction_id'] = self.instruction_id
        if self.instruction_type:
            if hasattr(self.instruction_type, 'to_alipay_dict'):
                params['instruction_type'] = self.instruction_type.to_alipay_dict()
            else:
                params['instruction_type'] = self.instruction_type
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_request_no:
            if hasattr(self.pay_request_no, 'to_alipay_dict'):
                params['pay_request_no'] = self.pay_request_no.to_alipay_dict()
            else:
                params['pay_request_no'] = self.pay_request_no
        if self.payer:
            if hasattr(self.payer, 'to_alipay_dict'):
                params['payer'] = self.payer.to_alipay_dict()
            else:
                params['payer'] = self.payer
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessPaymenthubQueryModel()
        if 'instruction_id' in d:
            o.instruction_id = d['instruction_id']
        if 'instruction_type' in d:
            o.instruction_type = d['instruction_type']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_request_no' in d:
            o.pay_request_no = d['pay_request_no']
        if 'payer' in d:
            o.payer = d['payer']
        return o


