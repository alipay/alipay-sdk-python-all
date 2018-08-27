#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradePartnerPaymentQueryModel(object):

    def __init__(self):
        self._in_apply_no = None

    @property
    def in_apply_no(self):
        return self._in_apply_no

    @in_apply_no.setter
    def in_apply_no(self, value):
        self._in_apply_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.in_apply_no:
            if hasattr(self.in_apply_no, 'to_alipay_dict'):
                params['in_apply_no'] = self.in_apply_no.to_alipay_dict()
            else:
                params['in_apply_no'] = self.in_apply_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradePartnerPaymentQueryModel()
        if 'in_apply_no' in d:
            o.in_apply_no = d['in_apply_no']
        return o


