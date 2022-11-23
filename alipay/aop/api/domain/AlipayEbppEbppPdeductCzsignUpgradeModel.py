#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppPdeductCzsignUpgradeModel(object):

    def __init__(self):
        self._agreement_id = None
        self._fix_amount = None
        self._pid = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def fix_amount(self):
        return self._fix_amount

    @fix_amount.setter
    def fix_amount(self, value):
        self._fix_amount = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.fix_amount:
            if hasattr(self.fix_amount, 'to_alipay_dict'):
                params['fix_amount'] = self.fix_amount.to_alipay_dict()
            else:
                params['fix_amount'] = self.fix_amount
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppEbppPdeductCzsignUpgradeModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'fix_amount' in d:
            o.fix_amount = d['fix_amount']
        if 'pid' in d:
            o.pid = d['pid']
        return o


