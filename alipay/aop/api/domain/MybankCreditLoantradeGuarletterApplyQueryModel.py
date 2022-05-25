#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeGuarletterApplyQueryModel(object):

    def __init__(self):
        self._apply_no = None
        self._scheme_ar_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def scheme_ar_no(self):
        return self._scheme_ar_no

    @scheme_ar_no.setter
    def scheme_ar_no(self, value):
        self._scheme_ar_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.scheme_ar_no:
            if hasattr(self.scheme_ar_no, 'to_alipay_dict'):
                params['scheme_ar_no'] = self.scheme_ar_no.to_alipay_dict()
            else:
                params['scheme_ar_no'] = self.scheme_ar_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeGuarletterApplyQueryModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'scheme_ar_no' in d:
            o.scheme_ar_no = d['scheme_ar_no']
        return o


