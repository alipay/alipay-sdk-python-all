#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityGoods import ActivityGoods


class AntOcrTesConsultModel(object):

    def __init__(self):
        self._oooo = None
        self._out = None
        self._ss = None
        self._sss = None
        self._sssss = None
        self._trhee = None
        self._yyy = None

    @property
    def oooo(self):
        return self._oooo

    @oooo.setter
    def oooo(self, value):
        self._oooo = value
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
    def ss(self):
        return self._ss

    @ss.setter
    def ss(self, value):
        self._ss = value
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value
    @property
    def sssss(self):
        return self._sssss

    @sssss.setter
    def sssss(self, value):
        self._sssss = value
    @property
    def trhee(self):
        return self._trhee

    @trhee.setter
    def trhee(self, value):
        self._trhee = value
    @property
    def yyy(self):
        return self._yyy

    @yyy.setter
    def yyy(self, value):
        self._yyy = value


    def to_alipay_dict(self):
        params = dict()
        if self.oooo:
            if hasattr(self.oooo, 'to_alipay_dict'):
                params['oooo'] = self.oooo.to_alipay_dict()
            else:
                params['oooo'] = self.oooo
        if self.out:
            if hasattr(self.out, 'to_alipay_dict'):
                params['out'] = self.out.to_alipay_dict()
            else:
                params['out'] = self.out
        if self.ss:
            if hasattr(self.ss, 'to_alipay_dict'):
                params['ss'] = self.ss.to_alipay_dict()
            else:
                params['ss'] = self.ss
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        if self.sssss:
            if hasattr(self.sssss, 'to_alipay_dict'):
                params['sssss'] = self.sssss.to_alipay_dict()
            else:
                params['sssss'] = self.sssss
        if self.trhee:
            if hasattr(self.trhee, 'to_alipay_dict'):
                params['trhee'] = self.trhee.to_alipay_dict()
            else:
                params['trhee'] = self.trhee
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
        if 'oooo' in d:
            o.oooo = d['oooo']
        if 'out' in d:
            o.out = d['out']
        if 'ss' in d:
            o.ss = d['ss']
        if 'sss' in d:
            o.sss = d['sss']
        if 'sssss' in d:
            o.sssss = d['sssss']
        if 'trhee' in d:
            o.trhee = d['trhee']
        if 'yyy' in d:
            o.yyy = d['yyy']
        return o


