#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceTparecoverySyncModel(object):

    def __init__(self):
        self._balance_recovery_amount = None
        self._balance_recovery_required = None
        self._claim_no = None
        self._company_type = None
        self._open_id = None
        self._tpa_id = None
        self._user_id = None

    @property
    def balance_recovery_amount(self):
        return self._balance_recovery_amount

    @balance_recovery_amount.setter
    def balance_recovery_amount(self, value):
        self._balance_recovery_amount = value
    @property
    def balance_recovery_required(self):
        return self._balance_recovery_required

    @balance_recovery_required.setter
    def balance_recovery_required(self, value):
        self._balance_recovery_required = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance_recovery_amount:
            if hasattr(self.balance_recovery_amount, 'to_alipay_dict'):
                params['balance_recovery_amount'] = self.balance_recovery_amount.to_alipay_dict()
            else:
                params['balance_recovery_amount'] = self.balance_recovery_amount
        if self.balance_recovery_required:
            if hasattr(self.balance_recovery_required, 'to_alipay_dict'):
                params['balance_recovery_required'] = self.balance_recovery_required.to_alipay_dict()
            else:
                params['balance_recovery_required'] = self.balance_recovery_required
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTparecoverySyncModel()
        if 'balance_recovery_amount' in d:
            o.balance_recovery_amount = d['balance_recovery_amount']
        if 'balance_recovery_required' in d:
            o.balance_recovery_required = d['balance_recovery_required']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


