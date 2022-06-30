#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeRecContext import ApeRecContext


class AlipaySecurityLifeQueryModel(object):

    def __init__(self):
        self._dsfg = None
        self._grt = None
        self._hh = None
        self._sdgd = None
        self._xcvb = None

    @property
    def dsfg(self):
        return self._dsfg

    @dsfg.setter
    def dsfg(self, value):
        if isinstance(value, list):
            self._dsfg = list()
            for i in value:
                if isinstance(i, ApeRecContext):
                    self._dsfg.append(i)
                else:
                    self._dsfg.append(ApeRecContext.from_alipay_dict(i))
    @property
    def grt(self):
        return self._grt

    @grt.setter
    def grt(self, value):
        if isinstance(value, list):
            self._grt = list()
            for i in value:
                self._grt.append(i)
    @property
    def hh(self):
        return self._hh

    @hh.setter
    def hh(self, value):
        self._hh = value
    @property
    def sdgd(self):
        return self._sdgd

    @sdgd.setter
    def sdgd(self, value):
        if isinstance(value, list):
            self._sdgd = list()
            for i in value:
                self._sdgd.append(i)
    @property
    def xcvb(self):
        return self._xcvb

    @xcvb.setter
    def xcvb(self, value):
        self._xcvb = value


    def to_alipay_dict(self):
        params = dict()
        if self.dsfg:
            if isinstance(self.dsfg, list):
                for i in range(0, len(self.dsfg)):
                    element = self.dsfg[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dsfg[i] = element.to_alipay_dict()
            if hasattr(self.dsfg, 'to_alipay_dict'):
                params['dsfg'] = self.dsfg.to_alipay_dict()
            else:
                params['dsfg'] = self.dsfg
        if self.grt:
            if isinstance(self.grt, list):
                for i in range(0, len(self.grt)):
                    element = self.grt[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.grt[i] = element.to_alipay_dict()
            if hasattr(self.grt, 'to_alipay_dict'):
                params['grt'] = self.grt.to_alipay_dict()
            else:
                params['grt'] = self.grt
        if self.hh:
            if hasattr(self.hh, 'to_alipay_dict'):
                params['hh'] = self.hh.to_alipay_dict()
            else:
                params['hh'] = self.hh
        if self.sdgd:
            if isinstance(self.sdgd, list):
                for i in range(0, len(self.sdgd)):
                    element = self.sdgd[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sdgd[i] = element.to_alipay_dict()
            if hasattr(self.sdgd, 'to_alipay_dict'):
                params['sdgd'] = self.sdgd.to_alipay_dict()
            else:
                params['sdgd'] = self.sdgd
        if self.xcvb:
            if hasattr(self.xcvb, 'to_alipay_dict'):
                params['xcvb'] = self.xcvb.to_alipay_dict()
            else:
                params['xcvb'] = self.xcvb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityLifeQueryModel()
        if 'dsfg' in d:
            o.dsfg = d['dsfg']
        if 'grt' in d:
            o.grt = d['grt']
        if 'hh' in d:
            o.hh = d['hh']
        if 'sdgd' in d:
            o.sdgd = d['sdgd']
        if 'xcvb' in d:
            o.xcvb = d['xcvb']
        return o


