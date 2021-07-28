#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillBalancehisQueryModel(object):

    def __init__(self):
        self._biz_date = None
        self._biz_month = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_month(self):
        return self._biz_month

    @biz_month.setter
    def biz_month(self, value):
        self._biz_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_month:
            if hasattr(self.biz_month, 'to_alipay_dict'):
                params['biz_month'] = self.biz_month.to_alipay_dict()
            else:
                params['biz_month'] = self.biz_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillBalancehisQueryModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_month' in d:
            o.biz_month = d['biz_month']
        return o


