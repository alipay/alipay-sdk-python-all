#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountFreeze(object):

    def __init__(self):
        self._freeze_amount = None
        self._freeze_name = None
        self._freeze_type = None

    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def freeze_name(self):
        return self._freeze_name

    @freeze_name.setter
    def freeze_name(self, value):
        self._freeze_name = value
    @property
    def freeze_type(self):
        return self._freeze_type

    @freeze_type.setter
    def freeze_type(self, value):
        self._freeze_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.freeze_name:
            if hasattr(self.freeze_name, 'to_alipay_dict'):
                params['freeze_name'] = self.freeze_name.to_alipay_dict()
            else:
                params['freeze_name'] = self.freeze_name
        if self.freeze_type:
            if hasattr(self.freeze_type, 'to_alipay_dict'):
                params['freeze_type'] = self.freeze_type.to_alipay_dict()
            else:
                params['freeze_type'] = self.freeze_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountFreeze()
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'freeze_name' in d:
            o.freeze_name = d['freeze_name']
        if 'freeze_type' in d:
            o.freeze_type = d['freeze_type']
        return o


