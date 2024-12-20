#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataserviceComplextestsecondRainystestQueryModel(object):

    def __init__(self):
        self._tc_case_01 = None

    @property
    def tc_case_01(self):
        return self._tc_case_01

    @tc_case_01.setter
    def tc_case_01(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._tc_case_01 = value
        else:
            self._tc_case_01 = RainyComplexTypesTheFourth.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.tc_case_01:
            if hasattr(self.tc_case_01, 'to_alipay_dict'):
                params['tc_case_01'] = self.tc_case_01.to_alipay_dict()
            else:
                params['tc_case_01'] = self.tc_case_01
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceComplextestsecondRainystestQueryModel()
        if 'tc_case_01' in d:
            o.tc_case_01 = d['tc_case_01']
        return o


