#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoPair import ExtInfoPair


class ItemPromoInfoSyncRequest(object):

    def __init__(self):
        self._promo_ext_info = None
        self._promo_price = None
        self._promo_stock_total = None
        self._promo_type = None
        self._valid_time_end = None
        self._valid_time_start = None

    @property
    def promo_ext_info(self):
        return self._promo_ext_info

    @promo_ext_info.setter
    def promo_ext_info(self, value):
        if isinstance(value, list):
            self._promo_ext_info = list()
            for i in value:
                if isinstance(i, ExtInfoPair):
                    self._promo_ext_info.append(i)
                else:
                    self._promo_ext_info.append(ExtInfoPair.from_alipay_dict(i))
    @property
    def promo_price(self):
        return self._promo_price

    @promo_price.setter
    def promo_price(self, value):
        self._promo_price = value
    @property
    def promo_stock_total(self):
        return self._promo_stock_total

    @promo_stock_total.setter
    def promo_stock_total(self, value):
        self._promo_stock_total = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def valid_time_end(self):
        return self._valid_time_end

    @valid_time_end.setter
    def valid_time_end(self, value):
        self._valid_time_end = value
    @property
    def valid_time_start(self):
        return self._valid_time_start

    @valid_time_start.setter
    def valid_time_start(self, value):
        self._valid_time_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_ext_info:
            if isinstance(self.promo_ext_info, list):
                for i in range(0, len(self.promo_ext_info)):
                    element = self.promo_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_ext_info[i] = element.to_alipay_dict()
            if hasattr(self.promo_ext_info, 'to_alipay_dict'):
                params['promo_ext_info'] = self.promo_ext_info.to_alipay_dict()
            else:
                params['promo_ext_info'] = self.promo_ext_info
        if self.promo_price:
            if hasattr(self.promo_price, 'to_alipay_dict'):
                params['promo_price'] = self.promo_price.to_alipay_dict()
            else:
                params['promo_price'] = self.promo_price
        if self.promo_stock_total:
            if hasattr(self.promo_stock_total, 'to_alipay_dict'):
                params['promo_stock_total'] = self.promo_stock_total.to_alipay_dict()
            else:
                params['promo_stock_total'] = self.promo_stock_total
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.valid_time_end:
            if hasattr(self.valid_time_end, 'to_alipay_dict'):
                params['valid_time_end'] = self.valid_time_end.to_alipay_dict()
            else:
                params['valid_time_end'] = self.valid_time_end
        if self.valid_time_start:
            if hasattr(self.valid_time_start, 'to_alipay_dict'):
                params['valid_time_start'] = self.valid_time_start.to_alipay_dict()
            else:
                params['valid_time_start'] = self.valid_time_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPromoInfoSyncRequest()
        if 'promo_ext_info' in d:
            o.promo_ext_info = d['promo_ext_info']
        if 'promo_price' in d:
            o.promo_price = d['promo_price']
        if 'promo_stock_total' in d:
            o.promo_stock_total = d['promo_stock_total']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'valid_time_end' in d:
            o.valid_time_end = d['valid_time_end']
        if 'valid_time_start' in d:
            o.valid_time_start = d['valid_time_start']
        return o


