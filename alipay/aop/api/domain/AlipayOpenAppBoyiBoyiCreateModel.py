#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne
from alipay.aop.api.domain.GavinTestnew import GavinTestnew


class AlipayOpenAppBoyiBoyiCreateModel(object):

    def __init__(self):
        self._com = None
        self._des = None
        self._desd = None
        self._desdmm = None
        self._header = None
        self._med = None
        self._query = None

    @property
    def com(self):
        return self._com

    @com.setter
    def com(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._com = value
        else:
            self._com = GavintestNewLeveaOne.from_alipay_dict(value)
    @property
    def des(self):
        return self._des

    @des.setter
    def des(self, value):
        self._des = value
    @property
    def desd(self):
        return self._desd

    @desd.setter
    def desd(self, value):
        if isinstance(value, GavinTestnew):
            self._desd = value
        else:
            self._desd = GavinTestnew.from_alipay_dict(value)
    @property
    def desdmm(self):
        return self._desdmm

    @desdmm.setter
    def desdmm(self, value):
        self._desdmm = value
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value
    @property
    def med(self):
        return self._med

    @med.setter
    def med(self, value):
        self._med = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value


    def to_alipay_dict(self):
        params = dict()
        if self.com:
            if hasattr(self.com, 'to_alipay_dict'):
                params['com'] = self.com.to_alipay_dict()
            else:
                params['com'] = self.com
        if self.des:
            if hasattr(self.des, 'to_alipay_dict'):
                params['des'] = self.des.to_alipay_dict()
            else:
                params['des'] = self.des
        if self.desd:
            if hasattr(self.desd, 'to_alipay_dict'):
                params['desd'] = self.desd.to_alipay_dict()
            else:
                params['desd'] = self.desd
        if self.desdmm:
            if hasattr(self.desdmm, 'to_alipay_dict'):
                params['desdmm'] = self.desdmm.to_alipay_dict()
            else:
                params['desdmm'] = self.desdmm
        if self.header:
            if hasattr(self.header, 'to_alipay_dict'):
                params['header'] = self.header.to_alipay_dict()
            else:
                params['header'] = self.header
        if self.med:
            if hasattr(self.med, 'to_alipay_dict'):
                params['med'] = self.med.to_alipay_dict()
            else:
                params['med'] = self.med
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppBoyiBoyiCreateModel()
        if 'com' in d:
            o.com = d['com']
        if 'des' in d:
            o.des = d['des']
        if 'desd' in d:
            o.desd = d['desd']
        if 'desdmm' in d:
            o.desdmm = d['desdmm']
        if 'header' in d:
            o.header = d['header']
        if 'med' in d:
            o.med = d['med']
        if 'query' in d:
            o.query = d['query']
        return o


