#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeGuarletterApplyCancelModel(object):

    def __init__(self):
        self._apply_no = None
        self._request_id = None
        self._scheme_ar_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
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
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = MybankCreditLoantradeGuarletterApplyCancelModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scheme_ar_no' in d:
            o.scheme_ar_no = d['scheme_ar_no']
        return o


