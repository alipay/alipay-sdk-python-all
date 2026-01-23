#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeFinanceOrderQueryModel(object):

    def __init__(self):
        self._settlement_no = None

    @property
    def settlement_no(self):
        return self._settlement_no

    @settlement_no.setter
    def settlement_no(self, value):
        self._settlement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.settlement_no:
            if hasattr(self.settlement_no, 'to_alipay_dict'):
                params['settlement_no'] = self.settlement_no.to_alipay_dict()
            else:
                params['settlement_no'] = self.settlement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeFinanceOrderQueryModel()
        if 'settlement_no' in d:
            o.settlement_no = d['settlement_no']
        return o


