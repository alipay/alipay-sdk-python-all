#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CedsipeihuanCcomplex(object):

    def __init__(self):
        self._d = None
        self._dede = None
        self._fgrf = None
        self._hdj_open_id = None
        self._sdcd = None

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value
    @property
    def dede(self):
        return self._dede

    @dede.setter
    def dede(self, value):
        self._dede = value
    @property
    def fgrf(self):
        return self._fgrf

    @fgrf.setter
    def fgrf(self, value):
        self._fgrf = value
    @property
    def hdj_open_id(self):
        return self._hdj_open_id

    @hdj_open_id.setter
    def hdj_open_id(self, value):
        self._hdj_open_id = value
    @property
    def sdcd(self):
        return self._sdcd

    @sdcd.setter
    def sdcd(self, value):
        self._sdcd = value


    def to_alipay_dict(self):
        params = dict()
        if self.d:
            if hasattr(self.d, 'to_alipay_dict'):
                params['d'] = self.d.to_alipay_dict()
            else:
                params['d'] = self.d
        if self.dede:
            if hasattr(self.dede, 'to_alipay_dict'):
                params['dede'] = self.dede.to_alipay_dict()
            else:
                params['dede'] = self.dede
        if self.fgrf:
            if hasattr(self.fgrf, 'to_alipay_dict'):
                params['fgrf'] = self.fgrf.to_alipay_dict()
            else:
                params['fgrf'] = self.fgrf
        if self.hdj_open_id:
            if hasattr(self.hdj_open_id, 'to_alipay_dict'):
                params['hdj_open_id'] = self.hdj_open_id.to_alipay_dict()
            else:
                params['hdj_open_id'] = self.hdj_open_id
        if self.sdcd:
            if hasattr(self.sdcd, 'to_alipay_dict'):
                params['sdcd'] = self.sdcd.to_alipay_dict()
            else:
                params['sdcd'] = self.sdcd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CedsipeihuanCcomplex()
        if 'd' in d:
            o.d = d['d']
        if 'dede' in d:
            o.dede = d['dede']
        if 'fgrf' in d:
            o.fgrf = d['fgrf']
        if 'hdj_open_id' in d:
            o.hdj_open_id = d['hdj_open_id']
        if 'sdcd' in d:
            o.sdcd = d['sdcd']
        return o


