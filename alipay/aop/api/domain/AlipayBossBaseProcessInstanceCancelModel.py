#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseProcessInstanceCancelModel(object):

    def __init__(self):
        self._memo = None
        self._operator = None
        self._puid = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseProcessInstanceCancelModel()
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'puid' in d:
            o.puid = d['puid']
        return o


