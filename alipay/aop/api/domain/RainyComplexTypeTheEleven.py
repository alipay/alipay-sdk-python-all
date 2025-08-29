#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypeTheEleven(object):

    def __init__(self):
        self._tc_01 = None

    @property
    def tc_01(self):
        return self._tc_01

    @tc_01.setter
    def tc_01(self, value):
        self._tc_01 = value


    def to_alipay_dict(self):
        params = dict()
        if self.tc_01:
            if hasattr(self.tc_01, 'to_alipay_dict'):
                params['tc_01'] = self.tc_01.to_alipay_dict()
            else:
                params['tc_01'] = self.tc_01
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypeTheEleven()
        if 'tc_01' in d:
            o.tc_01 = d['tc_01']
        return o


