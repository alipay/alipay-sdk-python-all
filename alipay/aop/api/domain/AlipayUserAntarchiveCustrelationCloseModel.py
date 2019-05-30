#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntarchiveCustrelationCloseModel(object):

    def __init__(self):
        self._close_date = None
        self._cust_id = None

    @property
    def close_date(self):
        return self._close_date

    @close_date.setter
    def close_date(self, value):
        self._close_date = value
    @property
    def cust_id(self):
        return self._cust_id

    @cust_id.setter
    def cust_id(self, value):
        self._cust_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.close_date:
            if hasattr(self.close_date, 'to_alipay_dict'):
                params['close_date'] = self.close_date.to_alipay_dict()
            else:
                params['close_date'] = self.close_date
        if self.cust_id:
            if hasattr(self.cust_id, 'to_alipay_dict'):
                params['cust_id'] = self.cust_id.to_alipay_dict()
            else:
                params['cust_id'] = self.cust_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntarchiveCustrelationCloseModel()
        if 'close_date' in d:
            o.close_date = d['close_date']
        if 'cust_id' in d:
            o.cust_id = d['cust_id']
        return o


