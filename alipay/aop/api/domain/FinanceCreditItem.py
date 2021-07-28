#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinanceCreditItem(object):

    def __init__(self):
        self._credit_id = None
        self._ver = None

    @property
    def credit_id(self):
        return self._credit_id

    @credit_id.setter
    def credit_id(self, value):
        self._credit_id = value
    @property
    def ver(self):
        return self._ver

    @ver.setter
    def ver(self, value):
        self._ver = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_id:
            if hasattr(self.credit_id, 'to_alipay_dict'):
                params['credit_id'] = self.credit_id.to_alipay_dict()
            else:
                params['credit_id'] = self.credit_id
        if self.ver:
            if hasattr(self.ver, 'to_alipay_dict'):
                params['ver'] = self.ver.to_alipay_dict()
            else:
                params['ver'] = self.ver
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinanceCreditItem()
        if 'credit_id' in d:
            o.credit_id = d['credit_id']
        if 'ver' in d:
            o.ver = d['ver']
        return o


