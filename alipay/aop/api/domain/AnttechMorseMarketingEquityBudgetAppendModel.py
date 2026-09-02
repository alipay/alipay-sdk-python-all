#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingEquityBudgetAppendModel(object):

    def __init__(self):
        self._append_amount = None
        self._equity_id = None
        self._request_id = None
        self._tenant_id = None

    @property
    def append_amount(self):
        return self._append_amount

    @append_amount.setter
    def append_amount(self, value):
        self._append_amount = value
    @property
    def equity_id(self):
        return self._equity_id

    @equity_id.setter
    def equity_id(self, value):
        self._equity_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.append_amount:
            if hasattr(self.append_amount, 'to_alipay_dict'):
                params['append_amount'] = self.append_amount.to_alipay_dict()
            else:
                params['append_amount'] = self.append_amount
        if self.equity_id:
            if hasattr(self.equity_id, 'to_alipay_dict'):
                params['equity_id'] = self.equity_id.to_alipay_dict()
            else:
                params['equity_id'] = self.equity_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingEquityBudgetAppendModel()
        if 'append_amount' in d:
            o.append_amount = d['append_amount']
        if 'equity_id' in d:
            o.equity_id = d['equity_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


