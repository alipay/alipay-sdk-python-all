#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CateringOrderInfo(object):

    def __init__(self):
        self._merchant_home_url = None
        self._table_num = None

    @property
    def merchant_home_url(self):
        return self._merchant_home_url

    @merchant_home_url.setter
    def merchant_home_url(self, value):
        self._merchant_home_url = value
    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_home_url:
            if hasattr(self.merchant_home_url, 'to_alipay_dict'):
                params['merchant_home_url'] = self.merchant_home_url.to_alipay_dict()
            else:
                params['merchant_home_url'] = self.merchant_home_url
        if self.table_num:
            if hasattr(self.table_num, 'to_alipay_dict'):
                params['table_num'] = self.table_num.to_alipay_dict()
            else:
                params['table_num'] = self.table_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateringOrderInfo()
        if 'merchant_home_url' in d:
            o.merchant_home_url = d['merchant_home_url']
        if 'table_num' in d:
            o.table_num = d['table_num']
        return o


