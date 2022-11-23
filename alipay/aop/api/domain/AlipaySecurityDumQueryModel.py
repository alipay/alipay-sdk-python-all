#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JinyoutestopenidThree import JinyoutestopenidThree


class AlipaySecurityDumQueryModel(object):

    def __init__(self):
        self._cc_open_id = None
        self._ccc = None
        self._f = None
        self._zip = None

    @property
    def cc_open_id(self):
        return self._cc_open_id

    @cc_open_id.setter
    def cc_open_id(self, value):
        self._cc_open_id = value
    @property
    def ccc(self):
        return self._ccc

    @ccc.setter
    def ccc(self, value):
        self._ccc = value
    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        if isinstance(value, JinyoutestopenidThree):
            self._f = value
        else:
            self._f = JinyoutestopenidThree.from_alipay_dict(value)
    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, value):
        self._zip = value


    def to_alipay_dict(self):
        params = dict()
        if self.cc_open_id:
            if hasattr(self.cc_open_id, 'to_alipay_dict'):
                params['cc_open_id'] = self.cc_open_id.to_alipay_dict()
            else:
                params['cc_open_id'] = self.cc_open_id
        if self.ccc:
            if hasattr(self.ccc, 'to_alipay_dict'):
                params['ccc'] = self.ccc.to_alipay_dict()
            else:
                params['ccc'] = self.ccc
        if self.f:
            if hasattr(self.f, 'to_alipay_dict'):
                params['f'] = self.f.to_alipay_dict()
            else:
                params['f'] = self.f
        if self.zip:
            if hasattr(self.zip, 'to_alipay_dict'):
                params['zip'] = self.zip.to_alipay_dict()
            else:
                params['zip'] = self.zip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDumQueryModel()
        if 'cc_open_id' in d:
            o.cc_open_id = d['cc_open_id']
        if 'ccc' in d:
            o.ccc = d['ccc']
        if 'f' in d:
            o.f = d['f']
        if 'zip' in d:
            o.zip = d['zip']
        return o


