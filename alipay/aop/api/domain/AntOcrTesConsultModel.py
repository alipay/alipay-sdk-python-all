#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityGoods import ActivityGoods


class AntOcrTesConsultModel(object):

    def __init__(self):
        self._out = None
        self._yyy = None

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        if isinstance(value, ActivityGoods):
            self._out = value
        else:
            self._out = ActivityGoods.from_alipay_dict(value)
    @property
    def yyy(self):
        return self._yyy

    @yyy.setter
    def yyy(self, value):
        self._yyy = value


    def to_alipay_dict(self):
        params = dict()
        if self.out:
            if hasattr(self.out, 'to_alipay_dict'):
                params['out'] = self.out.to_alipay_dict()
            else:
                params['out'] = self.out
        if self.yyy:
            if hasattr(self.yyy, 'to_alipay_dict'):
                params['yyy'] = self.yyy.to_alipay_dict()
            else:
                params['yyy'] = self.yyy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntOcrTesConsultModel()
        if 'out' in d:
            o.out = d['out']
        if 'yyy' in d:
            o.yyy = d['yyy']
        return o


