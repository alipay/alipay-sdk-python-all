#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DutyResidueAmount(object):

    def __init__(self):
        self._benefit_detail = None
        self._claim_count = None
        self._claim_duty_code = None
        self._claim_duty_name = None
        self._duty_deductible_excess = None
        self._duty_init_amount = None
        self._duty_residue_amount = None
        self._ext_info = None
        self._parent_claim_duty_code = None
        self._remark = None
        self._remark_en = None
        self._waiting_period = None

    @property
    def benefit_detail(self):
        return self._benefit_detail

    @benefit_detail.setter
    def benefit_detail(self, value):
        self._benefit_detail = value
    @property
    def claim_count(self):
        return self._claim_count

    @claim_count.setter
    def claim_count(self, value):
        self._claim_count = value
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
    def duty_init_amount(self):
        return self._duty_init_amount

    @duty_init_amount.setter
    def duty_init_amount(self, value):
        self._duty_init_amount = value
    @property
    def duty_residue_amount(self):
        return self._duty_residue_amount

    @duty_residue_amount.setter
    def duty_residue_amount(self, value):
        self._duty_residue_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def parent_claim_duty_code(self):
        return self._parent_claim_duty_code

    @parent_claim_duty_code.setter
    def parent_claim_duty_code(self, value):
        self._parent_claim_duty_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def remark_en(self):
        return self._remark_en

    @remark_en.setter
    def remark_en(self, value):
        self._remark_en = value
    @property
    def waiting_period(self):
        return self._waiting_period

    @waiting_period.setter
    def waiting_period(self, value):
        self._waiting_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_detail:
            if hasattr(self.benefit_detail, 'to_alipay_dict'):
                params['benefit_detail'] = self.benefit_detail.to_alipay_dict()
            else:
                params['benefit_detail'] = self.benefit_detail
        if self.claim_count:
            if hasattr(self.claim_count, 'to_alipay_dict'):
                params['claim_count'] = self.claim_count.to_alipay_dict()
            else:
                params['claim_count'] = self.claim_count
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
        if self.duty_init_amount:
            if hasattr(self.duty_init_amount, 'to_alipay_dict'):
                params['duty_init_amount'] = self.duty_init_amount.to_alipay_dict()
            else:
                params['duty_init_amount'] = self.duty_init_amount
        if self.duty_residue_amount:
            if hasattr(self.duty_residue_amount, 'to_alipay_dict'):
                params['duty_residue_amount'] = self.duty_residue_amount.to_alipay_dict()
            else:
                params['duty_residue_amount'] = self.duty_residue_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.parent_claim_duty_code:
            if hasattr(self.parent_claim_duty_code, 'to_alipay_dict'):
                params['parent_claim_duty_code'] = self.parent_claim_duty_code.to_alipay_dict()
            else:
                params['parent_claim_duty_code'] = self.parent_claim_duty_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.remark_en:
            if hasattr(self.remark_en, 'to_alipay_dict'):
                params['remark_en'] = self.remark_en.to_alipay_dict()
            else:
                params['remark_en'] = self.remark_en
        if self.waiting_period:
            if hasattr(self.waiting_period, 'to_alipay_dict'):
                params['waiting_period'] = self.waiting_period.to_alipay_dict()
            else:
                params['waiting_period'] = self.waiting_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DutyResidueAmount()
        if 'benefit_detail' in d:
            o.benefit_detail = d['benefit_detail']
        if 'claim_count' in d:
            o.claim_count = d['claim_count']
        if 'claim_duty_code' in d:
            o.claim_duty_code = d['claim_duty_code']
        if 'claim_duty_name' in d:
            o.claim_duty_name = d['claim_duty_name']
        if 'duty_deductible_excess' in d:
            o.duty_deductible_excess = d['duty_deductible_excess']
        if 'duty_init_amount' in d:
            o.duty_init_amount = d['duty_init_amount']
        if 'duty_residue_amount' in d:
            o.duty_residue_amount = d['duty_residue_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'parent_claim_duty_code' in d:
            o.parent_claim_duty_code = d['parent_claim_duty_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'remark_en' in d:
            o.remark_en = d['remark_en']
        if 'waiting_period' in d:
            o.waiting_period = d['waiting_period']
        return o


