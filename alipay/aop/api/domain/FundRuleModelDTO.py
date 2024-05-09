#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundRuleModelDTO(object):

    def __init__(self):
        self._fund_agreement_no = None
        self._fund_amount = None
        self._fund_type = None

    @property
    def fund_agreement_no(self):
        return self._fund_agreement_no

    @fund_agreement_no.setter
    def fund_agreement_no(self, value):
        self._fund_agreement_no = value
    @property
    def fund_amount(self):
        return self._fund_amount

    @fund_amount.setter
    def fund_amount(self, value):
        self._fund_amount = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_agreement_no:
            if hasattr(self.fund_agreement_no, 'to_alipay_dict'):
                params['fund_agreement_no'] = self.fund_agreement_no.to_alipay_dict()
            else:
                params['fund_agreement_no'] = self.fund_agreement_no
        if self.fund_amount:
            if hasattr(self.fund_amount, 'to_alipay_dict'):
                params['fund_amount'] = self.fund_amount.to_alipay_dict()
            else:
                params['fund_amount'] = self.fund_amount
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundRuleModelDTO()
        if 'fund_agreement_no' in d:
            o.fund_agreement_no = d['fund_agreement_no']
        if 'fund_amount' in d:
            o.fund_amount = d['fund_amount']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        return o


