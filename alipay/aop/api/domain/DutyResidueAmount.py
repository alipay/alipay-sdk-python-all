#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DutyResidueAmount(object):

    def __init__(self):
        self._claim_duty_code = None
        self._claim_duty_name = None
        self._duty_deductible_excess = None
        self._duty_residue_amount = None

    @property
    def claim_duty_code(self):
        return self._claim_duty_code

    @claim_duty_code.setter
    def claim_duty_code(self, value):
        self._claim_duty_code = value
    @property
    def claim_duty_name(self):
        return self._claim_duty_name

    @claim_duty_name.setter
    def claim_duty_name(self, value):
        self._claim_duty_name = value
    @property
    def duty_deductible_excess(self):
        return self._duty_deductible_excess

    @duty_deductible_excess.setter
    def duty_deductible_excess(self, value):
        self._duty_deductible_excess = value
    @property
    def duty_residue_amount(self):
        return self._duty_residue_amount

    @duty_residue_amount.setter
    def duty_residue_amount(self, value):
        self._duty_residue_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_duty_code:
            if hasattr(self.claim_duty_code, 'to_alipay_dict'):
                params['claim_duty_code'] = self.claim_duty_code.to_alipay_dict()
            else:
                params['claim_duty_code'] = self.claim_duty_code
        if self.claim_duty_name:
            if hasattr(self.claim_duty_name, 'to_alipay_dict'):
                params['claim_duty_name'] = self.claim_duty_name.to_alipay_dict()
            else:
                params['claim_duty_name'] = self.claim_duty_name
        if self.duty_deductible_excess:
            if hasattr(self.duty_deductible_excess, 'to_alipay_dict'):
                params['duty_deductible_excess'] = self.duty_deductible_excess.to_alipay_dict()
            else:
                params['duty_deductible_excess'] = self.duty_deductible_excess
        if self.duty_residue_amount:
            if hasattr(self.duty_residue_amount, 'to_alipay_dict'):
                params['duty_residue_amount'] = self.duty_residue_amount.to_alipay_dict()
            else:
                params['duty_residue_amount'] = self.duty_residue_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DutyResidueAmount()
        if 'claim_duty_code' in d:
            o.claim_duty_code = d['claim_duty_code']
        if 'claim_duty_name' in d:
            o.claim_duty_name = d['claim_duty_name']
        if 'duty_deductible_excess' in d:
            o.duty_deductible_excess = d['duty_deductible_excess']
        if 'duty_residue_amount' in d:
            o.duty_residue_amount = d['duty_residue_amount']
        return o


