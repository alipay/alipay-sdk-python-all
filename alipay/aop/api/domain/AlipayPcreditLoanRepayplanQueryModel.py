#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanRepayplanQueryModel(object):

    def __init__(self):
        self._loan_apply_no = None

    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanRepayplanQueryModel()
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        return o


