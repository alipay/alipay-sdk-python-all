#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PreConsultMap(object):

    def __init__(self):
        self._v_1 = None
        self._v_2 = None
        self._v_3 = None
        self._v_4 = None

    @property
    def v_1(self):
        return self._v_1

    @v_1.setter
    def v_1(self, value):
        self._v_1 = value
    @property
    def v_2(self):
        return self._v_2

    @v_2.setter
    def v_2(self, value):
        self._v_2 = value
    @property
    def v_3(self):
        return self._v_3

    @v_3.setter
    def v_3(self, value):
        self._v_3 = value
    @property
    def v_4(self):
        return self._v_4

    @v_4.setter
    def v_4(self, value):
        self._v_4 = value


    def to_alipay_dict(self):
        params = dict()
        if self.v_1:
            if hasattr(self.v_1, 'to_alipay_dict'):
                params['v_1'] = self.v_1.to_alipay_dict()
            else:
                params['v_1'] = self.v_1
        if self.v_2:
            if hasattr(self.v_2, 'to_alipay_dict'):
                params['v_2'] = self.v_2.to_alipay_dict()
            else:
                params['v_2'] = self.v_2
        if self.v_3:
            if hasattr(self.v_3, 'to_alipay_dict'):
                params['v_3'] = self.v_3.to_alipay_dict()
            else:
                params['v_3'] = self.v_3
        if self.v_4:
            if hasattr(self.v_4, 'to_alipay_dict'):
                params['v_4'] = self.v_4.to_alipay_dict()
            else:
                params['v_4'] = self.v_4
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreConsultMap()
        if 'v_1' in d:
            o.v_1 = d['v_1']
        if 'v_2' in d:
            o.v_2 = d['v_2']
        if 'v_3' in d:
            o.v_3 = d['v_3']
        if 'v_4' in d:
            o.v_4 = d['v_4']
        return o


