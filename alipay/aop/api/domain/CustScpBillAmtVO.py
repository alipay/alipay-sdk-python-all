#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustScpBillAmtVO(object):

    def __init__(self):
        self._fee = None
        self._prin = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def prin(self):
        return self._prin

    @prin.setter
    def prin(self, value):
        self._prin = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.prin:
            if hasattr(self.prin, 'to_alipay_dict'):
                params['prin'] = self.prin.to_alipay_dict()
            else:
                params['prin'] = self.prin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustScpBillAmtVO()
        if 'fee' in d:
            o.fee = d['fee']
        if 'prin' in d:
            o.prin = d['prin']
        return o


