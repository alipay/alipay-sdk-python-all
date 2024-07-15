#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoBillQueryModel(object):

    def __init__(self):
        self._bill_date = None
        self._eco_code = None
        self._shop_code = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoBillQueryModel()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        return o


