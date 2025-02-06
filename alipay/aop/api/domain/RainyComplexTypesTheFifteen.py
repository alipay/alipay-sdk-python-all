#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypesTheFifteen(object):

    def __init__(self):
        self._must_case = None
        self._tc_case = None

    @property
    def must_case(self):
        return self._must_case

    @must_case.setter
    def must_case(self, value):
        self._must_case = value
    @property
    def tc_case(self):
        return self._tc_case

    @tc_case.setter
    def tc_case(self, value):
        self._tc_case = value


    def to_alipay_dict(self):
        params = dict()
        if self.must_case:
            if hasattr(self.must_case, 'to_alipay_dict'):
                params['must_case'] = self.must_case.to_alipay_dict()
            else:
                params['must_case'] = self.must_case
        if self.tc_case:
            if hasattr(self.tc_case, 'to_alipay_dict'):
                params['tc_case'] = self.tc_case.to_alipay_dict()
            else:
                params['tc_case'] = self.tc_case
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesTheFifteen()
        if 'must_case' in d:
            o.must_case = d['must_case']
        if 'tc_case' in d:
            o.tc_case = d['tc_case']
        return o


