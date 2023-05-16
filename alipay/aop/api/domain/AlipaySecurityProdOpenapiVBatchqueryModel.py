#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CedsipeihuanCcomplex import CedsipeihuanCcomplex


class AlipaySecurityProdOpenapiVBatchqueryModel(object):

    def __init__(self):
        self._d_amount = None
        self._dd = None
        self._ddf = None
        self._jf = None
        self._lk = None
        self._longitudedd = None
        self._longitudeeee = None
        self._rr = None
        self._x_njd = None

    @property
    def d_amount(self):
        return self._d_amount

    @d_amount.setter
    def d_amount(self, value):
        self._d_amount = value
    @property
    def dd(self):
        return self._dd

    @dd.setter
    def dd(self, value):
        self._dd = value
    @property
    def ddf(self):
        return self._ddf

    @ddf.setter
    def ddf(self, value):
        self._ddf = value
    @property
    def jf(self):
        return self._jf

    @jf.setter
    def jf(self, value):
        self._jf = value
    @property
    def lk(self):
        return self._lk

    @lk.setter
    def lk(self, value):
        self._lk = value
    @property
    def longitudedd(self):
        return self._longitudedd

    @longitudedd.setter
    def longitudedd(self, value):
        self._longitudedd = value
    @property
    def longitudeeee(self):
        return self._longitudeeee

    @longitudeeee.setter
    def longitudeeee(self, value):
        if isinstance(value, CedsipeihuanCcomplex):
            self._longitudeeee = value
        else:
            self._longitudeeee = CedsipeihuanCcomplex.from_alipay_dict(value)
    @property
    def rr(self):
        return self._rr

    @rr.setter
    def rr(self, value):
        self._rr = value
    @property
    def x_njd(self):
        return self._x_njd

    @x_njd.setter
    def x_njd(self, value):
        self._x_njd = value


    def to_alipay_dict(self):
        params = dict()
        if self.d_amount:
            if hasattr(self.d_amount, 'to_alipay_dict'):
                params['d_amount'] = self.d_amount.to_alipay_dict()
            else:
                params['d_amount'] = self.d_amount
        if self.dd:
            if hasattr(self.dd, 'to_alipay_dict'):
                params['dd'] = self.dd.to_alipay_dict()
            else:
                params['dd'] = self.dd
        if self.ddf:
            if hasattr(self.ddf, 'to_alipay_dict'):
                params['ddf'] = self.ddf.to_alipay_dict()
            else:
                params['ddf'] = self.ddf
        if self.jf:
            if hasattr(self.jf, 'to_alipay_dict'):
                params['jf'] = self.jf.to_alipay_dict()
            else:
                params['jf'] = self.jf
        if self.lk:
            if hasattr(self.lk, 'to_alipay_dict'):
                params['lk'] = self.lk.to_alipay_dict()
            else:
                params['lk'] = self.lk
        if self.longitudedd:
            if hasattr(self.longitudedd, 'to_alipay_dict'):
                params['longitudedd'] = self.longitudedd.to_alipay_dict()
            else:
                params['longitudedd'] = self.longitudedd
        if self.longitudeeee:
            if hasattr(self.longitudeeee, 'to_alipay_dict'):
                params['longitudeeee'] = self.longitudeeee.to_alipay_dict()
            else:
                params['longitudeeee'] = self.longitudeeee
        if self.rr:
            if hasattr(self.rr, 'to_alipay_dict'):
                params['rr'] = self.rr.to_alipay_dict()
            else:
                params['rr'] = self.rr
        if self.x_njd:
            if hasattr(self.x_njd, 'to_alipay_dict'):
                params['x_njd'] = self.x_njd.to_alipay_dict()
            else:
                params['x_njd'] = self.x_njd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdOpenapiVBatchqueryModel()
        if 'd_amount' in d:
            o.d_amount = d['d_amount']
        if 'dd' in d:
            o.dd = d['dd']
        if 'ddf' in d:
            o.ddf = d['ddf']
        if 'jf' in d:
            o.jf = d['jf']
        if 'lk' in d:
            o.lk = d['lk']
        if 'longitudedd' in d:
            o.longitudedd = d['longitudedd']
        if 'longitudeeee' in d:
            o.longitudeeee = d['longitudeeee']
        if 'rr' in d:
            o.rr = d['rr']
        if 'x_njd' in d:
            o.x_njd = d['x_njd']
        return o


