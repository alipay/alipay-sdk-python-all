#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JhjTestNew import JhjTestNew


class AlipaySecurityRiskJhjtestComplexddBatchqueryModel(object):

    def __init__(self):
        self._comple_a = None
        self._regress = None

    @property
    def comple_a(self):
        return self._comple_a

    @comple_a.setter
    def comple_a(self, value):
        if isinstance(value, JhjTestNew):
            self._comple_a = value
        else:
            self._comple_a = JhjTestNew.from_alipay_dict(value)
    @property
    def regress(self):
        return self._regress

    @regress.setter
    def regress(self, value):
        self._regress = value


    def to_alipay_dict(self):
        params = dict()
        if self.comple_a:
            if hasattr(self.comple_a, 'to_alipay_dict'):
                params['comple_a'] = self.comple_a.to_alipay_dict()
            else:
                params['comple_a'] = self.comple_a
        if self.regress:
            if hasattr(self.regress, 'to_alipay_dict'):
                params['regress'] = self.regress.to_alipay_dict()
            else:
                params['regress'] = self.regress
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskJhjtestComplexddBatchqueryModel()
        if 'comple_a' in d:
            o.comple_a = d['comple_a']
        if 'regress' in d:
            o.regress = d['regress']
        return o


