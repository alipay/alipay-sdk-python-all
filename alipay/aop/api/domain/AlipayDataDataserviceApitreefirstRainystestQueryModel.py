#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFifteen import RainyComplexTypesTheFifteen


class AlipayDataDataserviceApitreefirstRainystestQueryModel(object):

    def __init__(self):
        self._demo_case = None

    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        if isinstance(value, RainyComplexTypesTheFifteen):
            self._demo_case = value
        else:
            self._demo_case = RainyComplexTypesTheFifteen.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceApitreefirstRainystestQueryModel()
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        return o


