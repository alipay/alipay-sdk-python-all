#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfaccruedprodCumpoaccbalamtQueryModel(object):

    def __init__(self):
        self._account_period = None
        self._po_no = None

    @property
    def account_period(self):
        return self._account_period

    @account_period.setter
    def account_period(self, value):
        self._account_period = value
    @property
    def po_no(self):
        return self._po_no

    @po_no.setter
    def po_no(self, value):
        self._po_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_period:
            if hasattr(self.account_period, 'to_alipay_dict'):
                params['account_period'] = self.account_period.to_alipay_dict()
            else:
                params['account_period'] = self.account_period
        if self.po_no:
            if hasattr(self.po_no, 'to_alipay_dict'):
                params['po_no'] = self.po_no.to_alipay_dict()
            else:
                params['po_no'] = self.po_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfaccruedprodCumpoaccbalamtQueryModel()
        if 'account_period' in d:
            o.account_period = d['account_period']
        if 'po_no' in d:
            o.po_no = d['po_no']
        return o


