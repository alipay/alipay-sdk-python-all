#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountCashpoolDetailQueryModel(object):

    def __init__(self):
        self._cash_pool_id = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountCashpoolDetailQueryModel()
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        return o


