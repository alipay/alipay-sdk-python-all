#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PriNestOther import PriNestOther


class AlipaySecurityJhjtestaaTestQueryModel(object):

    def __init__(self):
        self._ap_id = None
        self._ap_open_id = None
        self._complex_pri = None

    @property
    def ap_id(self):
        return self._ap_id

    @ap_id.setter
    def ap_id(self, value):
        self._ap_id = value
    @property
    def ap_open_id(self):
        return self._ap_open_id

    @ap_open_id.setter
    def ap_open_id(self, value):
        self._ap_open_id = value
    @property
    def complex_pri(self):
        return self._complex_pri

    @complex_pri.setter
    def complex_pri(self, value):
        if isinstance(value, PriNestOther):
            self._complex_pri = value
        else:
            self._complex_pri = PriNestOther.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ap_id:
            if hasattr(self.ap_id, 'to_alipay_dict'):
                params['ap_id'] = self.ap_id.to_alipay_dict()
            else:
                params['ap_id'] = self.ap_id
        if self.ap_open_id:
            if hasattr(self.ap_open_id, 'to_alipay_dict'):
                params['ap_open_id'] = self.ap_open_id.to_alipay_dict()
            else:
                params['ap_open_id'] = self.ap_open_id
        if self.complex_pri:
            if hasattr(self.complex_pri, 'to_alipay_dict'):
                params['complex_pri'] = self.complex_pri.to_alipay_dict()
            else:
                params['complex_pri'] = self.complex_pri
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityJhjtestaaTestQueryModel()
        if 'ap_id' in d:
            o.ap_id = d['ap_id']
        if 'ap_open_id' in d:
            o.ap_open_id = d['ap_open_id']
        if 'complex_pri' in d:
            o.complex_pri = d['complex_pri']
        return o


