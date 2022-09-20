#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyouTestTwo import JinyouTestTwo


class JinyouTestThree(object):

    def __init__(self):
        self._th_1_f = None
        self._th_2_n = None
        self._th_3_n = None

    @property
    def th_1_f(self):
        return self._th_1_f

    @th_1_f.setter
    def th_1_f(self, value):
        if isinstance(value, JinyouTestTwo):
            self._th_1_f = value
        else:
            self._th_1_f = JinyouTestTwo.from_alipay_dict(value)
    @property
    def th_2_n(self):
        return self._th_2_n

    @th_2_n.setter
    def th_2_n(self, value):
        self._th_2_n = value
    @property
    def th_3_n(self):
        return self._th_3_n

    @th_3_n.setter
    def th_3_n(self, value):
        self._th_3_n = value


    def to_alipay_dict(self):
        params = dict()
        if self.th_1_f:
            if hasattr(self.th_1_f, 'to_alipay_dict'):
                params['th_1_f'] = self.th_1_f.to_alipay_dict()
            else:
                params['th_1_f'] = self.th_1_f
        if self.th_2_n:
            if hasattr(self.th_2_n, 'to_alipay_dict'):
                params['th_2_n'] = self.th_2_n.to_alipay_dict()
            else:
                params['th_2_n'] = self.th_2_n
        if self.th_3_n:
            if hasattr(self.th_3_n, 'to_alipay_dict'):
                params['th_3_n'] = self.th_3_n.to_alipay_dict()
            else:
                params['th_3_n'] = self.th_3_n
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JinyouTestThree()
        if 'th_1_f' in d:
            o.th_1_f = d['th_1_f']
        if 'th_2_n' in d:
            o.th_2_n = d['th_2_n']
        if 'th_3_n' in d:
            o.th_3_n = d['th_3_n']
        return o


