#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreigtFlowAccount(object):

    def __init__(self):
        self._bank_id = None
        self._bank_name = None
        self._parent_id = None
        self._parent_name = None

    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def parent_name(self):
        return self._parent_name

    @parent_name.setter
    def parent_name(self, value):
        self._parent_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_id:
            if hasattr(self.bank_id, 'to_alipay_dict'):
                params['bank_id'] = self.bank_id.to_alipay_dict()
            else:
                params['bank_id'] = self.bank_id
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.parent_name:
            if hasattr(self.parent_name, 'to_alipay_dict'):
                params['parent_name'] = self.parent_name.to_alipay_dict()
            else:
                params['parent_name'] = self.parent_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreigtFlowAccount()
        if 'bank_id' in d:
            o.bank_id = d['bank_id']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'parent_name' in d:
            o.parent_name = d['parent_name']
        return o


