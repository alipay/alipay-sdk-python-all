#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceTruspleCustomsauthinitSubmitModel(object):

    def __init__(self):
        self._org_code = None

    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTruspleCustomsauthinitSubmitModel()
        if 'org_code' in d:
            o.org_code = d['org_code']
        return o


