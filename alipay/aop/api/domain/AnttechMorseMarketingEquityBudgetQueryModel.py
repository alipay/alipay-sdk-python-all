#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingEquityBudgetQueryModel(object):

    def __init__(self):
        self._equity_id = None
        self._tenant_id = None

    @property
    def equity_id(self):
        return self._equity_id

    @equity_id.setter
    def equity_id(self, value):
        self._equity_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.equity_id:
            if hasattr(self.equity_id, 'to_alipay_dict'):
                params['equity_id'] = self.equity_id.to_alipay_dict()
            else:
                params['equity_id'] = self.equity_id
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
        o = AnttechMorseMarketingEquityBudgetQueryModel()
        if 'equity_id' in d:
            o.equity_id = d['equity_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


