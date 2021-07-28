#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneEquityPortfolioQueryModel(object):

    def __init__(self):
        self._portfolio_code = None
        self._product_id = None

    @property
    def portfolio_code(self):
        return self._portfolio_code

    @portfolio_code.setter
    def portfolio_code(self, value):
        self._portfolio_code = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.portfolio_code:
            if hasattr(self.portfolio_code, 'to_alipay_dict'):
                params['portfolio_code'] = self.portfolio_code.to_alipay_dict()
            else:
                params['portfolio_code'] = self.portfolio_code
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneEquityPortfolioQueryModel()
        if 'portfolio_code' in d:
            o.portfolio_code = d['portfolio_code']
        if 'product_id' in d:
            o.product_id = d['product_id']
        return o


