#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Apitestjhj import Apitestjhj


class AlipayPcreditJhjtestGrayQueryModel(object):

    def __init__(self):
        self._para = None
        self._para_comp = None

    @property
    def para(self):
        return self._para

    @para.setter
    def para(self, value):
        self._para = value
    @property
    def para_comp(self):
        return self._para_comp

    @para_comp.setter
    def para_comp(self, value):
        if isinstance(value, Apitestjhj):
            self._para_comp = value
        else:
            self._para_comp = Apitestjhj.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.para:
            if hasattr(self.para, 'to_alipay_dict'):
                params['para'] = self.para.to_alipay_dict()
            else:
                params['para'] = self.para
        if self.para_comp:
            if hasattr(self.para_comp, 'to_alipay_dict'):
                params['para_comp'] = self.para_comp.to_alipay_dict()
            else:
                params['para_comp'] = self.para_comp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditJhjtestGrayQueryModel()
        if 'para' in d:
            o.para = d['para']
        if 'para_comp' in d:
            o.para_comp = d['para_comp']
        return o


