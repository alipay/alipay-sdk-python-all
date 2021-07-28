#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppDfsfasDeQueryModel(object):

    def __init__(self):
        self._desd = None
        self._desdde = None
        self._desf = None

    @property
    def desd(self):
        return self._desd

    @desd.setter
    def desd(self, value):
        self._desd = value
    @property
    def desdde(self):
        return self._desdde

    @desdde.setter
    def desdde(self, value):
        self._desdde = value
    @property
    def desf(self):
        return self._desf

    @desf.setter
    def desf(self, value):
        self._desf = value


    def to_alipay_dict(self):
        params = dict()
        if self.desd:
            if hasattr(self.desd, 'to_alipay_dict'):
                params['desd'] = self.desd.to_alipay_dict()
            else:
                params['desd'] = self.desd
        if self.desdde:
            if hasattr(self.desdde, 'to_alipay_dict'):
                params['desdde'] = self.desdde.to_alipay_dict()
            else:
                params['desdde'] = self.desdde
        if self.desf:
            if hasattr(self.desf, 'to_alipay_dict'):
                params['desf'] = self.desf.to_alipay_dict()
            else:
                params['desf'] = self.desf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppDfsfasDeQueryModel()
        if 'desd' in d:
            o.desd = d['desd']
        if 'desdde' in d:
            o.desdde = d['desdde']
        if 'desf' in d:
            o.desf = d['desf']
        return o


