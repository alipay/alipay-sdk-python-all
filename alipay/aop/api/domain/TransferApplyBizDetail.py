#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferApplyBizDetail(object):

    def __init__(self):
        self._amt = None
        self._penalty = None
        self._principal = None
        self._repay_type = None
        self._service_fee = None
        self._step_no = None
        self._trade_no = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        self._amt = value
    @property
    def penalty(self):
        return self._penalty

    @penalty.setter
    def penalty(self, value):
        self._penalty = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value
    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, value):
        self._service_fee = value
    @property
    def step_no(self):
        return self._step_no

    @step_no.setter
    def step_no(self, value):
        self._step_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.penalty:
            if hasattr(self.penalty, 'to_alipay_dict'):
                params['penalty'] = self.penalty.to_alipay_dict()
            else:
                params['penalty'] = self.penalty
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        if self.service_fee:
            if hasattr(self.service_fee, 'to_alipay_dict'):
                params['service_fee'] = self.service_fee.to_alipay_dict()
            else:
                params['service_fee'] = self.service_fee
        if self.step_no:
            if hasattr(self.step_no, 'to_alipay_dict'):
                params['step_no'] = self.step_no.to_alipay_dict()
            else:
                params['step_no'] = self.step_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferApplyBizDetail()
        if 'amt' in d:
            o.amt = d['amt']
        if 'penalty' in d:
            o.penalty = d['penalty']
        if 'principal' in d:
            o.principal = d['principal']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        if 'service_fee' in d:
            o.service_fee = d['service_fee']
        if 'step_no' in d:
            o.step_no = d['step_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


