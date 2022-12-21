#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenFundComponentDetailDTO(object):

    def __init__(self):
        self._amount = None
        self._cash = None
        self._component_id = None
        self._component_type = None
        self._fund_account = None
        self._fund_sub_account = None
        self._fund_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value
    @property
    def component_id(self):
        return self._component_id

    @component_id.setter
    def component_id(self, value):
        self._component_id = value
    @property
    def component_type(self):
        return self._component_type

    @component_type.setter
    def component_type(self, value):
        self._component_type = value
    @property
    def fund_account(self):
        return self._fund_account

    @fund_account.setter
    def fund_account(self, value):
        self._fund_account = value
    @property
    def fund_sub_account(self):
        return self._fund_sub_account

    @fund_sub_account.setter
    def fund_sub_account(self, value):
        self._fund_sub_account = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.cash:
            if hasattr(self.cash, 'to_alipay_dict'):
                params['cash'] = self.cash.to_alipay_dict()
            else:
                params['cash'] = self.cash
        if self.component_id:
            if hasattr(self.component_id, 'to_alipay_dict'):
                params['component_id'] = self.component_id.to_alipay_dict()
            else:
                params['component_id'] = self.component_id
        if self.component_type:
            if hasattr(self.component_type, 'to_alipay_dict'):
                params['component_type'] = self.component_type.to_alipay_dict()
            else:
                params['component_type'] = self.component_type
        if self.fund_account:
            if hasattr(self.fund_account, 'to_alipay_dict'):
                params['fund_account'] = self.fund_account.to_alipay_dict()
            else:
                params['fund_account'] = self.fund_account
        if self.fund_sub_account:
            if hasattr(self.fund_sub_account, 'to_alipay_dict'):
                params['fund_sub_account'] = self.fund_sub_account.to_alipay_dict()
            else:
                params['fund_sub_account'] = self.fund_sub_account
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
        o = OpenFundComponentDetailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'cash' in d:
            o.cash = d['cash']
        if 'component_id' in d:
            o.component_id = d['component_id']
        if 'component_type' in d:
            o.component_type = d['component_type']
        if 'fund_account' in d:
            o.fund_account = d['fund_account']
        if 'fund_sub_account' in d:
            o.fund_sub_account = d['fund_sub_account']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        return o


