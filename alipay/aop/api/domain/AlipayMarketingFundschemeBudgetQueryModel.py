#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingFundschemeBudgetQueryModel(object):

    def __init__(self):
        self._fund_scheme_id = None

    @property
    def fund_scheme_id(self):
        return self._fund_scheme_id

    @fund_scheme_id.setter
    def fund_scheme_id(self, value):
        self._fund_scheme_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_scheme_id:
            if hasattr(self.fund_scheme_id, 'to_alipay_dict'):
                params['fund_scheme_id'] = self.fund_scheme_id.to_alipay_dict()
            else:
                params['fund_scheme_id'] = self.fund_scheme_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingFundschemeBudgetQueryModel()
        if 'fund_scheme_id' in d:
            o.fund_scheme_id = d['fund_scheme_id']
        return o


