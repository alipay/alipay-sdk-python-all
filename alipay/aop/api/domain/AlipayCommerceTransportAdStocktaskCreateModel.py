#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StockQueryCondition import StockQueryCondition


class AlipayCommerceTransportAdStocktaskCreateModel(object):

    def __init__(self):
        self._ad_user_id = None
        self._charge_type = None
        self._sell_mode = None
        self._stock_query_condition = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def sell_mode(self):
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, value):
        self._sell_mode = value
    @property
    def stock_query_condition(self):
        return self._stock_query_condition

    @stock_query_condition.setter
    def stock_query_condition(self, value):
        if isinstance(value, StockQueryCondition):
            self._stock_query_condition = value
        else:
            self._stock_query_condition = StockQueryCondition.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.sell_mode:
            if hasattr(self.sell_mode, 'to_alipay_dict'):
                params['sell_mode'] = self.sell_mode.to_alipay_dict()
            else:
                params['sell_mode'] = self.sell_mode
        if self.stock_query_condition:
            if hasattr(self.stock_query_condition, 'to_alipay_dict'):
                params['stock_query_condition'] = self.stock_query_condition.to_alipay_dict()
            else:
                params['stock_query_condition'] = self.stock_query_condition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdStocktaskCreateModel()
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'sell_mode' in d:
            o.sell_mode = d['sell_mode']
        if 'stock_query_condition' in d:
            o.stock_query_condition = d['stock_query_condition']
        return o


