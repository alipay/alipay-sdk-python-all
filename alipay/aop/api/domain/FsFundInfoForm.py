#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FsFundInfoForm(object):

    def __init__(self):
        self._amount = None
        self._fund_provider = None
        self._fund_type = None
        self._fund_user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_provider(self):
        return self._fund_provider

    @fund_provider.setter
    def fund_provider(self, value):
        self._fund_provider = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def fund_user_id(self):
        return self._fund_user_id

    @fund_user_id.setter
    def fund_user_id(self, value):
        self._fund_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_provider:
            if hasattr(self.fund_provider, 'to_alipay_dict'):
                params['fund_provider'] = self.fund_provider.to_alipay_dict()
            else:
                params['fund_provider'] = self.fund_provider
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.fund_user_id:
            if hasattr(self.fund_user_id, 'to_alipay_dict'):
                params['fund_user_id'] = self.fund_user_id.to_alipay_dict()
            else:
                params['fund_user_id'] = self.fund_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FsFundInfoForm()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_provider' in d:
            o.fund_provider = d['fund_provider']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'fund_user_id' in d:
            o.fund_user_id = d['fund_user_id']
        return o


