#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenapiEnventrackingQueryModel(object):

    def __init__(self):
        self._u_tset = None

    @property
    def u_tset(self):
        return self._u_tset

    @u_tset.setter
    def u_tset(self, value):
        self._u_tset = value


    def to_alipay_dict(self):
        params = dict()
        if self.u_tset:
            if hasattr(self.u_tset, 'to_alipay_dict'):
                params['u_tset'] = self.u_tset.to_alipay_dict()
            else:
                params['u_tset'] = self.u_tset
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenapiEnventrackingQueryModel()
        if 'u_tset' in d:
            o.u_tset = d['u_tset']
        return o


