#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundConstraints(object):

    def __init__(self):
        self._deduct_account_id = None
        self._fund_service_id = None
        self._specified_bank_card_no = None

    @property
    def deduct_account_id(self):
        return self._deduct_account_id

    @deduct_account_id.setter
    def deduct_account_id(self, value):
        self._deduct_account_id = value
    @property
    def fund_service_id(self):
        return self._fund_service_id

    @fund_service_id.setter
    def fund_service_id(self, value):
        self._fund_service_id = value
    @property
    def specified_bank_card_no(self):
        return self._specified_bank_card_no

    @specified_bank_card_no.setter
    def specified_bank_card_no(self, value):
        self._specified_bank_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_account_id:
            if hasattr(self.deduct_account_id, 'to_alipay_dict'):
                params['deduct_account_id'] = self.deduct_account_id.to_alipay_dict()
            else:
                params['deduct_account_id'] = self.deduct_account_id
        if self.fund_service_id:
            if hasattr(self.fund_service_id, 'to_alipay_dict'):
                params['fund_service_id'] = self.fund_service_id.to_alipay_dict()
            else:
                params['fund_service_id'] = self.fund_service_id
        if self.specified_bank_card_no:
            if hasattr(self.specified_bank_card_no, 'to_alipay_dict'):
                params['specified_bank_card_no'] = self.specified_bank_card_no.to_alipay_dict()
            else:
                params['specified_bank_card_no'] = self.specified_bank_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundConstraints()
        if 'deduct_account_id' in d:
            o.deduct_account_id = d['deduct_account_id']
        if 'fund_service_id' in d:
            o.fund_service_id = d['fund_service_id']
        if 'specified_bank_card_no' in d:
            o.specified_bank_card_no = d['specified_bank_card_no']
        return o


