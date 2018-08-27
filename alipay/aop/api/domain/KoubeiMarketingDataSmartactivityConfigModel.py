#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataSmartactivityConfigModel(object):

    def __init__(self):
        self._diagnose_code = None

    @property
    def diagnose_code(self):
        return self._diagnose_code

    @diagnose_code.setter
    def diagnose_code(self, value):
        self._diagnose_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.diagnose_code:
            if hasattr(self.diagnose_code, 'to_alipay_dict'):
                params['diagnose_code'] = self.diagnose_code.to_alipay_dict()
            else:
                params['diagnose_code'] = self.diagnose_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataSmartactivityConfigModel()
        if 'diagnose_code' in d:
            o.diagnose_code = d['diagnose_code']
        return o


