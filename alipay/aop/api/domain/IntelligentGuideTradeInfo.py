#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IntelligentGuideTradeDetail import IntelligentGuideTradeDetail


class IntelligentGuideTradeInfo(object):

    def __init__(self):
        self._shop_id = None
        self._shop_name = None
        self._trade_details = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def trade_details(self):
        return self._trade_details

    @trade_details.setter
    def trade_details(self, value):
        if isinstance(value, list):
            self._trade_details = list()
            for i in value:
                if isinstance(i, IntelligentGuideTradeDetail):
                    self._trade_details.append(i)
                else:
                    self._trade_details.append(IntelligentGuideTradeDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.trade_details:
            if isinstance(self.trade_details, list):
                for i in range(0, len(self.trade_details)):
                    element = self.trade_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_details[i] = element.to_alipay_dict()
            if hasattr(self.trade_details, 'to_alipay_dict'):
                params['trade_details'] = self.trade_details.to_alipay_dict()
            else:
                params['trade_details'] = self.trade_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntelligentGuideTradeInfo()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'trade_details' in d:
            o.trade_details = d['trade_details']
        return o


