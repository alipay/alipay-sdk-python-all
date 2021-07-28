#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringKmsBakingBatchqueryModel(object):

    def __init__(self):
        self._forecast_date = None
        self._shop_id = None
        self._sku_id = None

    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, value):
        self._forecast_date = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        if isinstance(value, list):
            self._sku_id = list()
            for i in value:
                self._sku_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.forecast_date:
            if hasattr(self.forecast_date, 'to_alipay_dict'):
                params['forecast_date'] = self.forecast_date.to_alipay_dict()
            else:
                params['forecast_date'] = self.forecast_date
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sku_id:
            if isinstance(self.sku_id, list):
                for i in range(0, len(self.sku_id)):
                    element = self.sku_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_id[i] = element.to_alipay_dict()
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringKmsBakingBatchqueryModel()
        if 'forecast_date' in d:
            o.forecast_date = d['forecast_date']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


