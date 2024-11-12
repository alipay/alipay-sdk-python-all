#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditIsvwithdrawApplyModel(object):

    def __init__(self):
        self._alipay_pay_no = None
        self._amount = None
        self._enterprise_code = None
        self._enterprise_id = None
        self._out_freeze_no = None
        self._service_fee = None

    @property
    def alipay_pay_no(self):
        return self._alipay_pay_no

    @alipay_pay_no.setter
    def alipay_pay_no(self, value):
        self._alipay_pay_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
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
    def out_freeze_no(self):
        return self._out_freeze_no

    @out_freeze_no.setter
    def out_freeze_no(self, value):
        self._out_freeze_no = value
    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, value):
        self._service_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pay_no:
            if hasattr(self.alipay_pay_no, 'to_alipay_dict'):
                params['alipay_pay_no'] = self.alipay_pay_no.to_alipay_dict()
            else:
                params['alipay_pay_no'] = self.alipay_pay_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
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
        if self.out_freeze_no:
            if hasattr(self.out_freeze_no, 'to_alipay_dict'):
                params['out_freeze_no'] = self.out_freeze_no.to_alipay_dict()
            else:
                params['out_freeze_no'] = self.out_freeze_no
        if self.service_fee:
            if hasattr(self.service_fee, 'to_alipay_dict'):
                params['service_fee'] = self.service_fee.to_alipay_dict()
            else:
                params['service_fee'] = self.service_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditIsvwithdrawApplyModel()
        if 'alipay_pay_no' in d:
            o.alipay_pay_no = d['alipay_pay_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'enterprise_code' in d:
            o.enterprise_code = d['enterprise_code']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'out_freeze_no' in d:
            o.out_freeze_no = d['out_freeze_no']
        if 'service_fee' in d:
            o.service_fee = d['service_fee']
        return o


