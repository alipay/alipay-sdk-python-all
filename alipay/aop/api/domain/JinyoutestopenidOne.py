#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JinyoutestopenidOne(object):

    def __init__(self):
        self._c_1 = None
        self._q = None
        self._q_1_open_id = None

    @property
    def c_1(self):
        return self._c_1

    @c_1.setter
    def c_1(self, value):
        self._c_1 = value
    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, value):
        self._q = value
    @property
    def q_1_open_id(self):
        return self._q_1_open_id

    @q_1_open_id.setter
    def q_1_open_id(self, value):
        self._q_1_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.c_1:
            if hasattr(self.c_1, 'to_alipay_dict'):
                params['c_1'] = self.c_1.to_alipay_dict()
            else:
                params['c_1'] = self.c_1
        if self.q:
            if hasattr(self.q, 'to_alipay_dict'):
                params['q'] = self.q.to_alipay_dict()
            else:
                params['q'] = self.q
        if self.q_1_open_id:
            if hasattr(self.q_1_open_id, 'to_alipay_dict'):
                params['q_1_open_id'] = self.q_1_open_id.to_alipay_dict()
            else:
                params['q_1_open_id'] = self.q_1_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JinyoutestopenidOne()
        if 'c_1' in d:
            o.c_1 = d['c_1']
        if 'q' in d:
            o.q = d['q']
        if 'q_1_open_id' in d:
            o.q_1_open_id = d['q_1_open_id']
        return o


