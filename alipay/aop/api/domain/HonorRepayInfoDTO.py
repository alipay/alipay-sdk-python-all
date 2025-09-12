#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorRepayInfoDTO(object):

    def __init__(self):
        self._interest = None
        self._principal = None
        self._total_amount = None

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.interest:
            if hasattr(self.interest, 'to_alipay_dict'):
                params['interest'] = self.interest.to_alipay_dict()
            else:
                params['interest'] = self.interest
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorRepayInfoDTO()
        if 'interest' in d:
            o.interest = d['interest']
        if 'principal' in d:
            o.principal = d['principal']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


