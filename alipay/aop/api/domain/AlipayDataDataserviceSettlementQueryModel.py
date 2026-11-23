#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceSettlementQueryModel(object):

    def __init__(self):
        self._settlement_date = None
        self._settlement_month = None
        self._type = None

    @property
    def settlement_date(self):
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, value):
        self._settlement_date = value
    @property
    def settlement_month(self):
        return self._settlement_month

    @settlement_month.setter
    def settlement_month(self, value):
        self._settlement_month = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.settlement_date:
            if hasattr(self.settlement_date, 'to_alipay_dict'):
                params['settlement_date'] = self.settlement_date.to_alipay_dict()
            else:
                params['settlement_date'] = self.settlement_date
        if self.settlement_month:
            if hasattr(self.settlement_month, 'to_alipay_dict'):
                params['settlement_month'] = self.settlement_month.to_alipay_dict()
            else:
                params['settlement_month'] = self.settlement_month
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSettlementQueryModel()
        if 'settlement_date' in d:
            o.settlement_date = d['settlement_date']
        if 'settlement_month' in d:
            o.settlement_month = d['settlement_month']
        if 'type' in d:
            o.type = d['type']
        return o


