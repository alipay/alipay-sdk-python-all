#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceComplianceCheckResult(object):

    def __init__(self):
        self._match_result_type = None

    @property
    def match_result_type(self):
        return self._match_result_type

    @match_result_type.setter
    def match_result_type(self, value):
        self._match_result_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.match_result_type:
            if hasattr(self.match_result_type, 'to_alipay_dict'):
                params['match_result_type'] = self.match_result_type.to_alipay_dict()
            else:
                params['match_result_type'] = self.match_result_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceComplianceCheckResult()
        if 'match_result_type' in d:
            o.match_result_type = d['match_result_type']
        return o


