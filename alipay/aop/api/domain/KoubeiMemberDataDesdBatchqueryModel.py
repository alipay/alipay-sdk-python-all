#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class KoubeiMemberDataDesdBatchqueryModel(object):

    def __init__(self):
        self._a = None
        self._desd = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def desd(self):
        return self._desd

    @desd.setter
    def desd(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._desd = value
        else:
            self._desd = GavintestNewLeveaOne.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.desd:
            if hasattr(self.desd, 'to_alipay_dict'):
                params['desd'] = self.desd.to_alipay_dict()
            else:
                params['desd'] = self.desd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMemberDataDesdBatchqueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'desd' in d:
            o.desd = d['desd']
        return o


