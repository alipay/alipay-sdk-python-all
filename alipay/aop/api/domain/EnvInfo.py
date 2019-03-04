#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnvInfo(object):

    def __init__(self):
        self._operator_id = None
        self._store_id = None
        self._terminal_id = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnvInfo()
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        return o


